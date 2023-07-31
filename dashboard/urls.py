from django.urls import path
from dashboard.views import dashboard_view, delete_user_view, update_user_view

urlpatterns = [
    path('', dashboard_view, name='home'),
    path('delete/<user_uuid>', delete_user_view, name='delete'),
    path('update/<user_uuid>', update_user_view, name='update'),

]