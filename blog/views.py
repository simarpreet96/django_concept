from .models import Post, Product, Store, Cart, Order, Category, Wish, BillingAddress
from django.utils import timezone
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm, ProductForm, PostForm, StoreForm, BillingForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q


def home(request):
    return render(request, 'index.html')


def search(request):
    query = request.GET['query']
    if len(query) > 50:
        allpost = Product.objects.none()
    else:
        allpost = Product.objects.filter(Q(name__icontains=query) |
                                         Q(category__categoryname__icontains=query) |
                                         Q(description__icontains=query))
    if allpost.count() == 0:
        messages.error(request, 'can not found')
    return render(request, 'search.html', {'allpost': allpost, 'query': query})


def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'post_list.html', {'posts': posts})


@login_required
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})


def product_list(request):
    products = Product.objects.filter()
    return render(request, 'product_list.html', {'products': products})


@login_required
def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})


def product_edit(request, pk):
    post = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            post.author = request.user
            post.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=post)
    return render(request, 'product_edit.html', {'form': form})


def product_del(request, pk):
    post = get_object_or_404(Product, pk=pk)
    post.delete()
    return redirect('product_list')


@login_required
def user_product(request):
    userproduct = Product.objects.filter(Q(author=request.user))
    # print(posts.query)
    return render(request, 'user_product.html', {'userproduct': userproduct})


def product_publish(request, pk):
    post = Product.objects.get(pk=pk)
    if post.published == 0:
        post.published = 1
        post.save()
        messages.info(request, 'product is published')
    elif post.published == 1:
        post.published = 0
        post.save()
        messages.info(request, 'product is unpublished')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def category_list(request):
    categorylist = Category.objects.all()
    return render(request, 'category_list.html', {'categorylist': categorylist})


def category_product_list(request, pk):
    # categoryl = Category.objects.get(id=pk)
    # category_product = Product.objects.filter(category=categoryl)
    category_product = Product.objects.filter(category__id=pk)
    return render(request, 'category_product_list.html', {'category_product': category_product})


def filter_product(request):
    # print(request.GET["filter_type"])
    if 'filter_type' in request.GET and request.GET["filter_type"] == "low":
        fill_products = Product.objects.filter().order_by('price')
    else:
        fill_products = Product.objects.filter().order_by('-price')
    # print(Products.query)
    return render(request, 'product_list.html', {'fill_products': fill_products})


def add_to_wishlist(request, pk):
    user = request.user
    items = get_object_or_404(Product, pk=pk)
    wished_item, created = Wish.objects.get_or_create(item=items, pk=items.pk, user=user, )
    messages.info(request, 'The item was added to your wishlist')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def wishlist_view(request):
    user = request.user
    productw = Product.objects.filter(author=user, price=False)
    wishs = Wish.objects.filter(user=user)
    if wishs.exists():
        if wishs.exists():
            wish = wishs[0]
            return render(request, 'wishlist.html', {'productw': productw, 'wishs': wishs})
        else:
            messages.warning(request, "You do not have any item in your Cart")
            return redirect("product_list")
    else:
        messages.warning(request, "You do not have any item in your Cart")
        return redirect("product_list")

    return render(request, 'wishlist.html', {'wishs': wishs})


@login_required
def remove_wish(request, pk):
    item = get_object_or_404(Product, pk=pk)
    remove_list = Wish.objects.filter(item=item.pk, user=request.user)
    remove_list.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def add_to_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_item, created = Cart.objects.get_or_create(item=item, user=request.user)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item=item.pk).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, f"{item.name} quantity has update.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            order.orderitems.add(order_item)
            messages.info(request, f"{item.name} has added to your cart.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        order = Order.objects.create(user=request.user)
        order.orderitems.add(order_item)
        messages.info(request, f"{item.name} has added to your cart. ")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_view(request):
    user = request.user
    carts = Cart.objects.filter(user=user, price=False)
    orders = Order.objects.filter(user=user, ordered=False)
    if carts.exists():
        if orders.exists():
            order = orders[0]
            return render(request, 'cart.html', {'carts': carts, 'order': order})
        else:
            messages.warning(request, "You do not have any item in your wishlist")
            return redirect('product_list')
    else:
        messages.warning(request, "You do not have any item in your wishlist")
        return redirect('product_list')

    return render(request, 'cart.html', {'carts': carts})


def delete_cart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is the order
        if order.orderitems.filter(item=item.pk).exists():
            order_item = Cart.objects.filter(item=item, user=request.user)[0]
            order.orderitems.remove(order_item)
            order_item.delete()
            messages.warning(request, f"{item.name} has removed from your cart.")
            messages.info(request, f"{item.name} quantity has updated.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.info(request, f"{item.name} Your item is not delete")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def decreaseCart(request, pk):
    item = get_object_or_404(Product, pk=pk)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.orderitems.filter(item=item.pk).exists():
            order_item = Cart.objects.filter(item=item, user=request.user)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.orderitems.remove(order_item)
                order_item.delete()
                messages.warning(request, f"{item.name} has removed frpm your cart.")
            messages.info(request, f"{item.name} quantity has updated.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.info(request, f"{item.name} quantity has updated.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        messages.info(request, "You do not have an active order")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def checkout(request):
    form = BillingForm

    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order_items = order_qs[0].orderitems.all()
    order_total = order_qs[0].all_total()
    get_total = order_qs[0].get_totals()
    get_perse = order_qs[0].get_percentage()

    context = {"form": form,
               "order_items": order_items,
               "order_total": order_total,
               "get_total": get_total,
               "get_perse": get_perse
               }

    # Getting the saved saved_address
    saved_address = BillingAddress.objects.filter(user=request.user)
    if saved_address.exists():
        savedAddress = saved_address.first()
        context = {"form": form,
                   "order_items": order_items,
                   "order_total": order_total,
                   "savedAddress": savedAddress
                   }

    if request.method == "POST":
        saved_address = BillingAddress.objects.filter(user=request.user)
        if saved_address.exists():

            savedAddress = saved_address.first()
            form = BillingForm(request.POST, instance=savedAddress)
            if form.is_valid():
                billingaddress = form.save(commit=False)
                billingaddress.user = request.user
                billingaddress.save()
        else:
            form = BillingForm(request.POST)
            if form.is_valid():
                billingaddress = form.save(commit=False)
                billingaddress.user = request.user
                billingaddress.save()

    return render(request, 'checkout.html', context)


def payment(request):
    key = settings.STRIPE_PUBLISHABLE_KEY
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    order_total = order_qs[0].all_total()
    totalCents = float(order_total * 100);
    total = round(totalCents, 2)
    if request.method == 'POST':
        charge = stripe.Charge.create(amount=total,
                                      currency='usd',
                                      description=order_qs,
                                      source=request.POST['stripeToken'])
        print(charge)

    return render(request, 'payment.html', {"key": key, "total": total})


def store_list(request):
    storelist = Store.objects.all()
    return render(request, 'store_list.html', {'storelist': storelist})


def add_store(request):
    if request.method == "POST":
        form = StoreForm(request.POST)
        if form.is_valid():
            store = form.save(commit=False)
            # store.author = request.user
            store.save()
            return redirect('store_list')
    else:
        form = StoreForm()
    return render(request, 'add_store.html', {'form': form})


def store_product_list(request, pk):
    # storel = Store.objects.get(id=pk)
    # store_product = Product.objects.filter(store=storel)
    store_product = Product.objects.filter(store__id=pk)
    return render(request, 'store_product_list.html', {'store_product': store_product})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('post_list')
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})


# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             return redirect('post_list')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'registration/login.html', {'form': form})


# def logout_view(request):
#     if request.method == 'POST':
#         logout(request)
#         return redirect('home')
