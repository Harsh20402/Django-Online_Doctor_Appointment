from django.urls import path, reverse_lazy
from . import views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from .forms import MyPasswordChangeForm
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='home-page'),
    path('about', views.about, name='about-page'),
    path('service', views.service, name='service-page'),
    path('gallery', views.gallery, name='gallery-page'),
    path('team', views.team, name='team-page'),
    path('appointment', views.appointment, name='appointment-page'),
    path('blog', views.blog, name='blog-page'),
    path('contact', views.contact, name='contact-page'),
    path('registration', views.registration, name='registration-page'),
    path('login', views.UserLogin, name='login-page'),
    path('logout', views.userLogout, name='logout-page'),
    path('profile', views.profile, name='profile-page'),
    path('chngpro', views.changeProfile, name='chngpro-page'),
    path('appoint/<d_id>', views.makeAppoint, name='appoint-page'),
    path('change_password/',
         PasswordChangeView.as_view(
             template_name='myapplications/change_password.html',
             success_url=reverse_lazy('password_change_done'),
             form_class=MyPasswordChangeForm
         ),
         name='password_change'),
    path('change_password/done/',
         PasswordChangeDoneView.as_view(
             template_name='myapplications/password_change_done.html'
         ),
         name='password_change_done'),

    path('apphistory', views.appointmentHistory, name="apphist-page"),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='myapplications/password-reset.html'
             # success_url=reverse_lazy('password_reset_done')
         ),
         name='paswword_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='myapplications/password-reset-done.html'
         ),
         name='paswword_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='myapplications/password-reset-confirm.html'
         ),
         name='paswword_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='myapplications/password-reset-complete.html'
         ),
         name='paswword_reset_complete'),
]
