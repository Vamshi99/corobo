import logging
import os

COBOT_ROOT = os.environ.get('COBOT_ROOT', os.getcwd())

_BOT_IDENTITY_KEYS = (
    'endpoint',
    'nickname',
    'password',
    'port',
    'server',
    'ssl',
    'token',
    'username',
)

BOT_IDENTITY = {}

for _key in _BOT_IDENTITY_KEYS:
    BOT_IDENTITY[_key] = os.environ.get('BOT_' + _key.upper())

if not BOT_IDENTITY['token']:
    BOT_IDENTITY['token'] = os.environ.get('COBOT_TOKEN')

if BOT_IDENTITY['server'] and ':' in BOT_IDENTITY['server']:
    server, port = os.environ['BOT_SERVER'].split(':')
    BOT_IDENTITY['server'] = (server, int(port))

BACKEND = os.environ.get('BACKEND')
if not BACKEND:
    if BOT_IDENTITY['token']:
        BACKEND = 'Gitter'
    else:
        BACKEND = 'Text'

if BACKEND == 'Gitter':
    BOT_EXTRA_BACKEND_DIR = os.path.join(COBOT_ROOT, 'err-backend-gitter')
else:
    BOT_EXTRA_BACKEND_DIR = None

if BOT_EXTRA_BACKEND_DIR:
    plug_file = BACKEND.lower() + '.plug'
    if not os.path.exists(os.path.join(BOT_EXTRA_BACKEND_DIR, plug_file)):
        raise SystemExit('Directory %s not initialised' %
                         BOT_EXTRA_BACKEND_DIR)

HIDE_RESTRICTED_COMMANDS = True

BOT_DATA_DIR = os.path.join(COBOT_ROOT, 'data')
BOT_EXTRA_PLUGIN_DIR = COBOT_ROOT

BOT_LOG_FILE = os.path.join(COBOT_ROOT, 'errbot.log')
BOT_LOG_LEVEL = logging.DEBUG

BOT_PREFIX = os.environ.get('BOT_PREFIX', 'corobo ')

if 'COBOT_PREFIX' in os.environ:
    BOT_PREFIX = os.environ['COBOT_PREFIX']
    logging.warning(
        'Deprecation warning: environment variable COBOT_PREFIX is replaced '
        'by BOT_PREFIX.')

# Also listen to cobot, if the bot being ran is corobo
if not os.environ.get('BOT_PREFIX'):
    BOT_ALT_PREFIXES = ('cobot ', )

BOT_DEPRECATED_PREFIXES = os.environ.get(
    'BOT_DEPRECATED_PREFIXES', '').split() or ('cobot ', )

BOT_ADMINS = os.environ.get('BOT_ADMINS', '').split() or ('*@localhost', )
# Text is a special case
if BACKEND == 'Text':
    BOT_ADMINS = ('@localhost', )

IGNORE_USERNAMES = os.environ.get("IGNORE_USERNAMES",
                                  'co-robo coala-bot').split()

DIVERT_TO_PRIVATE = ('help', )

ROOMS_TO_JOIN = (
    'coala/coala',
    'coala/coala/offtopic',
    'coala/cobot-test',
    'coala/corobo',
    'coala/devops',
    'coala/community',
    'coala/coala/gsoc',
    'coala/coala/maintainers',
    'coala/coala-bears',
    'coala/bearship',
    'coala/gci',
    'coala/cobot'
)

CHATROOM_PRESENCE = os.environ.get('ROOMS', '').split() or ROOMS_TO_JOIN

USERS_TO_BLACKLIST = []

ACCESS_CONTROLS = {'render test': {
    'allowrooms': ('coala/cobot-test', 'coala/corobo',)},
    'LabHub:*': {'allowprivate': False}}

AUTOINSTALL_DEPS = True
