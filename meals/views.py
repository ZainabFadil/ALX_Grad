from django.shortcuts import render, get_object_or_404, redirect
from .models import Section, Meal
from .forms import MealForm

def meal_list(request):
    meals = Meal.objects.all()
    return render(request, 'meals/meal_list.html', {'meals': meals})

def meal_detail(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    return render(request, 'meals/meal_detail.html', {'meal': meal})

def meal_create(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('meal_list')
    else:
        form = MealForm()
    return render(request, 'meals/meal_form.html', {'form': form})

def meal_update(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    if request.method == 'POST':
        form = MealForm(request.POST, instance=meal)
        if form.is_valid():
            form.save()
            return redirect('meal_list')
    else:
        form = MealForm(instance=meal)
    return render(request, 'meals/meal_form.html', {'form': form})

def meal_delete(request, pk):
    meal = get_object_or_404(Meal, pk=pk)
    if request.method == 'POST':
        meal.delete()
        return redirect('meal_list')
    return render(request, 'meals/meal_confirm_delete.html', {'meal': meal})