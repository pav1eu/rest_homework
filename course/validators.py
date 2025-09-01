from rest_framework.exceptions import ValidationError
from urllib.parse import urlparse

class YoutubeOnlyValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        parsed_url = urlparse(value)
        domain = parsed_url.netloc.lower()
        if 'youtube.com' not in domain:
            raise ValidationError({self.field: "Разрешены только ссылки на YouTube."})