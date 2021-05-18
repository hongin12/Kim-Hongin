from django.contrib import admin
from django.urls import path, include
import portfolio.views


urlpatterns = [
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
]