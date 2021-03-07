from django.shortcuts import render, redirect
from .models import Product, Cart, CartProduct, Transaction

# Create your views here.


def cart_checker(request):
    "Check if there is a cart or not"
    if Cart.objects.all().count() < 1:
        c = Cart()
        c.save()
    return redirect('home')


def home(request):
    '''
    Show all the product
    '''
    total = 0
    Products = Product.objects.all()
    c = Cart.objects.all().first()
    i = c.items.all()
    for p in i:
        total = total+(p.product.price*p.Cquantity)
    return render(request, 'home.html', {"Products": Products, 'i': i, 'total': total})


def add_product(request, id):
    '''
    Add Product in the cart
    '''
    p = Product.objects.filter(id=id).first()
    if not p.quantity <= 0:
        c = Cart.objects.all().first()
        if not c.items.filter(product=p).exists():
            cp = CartProduct(product=p, Cquantity=1)
            cp.save()
            c.items.add(cp)
            c.save()
            p.quantity = p.quantity-1
            p.save()
        else:
            cp = CartProduct.objects.filter(product=p).first()
            cp.Cquantity = cp.Cquantity+1
            cp.save()
            c.save()
            p.quantity = p.quantity-1
            p.save()
    return redirect('home')


def remove_product(request, id):
    '''
    remove the product
    '''
    cp = CartProduct.objects.get(id=id)
    p = cp.product
    p.quantity = p.quantity+cp.Cquantity
    p.save()
    cp.delete()
    return redirect('home')


def decrease_item(request, id):
    '''
    Decrease the item quantity by 1
    '''
    cp = CartProduct.objects.get(id=id)
    if not cp.Cquantity <= 1:
        cp.Cquantity = cp.Cquantity-1
        p = cp.product
        p.quantity = p.quantity+1
        cp.save()
        p.save()
    else:
        removeProduct(request, id)
    return redirect('home')


def checkout(request):
    total = 0
    c = Cart.objects.all().first()
    i = c.items.all()
    for p in i:
        total = total+(p.product.price*p.Cquantity)
    if request.method == "POST":
        usr = request.POST.get('user')
        if usr == "":
            usr = "Anonymous"
        t = Transaction(user=usr)
        t.save()
        t.cartItems.set(i)
        t.save()
        c.items.clear()
        c.save()
        print("Done")
    return render(request, 'checkout.html', {'c': c, 'i': i, 'total': total})
