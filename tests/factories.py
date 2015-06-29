from __future__ import absolute_import

import datetime

import factory
from factory import fuzzy

from .models import TestModel


class TestModelFactory(factory.DjangoModelFactory):
    date_field = fuzzy.FuzzyDate(datetime.date(2000, 1, 1))
    count_field = fuzzy.FuzzyInteger(1, 200)

    class Meta:
        model = TestModel
