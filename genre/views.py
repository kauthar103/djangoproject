from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Collection,Piece   #we import these models bcos dis is where our DB is,
from django.views import generic
from .forms import UserForms
from django.contrib.auth import authenticate,login 
from django.views.generic import View

# Create your views here.
# We can use generic classes, it's easier, we import generic classes above, we define the class index, it takes a list view, bcos we 're
# listing out objs., we take the template path, we 've a func. to return our query set, return Collection..

class index(generic.ListView):
    template_name = 'genre/genretemplate.html'
    
    def get_queryset(self):
        return Collection.objects.all()

#we can't concatenate int + str , so we convert 2 str(genre_id) HttpResponse("<h1>The genre id is: "+ str(genre_id)+"</h1>")    

# In this 2nd page we just 've 1 obj., we want to give out the details of 1 obj., we created a class, DetailsView= render a detail view of 
# an obj, the func. of DetailView is to display, D details of an Obj., next, we define a model,model is Collection bcos we 're receiving
# the Pk from Collection, each of this obj is a part of the Collection, the obj. would not exist if the related of that obj. doesn't 
# exist, template_name =path, we receive the PrimaryK from Collection since we use DetailView.,
# template_name=path

class details(generic.DetailView):
    model =Collection
    template_name = "genre/detailstemplate.html"


class UserFormView(View):
    form_class=UserForms
    template_name='genre/formtemplate.html'
    
    def get(self, request):
        form=self.form_class(None)
        return render(request, self.template_name, {'form':form })
    
    def post(self, request):
        form=self.form_class(request.POST)
        
        if form.is_valid():
            user=form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user.set_password(password)
            user.save()
            
            newuser=authenticate(username=username,password=password)
            
            if newuser is not None:
                if newuser.is_active:
                    login(request,newuser)
                    return redirect("/genre")
                    
        return render(request, self.template_name, {'form':form})
     