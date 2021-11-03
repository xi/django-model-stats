from django.urls import path

from .views import stats_view

urlpatterns = [
    path('', stats_view, name='model-stats'),
]
