#!C:\hcq_softwares\python2_7_13_django_1_10_7\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Django==1.10.7','console_scripts','django-admin'
__requires__ = 'Django==1.10.7'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Django==1.10.7', 'console_scripts', 'django-admin')()
    )
