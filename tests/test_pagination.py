#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test Paginator
--------------

Tests for `django-cursor-pagination` paginator module.
"""
from __future__ import absolute_import

from cursor_pagination.paginator import Paginator

from .base import CursorBaseTestCase
from .models import TestModel


class TestCursorPagination(CursorBaseTestCase):
    def test_pagination(self):
        queryset = TestModel.objects.order_by('pk')
        page_count = 0
        object_count = 0
        paginator = Paginator(queryset, self.PAGE_SIZE)
        for i in range(self.TOO_MANY_PAGES):
            self.page_size = len(paginator)
            if not self.page_size:
                break
            object_count += self.page_size
            page_count += 1

            cursor = paginator.next_cursor()
            paginator.from_cursor(cursor)

        self.assertEqual(object_count, self.NUM_ITEMS)
        self.assertEqual(page_count, self.NUM_ITEMS / self.PAGE_SIZE)
