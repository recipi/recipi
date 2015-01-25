import urllib
from collections import namedtuple

import requests
from django.utils.http import urlquote


# There are some amazing APIs to query product information
# like:
#  * https://www.semantics3.com
#  * http://www.simpleupc.com/
# - but those are enormously expensive :'('
# More UPC integration ideas:
#
#   * http://zxing.org/w/decode.jspx (decode barcodes)
#   * http://www.upcdatabase.com/ (another addition to upcdatabase.org)
#   * http://www.scandit.com/product-api/ - appears to be free. Need to contact
#                                           them.
#   * http://www.codecheck.info/ - http://www.codecheck.info/essen/suesswaren/schokoladetafeln/ean_4012362024507/id_597214/Edel_Bitter_Schokolade.pro  # noqa
#   * http://fddb.info/db/i18n/about/de_api.html - http://fddb.info/db/de/lebensmittel/diverse_edel_bitter_75prozent_cacao/index.html  # noqa
# General stuff:
#   * http://platform.fatsecret.com/api/Default.aspx?screen=cu
#      -> Ask them regarding API usage.
#   * http://www.nutritionix.com/api
#   * http://www.crowdsourcingnutritionfacts.info/about/

# USDA:
# https://github.com/czarandy/usda
# https://github.com/notanumber/django-usda/blob/master/usda/models.py
# https://github.com/schirinos/nutrient-db/blob/master/nutrientdb.py

Response = namedtuple(
    'Response',
    'valid, reason, name, number, description, price, ratingsup, ratingsdown'
)


class UPCDBClient(requests.Session):
    API_URL = 'http://api.upcdatabase.org/json/'
    USER_AGENT = 'recipi UPCDB Api Client'

    def __init__(self, api_key):
        super(UPCDBClient, self).__init__()
        self.api_key = api_key

    def request(self, method, url, *args, **kwargs):
        headers = {
            'User-Agent': UPCDBClient.USER_AGENT,
            'Content-Type': 'application/json',
            'Method': method,
        }

        headers.update(kwargs.pop('headers', {}))

        kwargs.update({
            'headers': headers,
        })

        path = u'/'.join(urlquote(part) for part in (self.api_key, url))
        full_url = urllib.parse.urljoin(UPCDBClient.API_URL, path)

        print(full_url, path)

        # TODO: Error handling
        return super(UPCDBClient, self).request(method, full_url, *args, **kwargs)
