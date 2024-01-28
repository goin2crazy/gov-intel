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
    is_spam = spam_model.predict([f"Subject: {text}"])[0]
    print(f"{text} is spam with {is_spam * 100}%")
    if is_spam > 0.4: 
        return False
    else: 
        return True

def problem_rate(text):
    rate = rating_model.predict([text])[0]
    if rate > 2.: 
        return 3
    elif rate > 1 and rate < 2:
        return 2 
    elif rate < 1: 
        return 1
    
def problem_class(text):
    pred = ptype_model.predict([text])
    reverted = ptype_lencoder.inverse_transform(pred)
    return reverted[0]

def kid_from_adults(adult): 
    kids = PeopleKid.objects.filter(adult=adult).all() 
    if kids.exists(): 
        return kids.all()
    else: 
        return None
    
def translate(text): 
    translation = tr.translate(text, dest='en')
    return translation.text
