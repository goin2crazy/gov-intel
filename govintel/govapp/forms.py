from django import forms
from .models import LivinPlace, PeopleAdult, PeopleKid

class SignInForm(forms.Form):
    phone_number = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Phone Number'}))
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Jamshidbek'}))


class LivinPlaceForm(forms.ModelForm):
    class Meta:
        model = LivinPlace
        fields = ['location', 'status']

class PeopleAdultForm(forms.ModelForm):
    class Meta:
        model = PeopleAdult
        fields = ['name', 'family_name', 'surname', 'phone_number', 'passport_card_number',
                  'living_place', 'birth_date', 'work', 'financial_status', 'property', 'other_information']

class PeopleKidForm(forms.ModelForm):
    parents = forms.ModelMultipleChoiceField(queryset=PeopleAdult.objects.all())

    class Meta:
        model = PeopleKid
        fields = ['name', 'family_name', 'surname', 'birth_date', 'living_place',
                  'property', 'school', 'parents', 'other_information']
        
from .models import ComplaintRecord

class ComplaintRecordForm(forms.ModelForm):
    class Meta:
        model = ComplaintRecord
        fields = ['text', 'location', 'datetime']