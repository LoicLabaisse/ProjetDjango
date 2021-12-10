from django.http import response
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls.resolvers import URLPattern

from django.urls import reverse
import requests
import json

from .models import Persona

# Create your views here.
def persona_list(request):
    context = {
        'persona_list': Persona.objects.all()
    }
    return render(request,"persona/persona_list.html", context)
    
    # for personne in Persona.objects.all():
    #     return HttpResponse("Index")
    
    #return HttpResponse("Get all person ")

def persona_details(request,id):
    persona = Persona.objects.get(id=id)
    
    context = {
        'persona_object':persona
    }
    return render(request,'persona/persona_details.html', context)
    
    

def persona_generate(request):
    reponse = requests.get("https://randomuser.me/api/?")
    JsonStr = reponse.text
    jsonObject = json.loads(JsonStr)
    API_Info= jsonObject["results"][0]
    
    newUser = Persona()
    
    newUser.first_name = API_Info["name"]["first"]
    newUser.last_name = API_Info["name"]["last"]
    
    #============ LOCATION ============
    location = API_Info["location"]
    
    newUser.address_street = location["street"]['name']
    newUser.address_number = location["street"]["number"]
    newUser.city = location["city"]
    newUser.country = location['country']
    newUser.postcode = location['postcode']
    
    #=========== User Account =========
    newUser.email= API_Info["email"]
    newUser.username = API_Info["login"]["username"]
    newUser.password = API_Info["login"]["password"]
    newUser.age= API_Info["dob"]["age"]
    newUser.picture= API_Info["picture"]["large"]
    newUser.save()
  
    
  
    #redirect(f"url_persona_details/{newUser.id}")
    #return render(request, "persona/persona_details.html")
    # current_url = resolve(request.path_info).url_name

    # #return HttpResponseRedirect(reverse(viewname="url_persona_details"), args=(newUser.id,))
    
    # context = {
    #     'route':"{%url 'url_persona_details' personne.id %}"
    # }
    # render(request, '', context)
    #return HttpResponseRedirect(reverse("url_persona_list/"))
    #return HttpResponse(reverse("url_persona_details/"))
    
    return HttpResponseRedirect(f"/persona_details/{newUser.id}")
    