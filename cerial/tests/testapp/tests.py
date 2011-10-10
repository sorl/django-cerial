#coding=utf-8
import datetime
from django.utils import unittest
from testapp.models import JSONEntry, JSONNullEntry, PickleEntry


class A(object):
    def f(self, x):
        return x * x


class JSONTest(unittest.TestCase):
    def setUp(self):
        self.model = JSONEntry
        self.manager = self.model.objects

    def testCreate(self):
        entry = self.manager.create(pk=100, f={'k': 1})
        self.assertEqual(entry.f, {'k': 1})

    def testAssign(self):
        entry = self.manager.create(f={'k': 2})
        entry.f['k'] = {'j': 1}
        entry.save()
        self.assertEqual(entry.f, {'k': {'j': 1}})

    def testNULL(self):
        entry = self.manager.create(f=None)
        entry = self.manager.get(pk=entry.pk)
        self.assertEqual(entry.f, None)

    def testEmpty(self):
        entry = self.manager.create(f='')
        entry = self.manager.get(pk=entry.pk)
        self.assertEqual(entry.f, '')

    def testEmptyDict(self):
        entry = self.manager.create(f={})
        entry = self.manager.get(pk=entry.pk)
        self.assertEqual(entry.f, {})

    def testDate(self):
        d = datetime.date.today()
        entry = self.manager.create(f={'d': d})

    def testUnicode(self):
        entry = self.manager.create(f={'k': u'åäö'})
        entry = self.manager.get(pk=entry.pk)
        self.assertEqual(entry.f, {'k': u'åäö'})


class JSONNullTest(unittest.TestCase):
    def testNULL(self):
        entry = JSONNullEntry.objects.create(f=None)
        JSONNullEntry.objects.get(f__isnull=True)


class PickleTest(JSONTest):
    def setUp(self):
        self.model = PickleEntry
        self.manager = self.model.objects

    def testSimpleClass(self):
        entry = self.manager.create(f=A)
        entry = self.manager.get(pk=entry.pk)
        self.assertEqual(entry.f, A)

