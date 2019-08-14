from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from log import views
from content import views as content
from classes import views as classes
from attendance import views as attendance
from exam import views as exam
from marks import views as marks
from django.conf import settings
from django.conf.urls.static import static

from .views import GeneratePdf

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'^special/',views.special,name='special'),
    url(r'^log/',include('log.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
    path('sub', content.sub, name='sub'),  
    path('subshow',content.subshow,name='subshow'),  
    # path('subedit/<int:id>', views.edit),  
    path('subupdate/<int:id>', content.subupdate,name='subupdate'),  
    path('subdelete/<int:id>', content.subdestroy,name='subdelete'),
    path('proshow', views.proshow, name='proshow'),
    path('profileshow/<int:id>', views.profileshow, name='profileshow'),
    path('classes', classes.classes, name='classes'),  
    path('classshow',classes.classshow,name='classshow'),   
    # path('classupdate/<int:id>', classes.classupdate,name='classupdate'),  
    path('classdelete/<int:id>', classes.classdestroy,name='classdelete'),
    path('classdetails', classes.classdetails, name='classdetails'),  
    path('classdetailsshow',classes.classdetailsshow,name='classdetailsshow'),  
    # path('classdetailsupdate/<int:id>', classes.classdetailsupdate,name='classdetailsupdate'),  
    path('classdetailsdestroy/<int:id>', classes.classdetailsdestroy,name='classdetailsdestroy'),
    path('attend', attendance.attend, name='attend'),
    path('attendanceshow', attendance.attendanceshow, name='attendanceshow'),
    path('attendanceupdate/<int:id>', attendance.attendanceupdate, name='attendanceupdate'),
    path('attendancedestroy/<int:id>', attendance.attendancedestroy, name='attendancedestroy'),
    path('exam', exam.exam, name='exam'),
    path('examshow', exam.examshow, name='examshow'),
    path('examupdate/<int:id>', exam.examupdate, name='examupdate'),
    path('examdestroy/<int:id>', exam.examdestroy, name='examdestroy'),
    path('marks', marks.marks, name='marks'),
    path('marksshow', marks.marksshow, name='marksshow'),
    path('marksupdate/<int:id>', marks.marksupdate, name='marksupdate'),
    path('marksdestroy/<int:id>', marks.marksdestroy, name='marksdestroy'),
    path('studentreport/<int:id>', marks.studentreport, name='studentreport'),
    # url(r'^pdf/$',GeneratePdf.as_view()),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
