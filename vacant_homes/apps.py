# vacant_homes/apps.py
from django.apps import AppConfig

class VacantHomesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vacant_homes'
    verbose_name = '빈집 정보 관리'  # 관리자 페이지에서 보이는 앱의 이름