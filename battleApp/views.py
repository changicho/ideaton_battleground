from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .models import post, comment
from django.contrib import messages
from django.utils import timezone

# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return render(request, 'login.html')


def list(request):
    posts = post.objects
    return render(request, 'list.html', {'posts': posts})


def newpost(request):
    return render(request, 'new.html')


def create(request):
    inner_post = post()
    inner_post.Writer = request.GET['Writer']
    inner_post.title = request.GET['title']
    inner_post.TorI = request.GET['TorI']
    inner_post.body = request.GET['body']
    inner_post.pub_date = timezone.datetime.now()
    inner_post.save()
    return redirect('list')


def detail(request, post_id):
    post_detail = get_object_or_404(post, pk=post_id)
    # if request.user.is_authenticated:
    #         user = User.objects.get(username= request.user.get_username())
    #         return render(request,'detail.html', {'post':post_detail, 'user':user})
    # else:
    # return render(request, 'detail.html')

    return render(request, 'detail.html', {'post': post_detail})


def comment_write(request, post_id):
    print('comment write')

    if request.method == 'POST':

        inner_post = get_object_or_404(post, pk=post_id)
        content = request.POST.get('contents')
        content_type = request.POST.get('type')
        print(content)
        print(content_type)

        if not content:
            messages.info(request, "댓글을 쓸 수 없습니다!!!")
            return redirect('/post/'+str(post_id))

        comment.objects.create(
            post=inner_post, comment_contents=content, comment_type=content_type)
        return redirect('/post/'+str(post_id))
