from django import forms

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
