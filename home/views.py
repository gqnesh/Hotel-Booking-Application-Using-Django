from django.shortcuts import render
from . import models
from django.http import JsonResponse

# Create your views here.

def home(request):
    facilities_data = models.Category.objects.all()
    hotels_data = models.Hotels.objects.all()
    
    context = {'facilities': facilities_data, 'hotels_data': hotels_data}
    return render(request, 'home/home.html', context)

def hotels_api(request):
    hotel_obj = models.Hotels.objects.all()

    if request.GET.get('price'):
        
        hotel_obj = hotel_obj.filter(Price__lte = int(request.GET.get('price')))

    facilities = request.GET.get('facilities')
    if facilities:
        facilities = facilities.split(',')

        ct = []

        for e in facilities:
            try:
                ct.append(int(e))
            except:
                pass

        hotel_obj = hotel_obj.filter(Hotelcategory__in = ct).distinct()

    api_payload = []
    for obj in hotel_obj:
        result = {}
        result['hotel_name'] = obj.HotelName
        result['hotel_address'] = obj.HotelAddress
        result['hotel_image'] = str(obj.HotelImages)
        result['price'] = obj.Price
    
        api_payload.append(result)

    # print(api_payload)

    return JsonResponse(api_payload, safe=False)