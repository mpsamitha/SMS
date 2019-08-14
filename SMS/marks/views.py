from django.shortcuts import render, redirect  
from marks.forms import MarksForm  
from marks.models import Marks  
 
def marks(request):  
    if request.method == "POST":  
        form = MarksForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/marksshow')  
            except:  
                pass  
    else:  
        form = MarksForm()  
    return render(request,'marks.html',{'form':form})  
def marksshow(request):  
    marks = Marks.objects.all()  
    return render(request,"marksshow.html",{'marks':marks})  
def marksupdate(request, id):  
    marks = Marks.objects.get(id=id)  
    form = MarksForm(request.POST, instance = marks)  
    if form.is_valid():  
        form.save()  
        return redirect("/marksshow")  
    return render(request, 'marksedit.html', {'marks': marks})  
def marksdestroy(request, id):  
    marks = Marks.objects.get(id=id)  
    marks.delete()  
    return redirect("/marksshow") 

def studentreport(request, id):
    marks = Marks.objects.get(id=id)  
    form = MarksForm(request.POST, instance = marks)  
    if form.is_valid():  
        form.save()  
        return redirect("/marksshow")  
    return render(request, 'studentreport.html', {'marks': marks})