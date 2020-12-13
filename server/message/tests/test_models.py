from datetime import datetime
from message.models import RandomQuote, MessageOfTheDay


class TestRandomQuote:

    WRONG_URL = 'https://api.forismatic.com/2.0/'

    def test_init(self):
        rq = RandomQuote()
        assert rq.lang == 'en'
        assert rq.format == 'json'

    def test_wrong_url(self):
        rq = RandomQuote()
        rq.RANDOM_QUOTES_URL = self.WRONG_URL
        quote = rq.get_quote()
        assert quote in rq.BACKUP_QUOTES


class TestMessageOfTheDay:

    def test_instance(self):
        msg = MessageOfTheDay()
        assert isinstance(msg.content, str)
        assert isinstance(msg.created_at, datetime)
        assert 'content' in msg.to_dict()
