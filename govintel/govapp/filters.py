from .models import PeopleAdult, PeopleKid, ComplaintRecord
from googletrans import Translator
import pickle

print('initialize types...')
tr = Translator()
spam_model_fp = 'static/models/spam-filtering.pkl'

problem_type_fp = 'static/models/problem-type.pkl'
label_encoder_fp = 'static/models/problem-label-encoder.pkl'

rating_fp = 'static/models/rating.pkl'

print('Loading models...')

with open(spam_model_fp, 'rb') as model_file: 
    spam_model = pickle.load(model_file)
    # model_file.close()

with open(problem_type_fp, 'rb') as model_file: 
    ptype_model = pickle.load(model_file)
    # model_file.close()
    
with open(label_encoder_fp, 'rb') as enc_file: 
    ptype_lencoder = pickle.load(enc_file)
    # enc_file.close()

with open(rating_fp, 'rb') as model_file: 
    rating_model = pickle.load(model_file)
    # model_file.close()

print('Loading fuctions')
def filter_spam(text): 
    is_spam = spam_model.predict([text])[0]
    if int(is_spam) == 1: 
        return False
    else: 
        return True

def problem_rate(text):
    rate = rating_model.predict([text])[0]
    if rate > 2.: 
        return 'Critical'
    elif rate > 1 and rate < 2:
        return 'Serious' 
    elif rate < 1: 
        return 'Not Serious'

def  problem_class(text): 
    pred  = ptype_model([text])
    revert = ptype_lencoder.revert(pred)
    return revert[0]

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
    
def translate(text): 
    translation = tr.translate(text, dest='eng')
    return translation.text
