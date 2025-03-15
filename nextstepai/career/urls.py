from django.urls import path
from .views import home_page,recommend_career  # Import view function

urlpatterns = [
    path('',home_page,name='home-page'),
     path("recommend/", recommend_career, name="recommend_career"),  # Main page for recommendations
]
