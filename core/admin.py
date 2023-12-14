from django.contrib import admin
from .models import Book, Purchase, Author, Order

admin.site.register(Book)
admin.site.register(Purchase)
admin.site.register(Author)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'user', 'status', 'placed_at', 'get_purchased_books', 'get_total_price')

    def get_purchased_books(self, obj):
        return obj.get_purchased_books()
    get_purchased_books.short_description = "Purchased Books"

    def get_total_price(self, obj):
        return obj.get_total_price()
    get_total_price.short_description = "Total Price"
