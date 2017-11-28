from errbot import BotPlugin, re_botcmd


class Lmgtfy(BotPlugin):
    """
    For all those people who find it more convenient to bother you with their
    question rather than search it for themselves.
    """

    @re_botcmd(pattern=r'lmgtfy(\s+(.+))?',
               re_cmd_name_help='lmgtfy <search-string>',
               template='lmgtfy.jinja2')
    def lmgtfy(self, msg, match):
        """I'm lazy, please google for me."""  # Ignore QuotesBear
        if match.group(1) is None:
            return('Invalid command args. Usage: `{} lmgtfy '
                   '<search-string>`'.format(self.bot_config.BOT_PREFIX))
        return {'query': match.group(2)}
