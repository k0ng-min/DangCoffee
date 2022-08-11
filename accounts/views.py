from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User # USER라고 하는 내장된 객체(테이블)을 장고는 이미 갖고 있음

def login(request):
    # POST 요청이 들어오면, 로그인 처리
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
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
    if request.method == "POST":
        if request.POST['password'] == request.POST['repeat']:
            # 회원가입
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
            # 로그인
            auth.login(request, new_user)
            # 홈 리다이렉션
            return redirect('home')
    return render(request, 'register.html')





