from pathlib import Path
import os
import dj_database_url
from urllib.parse import urlparse

# 環境変数ファイルの読み込み
if os.path.isfile('env.py'):
    import env

# プロジェクトのベースディレクトリ
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# 環境変数から重要な設定を取得
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = True

ALLOWED_HOSTS = ['.herokuapp.com']

gitpod_url = os.getenv('GITPOD_WORKSPACE_URL')
if gitpod_url:
    # ポート番号を含めてホスト名を追加
    hostname = urlparse(gitpod_url).hostname
    ALLOWED_HOSTS.append(f"8080-{hostname}")
    ALLOWED_HOSTS.append(f"8000-{hostname}")
    ALLOWED_HOSTS.append(hostname)

print("ALLOWED_HOSTS:", ALLOWED_HOSTS)

# アプリケーションの設定
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django_summernote',
    'blog',
    'about'
]

SITE_ID = 1
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'codestar.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'codestar.wsgi.application'

# デバッグ出力: DATABASE_URLの値を確認
print("DATABASE_URL:", os.environ.get("DATABASE_URL"))

# データベース設定
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
}

CSRF_TRUSTED_ORIGINS = [
    "https://*.codeinstitute-ide.net/",
    "https://*.herokuapp.com"
]

# GitpodのURLを追加
gitpod_url = os.getenv('GITPOD_WORKSPACE_URL')
if gitpod_url:
    hostname = urlparse(gitpod_url).hostname
    CSRF_TRUSTED_ORIGINS.append(f"https://{hostname}")
    CSRF_TRUSTED_ORIGINS.append(f"https://8000-{hostname}")
    CSRF_TRUSTED_ORIGINS.append(f"https://8080-{hostname}")

# パスワードのバリデーション
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

ACCOUNT_EMAIL_VERIFICATION = 'none'

# その他の設定
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'