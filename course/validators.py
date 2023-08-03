from rest_framework import serializers


class UrlValidator:

    def __init__(self,field):
        self.field = field

    def __call__(self, value):
        if value.get('url_video'):
            if 'https://www.youtube.com/' not in value.get('url_video'):
                raise serializers.ValidationError('Ошибочный ресурс! Ссылка должна быть только с youtube.com!')


