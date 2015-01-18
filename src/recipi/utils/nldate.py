# -*- coding: utf-8 -*-
"""
Don't use this module. It's highly experimental, incomplete
and not supposed to work reliably. But, what works is cool:

>>> from recipi.utils.nldate import parse, convert_rrule_to_str

>>> convert_rrule_to_str(parse('every tuesday vegan').rule)
>>> 'dtstart:2015-01-18T00:00:00;freq:2;byhour:0;byweekday:1;bysecond:0;byminute:0;interval:1;'

>>> parse('every tuesday vegan')
>>> Rule(date=None, rule=<dateutil.rrule.rrule object at 0x7f0078062e48>, details='vegan')

"""

from collections import namedtuple
from datetime import datetime
from dateutil import parser, rrule
from dateutil.relativedelta import relativedelta

import nltk


ParseResult = namedtuple('Rule', 'date, rule, details')

RRULE_ATTRIBUTES = frozenset((
    'freq', 'dtstart', 'interval', 'count', 'until',
    'bysetpos', 'bymonth', 'bymonthday', 'byyearday',
    'byweekno', 'byweekday', 'byhour', 'byminute',
    'bysecond', 'byeaster'
))

days = "(mon|tue|wed|thu|fri|sat|sun|weekday|wday)"
months = "(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)"
dmy = "(year|day|week|month)"
rel_day = "(tod|yes|tom|ton)"

tokens = [
    (r'(ev)', 'recur'),
    (r'(yearly|monthly|weekly|daily)', 'recur_detail'),
    (r'(from)', 'start'),
    (r'(next)', 'jump'),
    (r'(at)', 'time_detail'),
    (rel_day, 'rel_day'),
    (r'(to|till|until)', 'end'),
    (days, 'day'),
    (dmy, 'dmy'),
    (months, 'month'),
    (r'[\s]*', 'join')
]

tagger = nltk.RegexpTagger(tokens)

WEEKDAYS = {
    'mon': rrule.MO,
    'tue': rrule.TU,
    'wed': rrule.WE,
    'thu': rrule.TH,
    'fri': rrule.FR,
    'sat': rrule.SA,
    'sun': rrule.SU
}


def join_tags(tags):
    result = []
    buffer = []
    for item in tags:
        if item[1] == 'join':
            buffer.append(item[0])
        else:
            if buffer:
                result.append((u' '.join(buffer), 'detail'))
                buffer = []
            result.append(item)
    if buffer:
        result.append((u' '.join(buffer), 'detail'))

    return result


def convert_rrule_to_dict(rrule):
    retval = {}
    for attr in RRULE_ATTRIBUTES:
        value = getattr(rrule, '_%s' % attr, None)
        if not value and not isinstance(value, (str, int)) and not value is None:
            value = None
        retval[attr] = value
    return retval


def convert_rrule_to_str(rrule):
    dct = convert_rrule_to_dict(rrule)
    retval = ''

    total = len(dct.keys())
    for idx, item in enumerate(dct.items()):
        key, value = item
        if value or isinstance(value, int):
            if isinstance(value, (list, set, tuple)):
                value = ','.join(str(x) for x in value)
            if isinstance(value, datetime):
                value = value.isoformat()
            retval += '%s:%s%s' % (key, str(value), ';' if idx < total else '')
    return retval


def parse(string, *args, **kwargs):
    result = join_tags(tagger.tag(string.split()))
    recur = False
    rrule_args = {}
    values = []
    details = []
    orig_today = kwargs.pop('default', None)
    info = parser.parserinfo()
    ignore = False
    if orig_today is None:
        today = datetime.today().date()
    else:
        kwargs['default'] = today = orig_today

    next = lambda: result[idx + 1] if len(result) > idx + 1 else (None, None)
    for idx, item in enumerate(result):
        if ignore:
            ignore = False
            continue
        value, type = item
        if type == 'recur':
            recur = True
        elif recur and type == 'recur_detail':
            rrule_args['freq'] = {'monthly': rrule.MONTHLY,
                                  'daily': rrule.DAILY,
                                  'weekly': rrule.WEEKLY,
                                  'yearly': rrule.YEARLY}[value]
            if 'dtstart' not in rrule_args:
                rrule_args['dtstart'] = today
        elif recur and type == 'dmy':
            rrule_args['freq'] = {'day': rrule.DAILY,
                                  'month': rrule.MONTHLY,
                                  'week': rrule.WEEKLY,
                                  'year': rrule.YEARLY}[value]
            if 'dtstart' not in rrule_args:
                rrule_args['dtstart'] = today
        elif type == 'day':
            if recur:
                rrule_args.setdefault('byweekday', ())
                if value in ('wday', 'weekday'):
                    val = tuple(WEEKDAYS[k] for k in WEEKDAYS.keys() if k in ('mon',
                        'tue', 'wed', 'thu', 'fri'))
                else:
                    val = (WEEKDAYS[value[:3]],)
                rrule_args['byweekday'] += val
                rrule_args['freq'] = rrule.WEEKLY
            else:
                values.append(value)
        elif type == 'month':
            if recur:
                rrule_args.setdefault('bymonth', ())
                rrule_args['byweekday'] += (info.month(value),)
                rrule_args['freq'] = rrule.MONTHLY
            else:
                values.append(value)
        elif type == 'start':
            rrule_args['dtstart'] = parser.parse(next()[0], fuzzy=True)
            recur = True
        elif type == 'end':
            rrule_args['until'] = parser.parse(next()[0], fuzzy=True)
            recur = True
        elif type == 'time_detail':
            if recur:
                val = parser.parse(next()[0], fuzzy=True)
                rrule_args.setdefault('byhour', ())
                rrule_args['byhour'] += (val.hour,)
            else:
                values.append('at')
        elif type == 'rel_day':
            now = today.timetuple()
            matcher = {'tod': today,
                       'yes': today + relativedelta(days=-1),
                       'tom': today + relativedelta(days=+1),
                       'ton': datetime(now[0], now[1], now[2], 22, now[4],
                                       now[5])}
            if not any(x for x in result if x[1] == 'start') and recur:
                rrule_args['dtstart'] = matcher[value[:3]]
            else:
                values.append(matcher[value[:3]].isoformat())
        elif type == 'jump':
            next = next()[0][:3]
            if next in info._weekdays:
                dt = today + relativedelta(weekday=WEEKDAYS[next[:3]](+1))
            elif next in info._months:
                dt = today + relativedelta(month=info._months[next] + 1)

            if not any(x for x in result if x[1] == 'start') and recur:
                rrule_args['dtstart'] = dt
            else:
                values.append(dt.isoformat())
            ignore = True
        elif type == 'detail':
            details.append(value)
        else:
            values.append(value)

    if recur:
        if 'dtstart' not in rrule_args:
            if orig_today:
                rrule_args['dtstart'] = orig_today
            else:
                rrule_args['dtstart'] = parser.parse(u' '.join(values), *args, **kwargs)
        return ParseResult(
            date=None,
            rule=rrule.rrule(**rrule_args),
            details=u' '.join(details)
        )
    else:
        kwargs['fuzzy'] = True
        return ParseResult(
            date=arser.parse(u' '.join(values), *args, **kwargs),
            rule=None,
            details=u' '.join(details)
        )
