from django.shortcuts import render, HttpResponse, redirect

from backend.serializer import ProductsSerializer
from .models import Category, Products, About, Member, Contact
from django.core.mail import send_mail
from django.contrib import messages
from rest_framework import viewsets


class ProductsApiviews(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

# Create your views here.


def index(request):
    data = {
        'categoryData': Category.objects.all(),
        'aboutData': About.objects.all()
    }
    return render(request, 'pages/home/home.html', data)


def about(request):
    data = {
        'aboutData': About.objects.all(),
        'memberData': Member.objects.all()
    }
    return render(request, 'pages/about/about.html', data)


def all_products(request, slug):
    data = {
        'allProduct': Products.objects.get(slug=slug),
        'categoryData': Category.objects.all()
    }
    return render(request, 'pages/all-products.html', data)


def product_category(request):
    data = {
        'categoryData': Category.objects.all()
    }
    return render(request, 'pages/product-category.html', data)


def inside_category(request, cat_id):
    data = {
        'categoryData': Category.objects.all(),
        'insidecatData': Products.objects.filter(cat_id=cat_id)
    }
    return render(request, 'pages/inside-category.html', data)


def contact(request):
    if request.method == "POST":
        fname = request.POST['fname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        send_mail(
            'subject',
            'message',
            'email',
            ['djangonewsportalproject2001@gmail.com'],
            fail_silently=False,)
        messages.success(request, 'mail sent sucessfully')
        Contact.objects.create(fname=fname, email=email,
                               subject=subject, message=message)
        return redirect(request.META.get('HTTP_REFERER'))

    else:
        return render(request, 'pages/contact.html')
