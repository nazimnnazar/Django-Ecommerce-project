from django.urls import path
from . import  views
urlpatterns = [
    path('product/',views.product,name='product'),
    path('<slug:c_slug>/',views.product,name='product'),
    path('<slug:c_slug>/<slug:product_slug>',views.viewdetails,name='view_details'),
]