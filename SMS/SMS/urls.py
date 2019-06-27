from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from log import views
from content import views as content
from classes import views as classes
from django.conf import settings
from django.conf.urls.static import static

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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
