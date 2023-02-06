from django.urls import path
from rest_framework import routers

from .views import product, category


router = routers.DefaultRouter()
router.register(r'product', product.ProductView, basename='product')
router.register(r'category', category.CategoryView, basename='category')

urlpatterns = [
    path('category/<int:pk>/products', category.CategoryProductsView.as_view(),
         name="category-products"),
    path('category/products', category.AllCategoryProductsView.as_view(),
         name="all-category-products"),
    path('test/api',category.TestAPI.as_view(),name="test-api")
]

urlpatterns += router.urls
