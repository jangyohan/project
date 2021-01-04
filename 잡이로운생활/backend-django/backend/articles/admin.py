from django.contrib import admin
from .models import Article
from .models import Certificate
from .models import Career
from .models import SelfIntroduction
# Register your models here.

admin.site.register(Article)
admin.site.register(Certificate)
admin.site.register(Career)
admin.site.register(SelfIntroduction)