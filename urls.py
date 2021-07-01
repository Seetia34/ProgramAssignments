from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
]

from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /HtH/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /HtH/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /HtH/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]