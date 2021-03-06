# Generated by Django 3.1.4 on 2020-12-27 19:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topictitle', models.CharField(max_length=120, verbose_name='Title')),
                ('createdtime', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created Time')),
                ('modifiedtime', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Modified Time')),
                ('data', models.TextField()),
                ('createdby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdtime', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('data', models.TextField()),
                ('createdby', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.topic')),
            ],
        ),
    ]
