from django.test import TestCase
from django.conf.urls import url
from verifications.views import *

# Create your tests here.
urlpatterns = [
    # 图形验证码
    url(r'^image_codes/(?P<uuid>[\w-]+)/$',ImageCodeView.as_view()),
]