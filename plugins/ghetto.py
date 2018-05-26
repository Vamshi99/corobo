import re

import requests

from errbot import BotPlugin, re_botcmd


class Ghetto(BotPlugin):
    """
    Real talk yo
    """

    @re_botcmd(pattern=r'ghetto(\s+(.+))?',
               re_cmd_name_help='ghetto <sentence>',
               flags=re.IGNORECASE)
    def ghetto(self, msg, match):
        """
        Real talk yo
        """
        if match.group(1) is None:
            return('Invalid command args. Usage: `{} '
                   'ghetto <sentence>`'.format(self.bot_config.BOT_PREFIX))
        rq = requests.post('http://www.gizoogle.net/textilizer.php',
                           data={'translatetext': match.group(2)})

        translated_text = re.search(
            r'<textarea .*;\"/>(.+)</textarea>', rq.text)
        if translated_text is not None:
            return translated_text.group(1)
        else:
            return 'Shiznit happens!'
