from django.shortcuts import render, redirect

from models import Product, Order

# Create your views here.

def cartItems(cart):
  items = []
  for product_id in cart:
    items.append(Product.objects.get(id=product_id))
  return items

def totalPrice(cartItems):
  total = 0.0
  for item in cartItems:
    total += item.price
  return total


def catalog(request):
  cart = request.session.get('cart', [])

  if request.method == 'POST':
    cart.append(int(request.POST['product_id']))
    request.session['cart'] = cart
    return redirect('catalog')

  request.session['cart'] = cart
  store_items = Product.objects.all()
  ctx = {'store_items' : store_items, 'cart' : cart, 'cart_size' : len(cart)} 
  return render(request, 'catalog.html', ctx)


def cart(request):
  cart = request.session.get('cart', [])
  request.session['cart'] = cart
  cart_items = cartItems(cart)
  total_price = totalPrice(cart_items)
  request.session['total_price'] = total_price
  ctx = {'cart' : cart, 'cart_size' : len(cart), 
      'cart_items' : cart_items, 
      'total_price': total_price }
  return render(request, 'cart.html', ctx)

def removeFromCart(request):
  cart = request.session.get('cart', [])
  product_id = int(request.POST['product_id'])
  product_idx = cart.index(product_id)
  cart.pop(product_idx)
  request.session['cart'] = cart
  return redirect('cart')

def checkout(request):
  cart = request.session.get('cart', [])
  total_price = request.session.get('total_price', 0.0)
  ctx = {'cart' : cart, 'cart_size' : len(cart), 'total_price' : total_price}
  return render(request, 'checkout.html', ctx)


def completeOrder(request):
  cart = request.session.get('cart', [])
  total_price = request.session.get('total_price', 0.0)
  cart_items = cartItems(cart)
  items_str = ','.join(map(lambda i: i.name, cart_items))

  order = Order()
  order.total_price = total_price
  order.first_name = request.POST['first_name']
  order.last_name = request.POST['last_name']
  order.address1 = request.POST['address1']
  order.address2 = request.POST['address2']
  order.city = request.POST['city']
  order.postcode = request.POST['postcode']
  order.payment_type = request.POST['payment_type']
  order.payment_data = request.POST['payment_data']
  order.items = items_str
  order.fulfilled = False
  order.save()
  request.session['cart'] = []
  return render(request, 'complete_order.html', {'cart_size' : len(request.session['cart'])})
