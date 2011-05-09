from django.core.serializers.json import DjangoJSONEncoder


class SortedJSONEncoder(DjangoJSONEncoder):
    """
    A json encoder that sorts the dict keys and that can encode datetime
    objects.
    """
    def __init__(self, **kwargs):
        kwargs['sort_keys'] = True
        super(SortedJSONEncoder, self).__init__(**kwargs)

