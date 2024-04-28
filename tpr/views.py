from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,redirect
from django.template import loader
from tpr.models import Tpr
from django.shortcuts import get_object_or_404
from urllib.parse import quote_plus
from django.views.decorators.http import require_POST
from django.http import HttpResponseBadRequest





def start(request):
  template = loader.get_template('index.html')
  return HttpResponse(template.render())


def tpr(request):
  template = loader.get_template('TPR_View.html')
  return HttpResponse(template.render())

def prince(request):
  template = loader.get_template('prince.html')
  return HttpResponse(template.render())

def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())

def emp_login(request):
  template = loader.get_template('emp_login.html')
  return HttpResponse(template.render())

def TPR(request):

    if request.method == "POST":
        TPR_NO = request.POST.get('TPR_NO')
        segment = request.POST.get('segment')
        customer = request.POST.get('customer')
        pdf_file = request.FILES.get('pdf_file')
        TPR = Tpr(TPR_NO = TPR_NO, segment= segment, customer=customer, pdf_file=pdf_file)
        TPR.save()
    return render(request, 'TPR.html')




def display_form_data(request):
    form_data = Tpr.objects.filter(is_deleted=False)  # Filtering out only non-deleted data
    
    return render(request, 'TPR_View.html', {'form_data': form_data})


def display_deleted_entries(request):
    deleted_entries = Tpr.objects.filter(is_deleted=True)
    return render(request, 'deleted_entries.html', {'deleted_entries': deleted_entries})


def admin_view(request):
    form_data = Tpr.objects.filter(is_deleted=False)
    return render(request, 'admin_tpr_view.html', {'form_data': form_data})

@require_POST
def add_deleted_to_tpr(request):
    deleted_entry_ids = request.POST.getlist('selected_deleted[]')

    for entry_id in deleted_entry_ids:
        try:
            entry = Tpr.objects.get(pk=entry_id)
            entry.is_deleted = False  # Mark as not deleted
            entry.save()
        except Tpr.DoesNotExist:
            return HttpResponseBadRequest("Tpr object does not exist.")

    return redirect('admin_view')

@require_POST
def delete_tpr(request):
    tpr_id = request.POST.get('id')  # Assuming 'id' is the primary key of Tpr model
    
    if tpr_id:
        try:
            tpr_object = Tpr.objects.get(pk=tpr_id)
            tpr_object.is_deleted = True  # Marking as deleted
            tpr_object.save()
        except Tpr.DoesNotExist:
            return HttpResponseBadRequest("Tpr object does not exist.")
    
    return redirect('admin_view')


def SPC(request):
  template = loader.get_template('SPC.html')
  return HttpResponse(template.render())

def slitting(request):
  template = loader.get_template('slitting.html')
  return HttpResponse(template.render())

def shearing(request):
  template = loader.get_template('shearing.html')
  return HttpResponse(template.render())
   
def Galva(request):
  template = loader.get_template('Galva.html')
  return HttpResponse(template.render())

def CTL(request):
  template = loader.get_template('CTL.html')
  return HttpResponse(template.render())

def CRCA(request):
  template = loader.get_template('CRCA.html')
  return HttpResponse(template.render())
