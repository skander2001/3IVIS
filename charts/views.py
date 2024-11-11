# charts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import SalesData
from .serializers import SalesDataSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chart-view')  # Redirect to the chart page upon successful login
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'charts/login.html')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout

# Chart view that requires login
@login_required(login_url='login')  # This ensures the user is redirected to the login page
def chart_view(request):
    return render(request, 'charts/chart.html')

# API view for SalesData (REST API)
class SalesDataAPI(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this API

    def get(self, request):
        data = SalesData.objects.all()
        serializer = SalesDataSerializer(data, many=True)
        return Response(serializer.data)
