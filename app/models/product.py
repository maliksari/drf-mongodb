from django.db import models

from .base import BaseModel
from app.models import Category


class Product(BaseModel):
    product_name = models.CharField(
        blank=False, null=False, max_length=250, help_text="Ürün adı")
    product_code = models.CharField(
        blank=False, null=False, max_length=64, unique=True)
    category = models.ManyToManyField(
        Category, blank=True, related_name='products')
