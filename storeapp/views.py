from django.shortcuts import render

from models import Product

# Create your views here.
def catalog(request):
  if 'cart' not in request.session:
    request.session['cart'] = []

  cart = request.session['cart']

  store_items = Product.objects.all()
  ctx = {'store_items' : store_items, 'cart' : cart} 
  return render(request, 'catalog.html', ctx)

