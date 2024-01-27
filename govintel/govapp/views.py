from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import SignInForm  # Create a form for signing in
from .filters import people_exist, get_adult, get_complient, kid_from_adults, translate

from .forms import ComplaintRecordForm
from django.contrib.auth.decorators import login_required

from .models import ComplaintRecord, PeopleAdult, PeopleKid

family_reg = ''
singin = ''
home = 'index.html'
add_complaint_record = ''
com_lst = ''

from .forms import LivinPlaceForm, PeopleAdultForm, PeopleKidForm

# FOR GOVERMenT workers 
@login_required
def regfamily(request):
    if request.user.status == 'adm': 
        if request.method == 'POST':
            livin_space = LivinPlaceForm(request.POST)
            people_adult = PeopleAdultForm(request.POST, prefix='adult')
            people_kid = PeopleKidForm(request.POST, prefix='kid')

            if people_kid.is_valid(): 
                people_kid.save()

            if livin_space.is_valid() and people_adult.is_valid():
                livin_space.save()
                people_adult.save()
                return redirect('succes_reg') 
        else:
            livin_space = LivinPlaceForm()
            people_adult = PeopleAdultForm(prefix='adult')
            people_kid = PeopleKidForm(prefix='kid')
    else: 
        return redirect('home')

    return render(request, family_reg, {
        'living_place_form': livin_space,
        'people_adult_form': people_adult,
        'people_kid_form': people_kid,
    })

@login_required
def complaint_list(request):
    if request.user.status == 'adm': 
        complaint_lst = ComplaintRecord.objects.all()

        return render(request, com_lst, {'complaints': complaint_lst})
    else: 
        return redirect('home') 
    
@login_required
def users_lst(request): 
    if request.user.status == 'adm':  
        context = {'adults': []}

        people_adult = PeopleAdult.objects.all()

        for obj in people_adult: 
            people_context = {'adult': obj} 

            people_kids = kid_from_adults(obj)
            if people_kids != None: 
                people_context['kids'] = people_kids

            context['adults'].append(people_context)

        return render(request, com_lst, {'peoples': context})
    else: 
        return redirect('home') 
        


# FOR USErs
@login_required
def add_complaint_record(request):
    if request.method == 'POST':
        form = ComplaintRecordForm(request.POST)

        if form.is_valid():
            complaint_record = form.save(commit=False)
            complaint_record.text = translate(complaint_record.text)

            complaint_record.adult = get_adult(request.user)  # Assign the logged-in user to the complaint record
            complaint_record.save()
            return redirect('home')  # Replace 'complaint_list' with the URL or view name for the complaints list page

    else:
        form = ComplaintRecordForm()

    return render(request, add_complaint_record, {'form': form})

def loginuser(request): 
    if request.method == 'POST':
        signin_form = SignInForm(request.POST)

        if signin_form.is_valid():
            phone_number = signin_form.cleaned_data['phone_number']
            name = signin_form.cleaned_data['name']

            if people_exist(phone_number, name):
                user = authenticate(request, phone_number=phone_number, name=name, status = 'def')

                login(request, user)
                messages.success(request, 'Successfully signed in.')
                return redirect('succes_reg')  # Redirect to the dashboard or another page upon successful sign-in
            else:
                messages.error(request, 'Invalid phone number or name')

    else:
        signin_form = SignInForm()

    return render(request, singin, {'signin_form': signin_form})

def homepage(request): 
    try: 
        adult = get_adult(request.user)
        if request.user.status == 'adm': 
            return redirect('complient_list')
        else: 
            user_complients = get_complient(adult)
            return render(request, home, {'complients': user_complients})
    except: 
        return render(request, home, {})


