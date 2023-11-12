
from django.urls import path
from blog1.views import index 


urlpatterns = [
    path('', index, name="blog1_index")
]