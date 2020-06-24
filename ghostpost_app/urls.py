from django.urls import path
from ghostpost_app import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('forms/', views.postadd),
    path('boast/', views.boast),
    path('roast/', views.roast),
    path('upvote/<int:id>/', views.upvote),
    path('downvote/<int:id>/', views.downvote),
    path('boasts/<int:id>/', views.boastview),
    path('roasts/<int:id>/', views.roastview), 
    path('popvote/', views.pop_vote)
]

