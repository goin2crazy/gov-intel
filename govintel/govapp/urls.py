from django.urls import path
from .views import *

urlpatterns = [
    path('add/', add_complaint_record, name='add_complaint'),
    path('success/', successp, name='success_page'),

    path('accounts/login/', login_user, name='login_user'),
    path('', homepage, name='homepage'),
    

]

urlpatterns += [
    path('complaints/', complaint_list, name='complients_list'),
    path('adults/', users_list, name='adults_lists'),
    path('complaint-list-class/', ComplaintListView.as_view(), name='complaint_list_class'),
]