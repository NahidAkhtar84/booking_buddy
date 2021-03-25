from django.urls import path
from . import views
from event_booking import views as event_views
from general import views as gen_views

urlpatterns = [
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('write-post/', views.WritePost, name='write-post'),
    path('manage-post/', views.ManagePost, name='manage-post'),
    path('edit-post/<str:pk>', views.EditPost, name='edit-post'),
    path('delete-post/<str:pk>', views.DeletePost, name='delete-post'),

    # Events Page
    path('event-requests/', event_views.EventRequests, name='all-events'),
    path('event/accept/<str:pk>', event_views.AcceptEvent, name='accept'),
    path('event/reject/<str:pk>', event_views.RejectEvent, name='reject'),
    path('event/edit/<str:pk>', event_views.EditEvent, name='edit-event'),

    # Website Information
    path('about-us/', gen_views.About, name='about-us'),
    path('edit-about/<str:pk>', gen_views.EditAbout, name='edit-about'),
    path('edit-cpy/<str:pk>', gen_views.EditCopy, name='edit-cpy'),

    # Address
    path('address/', gen_views.Address, name='address'),
    path('edit-address/<str:pk>', gen_views.EditAddress, name='edit-address'),

    # Social Links
    path('social/', gen_views.SocialLinks, name='social'),
    path('link-edit/<str:pk>', gen_views.EditSocial, name='edit-link'),
    path('delete-link/<str:pk>', gen_views.DeleteSocial, name='delete-link'),
]
