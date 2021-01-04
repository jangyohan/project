from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Recruitment
from .models import Introduction
from .serializers import RecruitmentListSerializer, RecruitmentSerializer
from .serializers import IntroductionSerializer

from datetime import datetime
# Create your views here.

# 공고
@api_view(['GET'])
def index(request):
    recruitments = Recruitment.objects.all()
    serializer = RecruitmentListSerializer(recruitments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def showlist(request):
    today = datetime.today().strftime("%Y%m%d%H%M")
    recruitments = Recruitment.objects.filter(deadline__gte=today).order_by('deadline')
    serializer = RecruitmentListSerializer(recruitments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def showlist2(request):
    today = datetime.today().strftime("%Y%m%d%H%M")
    recruitments = Recruitment.objects.filter(deadline__gte=today).order_by('?')
    serializer = RecruitmentListSerializer(recruitments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def calendar(request, date):
    recruitments = Recruitment.objects.filter(startdate__lte=date, deadline__gte=date)
    serializer = RecruitmentListSerializer(recruitments, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    serializer = RecruitmentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def detail(request, recruitment_pk):
    if request.method == 'GET':
        recruitment = get_object_or_404(Recruitment, pk=recruitment_pk)
        serializer = RecruitmentSerializer(recruitment)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        recruitment = get_object_or_404(Recruitment, pk=recruitment_pk)
        serializer = RecruitmentSerializer(data=request.data, instance=recruitment)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response({'message': '성공적으로 수정'})
    
    elif request.method == 'DELETE':
        recruitment = get_object_or_404(Recruitment, pk=recruitment_pk)
        recruitment.delete()
        return Response({'message': '성공적으로 삭제'})

# 자기소개
@api_view(['GET'])
def introduction_list(request, recruitment_pk):
    introductions = Introduction.objects.filter(recruitment_id=recruitment_pk)
    serializer = IntroductionSerializer(introductions, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def introduction_create(request, recruitment_pk):
    recruitment = get_object_or_404(Recruitment, pk=recruitment_pk)
    serializer = IntroductionSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, recruitment=recruitment)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def introduction_detail(request, recruitment_pk, introduction_pk):
    if request.method == 'GET':
        introduction = get_object_or_404(Introduction, pk=introduction_pk)
        serializer = IntroductionSerializer(introduction)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        introduction = get_object_or_404(Introduction, pk=introduction_pk)
        serializer = IntroductionSerializer(data=request.data, instance=introduction)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response({'message': '성공적으로 수정'})
    
    elif request.method == 'DELETE':
        introduction = get_object_or_404(Introduction, pk=introduction_pk)
        introduction.delete()
        return Response({'message': '성공적으로 삭제'})

@api_view(['GET'])
def apply(request, recruitment_pk, article_pk):
    recruitment = get_object_or_404(Recruitment, pk=recruitment_pk)
    if recruitment.applicants.filter(pk=article_pk).exists():
        recruitment.applicants.remove(article_pk)
    else:
        recruitment.applicants.add(article_pk)
    return Response({'message': '성공!'})