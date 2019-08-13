from django.shortcuts import render, redirect  
from exam.forms import ExamForm  
from exam.models import Exam  
 
def exam(request):  
    if request.method == "POST":  
        form = ExamForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/examshow')  
            except:  
                pass  
    else:  
        form = ExamForm()  
    return render(request,'exam.html',{'form':form})  
def examshow(request):  
    exam = Exam.objects.all()  
    return render(request,"examshow.html",{'exam':exam})  
def examupdate(request, id):  
    exam = Exam.objects.get(id=id)  
    form = ExamForm(request.POST, instance = exam)  
    if form.is_valid():  
        form.save()  
        return redirect("/examshow")  
    return render(request, 'examedit.html', {'exam': exam})  
def examdestroy(request, id):  
    exam = Exam.objects.get(id=id)  
    exam.delete()  
    return redirect("/examshow") 
