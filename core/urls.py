from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('book/<uuid:book_id>/', views.book_details, name='book_details'),
    path('search/', views.search, name='search'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('genre/<str:genre>/', views.genre_books, name='genre_books'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
