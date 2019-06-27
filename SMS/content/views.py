from django.shortcuts import render, redirect  
from content.forms import SubjectForm  
from content.models import Subject  
# Create your views here.  
def sub(request):  
    if request.method == "POST":  
        form = SubjectForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/subshow')  
            except:  
                pass  
    else:  
        form = SubjectForm()  
    return render(request,'index.html',{'form':form})  
def subshow(request):  
    subject = Subject.objects.all()  
    return render(request,"subshow.html",{'subject':subject})  
# def subedit(request, id):  
#     subject = Subject.objects.get(id=id)  
#     return render(request,'subedit.html', {'subject':subject})  
def subupdate(request, id):  
    subject = Subject.objects.get(id=id)  
    form = SubjectForm(request.POST, instance = subject)  
    if form.is_valid():  
        form.save()  
        return redirect("/subshow")  
    return render(request, 'subedit.html', {'subject': subject})  
def subdestroy(request, id):  
    subject = Subject.objects.get(id=id)  
    subject.delete()  
    return redirect("/subshow") 
