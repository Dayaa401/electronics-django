from django.shortcuts import render,redirect
from .product import Product
from .catogery import Catogery
from django.contrib.auth.hashers import make_password,check_password
from .customer import Customer
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
        if not email:
            error_msg = "Please fill in the email."
        elif Customer.objects.filter(email=email).exists():
            error_msg = "Email already exists."

        # If no error, save customer
        if not error_msg:
            success_msg = "Account created successfully."
            customerdata.password = make_password(password)
            msg ={'success': success_msg}
            customerdata.save()
            return render(request, 'signup.html', msg)
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
