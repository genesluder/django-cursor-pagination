# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.db import models

from cursor_pagination.managers import CursorManager


class ExampleModel(models.Model):
    date_field = models.DateField()
    count_field = models.PositiveIntegerField()

    objects = CursorManager()

    class Meta:
        ordering = ['pk']
