# Python
import datetime


# Djago
from django.test import TestCase
from django.utils import timezone


# Models
from .models import Question


# Views


class QuestionModelTest(TestCase):

    def test_was_published_recently_with_future_questions(self):
        """was_publishd_recently returns false for questions whose pub_date is in the future"""
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="Quien es el mejor course director de platzi",pub_date=time)
        self.assertIs(future_question.was_published_recently(),False)

