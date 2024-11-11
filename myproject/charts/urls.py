from django.urls import path
from .views import SalesDataAPI, chart_view, login_view, logout_view

urlpatterns = [
    path('chart/', chart_view, name='chart-view'),
    path('login/', login_view, name='login'),   # Login URL
    path('logout/', logout_view, name='logout'),  # Logout URL
    path('api/sales/', SalesDataAPI.as_view(), name='sales-data-api'),  # API URL
]
