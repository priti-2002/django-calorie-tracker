from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Food, Consume

# Create your views here.

def index(request):
    if request.method == "POST":
        # Note: This part will still fail if a guest tries to post, 
        # so we check if user is authenticated before saving.
        if request.user.is_authenticated:
            food_consumed = request.POST['food_consumed']
            consume_obj = Food.objects.get(name=food_consumed)
            user = request.user
            consume = Consume(user=user, food_consumed=consume_obj)
            consume.save()
        else:
            # Redirect to login if a guest tries to add food
            return redirect('/admin/login/') 

    foods = Food.objects.all()

    # FIX: Check if user is logged in before filtering
    if request.user.is_authenticated:
        consumed_food = Consume.objects.filter(user=request.user)
    else:
        consumed_food = Consume.objects.none() # Show an empty list for guests

    return render(request, 'myapp/index.html', {'foods': foods, 'consumed_food': consumed_food})


def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/')
    return render(request, 'myapp/delete.html')
