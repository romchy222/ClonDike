from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Application
from django.urls import reverse
from django.contrib import messages
from django.db.models import Q

def index(request):
    categories = Category.objects.all()
    return render(request, 'catalog/index.html', {'categories': categories})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = category.products.all()
    return render(request, 'catalog/category_detail.html', {
        'category': category,
        'products': products
    })

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment', '')

        if not name or not phone:
            messages.error(request, 'Пожалуйста, заполните имя и телефон.')
        else:
            Application.objects.create(
                product=product,
                name=name,
                phone=phone,
                comment=comment
            )
            messages.success(request, 'Заявка успешно отправлена!')
            return redirect(reverse('catalog:product_detail', args=[product.pk]))

    return render(request, 'catalog/product_detail.html', {'product': product})


def search_view(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Product.objects.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        )
    return render(request, 'catalog/search_results.html', {'query': query, 'results': results})
