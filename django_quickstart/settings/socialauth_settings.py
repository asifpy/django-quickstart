from configparser import SafeConfigParser
from django.conf import settings

parser = SafeConfigParser()
parser.read(settings.CONFIG_PATH)

SOCIAL_AUTH_GITHUB_KEY = parser.get('GITHUB_SOCIAL_AUTH', 'GITHUB_KEY')
SOCIAL_AUTH_GITHUB_SECRET = parser.get('GITHUB_SOCIAL_AUTH', 'GITHUB_SECRET')
