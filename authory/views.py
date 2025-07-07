from django.shortcuts import render,redirect,reverse
from django.http.response import JsonResponse
import random
import string
from django.core.mail import send_mail
from .models import Email_code
from django.views.decorators.http import require_http_methods
from .forms import RegisterForm, LoginForm
from django.contrib.auth import get_user_model,login,logout

User=get_user_model()

# Create your views here.
@require_http_methods(['POST','GET'])
def wmlogin(request):
    if request.method=='GET':
        return render(request, 'login.html')
    else:
        print("提交的数据:", request.POST)  # 检查是否有 email 和 emailcode
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            password=form.cleaned_data.get('password')
            remember=form.cleaned_data.get('remember')
            user=User.objects.filter(email=email).first()
            if user and user.check_password(password):
                login(request,user)
                if remember:
                    request.session.set_expiry(None)
                return redirect('/')
            else:
                print('email is wrong')
                # return render(request, 'login.html', {'form':form,'error':'用户名或密码错误'})

def wmlogout(request):
    logout(request)
    return redirect('/')

@require_http_methods(['POST','GET'])
def register(request):
    print("Request method:", request.method)  # 确认请求方法
    print("POST data:", request.POST)  # 确认是否有数据
    print("register view called!")
    if request.method=='GET':
        return render(request, 'register.html')
    else:
        print("提交的数据:", request.POST)  # 检查是否有 email 和 emailcode
        form=RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            User.objects.create_user(username=username,email=email,password=password)
            return redirect(reverse('authory:login'))
        else:
            print(form.errors)
            return render(request, 'register.html', {'form':form})



def email_code(request):
    email=request.GET.get('email')
    if not email:
        return JsonResponse({'code':400,'message':'输入准确邮箱'})
    emailcode=''.join(random.sample(string.digits,4))
    Email_code.objects.update_or_create(email=email,defaults={'emailcode':emailcode})
    send_mail('wdj验证码',f'你的验证码是{emailcode}',None,[email])
    return JsonResponse({'code':200,'message':'验证码已发送'})
