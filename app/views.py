from django.shortcuts import render,HttpResponse,redirect
from .models import login as log,state as st,district as dt,locations as loc
from .models import staff as stf,user as usr,feedback as fd, complaint as cm,labour as lb
from .models import bank as bnk,menu as mn
# Create your views here.

def index(request):
    role=request.session.get("role")
    if role == "admin":
        return redirect("/adminhome") 
    elif role == "staff":
        return redirect("/staffhome") 
    elif role == "user":
        return redirect("/userhome") 

    datast=st.objects.all()
    return render(request,"index.html",{"datast":datast})
def admin(request):
    role=request.session.get("role")
    if role == "admin":
        return redirect("/adminhome") 
    elif role == "staff":
        return redirect("/staffhome") 
    elif role == "user":
        return redirect("/userhome") 
    if request.POST:
        user = request.POST["username"]
        password = request.POST["password"]
        
        datac = log.objects.filter(username=user, password=password,role="admin").count()
        if datac==1:
                data=log.objects.get(username=user, password=password,role="admin")
                request.session['username'] = data.username
                request.session['role'] = data.role
                request.session['id'] = data.logid
                response = redirect('/adminhome')
                return response
        else:
                 return render(request,"adminlog.html",{"msg":"invalid username or password"})
    else:
        return render(request,"adminlog.html",{"msg":""})

def adminhome(request):
    role=request.session.get("role")
    if role != "admin":
        return redirect("/index")  

    return render(request,"adminhome.html")
def privacy(request):
    msg=""
    if request.POST:
        t1=request.POST["t1"]
        t2=request.POST["t2"]
        id=request.session['id']

        log.objects.filter(logid=id).update(username=t1,password=t2)


    returnpage="adminhead.html"
    pg="Privacy.html"
    if(request.session.get('role', ' ')=="staff"):
        returnpage="staffhead.html"
    elif(request.session.get('role', ' ')=="user"):
        returnpage="userhead.html"
        pg="Privacy1.html"
    return render(request,pg,{"role":returnpage,"msg":msg})
def getDistrict(request):
    id=request.GET["id"]
    datast=st.objects.get(state_id=id)
    datadt=dt.objects.filter(state=datast).all()
    res="<option value=''>-select-</option>"
    for d in datadt:
        res+="<option value='"+str(d.district_id)+"'>"+d.district+"</option>"
    return HttpResponse(res)

def Logout(request):
    try:
        del request.session['id']
        del request.session['role']
        del request.session['username']
        response = redirect("index")
        return response
    except:
        response = redirect("index")
        return response
def stafflogin(request):
    if request.POST:
        user = request.POST["username"]
        password = request.POST["password"]
        try:
            datac = log.objects.filter(username=user, password=password).count()
            if datac==1:
                data=log.objects.get(username=user, password=password)
                if data.role=="staff":
                    request.session['username'] = data.username
                    request.session['role'] = data.role
                    request.session['id'] = data.logid
                    response = redirect('/staffhome')
                    return response
                elif data.role=="user":
                    request.session['username'] = data.username
                    request.session['role'] = data.role
                    request.session['id'] = data.logid
                    response = redirect('/userhome')
                    return response
                else :
                    response = redirect('/index?msg=invalid access')
                    return response


            else:
                response = redirect('/index?msg=invalid username or password')
                return response
               
        except:
            response = redirect('/index?msg=something went wrong')
            return response
    else:
        response = redirect('/index')
        return response
def staffreg(request):
    name=request.POST["name"]
    addr=request.POST["addr"]
    aadhar=request.POST["aadhar"]
    category=request.POST["category"]
    Experience=request.POST["Experience"]
    salary=request.POST["salary"]
    state=request.POST["state"]
    district=request.POST["district"]
  
    phone=request.POST["phone"]
    mail=request.POST["mail"]
    files=request.FILES["files"]
    username=request.POST["username"]
    password=request.POST["password"]
    datast=st.objects.get(state_id=state)
    datadt=dt.objects.get(district_id=district)
    
    log.objects.create(username=username,password=password,role="staff")
    datal=log.objects.last()
    stf.objects.create(login=datal,name=name,address=addr,aadhaar_no=aadhar,phone_no=phone,email=mail,state=datast,district=datadt,category=category,exp=Experience,basic_salary=salary,photo=files,status="waiting")
    response = redirect('/index')
    return response
def userreg(request):
    name=request.POST["name"]
    addr=request.POST["addr"]
    state=request.POST["state"]
    district=request.POST["district"]
   
    phone=request.POST["phone"]
    mail=request.POST["mail"]
    files=request.FILES["file"]
    username=request.POST["username"]
    password=request.POST["password"]
    datast=st.objects.get(state_id=state)
    datadt=dt.objects.get(district_id=district)
    
    log.objects.create(username=username,password=password,role="user")
    datal=log.objects.last()
    usr.objects.create(login=datal,username=name,useraddress=addr,phoneno=phone,useremail=mail,
    state=datast,district=datadt,Photo=files,status="waiting")

    response = redirect('/index')
    return response
def staffhome(request):
    role=request.session.get("role")
    if role != "staff":
        return redirect("/index") 
    return render(request,"staffhome.html")
def userhome(request):
    role=request.session.get("role")
    if role != "user":
        return redirect("/index") 
    return render(request,"userhome.html")
def Add_state(request):
    msg=""
    if request.POST:
        t1=request.POST["state"]
        st.objects.create(state=t1)
        msg="inserted successfully"
    return render(request,"add_state.html",{"msg":msg})
def delete_state(request):
    id=request.POST["s_id"]
    st.objects.filter(state_id=id).delete()
    response = redirect("/list_state")
    return response
def edit_state(request):
    id=request.POST["s_id"]
    state=request.POST["state"]
    st.objects.filter(state_id=id).update(state=state)
    response = redirect("/list_state")
    return response
def list_state(request):
    datalst=st.objects.all()
    return render(request,"state_list.html",{"data":datalst})



def user_feed(request):
    if request.POST:
        t1= request.POST["t1"]
        t2= request.POST["t2"]
        fd.objects.filter(feedback_id=t1).update(reply=t2)
    data=fd.objects.all()
    return render(request,"user_feed.html",{"data":data})
def staff_complaints(request):
    if request.POST:
        t1= request.POST["t1"]
        t2= request.POST["t2"]
        cm.objects.filter(complaint_id=t1).update(reply=t2)
    data=cm.objects.all()
    return render(request,"staff_feed.html",{"data":data})

def complaints(request):
    id=request.session['id']
    datal=log.objects.get(logid=id)
    datas=stf.objects.get(login=datal)
    if request.POST:
        t1=request.POST["subject"]
        t2=request.POST["msg"]
        cm.objects.create(staff=datas,sub=t1,msg=t2,reply="")
    data=cm.objects.filter(staff=datas).all()
    return render(request,"complaints.html",{"data":data})
def feedback(request):
    id=request.session['id']
    datal=log.objects.get(logid=id)
    datau=usr.objects.get(login=datal)
    if request.POST:
        t1=request.POST["feedback"]
        fd.objects.create(userid=datau,feedback=t1,reply="")
    data=fd.objects.filter(userid=datau).all()
    return render(request,"feedback.html",{"data":data})

def find_labour(request):
    datas= st.objects.all()
    data=stf.objects.all()
    datc=stf.objects.count()
    
    if request.POST:
        t1=request.POST["state"]
        t2=request.POST["district"]
        t3=request.POST["location"]
        t4=request.POST["category"]
        datast=st.objects.get(state_id=t1)
        datadt=dt.objects.get(district_id=t2)
        datalc=loc.objects.get(location_id=t3)
        data=stf.objects.filter(state=datast,district=datadt,location=datalc).all()
        datc=stf.objects.filter(state=datast,district=datadt,location=datalc).count()


    
    return render(request,"find_labour.html",{"datas":datas,"data":data,"datc":datc})

def book_labour(request):
    staff=request.GET["staff"]
    state=request.GET["state"]
    district=request.GET["district"]
    location=request.GET["location"]
    category=request.GET["category"]
    datastf=stf.objects.get(staff_id=staff)
    if request.POST:
        t1=request.POST["fdate"]
        t2=request.POST["todate"]
        t3=request.POST["category"]
        t4=request.POST["staff"]
        t5=request.POST["aboutjob"]
        t6=request.POST["amt"]
        id=request.session['id']
        datal=log.objects.get(logid=id)
        datau=usr.objects.get(login=datal)
        
        datas=stf.objects.get(staff_id=t4)
        lb.objects.create(userid=datau,staff=datas,from_date=t1,to_date=t2,category=t3,desc=t5,amount=t6,reject="",status="waiting")
        return redirect("/find_labour/")

    return render(request,"book_labour.html",{"datastf":datastf,"staff":staff,"state":state,"district":district,"location":location,"category":category})


def staff_ongoing(request):
    datag=lb.objects.filter(status="approved").exclude(reject="rejected").all()
    return render(request,"staff_ongoing.html",{"data":datag})

def staff_rejected(request):
    datag=lb.objects.filter(reject="rejected").all()
    return render(request,"staff_rejected.html",{"data":datag})

def staff_completed(request):
    datag=lb.objects.filter(status="stfcompleted").all()
    return render(request,"staff_completed.html",{"data":datag})
def payment_completed(request):
    datag=lb.objects.filter(status="completed").all()
    return render(request,"payment_completed.html",{"data":datag})

def request_payment(request):
    lid=request.POST["lid"]
    lb.objects.filter(labour_id=lid).update(status="paymentrequested")
    return redirect("/staff_completed")

def waiting_payment(request):
    datag=lb.objects.filter(status="paymentrequested").all()
    return render(request,"waiting_payment.html",{"data":datag})

def payment_request(request):
    id=request.session['id']
    datal=log.objects.get(logid=id)
    datau=usr.objects.get(login=datal)
    msg=""
    if request.POST:
        t1=request.POST["lid"]
        t2=request.POST["holder"]
        t3=request.POST["card"]
        t4=request.POST["cvv"]
        t5=request.POST["exp"]
        t6=int(request.POST["amt"])
        bcc=bnk.objects.filter(holder=t2,card=t3,cvv=t4,exp=t5).count()
        if bcc==1:
            datb=bnk.objects.get(holder=t2,card=t3,cvv=t4,exp=t5)
            bal=int(datb.bal)
            if bal < t6 :
                msg="insufficient Balance"
            else:
                bmt=bal-t6
                bnk.objects.filter(holder=t2,card=t3,cvv=t4,exp=t5).update(bal=bmt)
                lb.objects.filter(labour_id=t1).update(status="completed")
                msg="payment successfull"
        else :
            msg="invalid account details"


    datag=lb.objects.filter(status="paymentrequested",userid=datau).all()
    datac=lb.objects.filter(status="paymentrequested",userid=datau).count()
    return render(request,"payment_request.html",{"data":datag,"datac":datac,"msg":msg})

def payment_history(request):
    datag=lb.objects.filter(status="completed").all()
    return render(request,"payment_history.html",{"data":datag})

def ongoing(request):
    id=request.session['id']
    datal=log.objects.get(logid=id)
    datau=stf.objects.get(login=datal)
    datag=lb.objects.filter(status="approved",reject="confirm",staff=datau).all()
    return render(request,"ongoing.html",{"data":datag})

# praveeen

def schedule(request):
    datasb=lb.objects.exclude(status="completed").exclude(status="paymentrequested").exclude(reject="rejected").all()
    return render(request,"schedule.html",{"datakk":datasb})



def delete_labour(request):
    id=request.POST["labour_id"]
    lb.objects.filter(labour_id=id).delete()
    response = redirect("/schedule")
    return response

def complete(request):
     dataty=lb.objects.filter(status="completed")
     return render(request,"complete.html",{"datatt":dataty})

def rejected(request):
     datatm=lb.objects.filter(reject="rejected").all()
     return render(request,"rejected.html",{"datamm":datatm})


#/* amitha */
def add_district(request):
    msg=""
    data=st.objects.all()
    if request.POST:
        t1=request.POST["state"]
        t2=request.POST["district"]
        datast=st.objects.get(state_id=t1)
        dt.objects.create(state=datast,district=t2)
        msg="inserted successfully"
    return render(request,"add_district.html",{"msg":msg,"data":data})

def list_district(request):
    data=dt.objects.all()
    dataldt=st.objects.all()
    return render(request,"list_district.html",{"data":data,"datas":dataldt})

def edit_district(request):
    id=request.POST["d_id"]
    state=request.POST["district"]
    sid=request.POST["state"]
    state=st.objects.get(state_id=sid)
    dt.objects.filter(district_id=id).update(district=state)
    response = redirect("/list_district")
    return response

def delete_district(request):
    id=request.POST["d_id"]
    st.objects.filter(district_id=id).delete()
    response = redirect("/list_district")
    return response

def list_user(request):
    datausr=usr.objects.filter(status="approved").all()
    if request.POST:
        t1=request.POST["ser_user"]
        datausr=usr.objects.filter(status="approved",username=t1).all()

    
    return render(request,"list_user.html",{"data":datausr})
def delete_user(request):
    id=request.POST["user_id"]
    usr.objects.filter(user_id=id).delete()
    response = redirect("/list_user")
    return response

def list_staff(request):
    datast=stf.objects.filter(status="approved").all()
    if request.POST:
        t1=request.POST["search_cat"]
        datast=stf.objects.filter(status="approved",category=t1).all()

    return render(request,"list_staff.html",{"data":datast})
def delete_staff(request):
    id=request.POST["staff_id"]
    stf.objects.filter(staff_id=id).delete()
    response = redirect("/list_staff")
    return response
def approve_staff(request):
    datastf=stf.objects.filter(status="waiting").all()
    return render(request,"approve_staff.html",{"data":datastf})
    
def approved_staff(request):
    id=request.POST["staff_id"]
    stf.objects.filter(staff_id=id).update(status="approved")
    response = redirect("/approve_staff")
    return response
def reject_staff(request):
    id=request.POST["staff_id"]
    stf.objects.filter(staff_id=id).delete()
    response = redirect("/approve_staff")
    return response
def approve_user(request):
    datauser=usr.objects.filter(status="waiting").all()
    return render(request,"approve_user.html",{"data":datauser})

def approved_user(request):
    id=request.POST["user_id"]
    usr.objects.filter(user_id=id).update(status="approved")
    response = redirect("/approve_user")
    return response

def reject_user(request):
    id=request.POST["user_id"]
    usr.objects.filter(user_id=id).delete()
    response = redirect("/approve_user")
    return response
def newjob(request):
    data=lb.objects.filter(status="waiting").all()
    return render(request,"newjob.html",{"data":data})

def job_confirm(request):
    dataff=lb.objects.filter(status="approved",reject="").all()
    return render(request,"job_confirm.html",{"datavb":dataff})

def confirm_labour(request):
    id=request.POST["labour_id"]
    lb.objects.filter(labour_id=id).update(reject="confirm")
    return redirect("/job_confirm")
    
def reject_labour(request):
    id=request.POST["labour_id"]
    lb.objects.filter(labour_id=id).update(reject="rejected")
    return redirect("/job_confirm")

def newjob_approve(request):
    id=request.POST["lid"]
    lb.objects.filter(labour_id=id).update(status="approved")
    return redirect("/newjob")

def task_complete(request):
    id=request.POST["lid"]
    lb.objects.filter(labour_id=id).update(status="stfcompleted")
    return redirect("/ongoing")
    
def addmenu(request):
    return render(request,"addmenu.html")

def menu(request):
    if request.POST:
        name=request.POST["name"]
        price=request.POST["price"]
        details=request.POST["details"]
        image=request.FILES["image"]
        mn.objects.create(name=name,price=price,details=details,image=image)
    return render(request,"/addmenu?msg=menu added successfully")

def menudetails(request):
    return render(request,"menudetails.html")

def neworders(request):
    return render(request,"neworders.html")

def delivered(request):
    return render(request,"delivered.html")
