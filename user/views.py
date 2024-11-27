from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,HttpResponseForbidden
from django.views import View
import re
from django.db import DatabaseError
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.



class UserInfoView(LoginRequiredMixin, View):
    """用户中心"""

    def get(self,request):
        """提供用户中心页面"""
        # if request.user.is_authenticated:
        #     return render(request, 'user_center_info.html')
        # else:
        #     return redirect(reverse('users:login'))
        context = {
            'username': request.user.username,
            'tel': request.user.last_name,
            'email': request.user.email,
        }
        return render(request, 'user_center_info.html', context)
        # return render(request,'user_center_info.html')



class Login(View):
    # 用户登录
    def get(self, request):
          # 返回登录以页面
       return render(request,'login.html')
    def post(self,request):

        username = request.POST.get('username')
        password = request.POST.get('password')


        if not all([username, password]):
            return HttpResponseForbidden('缺少必传参数')
        if not re.match(r'^[0-9a-zA-Z]{5,11}@(qq|163|192)\.com',username) and not re.match(r'^\d{11}$',username):
            return HttpResponseForbidden('昵称不合规')
        if not re.match(r'^[a-zA-Z0-9]{8,20}$',password):
            return HttpResponseForbidden('密码不合规')

        print(username, password)

        # 验证登录信息
        if re.match(r'^\d{11}$',username):
            # 手机号码
            # user1 = User.objects.get(password=password)
            # user1 = authenticate(last_name=username, password=password)
            # user1 = authenticate(last_name=username, first_name=password)
            # user1 = User.objects.filter(username=username, first_name=password)
            # print(user1, 'dd')
            # if user1 is None:
            #     return render(request,'login.html')
            try:
                user = User.objects.get(last_name=username)
                if user.first_name != password:
                    return render(request,'login.html',{'login_err': '密码错误'})
            except Exception as e:
                return render(request,'login.html',{'login_err': '账号不存在'})
        else:
            #  邮箱
            # user2 = authenticate(email=username, password=password)
            # # user2 = User.objects.filter(username=username, password=password)
            # print(user2)
            # if user2 is None:
            #     return render(request,'login.html')
            try:
                user = User.objects.get(email=username)
                if user.first_name != password:
                    return render(request, 'login.html',{'login_err': '密码错误'})
            except Exception as e:
                return render(request, 'login.html',{'login_err': '账号不存在'})

                # 实现状态保持
        login(request, user)

        next = request.GET.get('next')
        if next:
            # 重定向到next
            response = redirect(next)
        else:
            # 重定向到首页
            response = redirect('/')

        # 为了实现在首页的右上角展示用户名信息，我们需要将用户名缓存到cookie中
        # response.set_cookie('key', 'val', 'expiry')
        response.set_cookie('username', user.username, max_age=3600 * 24 * 15)

        return response





def login1(request):
    return render(request,'login.html')

class Register(View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        # 用户注册
        # 接收参数：表单参数
        username = request.POST.get('name')
        usertel = request.POST.get('usertel')
        userm = request.POST.get('userm')
        password = request.POST.get('password')
        # print(name,password,usertel,userm)
        # 校验数据
        if not all([username, password, userm, usertel]):
            return HttpResponseForbidden('缺少必传参数')
        if not re.match(r'^\w{3,10}$',username):
            return HttpResponseForbidden('昵称不合规')
        if not re.match(r'^[0-9]{11}$',usertel):
            return HttpResponseForbidden('手机号码不合规')
        if not re.match(r'^[0-9a-zA-Z]{5,11}@(qq|163|192)\.com$', userm):
            return HttpResponseForbidden('邮箱不合规')
        if not re.match(r'^[a-zA-Z0-9]{8,20}$',password):
            return HttpResponseForbidden('密码不合规')

        # 哈希算法
        # password = make_password(password, None, 'pbkdf2_sha256')
        # 写入数据库
        try:
            # user = User.objects.create_user(username=name, password=password,email=userm,last_name=usertel)
            user = User(username=username, first_name=password, email=userm,last_name=usertel)
            user.save()
        except DatabaseError:
            return render(request, 'register.html')

        # 实现状态保持
        login(request, user)

        # 响应结果:重定向到首页
        response = redirect('/')

        # 为了实现在首页的右上角展示用户名信息，我们需要将用户名缓存到cookie中
        # response.set_cookie('key', 'val', 'expiry')
        response.set_cookie('username', user.username, max_age=3600 * 24 * 15)

        return response
        # return render(request,'login.html')

class UsernameCountView(View):
    """判断用户名是否重复注册"""
    def get(self, request, username):
        """
        :param username: 用户名
        :return: JSON
        """
        # 实现主体业务逻辑：使用username查询对应的记录的条数(filter返回的是满足条件的结果集)
        count = User.objects.filter(username=username).count()
        # 响应结果
        return JsonResponse({'code': '0', 'errmsg': 'OK', 'count': count})
class UsertelCountView(View):
    """判断手机号是否重复注册"""
    def get(self, request, usertel):
        print(usertel)
        count = User.objects.filter(last_name=usertel).count()
        print(count)
        return JsonResponse({'code': '0', 'errmsg': 'OK', 'count': count})

class LogoutView(View):
    """用户退出登录"""

    def get(self, request):
        """实现用户退出登录的逻辑"""
        # 清除状态保持信息
        logout(request)

        # 退出登录后重定向到首页
        response = redirect('/')

        # 删除cookies中的用户名
        response.delete_cookie('username')

        # 响应结果
        return response



