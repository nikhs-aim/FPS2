from django.urls import path
from .views import conference_details,conferencecreate,journal_details,journalcreate,Options
from django.contrib.auth.views import LogoutView
from .import views

urlpatterns = [
    path('conferences/', conference_details, name='conferences'),
    path('hodviewotherconf',views.hod_view_other_conference_details,name='hodviewotherconf'),
    path('conf-create/',conferencecreate.as_view(),name='conf-create'),
    path('journals/', journal_details, name='journals'),
    path('hodviewotherjourn',views.hod_view_other_journal_details,name='hodviewotherjourn'),
    path('journ-create/',journalcreate.as_view(),name='journ-create'),
    path('logout/',LogoutView.as_view(next_page='login'),name='logout'),
    path('options',Options,name='options'),
    path('hodoptions',views.hod_options,name='hodoptions'),
    path('register/', views.registration_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('choose',views.choose,name='choose'),
    path('',views.home,name='home')
    
]
    




















# {% if request.user.is_authenticated %}
# <p>{{request.user}}</p>
# <a href="{% url 'logout' %}">Logout</a>
# {% else %}
# <a href="{% url 'login' %}">Login</a>
# {% endif %}
# <hr>










