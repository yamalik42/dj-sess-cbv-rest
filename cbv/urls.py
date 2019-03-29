"""cbv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crud.views import AuthorView, session_prac
from rest import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('author/', AuthorView.as_view()),
    path('author/create', AuthorView.as_view()),
    path('author/<int:_id>', AuthorView.as_view()),
    path('', session_prac),
    path('api/question/<int:pk>', views.QuestionDetail.as_view()),
    path('api/question/', views.QuestionList.as_view()),
    path('api/question', views.QuestionList.as_view()),
    path('api/choice/<int:pk>', views.ChoiceDetail.as_view()),
    path('api/choice/', views.ChoiceList.as_view()),
    path('api/choice', views.ChoiceList.as_view()),
]
