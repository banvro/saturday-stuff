from django.urls import path
from bloging import views

urlpatterns = [
   path("", views.homepage, name = "home"),
   path("about", views.aboutuspage, name = "about"),
   path("services", views.servicesuspage, name = "services"),
   path("contact", views.contactuspage, name = "contact"), 
   path("show", views.showingdata, name = "show"), 

   path("savinng-data", views.savingdata, name = "datasave"),

   path("delete-record/<int:card_id>", views.deletethis, name = "delete"),

   path("updatedata/<int:myid>", views.updatedata, name = "update"),

   path("updatedatanow/<int:myid>", views.updatedatanow, name = "updatenow"),
]