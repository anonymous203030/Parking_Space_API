from django.contrib import admin

from .models import BookTime, ReserveBookTime


class BookTimeAdmin(admin.ModelAdmin):
    list_display = ['floor', 'parking_space_id', 'booking_start_time', 'booking_end_time']
    list_filter = ['booking_start_time', 'booking_end_time', 'floor']
    ordering = ['booking_start_time', 'booking_end_time', 'floor']
    search_fields = ['floor', 'parking_space_id', 'booking_start_time', 'booking_end_time']


admin.site.register(BookTime, BookTimeAdmin)


class ReserveAdmin(admin.ModelAdmin):
    list_display = ['book_time', 'owner', 'created_at', 'updated_at']
    list_filter = ['book_time', 'owner']
    ordering = ['created_at', 'updated_at']
    search_fields = ['book_time', 'owner', 'created_at', 'updated_at']

admin.site.register(ReserveBookTime, ReserveAdmin)
