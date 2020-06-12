from django.urls import path
from .views import home,secondGraph,product_page,programming,pie,piechartDB

urlpatterns = [
    path('',home,name='home'),
    path('secondGraph/',secondGraph,name='secondGraph'),
    path('product_page/',product_page,name='product_page'),
    path('programming/',programming,name='programming'),
    path('piechart/',pie,name='piechart'),
    path('piedb/',piechartDB,name='piechartdb'),
]