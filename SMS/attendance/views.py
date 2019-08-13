from django.shortcuts import render, redirect  
from attendance.forms import AttendanceForm  
from attendance.models import Attendance  
 
def attend(request):  
    if request.method == "POST":  
        form = AttendanceForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/attendanceshow')  
            except:  
                pass  
    else:  
        form = AttendanceForm()  
    return render(request,'attendance.html',{'form':form})  
def attendanceshow(request):  
    attendance = Attendance.objects.all()  
    return render(request,"attendanceshow.html",{'attendance':attendance})  
def attendanceupdate(request, id):  
    attendance = Attendance.objects.get(id=id)  
    form = AttendanceForm(request.POST, instance = attendance)  
    if form.is_valid():  
        form.save()  
        return redirect("/attendanceshow")  
    return render(request, 'attendanceedit.html', {'attendance': attendance})  
def attendancedestroy(request, id):  
    attendance = Attendance.objects.get(id=id)  
    attendance.delete()  
    return redirect("/attendanceshow") 
