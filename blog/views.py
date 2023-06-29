from django.shortcuts import render, get_list_or_404
from . import models
# Create your views here.


def render_post(request):
    post = models.Post.objects.all()
    return render(request,'posts.html',{
        'post': post
    })

def post_detail(request,post_id):
    post = get_list_or_404(models.Post,pk=post_id)
    return render(request,'post_detail.html',{
        'post' : post
    })