from django.conf.urls import url
from user.views import *

urlpatterns = [
    url(r'^login$',Login.as_view()),
    url(r'^login/$',Login.as_view()),
    url(r'^login.html$', Login.as_view()),
    url(r'^login.html/$', Login.as_view()),
    url(r"login1/$",login1),
    url(r'^register$',Register.as_view()),
    url(r'^register.html$',Register.as_view()),
    url(r'^register.html/$',Register.as_view()),
    url(r'^register/$', Register.as_view()),
    # 判断用户名是否重复注册
    url(r'^/usernames/(?P<username>[a-zA-Z0-9_-]{3,10})/count/$', UsernameCountView.as_view()),
    url(r'^usernames/(?P<username>[a-zA-Z0-9_-]{3,10})/count/$', UsernameCountView.as_view()),
    url(r'^usertels/(?P<usertel>[0-9]{11})/count/$', UsertelCountView.as_view()),
#     http://127.0.0.1:8000/usernames/004/count/
    # 用户退出登录
    url(r'^logout/$', LogoutView.as_view()),
    url(r'^/logout/$',LogoutView.as_view()),
    # a标签直接写 /logout/

    # 用户中心
    url(r'^user_center_info/$', UserInfoView.as_view()),
    url(r'^user_center_info.html$', UserInfoView.as_view())
]
