from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Post,Comment
from .forms import FeedForm


def my_feed(request):
    
    posts = Post.objects.filter(author=request.user)
    count =  posts.count()
    lastfeed=posts[0].published_at
    context = {
        'posts': posts,
        'count':count,
         'lastfeed': lastfeed
    }
    return render(request,'posts.html',context)
def feed(request):
    context=data(request)
    return render(request,'posts.html',context)

@login_required
def create_feed(request):
    if request.method == 'GET':
        context = {'form': FeedForm()}
        return render(request, 'feed_form.html', context)
    elif request.method == 'POST':
        form = FeedForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.author = request.user
            form.save()
            messages.success(request, 'The post has been created successfully.')
            return redirect('/feed/')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'feed_form.html',{'form':form})
@login_required
def edit_feed(request, id):
    queryset = Post.objects.filter(author=request.user)
    post = get_object_or_404(queryset, post_id=id)

    if request.method == 'GET':
        context = {'form': FeedForm(instance=post), 'id': id}
        return render(request,'feed_form.html',context)
    elif request.method == 'POST':
        form = FeedForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'The feed has been created successfully.')
            return redirect('/feed/')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request,'feed_form.html',{'form':form})
@login_required      
def delete_feed(request, id):
    queryset=Post.objects.filter(author=request.user)
    post = get_object_or_404(queryset, pk=id)
    context = {'post': post}    
    if request.method == 'GET':
        return render(request, 'feed_confirm_delete.html',context)
    elif request.method == 'POST':
        post.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('/feed/')

@login_required
def like_post(request,id):
    post = Post.objects.get(post_id=id)
    if request.user.is_authenticated:
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
    context = data(request)
    return render(request,'posts.html',context)

@login_required
def add_comment(request, post_id):
    if request.method == 'POST':
        post = Post.objects.get(post_id=post_id)
        comment_text = request.POST['comment']

        # Create and save the comment
        Comment.objects.create(user=request.user, post=post, content=comment_text)
    context=data(request)
    return render(request,'posts.html',context)

def data(request):
    lastfeed=None
    if request.user.is_authenticated:
        myposts = Post.objects.filter(author=request.user)
        count=myposts.count()
        if myposts:
            lastfeed=myposts[0].published_at
    else:
        count=lastfeed=0
    
    posts = Post.objects.all()
    comments=Comment.objects.all()
    context = {
        'posts': posts,
        'count': count,
        'lastfeed': lastfeed,
        'comments':comments
    }
    return context