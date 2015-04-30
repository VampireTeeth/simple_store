

import os
import sys


def main():
  os.environ.setdefault("DJANGO_SETTINGS_MODULE", "simple_store.settings")
  import django
  django.setup()
  from storeapp.models import Product 
  Product.objects.all().delete()
  products = [
      {'name' : 'Good keyboard', 
        'price' : 10.99, 
        'description' : 'A very gaming keyboard', 
        'imglink' : 'http://hothardware.com/articleimages/Item2168/small_das_keyboard_stock.jpg'}, 

      {'name' : 'Gaming keyboard', 
        'price' : 21.99, 
        'description' : 'A cool gaming keyboard', 
        'imglink' : 'http://hothardware.com/articleimages/Item2168/small_das_keyboard_stock.jpg'}, 

      {'name' : 'Good keyboard 1', 
        'price' : 11.99, 
        'description' : 'Another very gaming keyboard', 
        'imglink' : 'http://hothardware.com/articleimages/Item2168/small_das_keyboard_stock.jpg'}, 

      {'name' : 'Lenovo laptop',
        'price' : 493.95,
        'description' : 'A robust entry-level laptop for the user looking for an affordable yet fully featured laptop, the Lenovo G50-30 features a 15.6" HD display, Celeron N2830 processor and Intel HD graphics card',
        'imglink' : 'https://doxz7msmg7sxx.cloudfront.net/media/catalog/product/cache/21/image/992x558/9df78eab33525d08d6e5fb8d27136e95/g/5/g50_1_1.jpg'},


      {'name' : 'Performance Mouse M950t',
        'price' : 129.95,
        'description' : 'Both optical and traditional laser mice use irregularities on the surface to track the direction and speed of the mouse movements. For this reason, traditional mice do not perform well on shiny surfaces. This is where Darkfield Laser Tracking comes in. Darkfield uses the smallest possible detail to create a micro-road map of the surface so you get better precision on more surfaces, even glass.',
        'imglink' : 'http://www.logitech.com/assets/19681/19681.png' },
      ]


  for kwargs in products:
    p = Product(**kwargs)
    p.save()


if __name__ == "__main__":
  main()
