from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import TweetForm, RegisterForm, LoginForm
from django.contrib.auth import login, logout
from django.contrib import messages

from django.contrib.auth.views import LoginView, LogoutView

from .models import Tweet
from django.db.models import Q


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
            messages.success(request, "Your Tweet Has Been Sucessfully Added.")
            return redirect("tweet_app:index")
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
            messages.success(request, "Your Tweet Has Been Updated.")
            return redirect("tweet_app:index")

    else:
        form = TweetForm(instance=tweet)
        return render(request, "tweetApp/tweet_create.html", {"form": form})


@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)
    if request.method == "POST":
        tweet.delete()
        messages.success(request, "Your Tweet Has Been Deleted.")
        return redirect("tweet_app:index")

    else:
        return render(request, "tweetApp/tweet_delete.html", {"tweet": tweet})


def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Succesfully Register.")
            return redirect("login")

    else:
        form = RegisterForm()
        return render(request, "tweetApp/user_register.html", {"form": form})


class TweetLoginView(LoginView):
    template_name = "tweetApp/user_login.html"
    authentication_form = LoginForm

    def form_valid(self, form):
        login(self.request, form.get_user())
        messages.success(self.request, "Successfully Logged In.")
        return redirect("tweet_app:index")

    def form_invalid(self, form):
        messages.error(self.request, "Please Check Your Details.")
        return self.render_to_response(self.get_context_data(form=form))


class TweetLogoutView(LogoutView):
    def post(self, request):
        messages.success(self.request, "Successfully Logged Out.")
        logout(request)
        return redirect("tweet_app:index")


# This is second method to logout user.
def user_logout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out.")
    return redirect("tweet_app:index")


def search(request):
    user_query = request.GET.get("user-search")
    search_result = Tweet.objects.filter(
        Q(user_name__icontains=user_query) | Q(user_text__icontains=user_query))

    return render(request, "tweetApp/search.html", {"results": search_result})
