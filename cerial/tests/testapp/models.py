from django.db import models
from cerial import JSONField, PickleField


class JSONEntry(models.Model):
    f = JSONField(blank=True)

class PickleEntry(models.Model):
    f = PickleField(blank=True)

class JSONNullEntry(models.Model):
    f = JSONField(null=True)

