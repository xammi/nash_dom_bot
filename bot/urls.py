from django.urls import path
from bot.views import TgWebhookView

urlpatterns = [
    path('telegram/webhook/', TgWebhookView.as_view(), name='tg_webhook'),
]
