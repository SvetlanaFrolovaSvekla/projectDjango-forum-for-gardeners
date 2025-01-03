import uuid
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.timezone import now

# Создадим модель нашего покупателя, просто унаследовав пользователя Django
from django.urls import reverse

