from django.urls import path
from home import views
urlpatterns = [
    path('',views.index ),
    path('contact/',views.contact ),
    path('about/',views.about ),
    path('services/',views.services ),
    
]
