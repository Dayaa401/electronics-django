from django.db import  models

class Customer(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField(unique=True)
    mobile=models.CharField(max_length=10)
    password=models.CharField(max_length=20)

    def isexit(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False

    #check email id is match or not
    @staticmethod
    def getmail(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
    

    def __str__(self):
        return self.firstname+" "+self.lastname