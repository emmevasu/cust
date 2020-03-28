import json
from django.shortcuts import render
from customerapp.models import Customer
from django.http import HttpResponse

# Create your views here.
def input(request):
    return render(request,'input.html')
def customer_data(request):
    customer_name1=request.POST['t1']
    customer_mobile1=int(request.POST['t2'])
    customer_age1=float(request.POST['t3'])
    customer_city1=request.POST['t4']
    f=Customer(customer_name=customer_name1,customer_mobile_no=customer_mobile1,customer_age=customer_age1,customer_city=customer_city1)
    f.save()
    main_dict = {}
    cust_data = Customer.objects.filter(customer_mobile_no=customer_mobile1)
    count = 0
    for c_d in cust_data:
        count += 1
        data_dict = {}
        data_dict['customer_name'] = c_d.customer_name
        data_dict['customer_mobile_no'] = c_d.customer_mobile_no
        data_dict['customer_age'] = c_d.customer_age
        data_dict['customer_city'] = c_d.customer_city
        row = 'Rec' + str(count)
        main_dict[row] = data_dict
        # main_dict.update(data_dict)
    return HttpResponse(json.dumps(main_dict))


