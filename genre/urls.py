#in 2nd path, we used <pk>, to change from defined func. to classes we use .as_view(), it's a main entry point for req- response 
from django.urls import path
from . import views

urlpatterns = [
    #/genres/   this is the 1st path, wen the user opens the 1st page
    
    path('', views.index.as_view(), name="index"),
    
    
    #genre/1    , this is the 2nd path, 1 indicate the id of the collection chosen;
    
    path('<pk>', views.details.as_view(),name="details"),    # the xprsion is an int number since the 1st path genre/ is already matched,
                                        #we store it in genre_id, comma, the response views.de..., the name = details, nxt we de5n details
                                        # which will give response the url in views page
                        
    # for our registation page, we created a url, it will be genre/register, it will call a views func. called UswrFormView 
    path('register/', views.UserFormView.as_view(),name="UserFormView")
]                                       

