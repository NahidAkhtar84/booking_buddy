from django.contrib import admin
from django.urls import path, include
from event_booking.views import add_event, EventBook, update, remove
from general.views import AboutUs
from admin_site import views as ad_site

urlpatterns = [
    # user View
    # path('calendar/', calendar, name='calendar'),
    path('add_event$', add_event, name='add_event'),
    path('eventbookingpage', EventBook.as_view(), name='eventbookingpage'),
    path('booking', EventBook.as_view(), name='booking'),
    path('update$', update, name='update'),
    path('remove', remove, name='remove'),
    path('aboutus', AboutUs.as_view(), name='aboutus'),
    path('eventsdatewise', AboutUs.as_view(), name='aboutus'),

    # DJ Admin Section
    path('admin/', admin.site.urls),

    # custom admin
    path('admin-site/', include('admin_site.urls')),
    path('login/', ad_site.Login, name='login'),
    path('logout/', ad_site.logout_user, name='logout'),
    path('', include('blog.urls')),
]
