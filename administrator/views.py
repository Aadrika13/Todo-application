from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
@login_required(login_url='login')
@staff_member_required(login_url='login')
def home(request):
    return render(request, 'administrator/index.html')