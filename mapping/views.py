from django.shortcuts import render
# from .models import Mapping
from records.models import Staging
from django.shortcuts import render, redirect
from records.forms import Staging_form
from django.http import HttpResponse
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import os
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.shortcuts import get_object_or_404
import json
import datetime
from pprint import pprint
from django.forms.models import model_to_dict

# Create your views here.
CSV_STORAGE = os.path.join(os.getcwd(),  'static', 'csv')


@csrf_exempt
def import_data(request):
    if request.method == 'POST':
        new_students = request.FILES['myfile']
        if new_students.content_type == 'text/csv':
            df = pd.read_csv(new_students)
        else:
            df = pd.read_excel(new_students)  # make sure that there' no header
        path_name = os.path.join( 'static', 'tempcsv', 'temp.csv')
        df.to_csv(path_name, index=False)
        return redirect('/fieldmatching?df=' + path_name)
    else:
        return render(request, 'import_data.html')


def fieldmatching(request):
    if request.method == 'POST':
        path_name = request.POST['path_name']
        df = pd.read_csv(path_name)
        t = df.isnull()
        if t is True:
            s = df.isnumeric()
            if s is True:
                df = df.fillna("0")
            # else:
            # df = df.fillna("None")

        df = df.fillna("0")
        names = list(df.columns)

        if request.POST.get('checkBox') == None:
            matched = {key: request.POST.get(key, False) for key in names}
            df.rename(columns=matched, inplace=True)
        # df.drop('id', axis=1, inplace=True)
        df.set_index("id", drop=True, inplace=True)

        dictionary = df.to_dict(orient="index")
        for index, object in dictionary.items():
            m = Staging()
            for k, v in object.items():
                setattr(m, k, v)
            setattr(m, 'id', index)
            m.save()
        return render(request, 'import_data.html')
    else:
        path_name = request.GET.get('df')
        df = pd.read_csv(path_name)
        t = df.isnull()
        if t is True:
            s = df.isnumeric()
            if s is True:
                df = df.fillna("0")
            else:
                df = df.fillna("None")
        names = list(df.columns)
        fields = [field.name for field in Staging._meta.get_fields()]
        return render(request, 'fieldmatching.html',
                      {'fields': fields, 'path_name': path_name, 'names': names})


def disp(request):
    data = pd.read_excel(r"H:\Candidate Report.xlsx")
    df = []
    db = []
    context = {
        'df': list(data.columns),
        'db': list(field.name for field in Staging._meta.get_fields())
    }

    return render(request, 'mapping.html', context)