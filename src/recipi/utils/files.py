import sys
import uuid
import time
import os


def upload_to(template):
    if len(sys.argv) > 1 and sys.argv[1] in ('makemigrations', 'migrate'):
        return None  # Hide ourselves from Django migrations

    def _handler(self, filepath):
        filename = os.path.basename(filepath)

        # Get two 4-char codes from a uuid. This, plus a base
        # template with year/month should be more than
        # enough for our use-cases.

        uu = str(uuid.uuid4()).split('-')[1:3]
        base = time.strftime(template.format(*uu))

        return os.path.join(base, filename)
    return _handler
