from rest_framework.exceptions import ValidationError
from urllib.parse import urlparse

class YoutubeOnlyValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, attrs):
        url_value = None
        if isinstance(attrs, dict):
            url_value = attrs.get(self.field)
        else:
            url_value = attrs

        if not url_value:
            return

        parsed_url = urlparse(url_value)
        domain = parsed_url.netloc.lower()
        if 'youtube.com' not in domain:
            raise ValidationError({self.field: "Разрешены только ссылки на YouTube."})