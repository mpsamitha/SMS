from django.shortcuts import render, redirect

from classes.forms import ClassesForm, ClassdetailsForm

from classes.models import Classes, Classdetails  
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

############### class details #########################
def classdetails(request):  
    if request.method == "POST":  
        form = ClassdetailsForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/classdetailsshow')  
            except:  
                pass  
    else:  
        form = ClassdetailsForm()  
    return render(request,'classdetails.html',{'form':form})

def classdetailsshow(request):  
    classdetails = Classdetails.objects.all()
    classes = Classes.objects.all()
    return render(request,"classdetailsshow.html",{'classdetails':classdetails, 'classes':classes})

def classdetailsupdate(request, id):
    classdetails = Classdetails.objects.get(classes_id=id)
    classes = Classes.objects.get(id=id)
    form = ClassdetailsForm(request.POST, instance = classesdetail)
    if form.is_valid():  
        form.save()  
        return redirect("/classshow")  
    return render(request, 'classdetailsshow.html', {'classes': classes, 'classdetails':classdetails}) 

# def subedit(request, id):  
#     subject = Subject.objects.get(id=id)  
#     return render(request,'subedit.html', {'subject':subject})  
# def classdetailsupdate(request, id):  
#     classdetails = Classdetails.objects.get(id=id)  
#     form = ClassdetailsForm(request.POST, instance = classdetails)  
#     if form.is_valid():  
#         form.save()  
#         return redirect("/classdetails")  
#     return render(request, 'classdetailsedit.html', {'classdetails': classdetails})  
def classdetailsdestroy(request, id):  
    classdetails = Classdetails.objects.get(id=id)  
    classdetails.delete()  
    return redirect("/classdetails") 