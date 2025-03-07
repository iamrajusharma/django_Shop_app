from django.shortcuts import render,redirect
from shopapp.models import user
from .models import user,product,catagry
from django.contrib.auth.hashers import make_password,check_password



from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from .models import user,order


def home(request):
    products=product.objects.all()
    catagrys=catagry.objects.all()
    cetagryID = request.GET.get('category')
    if 'cart' not in request.session:
        request.session['cart'] = {}
    
    if cetagryID:
              products = products.filter(Catagry_id=cetagryID) 
    return render(request,'home.html',{'products':products,'catagrys':catagrys})
"""def get_product(request):
      if request.method=="POST":
          product_id=request.POST.get('product_id')
          print(product_id)    
          return redirect('home')
    return redirect('home')
def get_product(request):
    if request.method == "POST":
       
        product_id = request.POST.get('product_id')
        cart=request.session.get('cart')
        if cart:
            quantity=cart.get(product_id)
            if quantity:
                cart[product_id]=quantity+1
            else:
                cart[product_id]=1
        else:
            cart[product_id]=1
    else:
        cart={}
        cart[product_id]=1
    request.session['cart']=cart
    print(request.session['cart'])

        return redirect('home')
    return redirect('home')"""
def get_product(request):
    if request.method == "POST":
        product_id = request.POST.get('product_id')  
        action=request.POST.get('action')
    

        # Debugging to ensure product_id is captured
        if not product_id or not action:
            print("Product ID is missing in the request!")
            return redirect('home')
       
        # Get the cart from the session or initialize an empty cart
        cart = request.session.get('cart', {})

        # Update the cart with the product
        if action == "add":
            cart[product_id]=cart.get(product_id,0)+1
        elif action=="remove":
            if product_id in cart:
                if cart[product_id]>1:
                    cart[product_id] -=1
                else:
                    del cart[product_id]      

        
        request.session['cart'] = cart
        print("prodcts :", request.session['cart'])  # Debugging

    return redirect('home')


def about(request):
    return render(request,'about.html')



def singup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        register_data=user.objects.filter(email=email).exists()
        if register_data:
           return render(request,'singup.html',{'error':'email alredy register'})
          
        else:
            hashed_password = make_password(password)
            
            # Create a new user instance and assign the hashed password
            new_user = user(name=name, email=email, phone=phone, password=hashed_password)
            new_user.save()
       
            return render(request, 'login.html')  
        
    return render(request, 'singup.html') 
 
# def login(request): 
#     if request.method=="POST":
#          email=request.POST.get('email')
#          password=request.POST.get('password')
#          """  print(email,password)"""
#          data=user.objects.filter(email=email,password=password).exists()
#          user_instance = user.objects.get(email=email)
#          if user_instance:
#             print(user_instance)
#             role = user_instance.Role
#             print(f"The role of the user with email {email} is {role}.")
#          else:
#             print("No user found with the provided email.")

        
#          if data:
#                return redirect('home')
#          else:
#                return render(request,'login.html',{'error': 'Invalid Email or password'})
        
#     return render(request,'login.html')
# Replace 'shopapp.models' with the correct import path for your user model
 # Ensure you're importing the correct user model

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        request.session.clear()
        # Check if the user exists with the given email
        data = user.objects.filter(email=email).exists()
        

        if data:
           
            user_instance = user.objects.get(email=email)
            
            # Check the password using check_password()
            if check_password(password, user_instance.password):
                request.session['user_name'] = user_instance.name 
                
                # Check the user's role
                role = user_instance.Role  # Assuming Role is stored in a case-sensitive way
                
                # Redirect based on the role
                if role == "Custumer":  # If role is 'customer'
                    return redirect('home')  # Replace 'customerhome' with the correct URL name for your customer home page
                elif role == "home":  # If role is 'admin'
                    return redirect('adminapp:admin')  # Replace 'adminhome' with the correct URL name for your admin home page
                else:
                    return render(request, 'login.html', {'error': 'Invalid role assigned to the user.'})
            else:
                return render(request, 'login.html', {'error': 'Invalid Email or Password'})
        else:
            return render(request, 'login.html', {'error': 'Invalid Email or Password'})
    
    return render(request, 'login.html')



    

  
"""
def show_prodct(request):
    data = product.objects.all() 
    return render(request, 'admin.html', {'data': data}) """



def logout(request):
    # Clear the session to log the user out
    request.session.clear()
    return redirect('home')



def cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_amount=0

    # Loop through the cart to get product details
    for product_id, quantity , in cart.items():
        try:
            product_obj = product.objects.get(id=product_id)
            product_total=int(product_obj.price)*int(quantity)
            total_amount +=product_total
            cart_items.append({
                'name': product_obj.product_name,
                'product': product_obj,
                'quantity': quantity,
                'image': product_obj.image.url if product_obj.image else None,
                'total_price': product_total
                
            })
             
        except product.DoesNotExist:
            continue  # Skip if the product does not exist

    return render(request, 'cart.html', {'cart_items': cart_items,'total_amount':total_amount})




# def order(request):
#      if request.method=="POST":
#          state=request.POST.get('state')
#          phone=request.POST.get('phone')
#          user=request.session.get('user_name')
#          cart=request.session.get('cart')
#          print(state,phone,user,cart)
#          return redirect('cart')
         


# def product_order(request):
#     if request.method == "POST":
#         # Get form data
#         address = request.POST.get('address')
#         phone = request.POST.get('phone')
#         user_name = request.session.get('user_name')
#         cart = request.session.get('cart', {})
#         print(address,phone,user_name,cart)

#         place_order=order(address=address,phone=phone,user_name=user_name,cart=cart)
#         place_order.save()
#         return redirect('cart')
#     return render(request,'cart')

def product_order(request):
    if request.method == "POST":
        address = request.POST.get('address', '')
        phone = request.POST.get('phone', '')
        user_name = request.session.get('user_name', 'Anonymous')  # Fallback for user_name
        cart = request.session.get('cart', {})
        print("Debug data:", address, phone, user_name, cart)

        try:
            # Fetch or create a default user from your custom user model
            default_user,created = user.objects.get_or_create(name=user_name)

            for product_id, quantity in cart.items():
                try:
                    product_obj = product.objects.get(id=product_id)
                except product.DoesNotExist:
                    print(f"Product with ID {product_id} not found")
                    continue

                total_price = product_obj.price * quantity

                # Create the order
                order.objects.create(
                    product=product_obj,
                    user=default_user,  # Use the instance of your custom user
                    address=address,
                    phone=phone,
                    user_name=user_name,
                    cart={"product_id": product_id, "quantity": quantity},
                    price=int(total_price),
                    quantity=quantity
                )

            # Clear cart after successful orders
            request.session['cart'] = {}
            return redirect('product_order')

        except Exception as e:
            print(f"Error creating orders: {e}")

    return render(request,'cart.html')


# def order_summary(request, order_ids):
#     # Split the order IDs passed from the URL
#     order_ids = order_ids.split(',')
#     orders = order.objects.filter(id__in=order_ids)

#     return render(request, 'order_summary.html', {'orders': orders})


def order_view(request):
    if request.user.is_authenticated:
        orders = order.objects.filter(user=request.user)
        print("Orders:", orders)
    else:
        orders = []
    return render(request, 'order.html', {'orders': orders})




