from django.shortcuts import render, redirect
from django.views import View
from .models import about_us, company_address, copyright, sociallinks
from .forms import AboutForm, SocialLinkForm
import os
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

class AboutUs(View):
    def get(self, request):
        aboutus = about_us.objects.first()
        context = {
            'aboutus': aboutus,
        }
        return render(request, 'index/aboutus.html', context)


@login_required(login_url='login')
def About(request):
    about = about_us.objects.get()
    cr_info = copyright.objects.get()

    context = {
        'about': about,
        'copyright': cr_info
    }
    return render(request, 'admin/about/about_us.html', context)


@login_required(login_url='login')
def EditAbout(request, pk):
    about_info = about_us.objects.get(id=pk)
    copyright_info = copyright.objects.first()

    form = AboutForm(request.POST, request.FILES)
    img = request.FILES.get('image')
    if img:
        if form.is_valid():
            about = about_us(id=pk)
            about.title = form.cleaned_data['title']
            about.mobile = form.cleaned_data['mobile']
            about.image = form.cleaned_data['image']
            about.description = form.cleaned_data['details']

            # deleting old uploaded image.
            image_path = about.image.path
            if os.path.exists(image_path):
                os.remove(image_path)

            about.save()
            messages.success(request, 'Information Updated')
            return redirect("about-us")
    else:
        if request.method == 'POST':
            title = request.POST.get('title')
            mobile = request.POST.get('mobile')
            c_image = request.POST.get('current_image')
            description = request.POST.get('details')

            about_us.objects.filter(id=pk).update(title=title, mobile=mobile, image=c_image, description=description)
            messages.success(request, 'Information Updated')
            return redirect("about-us")

    context = {
        'about': about_info,
        'cpy': copyright_info
    }
    return render(request, 'admin/about/edit_about.html', context)


@login_required(login_url='login')
def EditCopy(request, pk):
    if request.method == 'POST':
        data = request.POST.get('cpy')

        copyright.objects.filter(id=pk).update(copyright=data)
        messages.success(request, 'Information Updated')
        return redirect('about-us')


@login_required(login_url='login')
def Address(request):
    address = company_address.objects.get()

    context = {
        'address': address
    }
    return render(request, 'admin/about/address.html', context)


@login_required(login_url='login')
def EditAddress(request, pk):
    ad_inf = company_address.objects
    ad_info = ad_inf.get(id=pk)

    if request.method == 'POST':
        data = request.POST
        title = data.get('title')
        title_desc = data.get('title_desc')
        address_title = data.get('address_title')
        phone = data.get('phone')
        email = data.get('email')
        address = data.get('details')

        ad_inf.filter(id=pk).update(title=title, title_desc=title_desc, address_title=address_title,
                                    phone=phone, email=email, address=address)

        messages.success(request, 'Information Updated')
        return redirect('address')

    context = {
        'add': ad_info
    }
    return render(request, 'admin/about/edit_address.html', context)


@login_required(login_url='login')
def SocialLinks(request):
    if request.method == 'POST':
        link_form = SocialLinkForm(request.POST)
        if link_form.is_valid():
            link = sociallinks()
            link.name = link_form.cleaned_data['name']
            link.link = link_form.cleaned_data['link']
            link.save()

        messages.success(request, 'A new Social Link added')
        return redirect('social')

    links = sociallinks.objects.all()
    context = {
        'links': links
    }
    return render(request, 'admin/about/social.html', context)


@login_required(login_url='login')
def EditSocial(request, pk):
    info = sociallinks.objects.get(id=pk)

    if request.method == 'POST':
        name = request.POST.get('name')
        link = request.POST.get('link')

        sociallinks.objects.filter(id=pk).update(name=name, link=link)
        messages.success(request, 'Information Updated')
        return redirect('social')

    context = {
        'info': info
    }
    return render(request, 'admin/about/edit_social.html', context)


@login_required(login_url='login')
def DeleteSocial(request, pk):
    sociallinks.objects.filter(id=pk).delete()
    messages.success(request, 'Link is deleted')
    return redirect('social')
