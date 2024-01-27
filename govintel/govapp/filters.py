from .models import PeopleAdult, PeopleKid, ComplaintRecord

def people_exist(phone_number = None, name = None) -> bool:
    # Query the PeopleAdult model to check if a person with the given phone number and passport card number exists
    person_exists = PeopleAdult.objects.filter(phone_number=phone_number, name=name).exists()

    return person_exists

def get_adult(user): 
    phone_number = user.phone_number
    name = user.name

    person = PeopleAdult.objects.filter(phone_number=phone_number, name=name)
    if person.exists(): 
        return person[0]
    else: 
        return None 

def get_complient(adult): 
    complient = ComplaintRecord.objects.filter(adult=adult)
    if complient.exists(): 
        return complient.all()
    else: 
        return None

def kid_from_adults(adult): 
    kids = PeopleKid.objects.filter(adult=adult).all() 
    if kids.exists(): 
        return kids.all()
    else: 
        return None