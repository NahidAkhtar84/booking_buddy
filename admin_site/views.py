from django.shortcuts import render, redirect
from admin_site.forms import BlogPostForm
from .models import BlogPost
import os
from datetime import date, datetime, timedelta
from django.http import JsonResponse
from event_booking.models import Events
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



# Create your views here.

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Username or Password is incorrect!!')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'Logged Out')
    return redirect('login')


@login_required(login_url='login')
def Dashboard(request):
    all_events = Events.objects.filter(status='accepted')
    total_events = Events.objects.filter(status='accepted').filter(end__lte=datetime.now()).count()
    # This months events number
    this_month = datetime.now().month
    current_month_events = Events.objects.filter(status='accepted').filter(start__month=this_month).count()

    # Groth than previous month
    todayh = date.today()
    firstday = todayh.replace(day=1)
    lastMonthdate = firstday - timedelta(days=1)
    lastMonth = lastMonthdate.month
    last_month_events = Events.objects.filter(status='accepted').filter(start__month=lastMonth).count()
    growth =(current_month_events - last_month_events)*10

    # Month wise data of the year
    data = []
    for i in range(1, 13):
        month_data_count = Events.objects.filter(status='accepted').filter(start__month=i).count()
        data.append(month_data_count)
    print("data", type(data))

    # pie chart
    accepted_events = Events.objects.filter(status='accepted').filter(start__month=this_month).count()
    pending_events = Events.objects.filter(status='pending').filter(start__month=this_month).count()

    context = {
        "events": all_events,
        "total_events": total_events,
        "current_month_events": current_month_events,
        "last_month_events": last_month_events,
        "accepted_events": accepted_events,
        "pending_events": pending_events,
        "growth": growth,
        "data": data,
    }
    return render(request, 'admin/contents/dashboard.html', context)


@login_required(login_url='login')
def WritePost(request):
    if request.method == 'POST':
        post_form = BlogPostForm(request.POST, request.FILES)
        if post_form.is_valid():
            blog = BlogPost()
            blog.title = post_form.cleaned_data['title']
            blog.category = post_form.cleaned_data['category']
            blog.images = post_form.cleaned_data['image']
            blog.details = post_form.cleaned_data['details']

            blog.save()

        messages.success(request, 'A New Blog Post Added.')
        return redirect('manage-post')
    else:
        post_form = BlogPostForm()
    # return JsonResponse(context, safe=False)
    return render(request, 'admin/contents/write_blog.html')


@login_required(login_url='login')
def ManagePost(request):
    posts = BlogPost.objects.all().order_by('-id')

    context = {
        'posts': posts,
    }
    return render(request, 'admin/contents/manage_post.html', context)


@login_required(login_url='login')
def EditPost(request, pk):
    post = BlogPost.objects.get(id=pk)

    form = BlogPostForm(request.POST, request.FILES)

    img = request.FILES.get('image')
    if img:
        if form.is_valid():
            blog = BlogPost(id=pk)
            blog.title = form.cleaned_data['title']
            blog.category = form.cleaned_data['category']
            blog.images = form.cleaned_data['image']
            blog.details = form.cleaned_data['details']
            blog.date = date.today()

            # deleting old uploaded image.
            image_path = post.images.path
            if os.path.exists(image_path):
                os.remove(image_path)

            blog.save()
            messages.success(request, 'Information Updated')
            return redirect("manage-post")
    else:
        if request.method == 'POST':
            title = request.POST.get('title')
            category = request.POST.get('category')
            c_image = request.POST.get('current_image')
            details = request.POST.get('details')

            BlogPost.objects.filter(id=pk).update(title=title, category=category, images=c_image, details=details,
                                                  date=date.today())
            messages.success(request, 'Information Updated')
            return redirect("manage-post")
    context = {
        'post': post
    }
    # return JsonResponse(context, safe=False)
    return render(request, 'admin/contents/edit_post.html', context)


@login_required(login_url='login')
def DeletePost(request, pk):
    post = BlogPost.objects.get(id=pk)
    post.delete()
    image_path = post.images.path
    if os.path.exists(image_path):
        os.remove(image_path)
    return redirect('manage-post')
