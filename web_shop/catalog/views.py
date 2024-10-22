from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Contact, Product, Category


# Create your views here.
def home_views(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        image = request.POST.get("image")
        categories = Category.objects.all()
        category = [category for category in categories if request.POST.get("category") == category.name]
        price = request.POST.get("price")

        new_product = Product.objects.create(
            name=name, description=description, image=image, category=category[0], price=price
        )

        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Вы добавили товар - {name}!")

    categories = Category.objects.all()
    products = Product.objects.all()

    paginator = Paginator(products, 3)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    context = {
        "products": products,
        "categories": categories,
        "page_obj": page_obj,
    }

    return render(request, "catalog/home.html", context)


def category_views(request):
    return render(request, "catalog/category.html")


def catalog_views(request):
    return render(request, "catalog/catalog.html")


def contact_views(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        print(name)
        print(email)
        # Здесь мы просто возвращаем простой ответ
        return HttpResponse(f"Спасибо, {name}! Ваше email {email} получен.")
    contacts = Contact.objects.get(id=1)
    contact = {"phone_number": contacts.phone_number, "address": contacts.address, "email": contacts.email}
    return render(request, "catalog/contact.html", contact)


def product_views(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {"product": product}
    return render(request, "catalog/product.html", context)