from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Article
from .models import Certificate
from .models import Language
from .models import Career
from .models import SelfIntroduction
from recruitments.models import Recruitment
from .serializers import ArticleListSerializer, ArticleSerializer
from .serializers import CertificateListSerializer, CertificateSerializer
from .serializers import LanguageListSerializer, LanguageSerializer
from .serializers import CareerListSerializer, CareerSerializer
from .serializers import SelfintroductionSerializer

# 이력서
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def index(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def detail(request, article_pk):
    if request.method == 'GET':
        article = get_object_or_404(Article, pk=article_pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'PUT':
        article = get_object_or_404(Article, pk=article_pk)
        serializer = ArticleSerializer(data=request.data, instance=article)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response({'message': '성공적으로 수정'})

    elif request.method == 'DELETE':
        article = get_object_or_404(Article, pk=article_pk)
        article.delete()
        return Response({'message': '성공적으로 삭제'})

# 자격사항
@api_view(['GET'])
def certificate_list(request, article_pk):
    certificates = Certificate.objects.filter(article_id=article_pk)
    serializer = CertificateListSerializer(certificates, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def certificate_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CertificateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, article=article)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def certificate_detail(request, article_pk, certificate_pk):
    if request.method == 'GET':
        certificate = get_object_or_404(Certificate, pk=certificate_pk)
        serializer = CertificateSerializer(certificate)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        certificate = get_object_or_404(Certificate, pk=certificate_pk)
        serializer = CertificateSerializer(data=request.data, instance=certificate)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response({'message':'성공적으로 수정'})

    elif request.method == 'DELETE':
        certificate = get_object_or_404(Certificate, pk=certificate_pk)
        certificate.delete()
        return Response({'message': '성공적으로 삭제'})

# 어학사항
@api_view(['GET'])
def language_list(request, article_pk):
    languages = Language.objects.filter(article_id=article_pk)
    serializer = LanguageListSerializer(languages, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def language_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = LanguageSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, article=article)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def language_detail(request, article_pk, language_pk):
    if request.method == 'GET':
        language = get_object_or_404(Language, pk=language_pk)
        serializer = LanguageSerializer(language)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        language = get_object_or_404(Language, pk=language_pk)
        serializer = LanguageSerializer(data=request.data, instance=language)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response({'message':'성공적으로 수정'})

    elif request.method == 'DELETE':
        language = get_object_or_404(Language, pk=language_pk)
        language.delete()
        return Response({'message': '성공적으로 삭제'})

# 경력사항
@api_view(['GET'])
def career_list(request, article_pk):
    careers = Career.objects.filter(article_id=article_pk)
    serializer = CareerListSerializer(careers, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def career_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CareerSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, article=article)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def career_detail(request, article_pk, career_pk):
    if request.method == 'GET':
        career = get_object_or_404(Career, pk=career_pk)
        serializer = CareerSerializer(career)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        career = get_object_or_404(Career, pk=career_pk)
        serializer = CareerSerializer(data=request.data, instance=career)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response({'message':'성공적으로 수정'})

    elif request.method == 'DELETE':
        career = get_object_or_404(Career, pk=career_pk)
        career.delete()
        return Response({'message': '성공적으로 삭제'})

@api_view(['GET'])
def selfintroduction_list(request, article_pk, recruitment_pk):
    selfintroductions = SelfIntroduction.objects.filter(recruitment_id=recruitment_pk, article_id=article_pk)
    serializer = SelfintroductionSerializer(selfintroductions, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def selfintroduction_list2(request, article_pk):
    selfintroductions = SelfIntroduction.objects.filter(article_id=article_pk)
    serializer = SelfintroductionSerializer(selfintroductions, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def selfintroduction_create(request, article_pk, recruitment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    recruitment = get_object_or_404(Recruitment, pk=recruitment_pk)
    serializer = SelfintroductionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, article=article, recruitment=recruitment)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def selfintroduction_detail(request, article_pk, recruitment_pk, selfintroduction_pk):
    if request.method == 'GET':
        selfintroduction = get_object_or_404(SelfIntroduction, pk=selfintroduction_pk)
        serializer = SelfintroductionSerializer(selfintroduction)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        selfintroduction = get_object_or_404(SelfIntroduction, pk=selfintroduction_pk)
        serializer = SelfintroductionSerializer(data=request.data, instance=selfintroduction)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response({'message': '성공적으로 수정'})
        
    elif request.mehtod == 'DELETE':
        selfintroduction = get_object_or_404(SelfIntroduction, pk-selfintroduction_pk)
        selfintroduction.delete()
        return Response({'message': '성공적으로 삭제'})

@api_view(['POST'])
def search(request, query):
    # articles = Article.objects.filter(user__contains)
    articles = Article.objects.filter(name__contains=query)
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)