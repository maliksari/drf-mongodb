from django.db import models

from .base import BaseModel


class Category(BaseModel):
    category_name = models.CharField(
        null=True, blank=True, help_text="Kategori Adı", max_length=150)
    category_code = models.CharField(
        null=True, blank=True, help_text="Kategori kodu", max_length=150, unique=True)
