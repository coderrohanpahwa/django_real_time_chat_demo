from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .models import Chat
def index(request):
    return render(request,'index.html')
def room(request,room_name):
    chats=Chat.objects.all()
    return render(request,'room.html',{'room_name':room_name,"chats":chats})
@csrf_exempt
def upload(request):
    print(request.body)
    return JsonResponse({"success":"True"})