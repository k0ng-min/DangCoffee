from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User # User라고 하는 내장된 객체(테이블)을 장고는 이미 갖고 있음
from .models import User as UserOrigin

def login(request):
    # POST 요청이 들어오면, 로그인 처리
    if request.method == 'POST':
        userid = request.POST.get('username')
        pwd = request.POST.get('password')
        # DB에 등록되어 있는 회원인지의 여부를 검사 -> 있으면 User 객체 반환
        user = auth.authenticate(request, username=userid, password=pwd)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'failed_login.html')
    # GET 요청이 들어오면, login form을 담고 있는 login.html을 띄어줌
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')

def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')

    elif request.method == "POST":
        username = request.POST.get('User ID', None)
        password = request.POST.get('Password', None)
        re_password = request.POST.get('Password (Repeat)', None)
        res_data = {}
        if not (username and password and re_password):
            res_data['error'] = "모든 값을 입력해야 합니다."
        if password != re_password:
            res_data['error'] = "비밀번호가 다릅니다."
        else:
            user = User(username=username, password=make_password(password))
            user.save()
            return render(request, 'success_signup.html')
        return render(request, 'signup.html')





