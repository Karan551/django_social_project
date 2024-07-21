from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import TweetForm, RegisterForm, LoginForm
from django.contrib.auth import login, logout

from django.contrib.auth.views import LoginView

from .models import Tweet


# Create your views here.


def index(request):
    all_tweets = Tweet.objects.all().order_by("-cretated_at")
    return render(request, "tweetApp/index.html", {"tweets": all_tweets})


def tweets_list(request):
    all_tweets = Tweet.objects.all().order_by("-cretated_at")

    return render(request, "tweetApp/tweets_list.html", {"tweets": all_tweets})


@login_required
def tweet_create(request):
    form = TweetForm()
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("/")

    else:
        return render(request, "tweetApp/tweet_create.html", {"form": form})


@login_required
def edit_tweet(request, tweet_id):
    tweet = get_object_or_404(Tweet, id=tweet_id, user=request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect("tweet_app:index")

    else:
        form = TweetForm(instance=tweet)
        return render(request, "tweetApp/tweet_create.html", {"form": form})


@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        tweet.delete()
        return redirect("tweet_app:index")

    else:
        return render(request, "tweetApp/tweet_delete.html", {"tweet": tweet})


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        # print("This is post data :", request.POST)
        # print("This is user:", request.user)
        if form.is_valid():
            form.save()
            return HttpResponse("Thanks For register.")
        pass
    else:
        form = RegisterForm()
        return render(request, "tweetApp/user_register.html", {"form": form})


# https://docs.djangoproject.com/en/5.0/ref/settings/#auth
# def user_login(request):
#     if request.method == "POST":
#         print("this is request.post", request.POST)

#         form = LoginForm(request.POST)
#         print("valid form errors:", form.errors)
#         print("valid form or not:", form.is_valid())
#         if form.is_valid():
#             return HttpResponse("Successfully Logged In.")

#         else:
#             return HttpResponse("Yeah Logout can.")
#     else:
#         form = LoginForm()
#         return render(request, "tweetApp/user_login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("tweet_app:index")
