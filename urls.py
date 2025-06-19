from django.urls import include,path
from .import views
from .views import job_post, job_list
from .views import donation_view

urlpatterns = [
    path('',views.index),
    path('index',views.index,name="index"),
    path('index1',views.index1,name="index1"),
    path('search/', views.search_alumni, name='search_alumni'),
    path('AlmaShines/Logout', views.Logout, name="Logout"),
    path('login/',views.alumni_login, name="alumni_login"),
    path('thank-you/', views.thank_you, name='thank_you'),
    path('event/<int:event_id>/', views.events1, name='events1'),
    path('events1/', views.events1, name='events1'),
    path('event/<int:event_id>/', views.events2, name='events2'),
    path('events2/', views.events2, name='events2'),
    path('event/<int:event_id>/', views.event3, name='event3'),
    path('event3/', views.event3, name='event3'),
    path('event/<int:event_id>/', views.event4, name='event4'),
    path('event4/', views.event4, name='event4'),
    path('event/<int:event_id>/', views.event5, name='event5'),
    path('event5/', views.event5, name='event5'),
    path('event/<int:event_id>/', views.event6, name='event6'),
    path('event6/', views.event6, name='event6'),
    path('jobs/post/', job_post, name='job_post'),  # URL to post a job
    path('jobs/', job_list, name='job_list'),
    path('register/', views.alumni_register, name='alumni_register'), 
    path('donate/', views.donation_view, name='donate'),
    path('payment/', views.payment_view, name='payment'),
    path('thank-you/<int:donation_amount>/', views.thank_you, name='thank_you'),
    path('about/', views.about_us, name='about'),
    path('reviews/', views.review_page, name='reviews'),
    path('reviews/', views.review_page, name='reviews'),
    
]
    


    


