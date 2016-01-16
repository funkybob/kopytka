from django.db.models import CharField, Func
from django.contrib.postgres.fields import ArrayField


class SKeys(Func):
    function = 'skeys'
    arity = 1
    output_field = ArrayField(CharField())
