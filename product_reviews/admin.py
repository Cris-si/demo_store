from django.contrib import admin
from .models import Review

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'rating', 'created_at']
    list_filter = ['rating', 'created_at', 'updated_at']
    search_fields = ['user__username', 'product__name', 'comment']
    raw_id_fields = ['product', 'user']
