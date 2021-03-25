from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # index page
    path('', views.Index, name='index'),
    path('blog-details/<str:slug>', views.BlogDetails, name='details'),
    path('likeinc/<str:slug>', views.Likes, name='likeinc'),
    path('lcomment', views.LeaveComment , name='lcomment'),
    path('blog', views.BlogList, name='blog_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
