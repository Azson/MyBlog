from django.shortcuts import render, redirect, render_to_response

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.template.context_processors import csrf
from django.contrib import messages

from .models import Post, Mood, Mark, User, MyUser, Diary, Problem
from datetime import datetime
from django.template.loader import get_template
from mainsite import forms

from .func import sendEmail

from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def homepage(request, res=None, pid=None, del_pass=None):
    #use follow when login is by session
    #if("username" in request.session):
     #   username = request.session['username']
      #  useremail = request.session['useremail']
    if(res is not None):
        return redirect('/')
    #login by auth
    #username = "tmp"
    if(request.user.is_authenticated()):
        username = request.user.username
    #print("username is {0}".format(username))
    mymsg = messages.get_messages(request)
    template = get_template('index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    #post_list = list()
    #for count, post in enumerate(posts):
     #   post_list.append("No.{}".format(str(count) + str(post) + "<hr>"))
      #  post_list.append("<pre>" + str(post.body) + "</pre><br><br>")
    return HttpResponse(html)

def showpost(request, slug):
    #print("in fun showpost")
    if (request.user.is_authenticated()):
        username = request.user.username
    template = get_template('post.html')
    try:
        #print(str(slug))
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except :
        return redirect('/')
    return

def login(request):

    template = get_template('login.html')
    try:
        urid = request.GET.get('user_id')
        urpass = request.GET.get("user_pass")
    except:
        urid = None
        urpass = None
    if(urid != None and urpass == '123'):
        verified = True
    else:
        verified = False
    print("login id:{0}, code:{1} ,ver:{2}".format(urid, urpass, verified))

    years = range(1960, 2021)
    birthYear = request.GET.get('byear')
    urfcolor = request.GET.getlist('fcolor')

    html = template.render(locals())
    return HttpResponse(html)

def showMark(request, pid=None, del_pass=None):
    if (request.user.is_authenticated()):
        username = request.user.username
    print("accept request")
    template = get_template('showMark.html')
    posts = Mark.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = Mood.objects.all()

    try:
        user_id = request.GET.get('user_id')
        user_pass = request.GET.get('user_pass')
        user_post = request.GET.get('user_post')
        user_mood = request.GET.get('mood')
    except:
        user_id = None
        message = "请输入所有选项"
    print("user_mod:{0}".format(user_mood))
    print("del_pass {0}. pid {1}".format(del_pass, pid))
    if del_pass and pid:

        try:
            post = Mark.objects.get(id=pid)
        except:
            post = None
            print("Sorry, not find id:{0} post!".format(pid))

        if post:
            print("do delete pass is {0}  right is {1}".format(del_pass, post.del_pass))
            if post.del_pass == del_pass:
                post.delete()
                message = "数据删除成功！"
            else:
                message = "密码错误"
    elif user_id != None:
        try:
            mood = Mood.objects.get(status=user_mood)
            post = Mark.objects.create(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
            post.save()
            message = "上传成功！请记住您的密码: {0}!信息需要经过审核才会显示！".format(user_pass)
        except:
            message = "请完成所有字段信息的填写"


    html = template.render(locals())
    return HttpResponse(html)

def contact(request):
    if (request.user.is_authenticated()):
        username = request.user.username
    print("in contact!")
    if(request.method == "POST"):
        print(request.POST)
        #print("post ! {0}".format(request.POST.__getattribute__("user_email")))
        form = forms.ContactForm(request.POST)
        if(form.is_valid()):
            message = "感谢您的来信"
            user_name = form.cleaned_data["user_name"]
            user_city = form.cleaned_data["user_city"]
            user_school = form.cleaned_data["user_school"]
            user_email = form.cleaned_data["user_email"]
            user_message = form.cleaned_data["user_message"]
            print(type(user_name))
            if(user_school):
                text = "在校"
            else:
                text = "未在校"
            mailbody = "来自AzsonWeb的信息：\n网友姓名：" + user_name + "\n网友邮箱：" + user_email + "\n网友城市：" + user_city + "\n是否在学：" + text + "\n网友意见：" + user_message
            sendEmail.EmailClass.sendEmail(mailbody, user_email)
        else:
            message = "请检查您输入的信息是否正确！"
    else:
        form = forms.ContactForm()
        message = "请填写下列信息 ~"
    template = get_template("contact.html")

    #request_context = RequestContext(request)
    #request_context.push(locals())
    #print(type(request_context))
    #print(request_context)
    #print(locals())
    #context_instance = RequestContext(request)
    c = csrf(request)
    c.update(locals())
    html = template.render(c)#context must be dict

    return HttpResponse(html)
    #return render_to_response("contact.html", context=c)

def showMark2(request):
    message = "如果要发布您的心情，请填写每一个字段！"
    if(request.method == "POST"):
        post_form = forms.PostForm(request.POST)
        if(post_form.is_valid()):
            message = "信息存储成功，待管理员审核通过后即可显示！"
            post_form.save()
        else:
            message = "请确保您的每个信息都填了，并且验证码正确！"
        if (request.session.test_cookie_worked()):
            request.session.delete_test_cookie()
            message = "cookie is ok!"
        else:
            message = "fail!"
    else:
        post_form = forms.PostForm()
    template = get_template("post2db.html")

    request.session['test'] = "abcd"
    if(request.session['test'] != "abcd"):
        message = "fail"
    else:
        message = "succuss"
    moods = Mood.objects.all()
    #request


    c = csrf(request)
    c.update(locals())

    html = template.render(c)
    return HttpResponse(html)
#login by session
def login2(request):
    print("request login2 {0}".format(messages.get_messages(request)))
    if(request.method == "POST"):
        print("POST request")
        login_form = forms.LoginForm(request.POST)
        if(login_form.is_valid()):
            login_name = request.POST['user_name'].strip()
            login_password = request.POST['password']
            #user = auth.authenticate(username=login_name, password=login_password)
            message = "登录成功!"
            try:
                user = User.objects.get(name=login_name)
                if(user.password == login_password):
                    response = redirect("/")#####
                    request.session['username'] = user.name
                    request.session['useremail'] = user.email
                    messages.add_message(request, messages.SUCCESS, "登录成功！")
                    return response
                else:
                    message = "密码错误！"
                    messages.add_message(request, messages.WARNING, "登录失败！")
            except:
                message = "目前无法登录！"
                messages.add_message(request, messages.WARNING, "目前无法登录！")
        else:
            message = "登录失败,请检测各字段数据是否合法！"
            messages.add_message(request, messages.INFO, "登录失败,请检测各字段数据是否合法！")
    else:
        login_form = forms.LoginForm()

    template = get_template("login2.html")
    c = csrf(request)
    c.update(locals())
    html = template.render(c)
    #response = HttpResponse(html)

    return HttpResponse(html)

def login3(request):
    if (request.method == "POST"):
        login_form = forms.LoginForm(request.POST)
        if (login_form.is_valid()):
            login_name = request.POST['user_name'].strip()
            login_password = request.POST['password']
            user = auth.authenticate(username=login_name, password=login_password)
            if(user is not None):
                if(user.is_active):
                    auth.login(request, user)
                    print("success login")
                    messages.add_message(request, messages.SUCCESS, "登陆成功！")
                    return redirect("/")
                else:
                    messages.add_message(request, messages.WARNING, "该账号尚未启用！")
            else:
                messages.add_message(request, messages.WARNING, "登录失败")
        else:
            messages.add_message(request, messages.WARNING, "请检查输入字段内容")

    else:
        login_form = forms.LoginForm()
    #login_form.user_name.label
    template = get_template("login2.html")
    c = csrf(request)
    c.update(locals())
    html = template.render(c)
    # response = HttpResponse(html)

    return HttpResponse(html)

#@login_required(login_url='/login/')
def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.INFO, "注销成功！")
    print(type(messages))
    print(messages)
    print(messages.get_messages(request))

    return redirect("/")

@login_required(login_url='/login/')
def userinfo(request):

    #if("username" in request.session):
    if(request.user.is_authenticated()):
        username = request.user.username
        print("username is {0}".format(username))
    else:
        return redirect("/")
    from django.contrib.auth.models import User as authUser
    user = authUser.objects.get(username=username)
    #user = User.objects.get(name=username)
    try:
        #userinfo1 = auth.get_user_model().objects.get(username=username)#User.objects.get(name=username)
        #user = auth.get_user_model().objects.get(username=username)
        #userinfo1 = MyUser.objects.get(user=user)
        profile = MyUser.objects.get(user=user)
    except:
        profile = MyUser(user=user)
        print("userinfo is exception")
        pass
    if(request.method == 'POST'):
        profile_form = forms.ProfileForm(request.POST, instance=profile)
        if(profile_form.is_valid()):
            messages.add_message(request, messages.INFO, "个人资料更新成功！")
            profile_form.save()
            return HttpResponseRedirect('/userinfo/')
        else:
            messages.add_message(request, messages.INFO, "请确定每个字段都填写完成")
    else:
        profile_form = forms.ProfileForm()
    template = get_template("userinfo.html")
    c = csrf(request)
    c.update(locals())
    html = template.render(c)
    return HttpResponse(html)

def writeBlog(request):
    if(request.user.is_authenticated()):
        username = request.user.username
    messages.get_messages(request)

    if(request.method == "POST"):
        #diaryForm = forms.DiaryForm(request)
        user = auth.get_user_model().objects.get(username=username)
        diary = Diary(user=user)
        post_form = forms.DiaryForm(request.POST, instance=diary)
        if(post_form.is_valid()):
            messages.add_message(request, messages.INFO, "日记已存储")
            post_form.save()
            return HttpResponseRedirect("/")
        else:
            messages.add_message(request, messages.INFO, "请检查每个字段是否都已填写")

    else:
        post_form = forms.DiaryForm()
        messages.add_message(request, messages.INFO, "请检查每个字段是否都已填写")

    template = get_template("writeDiary.html")
    c = csrf(request)
    c.update(locals())

    html = template.render(c)
    return HttpResponse(html)

def showBlog(request):
    if(request.user.is_authenticated()):
        username = request.user.username
        try:
            #user = MyUser.objects.get(username=username)
            user = auth.get_user_model().objects.get(username=username)
            print(user)
            diaries = Diary.objects.filter(user=user).order_by('-ddate')
            print(diaries)
        except:
            print("showBlog exception")
            pass
    messages.get_messages(request)

    template = get_template("showDiary.html")
    c = csrf(request)
    c.update(locals())
    html = template.render(c)
    return HttpResponse(html)

#import MySQLdb
def showProblem(request, page=0):
    if (request.user.is_authenticated()):
        username = request.user.username
    messages.get_messages(request)
    page = int(page)
    #posts = Mark.objects.filter(enabled=True).order_by('-pub_time')[:30]
    problems = Problem.objects.order_by('id')[100*page:100 + 100*page]
    problem_nums = range(int((len(Problem.objects.all())+99) /100))
    #problems = [12,2]
    print("num is {}".format(problem_nums))
    template = get_template("showProblem.html")
    c = csrf(request)
    c.update(locals())
    html = template.render(c)
    #print("hello problem")
    return HttpResponse(html)

def showProblemPage(request, qusId=None):
    if (request.user.is_authenticated()):
        username = request.user.username
    messages.get_messages(request)

    item = Problem.objects.filter(id=qusId)
    if(item is None or len(item) == 0):
        return HttpResponse("<h1>无法找到你请求的页面</h1>")
    item = item[0]
    template = get_template("showProblemPage.html")
    c = csrf(request)
    c.update(locals())
    html = template.render(c)
    print("hello page")
    print(item)
    return HttpResponse(html)