from django.db.models import Q
from django.shortcuts import render,redirect,reverse
from django.contrib.auth.decorators import login_required
from django.template.defaultfilters import title
from django.views.decorators.http import require_http_methods,require_POST,require_GET
from unicodedata import category
from .forms import PubBlogForm
from .models import Blog,BlogComment,BlogCategory
from django.http import HttpResponse, JsonResponse


# Create your views here.
def index(request):
    blogs=Blog.objects.all()
    return render(request, 'index.html',context={'blogs':blogs})

def blog_view(request,blog_id):
    try:
        blog=Blog.objects.get(pk=blog_id)
    except Exception as e:
        blog=None
    return render(request, 'blog.html',context={'blog':blog})

# @login_required(login_url='/authory/login/')
@require_http_methods(["GET", "POST"])
@login_required()
def public(request,pub):
    if request.method== 'GET':
        categories=BlogCategory.objects.all()
        return render(request, 'public.html',context={'categories':categories})
    else:
        form=PubBlogForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data.get('title')
            content=form.cleaned_data.get('content')
            category_id=form.cleaned_data.get('category')
            blog=Blog.objects.create(title=title,content=content,category_id=category_id,author=request.user)
            return JsonResponse({'code':200,'message':'success','data':{'blog_id':blog.id}})
        else:
            print('false')
            return JsonResponse({'code':400,'message':'fail'})


@require_POST
@login_required()
def pub_comment(request):
    blog_id = request.POST.get('blog_id')
    content = request.POST.get('content')
    BlogComment.objects.create(blog_id=blog_id, content=content, author=request.user)
    return redirect(reverse('blog:blog_view', kwargs={'blog_id': blog_id}))

@require_GET
def search(request):
    #通过 /search?q=xxx 获取参数
    q = request.GET.get('q')
    #博客标题和内容中查找
    blogs = Blog.objects.filter(Q(title__icontains=q)|Q(content__icontains=q)).all()
    return render(request,'index.html',context={'blogs':blogs})
