from django import forms
from .models import User

class RegisterFrom(forms.Form):
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
                    password = c_password
                )
                temp_user.save()
