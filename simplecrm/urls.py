from django.contrib import admin
from django.urls import path

from accounts import views as aviews 
from leads import views as lviews
from opportunities import views as oviews
from contacts import views as cviews

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'accounts/', aviews.AccountListAPIView.as_view(), name='account-list'),
    path(r'leads/', lviews.LeadListAPIView.as_view(), name='lead-list'),
    path(r'opportunities/', oviews.OpportunityListAPIView.as_view(), name='opportunity-list'),
    path(r'contacts/', cviews.ContactListAPIView.as_view(), name='contact-list')
]
