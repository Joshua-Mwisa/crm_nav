from django.contrib import admin
from django.urls import path, include

from apps.common.views import ProfileUpdateView, ProfileView, SignUpView, \
    DashboardView, ContactsView, ChatView, CalendarView, SocialMediaView, CallsView
from apps.linkedin_app.views import LinkedinView
from apps.facebook_app.views import FacebookView
from apps.twitter.views import TwitterView, TwitterSearch

from apps.instagram.views import instagramView
from apps.whatsapp.views import whatsappView
from apps.telegram.views import telegramView

from apps.youtube.views import youtubeView
from apps.tiktok.views import tiktokView
from apps.snapchat.views import snapchatView

from apps.quora.views import quoraView
from apps.reddit.views import redditView
from apps.pinterest.views import pinterestView

from apps.chatbot.views import ChatbotView
from django.views.generic import TemplateView

from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', auth_views.LoginView.as_view(
        template_name='common/login.html'), name='login'),

    path('login/', auth_views.LoginView.as_view(
        template_name='common/login.html'), name='login'),

    path('logout/', auth_views.LogoutView.as_view(
        next_page='login'), name='logout'),

    path('register/', SignUpView.as_view(), name='register'),

    path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/', ProfileView.as_view(), name='profile'),

    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('calls/', CallsView.as_view(), name='calls'),

    path('linkedin/', LinkedinView, name='linkedin'),
    path('facebook/', FacebookView.as_view(), name='facebook'),
    path('twitter/', TwitterView, name='twitter'),
    path('twitterSearch/', TwitterSearch, name='twitterSearch'),

    path('instagram/', instagramView, name='instagram'),
    path('whatsapp/', whatsappView, name='whatsapp'),
    path('telegram/', telegramView, name='telegram'),

    path('youtube/', youtubeView, name='youtube'),
    path('tiktok/', tiktokView, name='tiktok'),
    path('snapchat/', snapchatView, name='snapchat'),

    path('quora/', quoraView, name='quora'),
    path('reddit/', redditView, name='reddit'),
    path('pinterest/', pinterestView, name='pinterest'),


    path('calendar/', CalendarView.as_view(), name='calendar'),
    path('social-media/', SocialMediaView.as_view(), name='social_media'),

    path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name='common/change-password.html',
        success_url='/'), name='change-password'),

    path('accounts/', include('allauth.urls')),

    # Forgot password

    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='common/password-reset/password_reset.html',
             subject_template_name='common/password-reset/password_reset_subject.txt',
             email_template_name='common/password-reset/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='common/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='common/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='common/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    path('social-auth/', include('social_django.urls', namespace='social')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
