from django.shortcuts import render
from first_app.models import Topic,AceessRecord,Webpage

# Create your views here.

def index(request):
    web_pages_list=AceessRecord.objects.order_by('date')

    date_dict={'access_records':web_pages_list}

    return render(request,"first_app/index.html",context=date_dict)
