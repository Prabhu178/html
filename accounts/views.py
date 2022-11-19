from django.shortcuts import render

# Create your views here.
def home_view(request):
    # context={
    #     'first':'prabhu','last': 'kumar'
    # }
    return render(request,'index3.html')