from django.shortcuts import render,redirect
from django.views import View
from .forms import RecipeForm
from .langchain import askJarvisChef
# Create your views here.

class Home(View):
    def get(self,request):
        ai_recipe = request.session.get('ai_recipe', '')
        form = RecipeForm()
        data = {
            'form':form,
            'ai_recipe':ai_recipe,
        }
        return render(request,'home.html',data)
    

    def post(self,request):
        form =RecipeForm(request.POST)
        if form.is_valid():
            recipe_message = form.cleaned_data['recipe_message']
            ai_res_recipe = askJarvisChef(recipe_message)
            request.session['ai_recipe'] = ai_res_recipe
        form = RecipeForm()
        return redirect('home')