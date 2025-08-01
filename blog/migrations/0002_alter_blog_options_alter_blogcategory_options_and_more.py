# Generated by Django 5.2.3 on 2025-07-04 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': '博客', 'verbose_name_plural': '博客'},
        ),
        migrations.AlterModelOptions(
            name='blogcategory',
            options={'verbose_name': '博客分类', 'verbose_name_plural': '博客分类'},
        ),
        migrations.AlterModelOptions(
            name='blogcomment',
            options={'verbose_name': '博客评论', 'verbose_name_plural': '博客评论'},
        ),
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.TextField(verbose_name='博客内容'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=100, verbose_name='博客标题'),
        ),
        migrations.AlterField(
            model_name='blogcategory',
            name='name',
            field=models.CharField(max_length=100, verbose_name='分类名称'),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='content',
            field=models.TextField(verbose_name='评论内容'),
        ),
    ]
