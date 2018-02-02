# Generated by Django 2.0.1 on 2018-02-02 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180202_1037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(max_length=100, null=True, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='date_created',
            new_name='created',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='date_posted',
            new_name='posted',
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, null=True, related_name='posts', to='blog.Tags'),
        ),
    ]