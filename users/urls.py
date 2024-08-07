from allauth.account import views as account_views
from allauth.mfa import urls as mfa_urls
from allauth.mfa import views as mfa_views
from allauth.socialaccount import views as socialaccount_views
from django.urls import path, include, re_path

from users import views

urlpatterns = [
    ############################# User Urls #############################
    path("make-friends/", views.AllUsers.as_view(), name="make-friends"),
    path("user-page/<username>/", views.UserPageView.as_view(), name="user_page"),
    path("user-page/<username>/followers/", views.FollowersListView.as_view(), name="user_followers"),
    path("user-page/<username>/followings/", views.FollowingsListView.as_view(), name="user_followings"),
    path("change-data/", views.CustomUserChangeView.as_view(), name="socialaccount_connections"),
    ######################### Chat Urls #################################
    path("user-chats/", views.ChatList.as_view(), name="user-chats"),
    path("user-page/<username>/chat/", views.ConversationView.as_view(), name="conversation"),
    path("user-page/<username>/chat/settings/", views.ChatSettings.as_view(), name="conversation_settings"),
    ######################### Publication Urls ##########################
    path("user-page/<username>/new-publication/", views.CreatePublication.as_view(), name="new_publication"),
    path("publication/<int:pk>/", views.PublicationDetailView.as_view(), name="user_publication"),
    ########################## Comments Urls ############################
    path("remove-comments-p/<int:answer_id>/", views.RemoveCommentPublication.as_view(), name="remove_comment_p"),
    ########################### AllAuth Urls ############################
    path("signup/", account_views.SignupView.as_view(), name="account_signup"),
    path("login/", account_views.LoginView.as_view(), name="account_login"),
    path("logout/", account_views.LogoutView.as_view(), name="logout"),
    path("password-reset/", account_views.PasswordResetView.as_view(), name="account_reset_password"),
    re_path(
        r"^password-reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        account_views.PasswordResetFromKeyView.as_view(),
        name="account_reset_password_from_key",
    ),
    path(
        "password-reset/key/done/",
        account_views.PasswordResetFromKeyDoneView.as_view(),
        name="account_reset_password_from_key_done",
    ),
    path("password-reset/done/", account_views.PasswordResetDoneView.as_view(), name="account_reset_password_done"),
    path("change-password/", account_views.PasswordChangeView.as_view(), name="account_change_password"),
    path("set-password/", account_views.PasswordSetView.as_view(), name="account_set_password"),
    ######################## Social account Urls ########################
    path(
        "accounts/github/login/callback/", include("allauth.socialaccount.providers.github.urls"), name="github_login"
    ),
    path("accounts/", include("allauth.socialaccount.providers.google.urls"), name="google_login"),
    path("end-login3p/", socialaccount_views.SignupView.as_view(), name="socialaccount_signup"),
    path("confirm-email/<key>/", account_views.ConfirmEmailView.as_view(), name="account_confirm_email"),
    path("change-data/disconnect/<provider>/", views.disconnect_account, name="disconnect_account"),
    ########################### MFA Urls ################################
    path("change-data/mfa/", include(mfa_urls)),
    path("change-data/mfa/totp/", mfa_views.reauthenticate, name="mfa_reauthenticate"),
    path("change-data/account/reauth/", account_views.reauthenticate, name="account_reauthenticate"),
]
