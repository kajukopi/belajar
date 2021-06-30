from django.urls import path


# importing views from views..py
from geeks.views import GeeksCreate, GeeksList, GeeksDetailView, GeeksUpdateView, GeeksDeleteView

urlpatterns = [
    path('create/', GeeksCreate.as_view(), name='create'),
    path('list/', GeeksList.as_view(), name='list'),
    path('<pk>/', GeeksDetailView.as_view(), name='detail'),
    path('<pk>/update', GeeksUpdateView.as_view(), name='update'),
    path('<pk>/delete/', GeeksDeleteView.as_view(), name='delete'),
    path('', GeeksList.as_view(), name='home'),
    path('accounts/login/', GeeksList.as_view(), name='login'),

]
