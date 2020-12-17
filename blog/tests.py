from django.test import TestCase
from django.utils import timezone

class Test(TestCase):

    def primer_test(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
