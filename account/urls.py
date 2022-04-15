from django.urls import include, path

from .views import AccountView, LoginViewCustom, LogoutViewCustom

urlpatterns = [
    path('', AccountView.as_view(), name='account'),
    path('login/', LoginViewCustom.as_view(), name='login'),
    path('logout/', LogoutViewCustom.as_view(), name='logout'),
]