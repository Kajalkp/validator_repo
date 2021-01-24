from django.shortcuts import render
from myApp.forms import Feedback

# Create your views here.
def view1(request):
    f=Feedback()
    if request.method=="POST":
        f=Feedback(request.POST)
        if f.is_valid():
            name=f.cleaned_data['name']
            roll=f.cleaned_data['roll']
            email=f.cleaned_data['email']
            comments=f.cleaned_data['comments']
            d={"name":name,"roll":roll,"email":email,"comments":comments}
            return render(request,'myApp/output.html',d)
    d={"form":f}
    return render(request,'myApp/input.html',d)
    
            
