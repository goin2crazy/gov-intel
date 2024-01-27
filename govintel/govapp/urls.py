from django.urls import path
from .views import (
    regfamily,
    complaint_list,
    users_lst,
    add_complaint_record,
    loginuser,
    homepage,
)

urlpatterns = [
    path('regfamily/', regfamily, name='regfamily'),
    path('complaint_list/', complaint_list, name='complaint_list'),
    path('users_lst/', users_lst, name='users_lst'),
    path('add_complaint_record/', add_complaint_record, name='add_complaint_record'),
    path('loginuser/', loginuser, name='loginuser'),
    path('', homepage, name='home'),
]
