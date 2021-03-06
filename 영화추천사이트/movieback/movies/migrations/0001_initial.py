# Generated by Django 2.1.15 on 2020-06-17 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Best_Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('count', models.IntegerField()),
                ('director', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='M_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('post', models.CharField(max_length=10000)),
                ('score', models.CharField(max_length=20)),
                ('genre', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=100)),
                ('pubDate', models.IntegerField()),
                ('director', models.CharField(max_length=100)),
                ('actor', models.CharField(max_length=100)),
                ('userRating', models.FloatField(max_length=100)),
                ('key_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MovieData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieCd', models.CharField(default='null', max_length=10000)),
                ('movieNm', models.CharField(default='null', max_length=10000)),
                ('movieNmEn', models.CharField(default='null', max_length=10000)),
                ('prdtYear', models.CharField(default='null', max_length=10000)),
                ('openDt', models.CharField(default='null', max_length=10000)),
                ('typeNm', models.CharField(default='null', max_length=10000)),
                ('prdtStatNm', models.CharField(default='null', max_length=10000)),
                ('nationAlt', models.CharField(default='null', max_length=10000)),
                ('genreAlt', models.CharField(default='null', max_length=10000)),
                ('repNationNm', models.CharField(default='null', max_length=10000)),
                ('repGenreNm', models.CharField(default='null', max_length=10000)),
                ('directors', models.CharField(default='null', max_length=10000)),
                ('companys', models.CharField(default='null', max_length=10000)),
            ],
        ),
    ]
