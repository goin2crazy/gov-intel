from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import SignInForm, ComplaintRecordForm
from .models import ComplaintRecord, PeopleAdult, PeopleKid


from .filters import (kid_from_adults, 
                      
                      translate,
                      filter_spam,
                      problem_class, 
                      problem_rate)

from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_authenticated and user.is_staff

def successp(request): 
    return render(request, 'success.html', )


from django.shortcuts import render
from .models import ComplaintRecord
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views import View
# Apply the decorator to complaint_list and users_list
@user_passes_test(is_admin)
def complaint_list(request):
    complaint_types = ['Divorce', 'Violence', 'Disability', "Women's Rights", "Children's Rights"]
    complaint_type_ = ['divorce', 'violence', 'disability', "women_rights", "children_rights"]

    context = {}

    for t, t_ in zip(complaint_types, complaint_type_): 
        complaints = ComplaintRecord.objects.filter(type=t)
        complaint_lst = complaints.order_by('rating').all()

        context[t_] = complaint_lst

    return render(request, 'complaints.html', {'context': context})

class ComplaintListView(View):
    @method_decorator(user_passes_test(is_admin))
    def get(self, request, *args, **kwargs):
        return complaint_list(request)
    
@user_passes_test(is_admin)
def users_list(request): 
    context = {'adults': []}
    people_adult = PeopleAdult.objects.all()

    for obj in people_adult: 
        people_context = {'adult': obj} 
        people_kids = kid_from_adults(obj)

        if people_kids:
            people_context['kids'] = people_kids

        context['adults'].append(people_context)

    return render(request, 'complaint_list.html', {'peoples': context})

@login_required
def add_complaint_record(request):
    if request.method == 'POST':
        form = ComplaintRecordForm(request.POST)
        print(form.is_valid())
        if form.is_valid():

            if filter_spam(form.cleaned_data['text']): 
                
                print('not spam')
                complaint_record = form.save(commit=False)

                complaint_record.text = translate(complaint_record.text)
                complaint_record.type = problem_class(complaint_record.text)
                complaint_record.rating = problem_rate(complaint_record.text)

                complaint_record.adult = PeopleAdult.objects.get(user = request.user)
                complaint_record.save()

                return redirect('success_page')  # Replace 'success_page' with your actual success page name            
        return redirect('homepage')
    else:
        form = ComplaintRecordForm()

    return render(request, 'add_complaint.html', {'form': form})


def login_user(request): 
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            print('form is valid')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('success_page')  # replace 'homepage' with your actual homepage name
    else:
        form = SignInForm()

    return render(request, 'singin.html', {'form': form})


from django.shortcuts import render
import matplotlib.pyplot as plt
from io import BytesIO
import base64

from django.db import models

def generate_histogram(data, title, xlabel, ylabel):
    plt.bar(data.keys(), data.values())
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    # Save the plot to a BytesIO object
    image_stream = BytesIO()
    plt.savefig(image_stream, format='png')
    plt.close()

    # Convert the BytesIO object to a base64-encoded string
    image_stream.seek(0)
    image_data = base64.b64encode(image_stream.read()).decode('utf-8')

    return image_data

def homepage(request):
    # Assuming complaints is a queryset of ComplaintRecord objects
    # complaints = ComplaintRecord.objects.all()

    # # Generate histogram data for rating
    # rating_counts = dict(complaints.values_list('rating').annotate(count=models.Count('id')))
    # rating_histogram = generate_histogram(rating_counts, 'Rating Histogram', 'Rating', 'Count')
    # plt.close()
    # # Generate histogram data for type
    # type_counts = dict(complaints.values_list('type').annotate(count=models.Count('id')))
    # type_histogram = generate_histogram(type_counts, 'Type Histogram', 'Type', 'Count')
    # plt.close()

    return render(request, 'index.html', {})