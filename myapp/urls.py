from django.urls import path
from myapp.views import SimpleView

urlpatterns = [
    path('logging', SimpleView.as_view()),
]
