from django.urls import path
from . import views
from django.contrib.auth import views as auth_view
from .forms import LoginForm

app_name = "tweet_app"
urlpatterns = [
    path("", views.index, name="index"),
    # path("tweets-list", views.tweets_list, name="all_tweets"),
    path("create-tweet/", views.tweet_create, name="tweet"),
    path("<int:tweet_id>/edit-tweet/", views.edit_tweet, name="edit_tweet"),
    path("<int:tweet_id>/del-tweet/", views.tweet_delete, name="delete_tweet"),
    path("register-user", views.register_user, name="register"),
    path(
        "login-user",
        auth_view.LoginView.as_view(
            template_name="tweetApp/user_login.html", authentication_form=LoginForm
        ),
        name="login",
    ),
    path("logout-user", views.user_logout, name="logout"),
]
