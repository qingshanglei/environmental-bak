from django.conf.urls import url
from common.views import *

urlpatterns = [
   url(r'^$',Index.as_view()),
   url(r'^index.html/$',Index.as_view()),
   url(r'^index.html$',Index.as_view()),
   url(r'^news1.html$',news1),
   url(r'^news2.html$',news2),
   url(r'^news3.html$', news3),
   url(r'^news4.html$', news4),
   url(r'^news5.html$', news5),

   url(r'^zixun.html$',zixun),
   url(r'^kepu.html$',kepu)
]
