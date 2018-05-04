from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User as SysUser
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()

    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date', )

    def __str__(self):
        return self.title

class Mood(models.Model):
    status = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.status

class Mark(models.Model):
    mood = models.ForeignKey('Mood', on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10, default="不愿透露姓名")
    message = models.TextField(null=False)
    del_pass = models.CharField(max_length=10)
    pub_time = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.message

class User(models.Model):
    name = models.CharField(max_length=20, null=False)
    email = models.EmailField()
    password = models.CharField(max_length=20, null=False)
    enabled = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class MyUser(models.Model):
    from django.contrib.auth.models import User as authUser
    user = models.OneToOneField(authUser, on_delete=models.CASCADE)
    height = models.PositiveIntegerField(default=160)
    male = models.BooleanField(default=False)
    website = models.URLField(null=True)

    def __str__(self):
        return self.user.username

class Diary(models.Model):
    user = models.ForeignKey(SysUser, on_delete=models.CASCADE)
    budget = models.FloatField(default=0)
    weight = models.FloatField(default=0)
    note = models.TextField()
    ddate = models.DateField()

    def __str__(self):
        return "{} ({})".format(self.ddate, self.user)

class Problem(models.Model):
    title = models.CharField(max_length=255)
    id = models.CharField(max_length=255, primary_key=True)
    accept_nums = models.CharField(max_length=30)
    submisions_nums = models.CharField(max_length=30)
    context = models.CharField(max_length=10000)
    Input = models.CharField(max_length=3000)
    Output = models.CharField(max_length=3000)
    sample_input = models.CharField(max_length=1000)
    sample_output = models.CharField(max_length=1000)
    author = models.CharField(max_length=255)
    recommend = models.CharField(max_length=255)
    lmit = models.CharField(max_length=255)

from ckeditor.fields import RichTextField
class Blog1(models.Model):
    title = models.CharField(max_length=50, verbose_name="标题")
    content = RichTextField(blank=True, null=True, verbose_name="内容")

    def __str__(self):
        return self.title
