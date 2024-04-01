from django.http import HttpResponse
from django.shortcuts import render,HttpResponse,redirect
from django.template import loader
from tpr.models import Tpr
from django.shortcuts import get_object_or_404
from urllib.parse import quote_plus
from django.views.decorators.http import require_POST




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
    form_data = Tpr.objects.all()
    for a in form_data:
       print(form_data)
    return render(request, 'TPR_View.html', {'form_data': form_data})




def admin_view(request):
    form_data = Tpr.objects.all()
    return render(request, 'admin_tpr_view.html', {'form_data': form_data})

@require_POST
def delete_tpr(request):
    tpr_id = request.POST.get('id')  # Assuming 'id' is the primary key of Tpr model
    
    if tpr_id:
        try:
            tpr_object = Tpr.objects.get(pk=tpr_id)
            tpr_object.delete()
        except Tpr.DoesNotExist:
            pass 
    
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
