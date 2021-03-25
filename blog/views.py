from time import strptime

from django.shortcuts import render, redirect, HttpResponseRedirect
from event_booking.models import Events
from datetime import datetime, timedelta
from django.core.paginator import Paginator, EmptyPage
from admin_site.models import BlogPost, Comment
from general.models import about_us, company_address
from django.urls import reverse
from django.http import JsonResponse


# Create your views here.

def Index(request):
    all_events = Events.objects.filter(status='accepted')
    firstblog = BlogPost.objects.all().order_by('-date')[0]
    blogs = BlogPost.objects.all().order_by('-date')[1:3]
    aboutus = about_us.objects.first()
    comp_address = company_address.objects.first()
    dteve = request.GET.get('dateeve')
    if dteve:
        date = datetime.now()
        poj = date + timedelta(days=int(dteve))

    if dteve:
        recent_events = Events.objects.filter(status='accepted').filter(start__lte = poj, end__gte = poj).order_by('-start')
    else:
        recent_events = Events.objects.filter(status='accepted').filter(start__gte=datetime.now()).order_by('-start')


    page = request.GET.get('page', 1)
    paginator = Paginator(recent_events, 3)

    try:
        recent_events = paginator.page(page)
    except EmptyPage:
        recent_events = paginator.page(paginator.num_pages)


    context = {
        "events": all_events,
        "recent_events": recent_events,
        "blogs": blogs,
        "firstblog": firstblog,
        'aboutus': aboutus,
        'comp_address': comp_address,
        'n': range(5)
    }
    return render(request, 'index/index.html', context)


def BlogDetails(request, slug):
    details_post = BlogPost.objects.get(slug=slug)
    related = BlogPost.objects.filter(category=str(details_post.category)).exclude(title=str(details_post.title)).all() \
                  .order_by('date')[0:3]

    context = {
        'details': details_post,

        'related': related,
    }
    # return JsonResponse(context, safe=False)
    return render(request, 'index/blog_details.html', context)

def Likes(request, slug):
    bid = BlogPost.objects.get(slug=slug)
    field_obj = BlogPost._meta.get_field('likes')
    field_val = int(field_obj.value_from_object(bid))
    field_val += 1
    bid.likes = field_val
    bid.save()
    return redirect('details', slug=slug)

def LeaveComment(request):
    pt = request.POST
    bid = BlogPost.objects.get(slug=pt.get('bid'))
    # bid = BlogPost.objects.get(slug=slug)
    name = pt.get('name')
    email = pt.get('email')
    phone = pt.get('phone')
    message = pt.get('message')
    
    comment = Comment(
        blog = bid,
        name = name,
        phone = phone,
        email = email,
        message = message
                      )
    comment.save()
    
    return redirect("details", slug=pt.get('bid'))


def BlogList(request):
    blog_list = BlogPost.objects.all().order_by('-date')
    paginator = Paginator(blog_list, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'all_post': blog_list,
        'page_obj': page_obj
    }

    return render(request, 'index/blog_list.html', context)
