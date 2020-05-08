from django.urls import path
from .views import BNBListView, BNBDetailView, BNBCreateView, BNBUpdateView, BNBDeleteView
from . import views

urlpatterns = [
    path('', BNBListView.as_view(), name='bnb-home'),
    path('<int:pk>/', BNBDetailView.as_view(), name='bnb-detail'),
    path('<int:pk>/update/', BNBUpdateView.as_view(), name='bnb-update'),
    path('<int:pk>/delete/', BNBDeleteView.as_view(), name='bnb-delete'),
    path('new/', BNBCreateView.as_view(), name='bnb-create'),
    
]
