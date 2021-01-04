from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer

from allauth.account import app_settings as allauth_settings
from allauth.utils import email_address_exists
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email

from .models import Transaction
from articles.models import Article

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
  password1 = serializers.CharField(required=True, write_only=True)
  password2 = serializers.CharField(required=True, write_only=True)
  class Meta:
    model = User
    fields = ('id', 'email', 'flag', 'first_name', 'last_name', 'password1', 'password2', 'wallet_addr', 'balance', 'it', 'electric'
    , 'semiconductor', 'design', 'eng')

  def validate_password1(self, password):
      return get_adapter().clean_password(password)

  def validate(self, data):
      if data['password1'] != data['password2']:
          raise serializers.ValidationError(
              ("비밀번호가 일치하지 않습니다."))
      return data

  def get_cleaned_data(self):
        return {
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }

  def save(self, request):
      adapter = get_adapter()
      user = adapter.new_user(request)
      self.cleaned_data = self.get_cleaned_data()
      adapter.save_user(request, user, self)
      setup_user_email(request, user, [])
      user.save()
      return user



## 구매 아이템 목록
class ItemListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Article
        fields = '__all__'

## 트랜잭션 목록
class TransListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'