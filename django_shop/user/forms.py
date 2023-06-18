from django import forms
from django.contrib.auth.hashers import check_password, make_password
from .models import User

class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required' : '이메일을 작성해주세요.'
        },
        max_length=256,
        label='이메일',
    )
    password = forms.CharField(
        error_messages={
            'required' : '비일번호를 입력해주세요.'
        },
        widget=forms.PasswordInput,
        label='비밀번호',
    )
    re_password = forms.CharField(
        error_messages={
            'required' : '비일번호를 다시 입력해주세요.'
        },
        widget=forms.PasswordInput,
        label='비밀번호 확인',
    )

    def clean(self):
        cleaned_data = super().clean()
        c_email = cleaned_data.get('email')
        c_password = cleaned_data.get('password')
        c_re_password = cleaned_data.get('re_password')

        if c_password and c_re_password:
            if c_password != c_re_password:
                self.add_error('password', '비밀번호가 일치하지 않습니다.')
                self.add_error('re_password', '비밀번호가 일치하지 않습니다.')
            else:
                temp_user = User(
                    email = c_email,
                    password = make_password(c_password)
                )
                temp_user.save()

class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required' : '이메일을 작성해주세요.'
        },
        max_length=256,
        label='이메일',
    )
    password = forms.CharField(
        error_messages={
            'required' : '비일번호를 입력해주세요.'
        },
        widget=forms.PasswordInput,
        label='비밀번호',
    )

    def clean(self):
        cleaned_data = super().clean()
        c_email = cleaned_data.get('email')
        c_password = cleaned_data.get('password')


        if c_email and c_password:
            try:
                user = User.objects.get(email=c_email)
                print(user.email, user.password)
            except User.DoesNotExist:
                self.add_error('email', '아이디가 없습니다.')
                return
            
            if not check_password(c_password, user.password):
                self.add_error('password', '비밀번호가 틀렸습니다.')
            else:
                self.email = user.email
