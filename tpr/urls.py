from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.start, name='start'),
    path('emp_login/',views.emp_login, name='emp_login'),
    path('tpr/', views.display_form_data, name='tpr'),
    path('prince/', views.prince, name='prince'),                                                                                           

    path('login/', views.login, name='login'),
    path('login/TPR/', views.TPR, name='TPR'),
    path('login/TPR/tpr', views.admin_view, name='admin_view'),
    path('login/TPR/tpr/delete/', views.delete_tpr, name='delete_tpr'),
    path('login/TPR/tpr/deleted/', views.display_deleted_entries, name='deleted_tpr'),
    path('add_deleted_to_tpr/', views.add_deleted_to_tpr, name='add_deleted_to_tpr'),

    path('CTL/', views.CTL, name='CTL'),
    path('CRCA/', views.CRCA, name='CRCA'),
    path('shearing/', views.shearing, name='shearing'),
    path('SPC/', views.SPC, name='SPC'),
    path('slitting/', views.slitting, name='slitting'),
    path('Galva/', views.Galva, name='Galva'),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
