from ninja import NinjaAPI, Redoc, Query
from services.models import Service, Contact, Address, Provider
from django.contrib.auth.models import User
from .models import ServiceInputSchema, ServiceOutputSchema, ProviderOutputSchema, MessageSchema
from typing import List


api =  NinjaAPI(docs=Redoc())


@api.get("/services/", response={200: List[ServiceOutputSchema]})
def get_services(request):
  
     
     services = Service.objects.all().order_by("thru_date")
     results = []

     for post in services:
            result = {
                 "id": post.id,
                 "name": post.name,
                 "description": post.description,
                 "price": post.price,
                 "from_date": post.from_date.strftime("%d/%m/%Y"),
                 "thru_date": post.thru_date.strftime("%d/%m/%Y"),
                 "provider": {
                     "id": post.provider.id,
                     "fantasy_name": post.provider.fantasy_name,
                     "text_name": post.provider.text_name,
                     "taxt_id": post.provider.tax_id,
            
                 },
            }
            for service in post.services.all():
                service = {
                    "price": service.price,
                    "thru_date": service.thru_date,
                }
                result["service"].append(service)
                results.append(result)

            return results


@api.get("/service/{service_id}/", response={200: ServiceOutputSchema, 404:MessageSchema})
def get_service(request, service_id: int):
   
    try:
        post = Service.objects.get(id=id)
    except Exception:
        return 404, {'message': 'Service not found'}
    
    result = {
        "id": post.id,
        "name": post.name,
        "description": post.description,
        "price": post.price,
        "from_date": post.from_date.strftime("%d/%m/%Y"),
        "thru_date": post.thru_date.strftime("%d/%m/%Y"),
        "provider": {
            "id": post.provider.id,
            "fantasy_name": post.provider.fantasy_name,
            "text_name": post.provider.text_name,
             "taxt_id": post.provider.tax_id,
        },
    }
    for service in post.services.all():
        service = {
         "price": service.price,
         "thru_date": service.thru_date,
        }
        result["service"].append(service)
        result.append(result)

    return result


@api.post("/service/", response={201: ServiceOutputSchema, 404:MessageSchema})
def create_service(request, service: ServiceInputSchema):
    
    try:
        provider = User.objects.get(id= service.provider)
    except Exception:
        return 404, {'message': 'Provider not found'}
    provider.append(provider)
    post = {
        "price": service.price,
        "thru_date": service.thru_date,
    }
    post = Service.objects.create(**post)
    post.save()
    
    for service in service:
        post.service.add(provider)
        post.save()
    return { 'message': 'Service has been created'}


@api.delete("/service/{service_id}/", response={204: None})
def delete_service(request, service_id: int):
    
    try:
        post = Service.objects.get(id=id)
    except Exception:
        return 404, {'message': 'Service not found'}
    post.delete()

    return { 'message': 'Service has been deleted'}