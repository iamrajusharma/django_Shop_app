from django.shortcuts import render
from shopapp.models import product,catagry
# Create your views here.
"""def admin_home(request):
    
       if request.method=="POST":
           image=request.POST.get('image')
           product_name=request.POST.get('product_name')
           description=request.POST.get('description')
           price=request.POST.get('price')
           image_data=product(image=image,price=price,description=description,product_name=product_name)
           image_data.save()
           return render(request,"admin.html")
       return render(request,'admin.html')"""

def admin_home(request):
      if request.method=="POST":
           image=request.POST.get('image')
          
           product_name=request.POST.get('product_name')
           description=request.POST.get('description')
           price=request.POST.get('price')
           image_data=product(image=image,price=price,description=description,product_name=product_name)
           image_data.save()
           return render(request,"admin.html")
      return render(request,'admin.html')
 

def show_prduct(request):
        """  data = user.objects.all()  
        data_image=product.objects.all()
        print(data_image)
         
        return render(request, 'admin.html', {'data': data})"""  
        products=product.objects.all()
        catagrys=catagry.objects.all()
        print(products)
        return render(request,'show_product.html',{'products':products,'catagrys':catagrys})
    

"""
def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if the user exists with the given email and password
        data = user.objects.filter(email=email, password=password).exists()
        
        if data:
            # Get the user instance
            user_instance = user.objects.get(email=email)

            # Check the user's role
            role = user_instance.Role  # Assuming Role is stored in a case-sensitive way
            print(role)
            # Redirect based on the role
            if role == "Custumer":  # If role is 'customer'
                return redirect('custumerapp:custumer')  # Replace 'customerhome' with the correct URL name for your customer home page
            elif role == "admin":  # If role is 'admin'
                return redirect('adminapp:admin')  # Replace 'adminhome' with the correct URL name for your admin home page
            else:
                return render(request, 'login.html', {'error': 'Invalid role assigned to the user.'})
        else:
            return render(request, 'login.html', {'error': 'Invalid Email or Password'})
    
    return render(request, 'login.html')"""
