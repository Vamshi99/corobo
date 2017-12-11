"""
Handle backend specific implementations.
"""
import urllib

def message_link(bot, msg):
    """
    :param bot: Plugin instance.
    :param msg: Message object.
    :returns:   Message link.
    """
    backend = bot.bot_config.BACKEND.lower()
    if backend == 'gitter':
        return 'https://gitter.im/{uri}?at={idd}'.format(uri=msg.frm.room.uri,
                                                         idd=msg.extras['id'])
    elif backend = 'zulip':
        quote = urllib.parse.quote(msg['subject'], safe=''
        return 'https://coala.zulipchat.com/#narrow/stream/{}/subject/{}/'
               'near/{}'.format(msg['display_recipient'], quote, msg['id'])
    elif backend == 'slack':
        return msg.extras['url']
    elif backend == 'telegram':
        return ''
    elif backend == 'text':
        return ''
    else:
        raise NotImplementedError
