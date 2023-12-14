from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from core.models import Purchase, Book, Order
from django.db.models import F

def cart_summary(request):
    
    if not request.user.is_authenticated:
        return redirect('login')  

    try:
        order = Order.objects.get(user=request.user, status='in_cart')
        purchases = order.purchases.all()
        total_price = sum(purchase.quantity * purchase.book.price for purchase in purchases)
    except Order.DoesNotExist:
        purchases = []
        total_price = 0

    request.session['total_price'] = float(total_price)
    context = {
        "purchases": purchases,
        "total_price": total_price,
    }

    return render(request, 'cart_summary.html', context)


@login_required
def cart_add(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    order, created = Order.objects.get_or_create(user=request.user, status='in_cart')

    purchase, created = Purchase.objects.get_or_create(order=order, book=book)
    if not created:
        purchase.quantity += 1
        purchase.save()

    return redirect("cart:cart_summary")



@login_required
def cart_delete(request, purchase_id):
    purchase = get_object_or_404(Purchase, id=purchase_id, order__user=request.user)
    purchase.delete()
    if not Purchase.objects.filter(order=purchase.order).exists():
        purchase.order.delete()
    return redirect("cart:cart_summary")


def cart_update(request):
    pass

@login_required
def checkout(request):
    order = get_object_or_404(Order, user=request.user, status='in_cart')
    purchases = order.purchases.all()
    total_price = sum(purchase.quantity * purchase.book.price for purchase in purchases)
    context = {
        "purchases": purchases,
        "total_price": total_price,
    }

    if request.method == 'POST':
        order.order_first_name = request.POST['order_first_name']
        order.order_last_name = request.POST['order_last_name']
        order.order_cc_no = request.POST['order_cc_no']
        order.order_cc_date = request.POST['order_cc_date']
        order.order_address = request.POST['order_address']
        order.status = 'purchased'
        order.save()

        request.session['order_number'] = order.order_number
        request.session.save()
        print("Session order_number:", request.session.get('order_number', 'Not set'))

        request.session['total_order_amount'] = float(total_price)
        return redirect('cart:success')

    return render(request, 'checkout.html', context)


def success(request):
    context = {
    "order_first_name": request.session.get('order_first_name', ''),
    "order_last_name": request.session.get('order_last_name', ''),
    "order_address": request.session.get('order_address', ''),
    "total_order_amount": request.session.get('total_order_amount', ''),
    "order_number": request.session.get('order_number', ''),
        }
    print(context) 
    return render(request, 'success.html', context)


@login_required
def order_history(request):
    purchases = Purchase.objects.filter(order__user=request.user, order__status='purchased').order_by('-order__placed_at')
    context = {
        "purchases": purchases,
    }
    return render(request, 'order_history.html', context)
