from rest_framework import serializers
from .models import Article, Certificate
from .models import Language
from .models import Career
from .models import SelfIntroduction
from accounts.serializers import UserSerializer
# from .models import Image

class ArticleListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Article
        fields = ('user', 'image', 'name', 'date_of_birth', 'email', 'phone_number')

class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    image = serializers.ImageField(use_url=True, required=False)

    class Meta:
        model = Article
        fields = '__all__'

class CertificateListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Certificate
        fields = '__all__'

class CertificateSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Certificate
        fields = '__all__'

class LanguageListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Language
        fields = '__all__'

class LanguageSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Language
        fields = '__all__'

class CareerListSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Career
        fields = '__all__'

class CareerSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = Career
        fields = '__all__'        

class SelfintroductionSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    class Meta:
        model = SelfIntroduction
        fields = '__all__'

# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Image
#         fields = '__all__'