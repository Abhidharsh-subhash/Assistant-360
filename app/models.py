from django.db import models

# Create your models here.

class login(models.Model):
    logid = models.AutoField(primary_key=True)
    username = models.CharField("username",max_length=100)
    password =  models.CharField("password",max_length=100)
    role=models.CharField('role',max_length=10)
    #logid,username,password,role

class state(models.Model):
    state_id = models.AutoField(primary_key=True)
    state=models.CharField("state",max_length=100)

class district(models.Model):
    district_id=models.AutoField(primary_key=True)
    district=models.CharField("district",max_length=100)
    state=models.ForeignKey(state, on_delete=models.CASCADE, null=True)

class locations(models.Model):
    location_id=models.AutoField(primary_key=True)
    location=models.CharField("location",max_length=100)
    distict=models.ForeignKey(district, on_delete=models.CASCADE, null=True)
    @property
    def getalldist(self):
        data=district.objects.filter(state=self.distict.state).all()
        return data

class staff(models.Model):
    staff_id= models.AutoField(primary_key=True)
    login=models.ForeignKey(login,on_delete=models.CASCADE,null=True)
    name=models.CharField("staffname",max_length=100)
    address=models.CharField("address",max_length=500)
    aadhaar_no=models.CharField("aadhaar",max_length=100)
    phone_no=models.CharField("phone_no",max_length=100)
    email=models.CharField("email",max_length=100)
    state=models.ForeignKey(state,on_delete=models.CASCADE, null=True)
    district=models.ForeignKey(district, on_delete=models.CASCADE, null=True)
    location=models.ForeignKey(locations, on_delete=models.CASCADE, null=True)
    category=models.CharField("category",max_length=100)
    
    exp=models.CharField("experience",max_length=100)
    basic_salary=models.CharField("basic_salary",max_length=100)
    photo=models.FileField("photo:",max_length=100,upload_to="images/")
    status=models.CharField("status:",max_length=100)
    #staff_id,login,name,address,aadhaar_no,phone_no,email,state,district,location,category,license,exp,basic_salary,photo,status
class user(models.Model):
    user_id=models.AutoField(primary_key=True)
    login=models.ForeignKey(login,on_delete=models.CASCADE,null=True)
    username=models.CharField("username",max_length=100)
    useraddress=models.CharField("address",max_length=500)
    phoneno=models.CharField("Phone_no",max_length=100)
    useremail=models.CharField("email",max_length=100)
    state=models.ForeignKey(state,on_delete=models.CASCADE, null=True)
    district=models.ForeignKey(district, on_delete=models.CASCADE, null=True)
    location=models.ForeignKey(locations, on_delete=models.CASCADE, null=True)
    Photo=models.FileField("photo:",max_length=100,upload_to="images/")
    status=models.CharField("status:",max_length=100)
    #user_id,login,username,useraddress,phoneno,useremail,state,district,location,Photo,status

class labour(models.Model):
    labour_id=models.AutoField(primary_key=True)
    userid=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    staff=models.ForeignKey(staff,on_delete=models.CASCADE,null=True)
    from_date=models.CharField("from date",max_length=100)
    to_date=models.CharField("to date",max_length=100)
    category=models.CharField("category",max_length=100)
    desc=models.CharField("description",max_length=500)
    amount=models.CharField("amount",max_length=100)
    reject=models.CharField("reject",max_length=100)
    status=models.CharField("status",max_length=100)
    #userid,staff,from_date,to_date,category,desc,amount,reject,status
class feedback(models.Model):
    feedback_id=models.AutoField(primary_key=True)
    userid=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    feedback=models.CharField("feedback",max_length=500)
    
    reply=models.CharField("reply",max_length=500)
    #userid,feedback,reply
class complaint(models.Model):
    complaint_id=models.AutoField(primary_key=True)
    staff=models.ForeignKey(staff,on_delete=models.CASCADE,null=True)
    sub=models.CharField("sublect",max_length=200)
    msg=models.CharField("message",max_length=500)
    reply=models.CharField("reply",max_length=500)
    #staff,sub,msg,reply
    
class bank(models.Model):
     bank_id=models.AutoField(primary_key=True)
     holder=models.CharField("holder",max_length=100)
     card=models.CharField("card",max_length=100)
     cvv=models.CharField("cvv",max_length=100)
     exp=models.CharField("exp",max_length=100)
     bal=models.CharField("bal",max_length=100)

class menu(models.Model):
     menuid=models.AutoField(primary_key=True)
     name=models.CharField("name",max_length=100)
     price=models.CharField("price",max_length=100)
     details=models.CharField("details",max_length=100)
     image=models.FileField("image:",max_length=100,upload_to="images/")

class orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    user=models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    menu=models.ForeignKey(menu,on_delete=models.CASCADE,null=True)
    order_status=models.CharField("order_status",max_length=100)
    @property
    def getOrderItems(self):
        return orderitem.objects.filter(order = self).all()

class orderitem(models.Model):
    order_itemid=models.AutoField(primary_key=True)
    order=models.ForeignKey(orders,on_delete=models.CASCADE,null=True)
    menu=models.ForeignKey(menu,on_delete=models.CASCADE,null=True)
    quantity=models.CharField("quantity",max_length=100)



