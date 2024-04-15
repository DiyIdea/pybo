from django.urls import path

from . import views

app_name = 'pybo'

urlpatterns = [
    path('', views.index, name='index'),#2-05 url 별칭에서 추가
    path('<int:question_id>/', views.detail, name='detail'),#2-05 url 별칭에서 추가
    path('question/create/<int:question_id>/', views.answer_create, name='answer_create')
]