from django.shortcuts import render
from .models import Destination,Payments
from paytm import Checksum
from django.views.decorators.csrf import csrf_exempt
import random
import string

def randomStringDigits(stringLength=10):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))

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

    MERCHANT_KEY = 'bQfzzkKzeCbR7jOl'
    param_dict = {
        'MID': 'amitgo59443067266036',
        'ORDER_ID': randomStringDigits(), # order id 
        'TXN_AMOUNT': str(price*quantity), # amount demanded for.
        'CUST_ID': "chiragrocks998@gmail.com",
        'INDUSTRY_TYPE_ID': 'Retail',
        'WEBSITE': 'STAGING', # for demo purpose only.
        'CHANNEL_ID': 'WEB',
        'CALLBACK_URL':'http://127.0.0.1:8000/notification/' # on this url paytm will send you the status of request
    };param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict,MERCHANT_KEY);
    
    return render(request,'pay/makepay.html',{'data':param_dict})

    
    #return render(request,'payment.html',{'payment_details':payments})

def ticket(request):
    return render(request,'contact.html')

@csrf_exempt
def notificationfrompaytm(request):
    data = dict()
    #id = request.session['id']
    #print(id)
    for k,v in request.POST.items():
        data.setdefault(k,v)
    return render(request,'pay/paymsg.html',data)
