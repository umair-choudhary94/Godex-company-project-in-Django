from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,"index.html")
def ecosystem(request):
    return render(request,"ecosystem.html")
def community(request):
    return render(request,"community.html")
def devlopers(request):
    return render(request,"developers.html")
def governance(request):
    return render(request,"governance.html")
def blog(request):
    return render(request,"blog.html")
def faq(request):
    return render(request,"faq.html")