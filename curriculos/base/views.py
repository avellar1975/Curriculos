from django.http import HttpResponse


def home(requests):
    return HttpResponse('<html><body>Olá Django</body></html>',
                        content_type='text/html')
