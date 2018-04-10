from django import forms

'''一个表单一个类'''

class RegisterForm(forms.Form):
    name = forms.CharField(label="姓名")
    passwd = forms.CharField(label="密码",widget=forms.PasswordInput)
    phone = forms.CharField(label="手机号")
    email = forms.EmailField(label="邮箱")