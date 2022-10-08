from django.urls import path

from . import views


urlpatterns = [
    path('list/', views.Games.as_view()),
    path('detail/', views.GameDetail.as_view()),
    path('set-detail-state/', views.SetGameState.as_view()),
    path('delete-detail/', views.DeleteGameDetail.as_view())
]