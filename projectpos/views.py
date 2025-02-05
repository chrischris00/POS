# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
from .models import Owners
from .models import Table
from django.core.mail import send_mail
from .models import Order
from .models import Tip
from .models import Bill_Setting

from .models import Orderlish


# Create your views here.
# Start Tong
log = []


def Login(request):
    return render(request, 'Login.html')


def Forgetpassword(request):
    email = request.POST.get('email', "x")
    idcard = request.POST.get('idcard', "x")
   # p = Owners.objects.get(email=email, ID_card=idcard)
    # if p == True:
    # send_mail('Thank you for registering to our site', p.password,
    #        'chonnasit.s@ku.th', ['tong25658@gmail.com'], fail_silently=False)

    return render(request, 'Forgetpassword.html')


def sub(request):
    email = request.POST.get('email')
    idcard = request.POST.get('idcard')

    p = Owners.objects.get(email=email, ID_card=idcard)
    print(p)
    if p:
        send_mail('Thank you for registering to our site', p.password,
                  'chonnasit.s@ku.th', ['tong25658@gmail.com'], fail_silently=False)
    return render(request, 'Login.html')


def Repassword(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    passwordnew = request.POST.get('passwordnew', "d")
    passwordnewre = request.POST.get('passwordnewre')
    if passwordnew == passwordnewre:
        p = Owners.objects.get(email=email, password=password)
        p.password = passwordnew
        p.save()
    return render(request, 'Repassword.html')


def Tableroom(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email != None:
        log.append(email)
        log.append(password)
    if Owners.objects.filter(email=log[0], password=log[1]).exists():
        tables = Table.objects.all()
        return render(request, 'Tableroom.html', {'tables': tables})
    else:
        log.remove(log[0])
        log.remove(log[0])
        return render(request, 'Login.html',  {'alert_flag': True})


def Kitchen(request):
    return render(request, 'Kitchen.html')


def Raw(request):
    return render(request, 'Raw.html')


def Rawmaterial(request):
    return render(request, 'Rawmaterial.html')
# End  Tong

# Start Top


def AddFood(request):
    fn=request.POST.get('abcdef',False)
    print(request)
    print(fn)
    if(fn != False):
        addtypefood=Order.objects.create(list=' ',priceorder=0,number = 0,price = 0,type_food = fn)
        addtypefood.save()
    
    data=Order.objects.all()
    return render(request,'addFood.html',{'posts':data})


def DeleteDrink(request):
    return render(request, 'deleteDrink.html')


def DeleteFood(request):
    return render(request, 'deleteFood.html')


def Deleteice(request):
    return render(request, 'deleteice.html')


def Drink(request):
    return render(request, 'Drink.html')


def Food(request):
    tableadd = request.POST.get('product', "a")
    Q = request.POST.get('Q', " None")
    print(tableadd)
    print(Q)
    return render(request, 'food.html')


def Ice_Cream(request):
    return render(request, 'Ice cream.html')


def SellectCategory(request):
    return render(request, 'sellectCategory.html')
# End top

# Start Frong


def Cash(request):
    return render(request, 'Cash.html')


def Cash_Success(request):
    return render(request, 'Cash_Success.html')


def Transfer(request):
    return render(request, 'Transfer.html')


def Transfer_Success(request):
    return render(request, 'Transfer_Success.html')
# End Frong

# start Tomtam


def Add_Employee(request):
    return render(request, 'Add_Employee.html')


def Edit_Food(request):
    return render(request, 'edit_food.html')


def Edit_Employee(request):
    return render(request, 'edit_Employee.html')


def Employee_list(request):
    return render(request, 'Employee_list.html')


def View_Employee(request):
    return render(request, 'view_Employee.html')
# End Tomtam

# Start Bank


def Orderhis(request):
    order = Order.objects.all()
    return render(request, 'Orderhis.html', {'order': order})


def Report(request):
    # Query Data From Model
    report = Owners.objects.all()
    return render(request, 'Report.html', {'report': report})


def Tipsd(request):
    tips = Tip.objects.all()
    return render(request, 'Tipsd.html', {'tips': tips})
# Stop Bank

# start Kris


def AddMenu(request):
    return render(request, 'AddMenu.html')


def AddTable(request):
    A=request.POST.get('NumberofTable',False)
    B=request.POST.get('QuantityofTable',False)

    print(request)
    print(A)
    print(B)
    if(A!= False and B!= False):
        Tables=Table.objects.create(number = A,Quantity = B,time=' ',Order_id =' ')
        Tables.save()
        
    data=Table.objects.all()
    return render(request,'AddTable.html')

def BillSetting(request):
    A=request.POST.get('StoreName',False)
    B=request.POST.get('VAT',False)
    C=request.POST.get('SC',False)
    D=request.POST.get('EndTextBill',False)
    print(request)
    print(A)
    print(B)
    print(C)
    print(D)
    if(A!= False and B!= False and C!= False and D!= False):
        BillSet=Bill_Setting.objects.create(StoreName = A,VAT = B,SC = C,EndTextBill = D)
        BillSet.save()
        A = False
        B = False
        C = False
        D = False
    data=Bill_Setting.objects.all()
    return render(request, 'BillSetting.html')


def BuyFoodBackHome(request):
    return render(request, 'BuyFoodBackHome.html')


def BuyMoreFood(request):
    return render(request, 'BuyMoreFood.html')


def ChangeFood(request):
    return render(request, 'ChangeFood.html')


def DeleteTable(request):
    Deletes = Table.objects.all()
    return render(request, 'DeleteTable.html',{'deletes': Deletes})
def DelTable(request,id):
    deletetable = Table.objects.get(id=id)
    deletetable.delete()
    Deletes = Table.objects.all()
    return render(request, 'DeleteTable.html',{'deletes': Deletes})


def listCustomer(request):
    data = Orderlish.objects.all()
    return render(request, 'listCustomer.html', {'posts': data})

# End Kris
