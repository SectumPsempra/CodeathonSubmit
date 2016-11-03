from django.shortcuts import render
from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from models import Questions,User_db

def local(request):
    d = "adad"
    context = {'c':d}
    return render(request,'first.html',context)
# Create your views here.
def login_page(request):
    log = {}
    log.update(csrf(request))
    return render(request,'login_page.html')

def login_auth(request):
    name = request.POST.get('NAME')
    pass_word = request.POST.get('PASSWORD')
    roll_no = request.POST.get('ROLL_NO')
    #print name,password,roll_no
    """    user = User.objects.get_or_create(username=roll_no,password=pass_word,first_name=name)
    print user
    user_auth = auth.authenticate(username=roll_no,password=pass_word)
    print user_auth
    if user_auth is not None :
        auth.login(request,user_auth)
        return HttpResponseRedirect('/questions')
    else :
        return HttpResponseRedirect('/invalid')
        """
    try:
        user=User.objects.get(username=roll_no,password=pass_word,first_name=name)
        user = auth.authenticate(username=roll_no,password=pass_word)
        if user is not None :
            auth.login(request,user)
            return HttpResponseRedirect('/instructions')
        else :
            return HttpResponseRedirect('/invalid')
    except:
        User.objects.create(username=roll_no,password=pass_word,first_name=name)
        user = User.objects.get(username=roll_no)
        auth.login(request,user)
        return HttpResponseRedirect('/instructions')

def question_page(request,num):
    user = auth.get_user(request)
    if str(user) == 'AnonymousUser':
        return HttpResponseRedirect('/login')
    log = {}
    log.update(csrf(request))
    usr = User_db.objects.get(roll=(User.objects.get(username=user)))
    prev_res=getattr(usr,'answer'+str(int(num)))
    #print prev_res
    myqsn = Questions.objects.get(number=num)
    context = {'myqsn':myqsn,'prev':prev_res}
    return render(request,'question_p.html',context)

def instructions(request):
    usr = auth.get_user(request)
    try:
        User_db.objects.create(roll=(User.objects.get(username=usr)))
    except:
        pass
    return render(request,'instructions.html')

def next_qsn(request):
    usr = auth.get_user(request)
    var = User_db.objects.get(roll=(User.objects.get(username=usr)))
    numb = request.POST.get('number')
    answ = request.POST.get('ans')
    setattr(var,'answer'+str(numb),answ)
    url_num = 'question/' + str(int(numb)+1)
    var.save()#print url_num
    return HttpResponseRedirect(url_num)

def question_list(request):
    qsn = Questions.objects.all()
    conte = {'value':qsn}
    return render(request,'question_list.html',conte)
