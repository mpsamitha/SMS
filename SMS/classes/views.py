from django.shortcuts import render, redirect

from classes.forms import ClassesForm

from classes.models import Classes  
from django.contrib import messages
  
def classes(request):  
    if request.method == "POST":  
        form = ClassesForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()
                # messages.success(request, 'Your added details successfully!', extra_tags='alert')  
                return redirect('/classshow')  
            except:  
                pass

        else:
            messages.warning(request, 'Please correct the error below that Class and Grade both are added already.', extra_tags='alert')  
    else:  
        form = ClassesForm() 
    return render(request,'classes.html',{'form':form})  

def classshow(request):  
    classes = Classes.objects.all().order_by('-class_grade')  
    return render(request,"classshow.html",{'classes':classes})  
  
# def classupdate(request, id):  
#     classes = Classes.objects.get(id=id)  
#     form = ClassesForm(request.POST, instance = classes)  
#     if form.is_valid():  
#         form.save()  
#         return redirect("/classshow")  
#     return render(request, 'classedit.html', {'classes': classes})  

def classdestroy(request, id):  
    classes = Classes.objects.get(id=id)  
    classes.delete()  
    return redirect("/classshow") 
