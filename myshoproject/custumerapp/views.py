from django.shortcuts import render
from shopapp.models import user
from  shopapp.models import user,product,catagry
# Create your views here.
def customer_home(request):
     products=product.objects.all()
     catagrys=catagry.objects.all()
     cetagryID = request.GET.get('category')
    
    

    #  if cetagryID:
            #   products = products.filter(Catagry_id=cetagryID) 
     print(products)
     return render(request,'custumer.html',{'products':products,'catagrys':catagrys})
    #  return render(request,'custumer.html')