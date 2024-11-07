# vacant_homes/admin.py
from django.contrib import admin
from .models import VacantHome

# VacantHome 모델을 관리자 페이지에 등록
@admin.register(VacantHome)
class VacantHomeAdmin(admin.ModelAdmin):
    # 관리자 페이지에서 표시할 필드
    list_display = ('title', 'location', 'address', 'home_type', 'size', 'registration_date', 'view_count', 'like_count', 'safety_grade')
    # 필터링 옵션
    list_filter = ('location', 'home_type', 'safety_grade')
    # 검색 가능한 필드
    search_fields = ('title', 'location', 'address', 'description')