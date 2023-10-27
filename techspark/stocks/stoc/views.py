from django.shortcuts import render
import joblib

def index(request):
    return render(request, "index.html")

def register(request):
    return render(request, "register.html")

def handleRegister(request):
    fname = request.POST.get('fname', 'default')
    lname = request.POST.get('lname', 'default')
    mail = request.POST.get('mail', 'default')
    passs = request.POST.get('passs', 'default')
    print(fname)
    print(lname)
    print(mail)
    print(passs)
    return render(request, "index.html")

def secScr(request):
    return render(request, "secScr.html")


def handlesecScr(request):
    stock = request.POST.get('stock', 'default')
    print(stock)
    # cls = joblib.load("model1.pkl")
    # lis = []
    # lis.append(request.GET['stock'])
    # print(lis)
    return render(request, "result.html", {'stock': stock})


def handleLogin(request):
    mail = request.POST.get('mail', 'default')
    passs = request.POST.get('passs', 'default')
    print(mail)
    print(passs)
    return render(request, "secScr.html")