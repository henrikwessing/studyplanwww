from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Flows
import pandas as pd
import pickle

# Create your views here.
def index(request, year):
    titles = list(Flows.objects.filter(year=year).values('code','name'))
    context = {"navbar" : titles, "title" : "Anbefalede studieforløb"}
    print(titles)
    return render(request,"basetemplate.html",context)

def replaceVF(df):
    df.loc[df['Gruppe']=='VF','Gruppe']='VF_old'
    return df

def flow(request,flow_id, year):
    flw = get_object_or_404(Flows,code=flow_id,year=year).flw
    data = pickle.loads(flw)
    if year == 2022:
        data = replaceVF(data)    
    titles = list(Flows.objects.filter(year=year).values('code','name'))
    title = [t['name'] for t in titles if t['code'] == flow_id][0] 
    context = {"data" : data, "navbar" : titles, "title" :title, "year" : year}
    return render(request,"flowtemplate.html",context)
