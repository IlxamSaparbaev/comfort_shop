from django.shortcuts import render, redirect      
from .models import Product
from .models import Transport
from .models import Furniture
from .models import Cloth
from .models import Sport
from django.db.models import Q
from django.contrib.auth.decorators import login_required


from .forms import ProductForm

def home(request):
    return render(request,'pages/home.html')

@login_required(redirect_field_name='login')
def electronics(request):
    search = request.GET.get('search')
    if search:
        products = Product.objects.filter(
            Q(title__icontains=search)
        )
    else:
        products = Product.objects.all()
    context = {
        'products': products
    }
    return render(
        request,
        'pages/electronics.html',
        context
    )
@login_required(redirect_field_name='login')
def sale_detail(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'product': product
    }
    return render(request, 'pages/sale_detail.html', context)
@login_required(redirect_field_name='login')
def transport(request):
    transports = Transport.objects.all()
    context = {
        'transports':transports
    }
    return render(request, 'pages/transport.html', context)

def transport_detail(request, pk):
    try:
        transport = Transport.objects.get(id=pk)
    except Transport.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'transport': transport
    }
    return render(request, 'pages/transport_detail.html', context)


@login_required(redirect_field_name='login')
def furniture(request):
    furnitures = Furniture.objects.all()
    context = {
        'furnitures': furnitures
    }
    return render(request, 'pages/furniture.html', context)

def furniture_detail(request, pk):
    try:
        furnitures = Furniture.objects.get(id=pk)
    except Furniture.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'furnitures': furnitures
    }
    return render(request, 'pages/furniture_detail.html', context)


@login_required(redirect_field_name='login')
def clothes(request):
    clothes = Cloth.objects.all()
    context = {
        'clothes': clothes
    }
    return render(request, 'pages/clothes.html', context)

def clothes_detail(request, pk):
    try:
        cloth = Cloth.objects.get(id=pk)
    except Cloth.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'cloth': cloth
    }
    return render(request, 'pages/clothes_detail.html', context)

@login_required(redirect_field_name='login')
def sport(request):
    sport = Sport.objects.all()
    context = {
        'sport': sport
    }
    return render(request, 'pages/sport.html', context)

def sport_detail(request, pk):
    try:
        sports = Sport.objects.get(id=pk)
    except Sport.DoesNotExist:
        return render(request, 'errors/404.html')
    context = {
        'sports': sports
    }
    return render(request, 'pages/sport_detail.html',context)

@login_required(redirect_field_name='login')
def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            """cd = form.changed_data
            Product.objects.create(
                title=cd['title'],
                image=cd['image'],
                description=cd['description'],
                price=cd['price'],
                author=cd['author'],
                condition=cd['condition']
            )"""
        return redirect(to='electronics')
    else: 
        form = ProductForm()

    #print(ProductForm(request.POST).is_valid())
    context = {
        'form': form
    }
    return render(request, 'pages/create.html', context)

def sale_delete(request, pk):
    ProductForm= Product.objects.get(id=pk)
    ProductForm.delete()
    return redirect(to='electronics')


def sale_update(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            image = form.cleaned_data['image']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            author = form.cleaned_data['author']

            product.title = title
            product.image = image
            product.description = description
            product.price = price
            product.author = author
            product.save()

            return redirect(to=electronics)
    else:
        form = ProductForm()
    
    context = {
        'form': form
    }
    return render(request, 'pages/update.html', context)