from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib import messages

def student_list(request):
    context = dict()
    student_list = StudentInformation.objects.all()
    context['items'] = student_list
    if request.method == 'POST':
        print("")
    return render(request, 'studentInfo/student_list.html', context)


def student_details(request, id):
    context = dict()
    detail = StudentInformation.objects.get(pk=id)
    context['data'] = detail
    return render(request, 'studentInfo/student_detail.html', context)


def student_form(request, id=None):
    context = dict()
    form = StudentInformationForm

    if request.method == 'POST' and id:
        item = get_object_or_404(StudentInformation, pk=id)
        form = StudentInformationForm(request.POST or None, instance=item)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            messages.success(request, 'Data Updated')
            return redirect('studentInfo:student_list')

    elif id:
        item = get_object_or_404(StudentInformation, pk=id)
        form = StudentInformationForm(request.POST or None, instance=item)

    elif request.method == 'POST':
        form = StudentInformationForm(request.POST, request.FILES or None)
        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            messages.success(request, 'Data Saved')
            return redirect('studentInfo:student_list')

    context['form'] = form
    return render(request, 'studentInfo/student_form.html', context)


def student_edit(request, std_id):
    context = dict()
    detail = StudentInformation.objects.get(pk=std_id)
    context['data'] = detail

    if request.method == 'POST':
        print("")
    return render(request, 'studentInfo/student_form.html', context)
