from django.urls import path

from . import views

app_name = "catalog"

urlpatterns = [
    path("home_views/", views.ProductListView.as_view(), name="home_views"),
    path("contact_views/", views.contact_views, name="contact_views"),
    path("category_views/", views.category_views, name="category_views"),
    path("catalog_views/", views.catalog_views, name="catalog_views"),
    path("product_views/<int:pk>/", views.ProductDetailView.as_view(), name="product_views"),
]
