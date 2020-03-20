from django.urls import path, include
from . import views


urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.first,name= 'first'),
    path('delete/<idno>',views.delete,name= 'delete'),
    path('edit/<idno>',views.edit,name= 'edit'),


]