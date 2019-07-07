from django.shortcuts import render
from .models import Destination,Payments
# Create your views here.
def index(request):
    dests = Destination.objects.all()
    return render(request,'index.html',{'dests':dests})

def payment(request):
    destination=request.POST.get('dest')
    uname=request.POST.get('username')
    quantity=int(request.POST.get('qtyTicket'))
    price=int(request.POST.get('priceTicket'))

    if request.method=='POST':
        payments=Payments()
        payments.DestinationName=destination
        payments.Name=uname
        payments.Quantity=quantity
        payments.Price=quantity*price
        payments.save()

    
    return render(request,'payment.html',{'payment_details':payments})

def ticket(request):
    return render(request,'contact.html')
