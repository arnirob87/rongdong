from django.urls import path
from . import views
from .views import AddProductView, UpdateProductView, DeleteProductView, HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('update_password/', views.update_password, name='update_password'),
    path('update_user/', views.update_user, name='update_user'),
    path('update_info/', views.update_info, name='update_info'),
    path('product/<int:pk>', views.product, name='product'),
    path('category/<str:foo>', views.category, name='category'),
    path('category_summary/', views.category_summary, name='category_summary'),
    path('search/', views.search, name='search'),
    path('add_product/', AddProductView.as_view(), name='add_product'),
    path('product/edit/<int:pk>/', UpdateProductView.as_view(), name='update_product'),
    path('product/delete/<int:pk>/', DeleteProductView.as_view(), name='delete_product'),
]