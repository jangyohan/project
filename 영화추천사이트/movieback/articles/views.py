from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated


from .models import Article, Comment
from .serializers import ArticleSerializer, ArticleListSerializer
from .serializers import CommentSerilizer, CommentListSerializer
# Create your views here.

@api_view(['GET'])
def index(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data)

@api_view(['GET'])
def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return Response({'message':'성공적으로 삭제'})

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleSerializer(data=request.data, instance=article)

    print('1')
    if serializer.is_valid(raise_exception=True):
        print('2')
        serializer.save(user=request.user)
        return Response({'message':'성공적으로 수정'})


@api_view(['GET'])
def comment(request):
    comments = Comment.objects.all()
    serializer = CommentListSerializer(comments, many=True)
    return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerilizer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, article_id=article_pk)
        return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_update_and_delete(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'PUT':
        serializer = CommentSerilizer(data=request.data, instance=comment)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response({'message':'성공적으로 수정'})
    else:
        comment.delete()
        return Response({'message':'성공적으로 삭제'})
        