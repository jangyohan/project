from django.db import models
from django.conf import settings
# from recruitments.models import Recruitment
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Article(models.Model):
    # 개인정보
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True
    )
    image = models.ImageField(upload_to="media", null=True, blank=True)
    imgae_thumnail = ImageSpecField(source='image',
                        processors=[ResizeToFill(300,300)],
                        format='JPEG',
                        options={'quality' : 60}
    )
    name = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length=50, null=True, blank=True)
    # 병역사항
    military_classification = models.CharField(max_length=100, null=True, blank=True)
    military_branch = models.CharField(max_length=100, null=True, blank=True)
    military_rank = models.CharField(max_length=100, null=True, blank=True)
    military_completed = models.CharField(max_length=100, null=True, blank=True)
    military_completed_reason = models.CharField(max_length=100, null=True, blank=True)
    military_start = models.CharField(max_length=100, null=True, blank=True)
    military_end = models.CharField(max_length=100, null=True, blank=True)
    # 고등학교
    highschool_name = models.CharField(max_length=100, null=True, blank=True)
    highschool_classification = models.CharField(max_length=100, null=True, blank=True)
    highschool_location = models.CharField(max_length=100, null=True, blank=True)
    highschool_entrance_year = models.CharField(max_length=100, null=True, blank=True)
    highschool_graduation_year = models.CharField(max_length=100, null=True, blank=True)
    # 전문대
    college_name = models.CharField(max_length=100, null=True, blank=True)
    college_classification = models.CharField(max_length=100, null=True, blank=True)
    college_location = models.CharField(max_length=100, null=True, blank=True)
    college_entrance_year = models.CharField(max_length=100, null=True, blank=True)
    college_graduation_year = models.CharField(max_length=100, null=True, blank=True)
    college_major = models.CharField(max_length=100, null=True, blank=True)
    college_minor = models.CharField(max_length=100, null=True, blank=True)
    college_grade = models.FloatField(null=True, blank=True)
    college_total = models.FloatField(null=True, blank=True)
    # 대학교
    university_name = models.CharField(max_length=100, null=True, blank=True)
    university_classification = models.CharField(max_length=100, null=True, blank=True)
    university_location = models.CharField(max_length=100, null=True, blank=True)
    university_entrance_year = models.CharField(max_length=100, null=True, blank=True)
    university_graduation_year = models.CharField(max_length=100, null=True, blank=True)
    university_major = models.CharField(max_length=100, null=True, blank=True)
    university_minor = models.CharField(max_length=100, null=True, blank=True)
    university_grade = models.FloatField(null=True, blank=True)
    university_total = models.FloatField(null=True, blank=True)  
    # 석사
    master_name = models.CharField(max_length=100, null=True, blank=True)
    master_classification = models.CharField(max_length=100, null=True, blank=True)
    master_location = models.CharField(max_length=100, null=True, blank=True)
    master_entrance_year = models.CharField(max_length=100, null=True, blank=True)
    master_graduation_year = models.CharField(max_length=100, null=True, blank=True)
    master_major = models.CharField(max_length=100, null=True, blank=True)
    master_minor = models.CharField(max_length=100, null=True, blank=True)
    master_grade = models.FloatField(null=True, blank=True)
    master_total = models.FloatField(null=True, blank=True) 
    # 박사
    doctor_name = models.CharField(max_length=100, null=True, blank=True)
    doctor_classification = models.CharField(max_length=100, null=True, blank=True)
    doctor_location = models.CharField(max_length=100, null=True, blank=True)
    doctor_entrance_year = models.CharField(max_length=100, null=True, blank=True)
    doctor_graduation_year = models.CharField(max_length=100, null=True, blank=True)
    doctor_major = models.CharField(max_length=100, null=True, blank=True)
    doctor_minor = models.CharField(max_length=100, null=True, blank=True)
    doctor_grade = models.FloatField(null=True, blank=True)
    doctor_total = models.FloatField(null=True, blank=True)
    # 기타
    veterans_classification = models.CharField(max_length=100, null=True, blank=True)
    veterans_number = models.CharField(max_length=100, null=True, blank=True)
    obstacle_classification = models.CharField(max_length=100, null=True, blank=True)
    obstacle_grade = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    buyer = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='seller', blank=True)

class Certificate(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    publisher = models.CharField(max_length=100, null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)

class Language(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    classification = models.CharField(max_length=100, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    score = models.CharField(max_length=100, null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)

class Career(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)  
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True, blank=True)
    start_term = models.CharField(max_length=100, null=True, blank=True)
    end_term = models.CharField(max_length=100, null=True, blank=True)
    retirement_reason = models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    rank = models.CharField(max_length=100, null=True, blank=True)
    duty = models.CharField(max_length=100, null=True, blank=True)
    statement = models.TextField()

class SelfIntroduction(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    recruitment = models.ForeignKey("recruitments.Recruitment", on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)

# 다중 이미지 업로드
# class Image(models.Model):
#     article = models.ForeignKey(Article, blank=True, null=True, on_delete=models.CASCADE)
#     image = ProcessedImageField(
#         upload_to = 'media', # 저장 위치
#         processors = [ResizeToFill(300, 300)],
#         format = 'JPEG',
#         options = {'quality': 60},
#         null = True
#     )