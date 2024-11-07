# myproject/wsgi.py

import os
from django.core.wsgi import get_wsgi_application

# Django의 기본 설정 모듈을 'myproject.settings'로 지정
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# WSGI 애플리케이션 객체를 가져옵니다.
application = get_wsgi_application()