from django.conf import settings
from random import choice
from string import ascii_letters, digits


SIZE = getattr(settings, "MAXIMUM_URL_CHARS", 7)

AVAILABLE_SIMBOLS = ascii_letters + digits


def create_random_simbols(chars=AVAILABLE_SIMBOLS):
    return "".join(
        [choice(chars) for _ in range(SIZE)]
    )


def create_shortened_url(model_instance):
    simbols = create_random_simbols()

    model_class = model_instance.__class__

    if model_class.objects.filter(short_url=simbols).exists():
        return create_shortened_url(model_instance)

    return simbols