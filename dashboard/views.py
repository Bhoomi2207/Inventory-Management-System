from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from pyparsing import Or
from .models import Product, Order
from .forms import ProductForm, OrderForm, StaffForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import auth_users, allowed_users
# Create your views here.


@login_required(login_url='user-login')
def index(request):
    product = Product.objects.all()
    product_count = product.count()
    order = Order.objects.all()
    order_count = order.count()
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.customer = request.user
            obj.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'form': form,
        'order': order,
        'product': product,
        'product_count': product_count,
        'order_count': order_count,
        'customer_count': customer_count,
    }
    return render(request, 'dashboard/index.html', context)


@login_required(login_url='user-login')
def products(request):
    products = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name')
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-products')
    else:
        form = ProductForm()
    context = {
        'product': products,
        'form': form,
    }
    return render(request, 'dashboard/products.html', context)


@login_required(login_url='user-login')
def product_detail(request, pk):
    context = {

    }
    return render(request, 'dashboard/products_detail.html', context)


@login_required(login_url='user-login')
def customers(request):
    customer = User.objects.filter(groups=2)
    customer_count = customer.count()
    context = {
        'customer': customer,
        'customer_count': customer_count,
    }
    return render(request, 'dashboard/customers.html', context)

@login_required(login_url='user-login')
def customer_edit(request, pk):
    worker = User.objects.get(id=pk)
    if request.method == 'POST':
        form = StaffForm(request.POST, instance=worker)
        if form.is_valid:
            form.save()
            return redirect('dashboard-customers')
    else:
        form = StaffForm(instance=worker)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/customer_edit.html', context)

@login_required(login_url='user-login')
def customer_detail(request, pk):
    products = Product.objects.all()
    customer = User.objects.get(id=pk)
    orders = Order.objects.all()
    context = {
        'products':products,
        'orders':orders,
        'customer': customer,
    }
    return render(request, 'dashboard/customers_detail.html', context)

@login_required(login_url='user-login')
def customer_delete(request, pk):
    worker = User.objects.get(id=pk)
    if request.method == 'POST':
        worker.delete()
        return redirect('dashboard-customers')
    return render(request, 'dashboard/customer_delete.html')


@login_required(login_url='user-login')
def product_edit(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-products')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/products_edit.html', context)


@login_required(login_url='user-login')
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-products')
    context = {
        'item': item
    }
    return render(request, 'dashboard/products_delete.html', context)

@login_required(login_url='user-login')
def order(request):
    order = Order.objects.order_by('-payment_status')
    order_count = order.count()
    context = {
        'order': order,
        'order_count': order_count,
    }
    return render(request, 'dashboard/order.html', context)
