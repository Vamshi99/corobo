import os

import wolframalpha

from errbot import BotPlugin, botcmd


class WolframAlpha(BotPlugin):
    """
    Query the Computational Knowledge Engine
    """

    def activate(self):
        super().activate()
        self.client = wolframalpha.Client(os.environ.get('WA_TOKEN'))

    @botcmd
    def wa(self, msg, arg):
        """
        Query the Computational Knowledge Engine.
        """
        ans = ''
        if arg:
            res = self.client.query(arg)
            try:
                for pod in res.pods:
                    if pod.title in ['Result', 'Results']:
                        for sub in pod.subpods:
                            ans += sub.plaintext
            except AttributeError:
                self.log.info('KeyError triggered on retrieving pods.')
            return ans if ans else 'Dunno :('
        else:
            return('Invalid command args. Usage: `{} wa '
                   '<query>`'.format(self.bot_config.BOT_PREFIX))
