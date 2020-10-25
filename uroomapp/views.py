from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Room

# Create your views here.
def main(request):
    room = Room.objects.all()
    return render(request, 'main.html', {'room':room})

def login(request):
    if request.method == 'POST':
        # login.html에서 넘어온 username과 password를 각 변수에 저장하기.
        username = request.POST['username']
        password = request.POST['password']
        # 해당 username과 password와 일치하는 user 객체를 가져온다.
        user = auth.authenticate(request, username=username, password=password)
        # 해당 user 객체가 존재한다면(객체가 존재하지 않는다면 none을 반환할 텐데, none이 not이니까 존재한다면!)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    return render(request, 'login.html')

def manage1(request):
    return render(request, 'manage1.html')

def manage2(request):
    return render(request, 'manage2.html')


def mypage(request):
    return render(request, 'mypage.html')

def newmember(request):
    if request.method == 'POST': #값이 넘겨졌을 경우 
        if request.POST['password'] == request.POST['password']:  # password 1,2입력된 값이 같다면
            # user 객체를 새로 생성
            user = User.objects.create_user(
                username=request.POST['username'], password=request.POST['password'])
            return redirect('/') #첫화면으로
    return render(request, 'newmember.html')

def review(request):
    return render(request, 'review.html')

def scrap(request):
    return render(request, 'scrap.html')

def seenroom(request):
    return render(request, 'seenroom.html')

def uploadroom(request):
    return render(request, 'uploadroom.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('/')
    return render(request, 'newmember.html')  

def tradelist(request):
    return render(request, 'tradelist.html')

def reviewlist(request):
    return render(request, 'reviewlist.html')

def create(request):
    room = Room()
    room.insurance = request.GET['insurance']
    room.monthly = request.GET['monthly']
    room.contact = request.GET['contact']
    room.adress = request.GET['adress']
    room.explain = request.GET['explain']
    room.save()
    return redirect('/')