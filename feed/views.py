from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Tweet, Comment
from .forms import TweetForm
from django.contrib.auth.forms import UserCreationForm

@login_required
def add_comment(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(user=request.user, content=content)
        return redirect('friends')  
    return redirect('friends') 

def friends_view(request):
    comments = Comment.objects.all()  
    return render(request, 'feed/friends.html', {'comments': comments})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'feed/register.html', {'form': form})


@login_required
def feed(request):
    tweets = Tweet.objects.all()
    return render(request, 'feed/feed.html', {'tweets': tweets})


@login_required
def create_tweet(request):
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('feed')
    else:
        form = TweetForm()
    return render(request, 'feed/create_tweet.html', {'form': form})
