from django.urls import path
from .views import (loginpage,registerpage,why_zaana,policy,about,password_reset,createnote,signout,
 delete_note,edit_note,download_note,view_notes, search_note,quotes)


urlpatterns=[

    path('',loginpage,name='login'),
    path('register',registerpage,name='register'),
    path('why_zaana',why_zaana,name='why'),
    path('policy',policy,name ='policy'),
    path('about',about,name='about'),
    path('password_reset',password_reset,name='password_reset'),
    path('create_note', createnote,name='create_note'),
    path('<id>/view_notes',view_notes,name='view_note'),
    path('logout',signout,name='logout'),
    path('<id>/edit_note',edit_note,name='edit_note'),
    path('<id>/delete_note',delete_note,name='delete_note'),
    path('<id>/download_note',download_note,name='download_note'),
    path('search_note',search_note,name='searcher'),
    path('quote_of_the_day',quotes,name='quote'),
    

]