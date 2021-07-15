from django.shortcuts import render
from django.template import RequestContext
from django.conf import settings
from django.contrib import messages
from sqlalchemy import create_engine
import numpy as np
import pandas as pd
import os


def uploadDatabase(request):
    # declaring template
    template_view = "upload.html"
    result = False

    # database_url = 'postgresql://postgres:postgres@172.17.0.1:5432/postgres'
    
    if request.method == 'POST':
        csv_file = request.FILES['file']
        
        # let's check if it is a csv file
        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'THIS IS NOT A CSV FILE')

        user = os.environ.get("SQL_USER")
        password = os.environ.get("SQL_PASSWORD")
        database_name = os.environ.get("SQL_DATABASE")

        database_url = 'postgresql://{user}:{password}@172.17.0.1:5432/{database_name}'.format(
            user=user,
            password=password,
            database_name=database_name,
        )

        engine = create_engine(database_url, echo=False)

        data_frame = pd.read_csv(csv_file)   
        
        data_frame.to_sql(request.POST['table_name'], con=engine, schema=request.POST['schema_name'], if_exists='replace')

        result = True

    return render(request, template_view, {'result':result})