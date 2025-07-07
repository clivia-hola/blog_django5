from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()
# Create your models here.
class BlogCategory(models.Model):
    name=models.CharField(max_length=100,verbose_name='分类名称')
    class Meta:
        verbose_name='博客分类'
        verbose_name_plural='博客分类'
    def __str__(self):
        return self.name

class Blog(models.Model):
    title=models.CharField(max_length=100,verbose_name='博客标题')
    content=models.TextField(verbose_name='博客内容')
    category=models.ForeignKey(BlogCategory,on_delete=models.CASCADE)
    pub_date=models.DateTimeField(auto_now_add=True)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        verbose_name='博客'
        verbose_name_plural='博客'
        ordering=['-pub_date']
    def __str__(self):
        return self.title

class BlogComment(models.Model):
    content=models.TextField(verbose_name='评论内容')
    pub_date=models.DateTimeField(auto_now_add=True)
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments',verbose_name='所属博客')
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    class Meta:
        verbose_name='博客评论'
        verbose_name_plural='博客评论'
        ordering = ['-pub_date']
    def __str__(self):
        return self.content