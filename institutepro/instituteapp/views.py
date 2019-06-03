from django.shortcuts import render
from .models import FeedbackData, ContactData, CoursesData
from .forms import FeedBackFrom, ContactForm
from django.http.response import HttpResponse
import datetime

date1 = datetime.datetime.now()

def main_page(request):
    return render(request, 'base.html')


def home_page(request):
    return render(request, 'home_page.html')


def contact_page(request):
    if request.method == 'POST':
        cform = ContactForm(request.POST)
        if cform.is_valid():
            name = cform.cleaned_data.get('name')
            email = cform.cleaned_data.get('email')
            mobile = cform.cleaned_data.get('mobile')
            courses = cform.cleaned_data.get('courses')
            shifts = cform.cleaned_data.get('shifts')
            locations = cform.cleaned_data.get('locations')
            gender = cform.cleaned_data.get('gender')
            start_date = cform.cleaned_data.get('start_date')

            data = ContactData(
                name=name,
                email=email,
                mobile=mobile,
                courses=courses,
                shifts=shifts,
                location=locations,
                gender=gender,
                start_date=start_date
            )
            data.save()
            cform = ContactForm()
            return render(request, 'contact_page.html',{'cform':cform})
        else:
            return HttpResponse('Invalid Data')
    else:
        cform = ContactForm()
        return render(request, 'contact_page.html',{'cform':cform})


def courses_page(request):
    courses = CoursesData.objects.all()
    return render(request, 'courses_page.html', {'courses': courses})


def feedback_page(request):
    if request.method == 'POST':
        fform = FeedBackFrom(request.POST)
        if fform.is_valid():
            name = request.POST.get('name')
            rating = request.POST.get('rating')
            feedback = request.POST.get('feedback')

            data = FeedbackData(
                name=name,
                rating=rating,
                feedback=feedback,
                date=date1
            )
            data.save()
            fform = FeedBackFrom()
            fdata = FeedbackData.objects.all()
            return render(request, 'feedback_page.html', {'fform': fform, 'fdata': fdata})
        else:
            return HttpResponse("Invalid User Data")

    else:
        fform = FeedBackFrom()
        fdata = FeedbackData.objects.all()
        return render(request, 'feedback_page.html', {'fform': fform, 'fdata': fdata})






def team_page(request):
    return render(request, 'team_page.html')


def gallery_page(request):
    return render(request, 'gallery_page.html')