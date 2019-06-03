from django.conf.urls import url
from django.contrib import admin
from instituteapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.main_page),
    url(r'^home/', views.home_page),
    url(r'^contact/', views.contact_page),
    url(r'^courses/', views.courses_page),
    url(r'^feedback/', views.feedback_page),
    url(r'^team/', views.team_page),
    url(r'^gallery/', views.gallery_page),

]
