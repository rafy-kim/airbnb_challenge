from django.contrib import admin
from .models import Tweet, Like

# Make a CUSTOM filter for Tweets that contain and don't contain the words Elon Musk
class ElonMuskFilter(admin.SimpleListFilter):
    title = "Elon Musk Filter"
    parameter_name = "elon_musk"

    def lookups(self, request, model_admin):
        return (
            ("with_elon_musk", "With 'Elon Musk'"),
            ("without_elon_musk", "Without 'Elon Musk'"),
        )

    def queryset(self, request, queryset):
        if self.value() == "with_elon_musk":
            return queryset.filter(payload__contains="Elon Musk")
        if self.value() == "without_elon_musk":
            return queryset.exclude(payload__contains="Elon Musk")
        return queryset

# Register your models here.
@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    search_fields = (
        "payload",
        "user__username",
    )
    list_display = (
        "user",
        "payload",
        "like_count",
    )
    list_filter = (
        "created_at",
        ElonMuskFilter,
    )

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    search_fields = (
        "user__username",
    )
    list_display = (
        "user",
        "tweet",
    )
    list_filter = (
        "created_at",
    )
