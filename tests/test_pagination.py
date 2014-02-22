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
    def test_iteration(self):
        queryset = TestModel.objects.all()
        page_count = 0
        object_count = 0
        paginator = Paginator(queryset, self.PAGE_SIZE)
        for i in range(self.TOO_MANY_PAGES):
            page_size = len(paginator)
            if not page_size:
                break
            object_count += page_size
            page_count += 1

            cursor = paginator.next_cursor()
            paginator.from_cursor(cursor)

        self.assertEqual(object_count, self.NUM_ITEMS)
        self.assertEqual(page_count, self.NUM_ITEMS / self.PAGE_SIZE)

    def test_construction(self):
        queryset = TestModel.objects.all()
        page_count = 0
        object_count = 0
        paginator = Paginator(queryset, self.PAGE_SIZE)

        cursor = paginator.next_cursor()
        paginator2 = Paginator(queryset, self.PAGE_SIZE, cursor=cursor)

        for i in range(self.TOO_MANY_PAGES):
            page_size = len(paginator2)
            if not page_size:
                break
            object_count += page_size
            page_count += 1

            cursor = paginator2.next_cursor()
            paginator2.from_cursor(cursor)

        self.assertEqual(object_count, self.NUM_ITEMS - self.PAGE_SIZE)
        self.assertEqual(page_count,
                         (self.NUM_ITEMS - self.PAGE_SIZE) / self.PAGE_SIZE)

    def test_indexing(self):
        queryset = TestModel.objects.all()
        paginator = Paginator(queryset, self.PAGE_SIZE)

        for i in range(0, self.PAGE_SIZE):
            self.assertEqual(queryset[i], paginator[i])
