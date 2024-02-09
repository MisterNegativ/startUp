from django.contrib import admin
from .models import Advertisement, FilterRegion

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'image', 'video_url']
    search_fields = ['title', 'content', 'image', 'video_url']
    model = Advertisement

    def save_model(self, request, obj, form, change):
        # Clear the selected regions when adding a new Advertisement
        if not change:  # If it's a new Advertisement
            obj.regions.clear()

        # Save the Advertisement object
        super().save_model(request, obj, form, change)


admin.site.register(FilterRegion)
admin.site.register(Advertisement, AdvertisementAdmin)
