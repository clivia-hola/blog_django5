from django import forms
from django.contrib.auth import get_user_model
from .models import Email_code

User=get_user_model()

class RegisterForm(forms.Form):
    username=forms.CharField(label='用户名',min_length=4,max_length=20,error_messages={'required':'用户名不能为空','min_length':'用户名长度不能小于4','max_length':'用户名长度不能大于20'})
    email=forms.EmailField(label='邮箱',error_messages={'required':'邮箱不能为空','invalid':'邮箱格式不正确'})
    emailcode=forms.CharField(label='验证码',min_length=4,max_length=4,error_messages={'invalid':'长度错误'})
    password=forms.CharField(label='密码',min_length=6,max_length=20,error_messages={'required':'密码不能为空','min_length':'密码长度不能小于6','max_length':'密码长度不能大于20'})

    def clean_email(self):
        email=self.cleaned_data.get('email')
        exists=User.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError('邮箱已被注册')
        return email

    def clean_emailcode(self):
        email = self.cleaned_data.get('email')
        emailcode = self.cleaned_data.get('emailcode')
        print(f"[DEBUG] clean_emailcode: email={email}, emailcode={emailcode}")  # 调试

        if not email:
            raise forms.ValidationError('邮箱不能为空！')

        # 检查数据库
        record = Email_code.objects.filter(email=email, emailcode=emailcode).first()
        print(f"[DEBUG] 数据库记录: {record}")  # 调试
        if not record:
            raise forms.ValidationError('验证码错误或已过期！')
        record.delete()
        return emailcode

class LoginForm(forms.Form):
    email=forms.EmailField(label='邮箱',error_messages={'required':'邮箱不能为空','invalid':'邮箱格式不正确'})
    password=forms.CharField(label='密码',min_length=6,max_length=20,error_messages={'required':'密码不能为空','min_length':'密码长度不能小于6','max_length':'密码长度不能大于20'})
    remember=forms.BooleanField(label='记住我',required=False)
