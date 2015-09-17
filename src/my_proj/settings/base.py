"""
Django settings for my_proj project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""
from django.core.urlresolvers import reverse_lazy
from os.path import dirname, join, exists

# Build paths inside the project like this: join(BASE_DIR, "directory")
BASE_DIR = dirname(dirname(dirname(__file__)))
STATICFILES_DIRS = [join(BASE_DIR, 'static')]
MEDIA_ROOT = join(BASE_DIR, 'media')
MEDIA_URL = "/media/"

# Use Django templates using the new Django 1.8 TEMPLATES settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            join(BASE_DIR, 'templates'),
            # insert more TEMPLATE_DIRS here
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Use 12factor inspired environment variables or from a file
import environ
env = environ.Env()

# Ideally move env file should be outside the git repo
# i.e. BASE_DIR.parent.parent
env_file = join(dirname(__file__), 'local.env')
if exists(env_file):
    environ.Env.read_env(str(env_file))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Raises ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django_admin_bootstrapped',
    'django.contrib.admin',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #'authtools',
    'social.apps.django_app.default',

    'crispy_forms',
    'easy_thumbnails',

    'profiles',
    'accounts',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'my_proj.urls'


AUTHENTICATION_BACKENDS = (
    #'social.backends.amazon.AmazonOAuth2',
    #'social.backends.angel.AngelOAuth2',
    #'social.backends.aol.AOLOpenId',
    #'social.backends.appsfuel.AppsfuelOAuth2',
    #'social.backends.beats.BeatsOAuth2',
    #'social.backends.behance.BehanceOAuth2',
    #'social.backends.belgiumeid.BelgiumEIDOpenId',
    #'social.backends.bitbucket.BitbucketOAuth',
    #'social.backends.box.BoxOAuth2',
    #'social.backends.clef.ClefOAuth2',
    #'social.backends.coinbase.CoinbaseOAuth2',
    #'social.backends.coursera.CourseraOAuth2',
    #'social.backends.dailymotion.DailymotionOAuth2',
    #'social.backends.disqus.DisqusOAuth2',
    #'social.backends.douban.DoubanOAuth2',
    #'social.backends.dropbox.DropboxOAuth',
    #'social.backends.dropbox.DropboxOAuth2',
    #'social.backends.eveonline.EVEOnlineOAuth2',
    #'social.backends.evernote.EvernoteSandboxOAuth',
    'social.backends.facebook.FacebookAppOAuth2',
    'social.backends.facebook.FacebookOAuth2',
    #'social.backends.fedora.FedoraOpenId',
    #'social.backends.fitbit.FitbitOAuth',
    #'social.backends.flickr.FlickrOAuth',
    #'social.backends.foursquare.FoursquareOAuth2',
    #'social.backends.github.GithubOAuth2',
    'social.backends.google.GoogleOAuth',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOpenId',
    'social.backends.google.GooglePlusAuth',
    'social.backends.google.GoogleOpenIdConnect',
    #'social.backends.instagram.InstagramOAuth2',
    #'social.backends.jawbone.JawboneOAuth2',
    #'social.backends.kakao.KakaoOAuth2',
    #'social.backends.linkedin.LinkedinOAuth',
    #'social.backends.linkedin.LinkedinOAuth2',
    #'social.backends.live.LiveOAuth2',
    #'social.backends.livejournal.LiveJournalOpenId',
    #'social.backends.mailru.MailruOAuth2',
    #'social.backends.mendeley.MendeleyOAuth',
    #'social.backends.mendeley.MendeleyOAuth2',
    #'social.backends.mineid.MineIDOAuth2',
    #'social.backends.mixcloud.MixcloudOAuth2',
    #'social.backends.nationbuilder.NationBuilderOAuth2',
    #'social.backends.odnoklassniki.OdnoklassnikiOAuth2',
    #'social.backends.open_id.OpenIdAuth',
    #'social.backends.openstreetmap.OpenStreetMapOAuth',
    #'social.backends.persona.PersonaAuth',
    #'social.backends.podio.PodioOAuth2',
    #'social.backends.rdio.RdioOAuth1',
    #'social.backends.rdio.RdioOAuth2',
    #'social.backends.readability.ReadabilityOAuth',
    #'social.backends.reddit.RedditOAuth2',
    #'social.backends.runkeeper.RunKeeperOAuth2',
    #'social.backends.skyrock.SkyrockOAuth',
    #'social.backends.soundcloud.SoundcloudOAuth2',
    #'social.backends.spotify.SpotifyOAuth2',
    #'social.backends.stackoverflow.StackoverflowOAuth2',
    #'social.backends.steam.SteamOpenId',
    #'social.backends.stocktwits.StocktwitsOAuth2',
    #'social.backends.stripe.StripeOAuth2',
    #'social.backends.suse.OpenSUSEOpenId',
    #'social.backends.thisismyjam.ThisIsMyJamOAuth1',
    #'social.backends.trello.TrelloOAuth',
    #'social.backends.tripit.TripItOAuth',
    #'social.backends.tumblr.TumblrOAuth',
    #'social.backends.twilio.TwilioAuth',
    'social.backends.twitter.TwitterOAuth',
    #'social.backends.vk.VKOAuth2',
    #'social.backends.weibo.WeiboOAuth2',
    #'social.backends.wunderlist.WunderlistOAuth2',
    #'social.backends.xing.XingOAuth',
    #'social.backends.yahoo.YahooOAuth',
    #'social.backends.yahoo.YahooOpenId',
    #'social.backends.yammer.YammerOAuth2',
    #'social.backends.yandex.YandexOAuth2',
    #'social.backends.vimeo.VimeoOAuth1',
    #'social.backends.lastfm.LastFmAuth',
    #'social.backends.moves.MovesOAuth2',
    #'social.backends.vend.VendOAuth2',
    'social.backends.email.EmailAuth',
    'social.backends.username.UsernameAuth',
    'django.contrib.auth.backends.ModelBackend',
)


WSGI_APPLICATION = 'my_proj.wsgi.application'

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in
    # os.environ
    'default': env.db(),
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_URL = '/static/'

ALLOWED_HOSTS = []

# Crispy Form Theme - Bootstrap 3
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# For Bootstrap 3, change error alert to 'danger'
from django.contrib import messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

# Authentication Settings
#AUTH_USER_MODEL = 'authtools.User'

LOGIN_REDIRECT_URL = reverse_lazy("profiles:show_self")
LOGIN_URL = reverse_lazy("accounts:login")

THUMBNAIL_EXTENSION = 'png'     # Or any extn for your thumbnails

SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'
SOCIAL_AUTH_GOOGLE_OAUTH_SCOPE = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/userinfo.profile'
]
# SOCIAL_AUTH_EMAIL_FORM_URL = '/signup-email'
SOCIAL_AUTH_EMAIL_FORM_HTML = 'email_signup.html'
#SOCIAL_AUTH_EMAIL_VALIDATION_FUNCTION = 'example.app.mail.send_validation'
SOCIAL_AUTH_EMAIL_VALIDATION_URL = '/email-sent/'
# SOCIAL_AUTH_USERNAME_FORM_URL = '/signup-username'
SOCIAL_AUTH_USERNAME_FORM_HTML = 'username_signup.html'

SOCIAL_AUTH_TWITTER_KEY = 'O9fDtYn1zM9AbyqLJubYAbrWz'
SOCIAL_AUTH_TWITTER_SECRET = 'Uh8BqBYtiR2m3KtyGAJwKmtzWgCndyl9aWOBWBrua2alWCyh6D'

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    #'example.app.pipeline.require_email',
    #'social.pipeline.mail.mail_validation',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.debug.debug',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    #'social.pipeline.user.update_user_details',
    'social.pipeline.debug.debug'
)
