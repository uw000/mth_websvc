# vacant_homes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # 메인 페이지
    path('search/', views.search_results, name='search_results'),  # 검색 결과 페이지
]