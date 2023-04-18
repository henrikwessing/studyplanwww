from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Flows
import pandas as pd
import pickle

# Create your views here.
def index(request):
    titles = list(Flows.objects.values_list('id','name'))
    context = {"navbar" : titles, "title" : "Anbefalede studieforløb"}
    return render(request,"basetemplate.html",context)
    

def flow(request,flow_id):
    flw = get_object_or_404(Flows,pk=flow_id).flw
    data = pickle.loads(flw)
    titles = list(Flows.objects.values_list('id','name'))
    title = [t[1] for t in titles if t[0] == flow_id][0] 
    context = {"data" : data, "navbar" : titles, "title" :title}
    return render(request,"flowtemplate.html",context)

        
