import cPickle
import json
from django.db import models
from .serializers import SortedJSONEncoder


class CerialField(models.TextField):
    def loads(self, s):
        """
        Deserialize s
        """
        raise NotImplemented

    def dumps(self, obj):
        """
        Serialize obj
        """
        raise NotImplemented

    def get_prep_value(self, value):
        if not isinstance(value, basestring):
            value = self.dumps(value)
        return value

    def contribute_to_class(self, cls, name):
        super(CerialField, self).contribute_to_class(cls, name)
        setattr(cls, self.name, CerialDescriptor(self))

    def south_field_triple(self):
        from south.modelsinspector import introspector
        args, kwargs = introspector(self)
        return 'django.db.models.TextField', args, kwargs


class CerialDescriptor(object):
    def __init__(self, field):
        self.field = field

    def __get__(self, obj, owner):
        value = obj.__dict__[self.field.name]
        # we don't try to serialize empty strings
        if value and isinstance(value, basestring):
            value = self.field.loads(value)
            obj.__dict__[self.field.name] = value
        return value

    def __set__(self, obj, value):
        obj.__dict__[self.field.name] = value


class JSONField(CerialField):
    def loads(self, s):
        return json.loads(s)

    def dumps(self, obj):
        return json.dumps(obj, cls=SortedJSONEncoder)


class PickleField(CerialField):
    def loads(self, s):
        return cPickle.loads(str(s).decode('base64'))

    def dumps(self, obj):
        return cPickle.dumps(obj).encode('base64')

