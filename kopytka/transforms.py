from django.contrib.postgres.fields import ArrayField
from django.db.models import CharField, Func


class SKeys(Func):
    function = 'skeys'
    arity = 1
    output_field = ArrayField(CharField())
