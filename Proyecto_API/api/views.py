from django.views.generic import View
from .models import Company
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.

class CompanyView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if(id>0):
            companies = list(Company.objects.filter(id=id).values())
            if len(companies)>0:
                company = companies[0]
                datos={
                    'message':"Success",
                    'companies':company
                }
            else:
                datos = {'message':"Company not found"}

            return JsonResponse(datos, safe=False)
        else:
            companies = list(Company.objects.values())
            if len(companies)>0:
                datos={
                    'message':"Success",
                    'companies':companies
                }
            
            else:
                datos={
                    'message':"Companies not found..."
                }

            return JsonResponse(datos, safe=False)

    def post(self, request):
        #print(request.body)
        jd = json.loads(request.body) #convierte de json a diccionario de python
        Company.objects.create(name=jd['name'], website=jd['website'],fundation = jd['fundation'])
        datos = {'message':"Company created successfully"}
        return JsonResponse(datos, safe=False)

    def put(self, request, id):
        jd = json.loads(request.body) #convierte de json a diccionario de python
        companies = list(Company.objects.filter(id=id).values())
        if len(companies)>0:
            company = Company.objects.get(id=id)
            company.name = jd['name']
            company.website = jd['website']
            company.fundation = jd['fundation']
            company.save()
            datos = {'message':"Company updated successfully"}

        else:
            datos = {'message':"Company not found"}

        return JsonResponse(datos, safe=False)
             
    def delete(self, request, id):
        companies = list(Company.objects.filter(id=id).values())
        if len(companies)>0:
            Company.objects.filter(id=id).delete()
            datos = {'message':"Company deleted successfully"}
        else:
            datos = {'message':"Company not found"}
        return JsonResponse(datos, safe=False)