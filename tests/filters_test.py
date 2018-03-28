import queue

from tests.isolated_testcase import IsolatedTestCase


class FiltersTest(IsolatedTestCase):

    def test_filter_users(self):
        self.bot_config.RESP_ONLY_REQ_USERS = False
        self.bot_config.REQUIRED_USERS = []
        self.assertCommand('!help', 'All commands')
        self.bot_config.RESP_ONLY_REQ_USERS = True
        self.bot_config.REQUIRED_USERS = ['testuser']
        self.bot_config.BOT_IDENTITY['nickname'] = 'testuser'
        with self.assertRaises(queue.Empty):
            self.assertCommand('!help', 'All commands')
