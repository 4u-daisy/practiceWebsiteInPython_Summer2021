from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name="hews_home"),
    path('create', views.create, name="create"),
    path('<int:pk>', views.newsDetailView.as_view(), name="detail_view"),
    path('<int:pk>/update', views.newsUpdateView.as_view(), name="update_view"),
    path('<int:pk>/delete', views.newsDeleteView.as_view(), name="delete_view")

]