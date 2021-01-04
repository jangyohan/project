from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager

class User(AbstractUser):
  flag = models.IntegerField(blank=True, default=1)
  balance = models.IntegerField(blank=True, default=0)
  wallet_addr = models.CharField(max_length=120, blank=True, default='')
  it = models.IntegerField(blank=True, default=0)
  electric = models.IntegerField(blank=True, default=0)
  semiconductor = models.IntegerField(blank=True, default=0)
  design = models.IntegerField(blank=True, default=0)
  eng = models.IntegerField(blank=True, default=0)
  username = None
  email = models.EmailField(_('email address'), unique=True)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  objects = CustomUserManager()


  
  def __str__(self):
      return self.email

# Create your models here.

class Transaction(models.Model):
    tx_hash = models.CharField(max_length=120)
    blockHash = models.CharField(max_length=120)
    blockNumber = models.IntegerField()
    from_adrr = models.CharField(max_length=120)
    to_addr = models.CharField(max_length=120)
    from_pk = models.IntegerField()
    to_pk = models.IntegerField()
    gas = models.IntegerField()
    gasPrice = models.IntegerField()
    nonce = models.IntegerField()
    r = models.CharField(max_length=120)
    s = models.CharField(max_length=120)
    v = models.CharField(max_length=120)
    value = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)