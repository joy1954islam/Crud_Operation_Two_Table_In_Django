from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from Crud.models import Ministry,GovernmentEmployee

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return render(request, 'Crud/SuperAdminNavbar.html')
        else:
            messages.error(request, 'Username or password incorrect')
    return render(request, 'Crud/login.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('../login/')
class MinistryForm(ModelForm):
    class Meta:
        model = Ministry
        fields = ['MinistryName', 'HonorableMinisterName','Address','Phone','Email']

@login_required
def Ministry_list(request, template_name='Crud/book_list.html'):
    if request.user.is_superuser:
        ministry = Ministry.objects.all()
    else:
        ministry = Ministry.objects.filter(user=request.user)
    data = {}
    data['object_list'] = ministry
    return render(request, template_name, data)

@login_required
def Ministry_create(request, template_name='Crud/book_form.html'):
    form = MinistryForm(request.POST or None)
    if form.is_valid():
        ministry = form.save(commit=False)
        ministry.user = request.user
        ministry.save()
        return redirect('Crud:Ministry_list')
    return render(request, template_name, {'form':form})

@login_required
def Ministry_update(request, pk, template_name='Crud/book_form.html'):
    if request.user.is_superuser:
        ministry= get_object_or_404(Ministry, pk=pk)
    else:
        ministry= get_object_or_404(Ministry, pk=pk, user=request.user)
    form = MinistryForm(request.POST or None, instance=ministry)
    if form.is_valid():
        form.save()
        return redirect('Crud:Ministry_list')
    return render(request, template_name, {'form':form})

@login_required
def Ministry_delete(request, pk, template_name='Crud/book_confirm_delete.html'):
    if request.user.is_superuser:
        ministry= get_object_or_404(Ministry, pk=pk)
    else:
        ministry= get_object_or_404(Ministry, pk=pk, user=request.user)
    if request.method=='POST':
        ministry.delete()
        return redirect('Crud:Ministry_list')
    return render(request, template_name, {'object':ministry})


class GovernmentEmployeeForm(ModelForm):
    class Meta:
        model = GovernmentEmployee
        fields = ['ministry', 'GovernmentEmployeeName','GovernmentEmployeeAddress','GovernmentEmployeePhnNumber','GovernmentEmployeeGmail',
                  'GovernmentEmployeeDesignation']

@login_required
def GovernmentEmployee_list(request, template_name='Crud/GovernmentEmployeeView.html'):
    if request.user.is_superuser:
        government = GovernmentEmployee.objects.all()
    else:
        government = GovernmentEmployee.objects.filter(user=request.user)
    data = {}
    data['object_list'] = government
    return render(request, template_name, data)

@login_required
def GovernmentEmployee_create(request, template_name='Crud/GovernmentEmployeeInsert.html'):
    form = GovernmentEmployeeForm(request.POST or None)
    if form.is_valid():
        government = form.save(commit=False)
        government.user = request.user
        government.save()
        return redirect('Crud:GovernmentEmployee_list')
    return render(request, template_name, {'form':form})

@login_required
def GovernmentEmployee_update(request, pk, template_name='Crud/GovernmentEmployeeInsert.html'):
    if request.user.is_superuser:
        government= get_object_or_404(GovernmentEmployee, pk=pk)
    else:
        government= get_object_or_404(GovernmentEmployee, pk=pk, user=request.user)
    form = GovernmentEmployeeForm(request.POST or None, instance=government)
    if form.is_valid():
        form.save()
        return redirect('Crud:GovernmentEmployee_list')
    return render(request, template_name, {'form':form})

@login_required
def GovernmentEmployee_delete(request, pk, template_name='Crud/GovernmentEmployeeDelete.html'):
    if request.user.is_superuser:
        government= get_object_or_404(GovernmentEmployee, pk=pk)
    else:
        government= get_object_or_404(GovernmentEmployee, pk=pk, user=request.user)
    if request.method=='POST':
        government.delete()
        return redirect('Crud:GovernmentEmployee_list')
    return render(request, template_name, {'object':government})