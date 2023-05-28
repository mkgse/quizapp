from django.shortcuts import render
from myapp.models import quiz_model

# Create your views here.

def home(request):
    return render(request,'myapp/Index.html')

def question(request):  
 quiz = quiz_model.objects.all()
 return render(request,'myapp/question.html',{'quiz':quiz})


def answer(request):
   return render(request,'myapp/answer.html')