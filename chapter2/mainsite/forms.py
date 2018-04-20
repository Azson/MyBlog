from django import forms
from captcha.fields import CaptchaField
from . import models
class ContactForm(forms.Form):
    CITY = [
        ['HN', '湖南'],
        ['HB', '湖北'],
        ['BJ', '北京'],
        ['SH', '上海'],
        ['GD', '广东'],
        ['XJ', '新疆'],
        ['QT', '其他'],
    ]

    user_name = forms.CharField(label="您的姓名", max_length=50, initial="游客")
    user_city = forms.ChoiceField(label="所在省份", choices=CITY)
    user_school = forms.BooleanField(label="是否在校", required=False)
    user_email = forms.EmailField(label="电子邮件")
    user_message = forms.CharField(label="您的意见", widget=forms.Textarea(attrs={'placeholder':'请认真填写您的意见，垃圾邮件会被拒收！'}))
    #captcha = form

class PostForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = models.Mark
        fields = ['mood', 'nickname', 'message', 'del_pass']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['mood'].label = "现在的心情"
        self.fields['nickname'].label = "您的昵称"
        self.fields['message'].label = "心情留言"
        self.fields['del_pass'].label = "设置密码"
        self.fields['captcha'].label = "验证码："

class LoginForm(forms.Form):
    CORLORS = [
        ['红', '红'],
        ['黄', '黄'],
        ['蓝', '蓝'],
        ['绿', '绿'],
        ['紫', '紫'],
    ]
    user_name = forms.CharField(label="您的账号", max_length=10, widget=forms.TextInput(attrs={'id':'user_name', 'placeholder':'请输入您的账号', 'class':'form-control'}))
    #user_color = forms.ChoiceField(label="您的幸运色", choices=CORLORS)
    password = forms.CharField(label="密码", widget=forms.PasswordInput(attrs={'id':'password', 'placeholder':'请输入您的密码', 'class':'form-control'}))

class DateInput(forms.DateField):
    #input_formats = 'date'
    input_type = "date"

class DiaryForm(forms.ModelForm):
    class Meta:
        model = models.Diary
        fields = ['budget', 'weight', 'note', 'ddate']
        widgets = {
            'ddate': forms.DateInput(attrs={'type':'date'}),
            'note': forms.Textarea(attrs={'class':"form-control", 'rows':"20"})
        }

    def __init__(self, *args, **kwargs):
        super(DiaryForm, self).__init__(*args, **kwargs)
        self.fields['budget'].label = "今日花费（元)"
        self.fields['weight'].label = "今日体重（KG)"
        self.fields['note'].label = "心情留言"
        self.fields['ddate'].label = "日期"
