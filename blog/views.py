from django.http import HttpResponse

# Create your views here.
import markdown
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from comments.forms import CommentForm
from blog.models import Post,Category


def index(request):
    post_list = Post.objects.order_by('-create_time')
    return render(request,'blog/index.html',context={
        'post_list':post_list
    })

def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.body =markdown.markdown(post.body,extensions=['markdown.extensions.extra',
                                                       'markdown.extensions.codehilite',
                                                       'markdown.extensions.toc'])
    form = CommentForm()
    comment_list = post.comment_set.all()

    context = {
        'post':post,
        'comment_list':comment_list,
        'form':form
    }


    return render(request,'blog/detail.html',context=context)

def archives(request,year,month):
    post_list = Post.objects.filter(create_time__year=year,
                                    create_time__month=month).order_by('-create_time')
    return render(request,'blog/index.html',context={'post_list':post_list})

def category(request,pk):
    cate = get_object_or_404(Category,pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-create_time')
    return render(request,'blog/index.html',context={'post_list':post_list})





