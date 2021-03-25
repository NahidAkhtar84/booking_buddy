from django.http import JsonResponse
from event_booking.models import Events
from django.views import View
from django.shortcuts import render, redirect
from event_management.utilities import twilioSMS
from general.models import about_us
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.


def add_event(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    event = Events(name=str(title), start=start, end=end)
    event.save()
    data = {}
    return JsonResponse(data)


def update(request):
    start = request.GET.get("start", None)
    end = request.GET.get("end", None)
    title = request.GET.get("title", None)
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.start = start
    event.end = end
    event.name = title
    event.save()
    data = {}
    return JsonResponse(data)


def remove(request):
    id = request.GET.get("id", None)
    event = Events.objects.get(id=id)
    event.delete()
    data = {}
    return JsonResponse(data)


class EventBook(View):
    # def get(self, request):
    #     return render(request, 'index/event_booking.html')

    def post(self, request):
        if request.method == 'POST':
            pst = request.POST
            name = pst.get('eventname')
            username = pst.get('username')
            phone = pst.get('mobilenumber')
            email = pst.get('email')
            start_date = pst.get('startdate')
            end_date = pst.get('enddate')
            # print("This is: ", start_date)
            event = Events(
                name=name,
                username=username,
                phone=phone,
                email=email,
                start=start_date,
                end=end_date
            )

            event.save()

            # Send SMS
            address = about_us.objects.values('mobile')
            ad_list = []

            for i in address:
                ad_list.append(i['mobile'])
            mobile = ' '.join(map(str, ad_list))

            try:
                body = f'This SMS is from Event Management APP and New Event From {event.username} and Contact ' \
                       f'{event.phone}'
                address = f'+88{mobile}'
                twilioSMS(body, address)
            except Exception:
                print(Exception)

            # context = {
            #     'mobile': str(address),
            #     'mbl': mobile
            # }
            # return JsonResponse(context)
            messages.success(request, 'We will be in contact soon.')
            return redirect('index')


# Custom Admin (Events) =========================================
@login_required(login_url='login')
def EventRequests(request):
    events = Events.objects.all().order_by('-id')
    context = {
        'events': events,
    }
    return render(request, 'admin/events/manage_events.html', context)


@login_required(login_url='login')
def AcceptEvent(request, pk):
    Events.objects.filter(id=pk).update(status='accepted')
    messages.success(request, 'New event request is accepted!')
    return redirect('all-events')


@login_required(login_url='login')
def RejectEvent(request, pk):
    Events.objects.filter(id=pk).delete()
    messages.warning(request, 'An Event Request is Deleted!!')
    return redirect('all-events')


@login_required(login_url='login')
def EditEvent(request, pk):
    event = Events.objects.filter(id=pk)
    event_info = event.get()

    if request.method == 'POST':
        data = request.POST.get
        name = data('name')
        username = data('username')
        phone = data('phone')
        email = data('email')
        start = data('startdate')
        end = data('enddate')
        status = data('status')
        color = data('color')
        text_color = data('text_color')

        event.update(name=name, username=username, phone=phone, email=email,
                     start=start, end=end, status=status, color=color, textcolor=text_color)
        messages.success(request, 'Information Updated Successfully!')
        return redirect('all-events')

    context = {
        'info': event_info
    }
    return render(request, 'admin/events/edit_event.html', context)
