
django-cerial
=============
Fields for storing serializable data.

What makes this different from other implementations available?

* This implementation deserializes only when necessary. Deserializing is done on
  field access rather than on model instance creation. Serializing is done right
  before saving the model instance.

* There is a test suite


Requirements
------------
* 2.5 <= Python < 3
* Django


Installation
------------
::

    pip install django-cerial



JSONField
---------
Serializes data as `JSON`_. Example::

    from django.db import models
    from cerial import JSONField

    class Entry(models.Model):
        data = JSONField()


PickleField
-----------
Serializes data using `cPickle`_. Example::

    from django.db import models
    from cerial import PickleField

    class Entry(models.Model):
        data = PickleField()


.. _JSON: http://www.json.org/
.. _cPickle: http://docs.python.org/library/pickle.html#module-cPickle
