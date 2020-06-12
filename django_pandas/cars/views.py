from django.shortcuts import render
from .models import  Cars
import pandas as pd 
# Create your views here.

def main_view(request):

    template = 'cars/main.html'
    qs = Cars.objects.all().values()
    data = pd.DataFrame(qs)
    '''
    #qs2 = Cars.objects.all().values_list()

    print(qs)

    print('################')
    print(qs2)
   
    data2 = pd.DataFrame(qs2)
    print(data)
    print(data2)
    #print(data.shape)
    '''
    context = {
        'df':data.to_html(),
        'describe':data.describe().to_html(),
            }
    return render(request,template,context)