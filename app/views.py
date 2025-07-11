from django.shortcuts import render,redirect
from .product import Product
from .catogery import Catogery
from django.contrib.auth.hashers import make_password,check_password
from .customer import Customer
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
   
    
    catogeries=Catogery.objects.all()
    catogery_ID=request.GET.get('catogery')
    if catogery_ID:
        products=Product.get_catogery_id(catogery_ID)
    else:
        products=Product.objects.all()
    data={'products':products, 'catogeries':catogeries}
    return render(request,'home.html',data)

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        password = request.POST['password']

        usedata = [firstname, lastname, email, mobile, password]
        print(usedata)
       
       # values 
        Uservalues={
        'firstname':firstname,
        'lastname':lastname,
        'email':email,
        'mobile':mobile
        }
        # Create a customer instance
        customerdata = Customer(
            firstname=firstname,
            lastname=lastname,
            email=email,
            mobile=mobile,
            password=password  # we'll hash it later
        )

        error_msg = None
        success_msg = None

        # Validate email field
        if (not firstname):
            error_msg = "First name is required."
        elif (not lastname):
            error_msg = "Lastname is required."
        elif (not email):
            error_msg = "Email is required."
        elif (not mobile):
            error_msg = "Mobile number is required."
        elif (not password):
            error_msg = "Password is required."
        elif (customerdata.isexit()):
            error_msg = "Email already exists."


        # If no error, save customer
        if not error_msg:
            customerdata.password = make_password(customerdata.password)
            success_msg = "Account created successfully."
            
            msg ={'success': success_msg}
            customerdata.save()
            return render(request,'signup.html', msg)
        else:

            msg = {'error': error_msg, 'value':Uservalues}
            return render(request, 'signup.html', msg)

def login(request):
    if request.method=='GET':
        return render (request,'login.html')
    else:
        email=request.POST['email']
        password=request.POST['password']
        users=Customer.getmail(email)
        error_msg=None
        if users:
            #password check
            check=check_password(password,users.password)
            if check:
                request.session['customer']=users.id
                return redirect('/')
            else:
                error_msg='incorrect password'
                msg={'error':error_msg}
                return render(request,'login.html',msg)
        else:
            error_msg="incorrect email"
            msg={'error':error_msg}
            return render(request,'login.html',msg)

# Create your views here.
# add to cart view

def add_to_cart(request):
    product_id = str(request.POST.get('product_id'))
    action = request.POST.get('action')
    quantity = int(request.POST.get('quantity', 1))

    cart = request.session.get('cart', {})

    if action == 'increase':
        cart[product_id] = cart.get(product_id, 0) + quantity
    elif action == 'decrease':
        if product_id in cart:
            cart[product_id] -= quantity
            if cart[product_id] <= 0:
                del cart[product_id]
    else:
        cart[product_id] = quantity

    request.session['cart'] = cart
    return redirect('/')



def cart(request):
    cart = request.session.get('cart')
    if not cart:
        cart = {}
    product_ids = list(cart.keys())
    products = Product.objects.filter(id__in=product_ids)

    return render(request, 'cart.html', {'products': products, 'cart': cart})


from .orders import Order

def checkout(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer_id = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.objects.filter(id__in=list(cart.keys()))

        for product in products:
            order = Order(
                customer=Customer(id=customer_id),
                product=product,
                price=product.price,
                address=address,
                phone=phone,
                quantity=cart[str(product.id)]
            )
            order.placeOrder()
        
        request.session['cart'] = {} 
        return redirect('/')





def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product_detail.html', {'product': product})
