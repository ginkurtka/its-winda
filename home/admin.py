from django.contrib import admin
from .models import Hotel, Room, Booking, Review

class HotelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Hotel._meta.fields]
admin.site.register(Hotel, HotelAdmin)


class RoomAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Room._meta.fields]
admin.site.register(Room, RoomAdmin)


class BookingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Booking._meta.fields]
admin.site.register(Booking, BookingAdmin)

class ReviewAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Review._meta.fields]
admin.site.register(Review, ReviewAdmin)

