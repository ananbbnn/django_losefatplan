from django.shortcuts import render, redirect
from .models import Plan
from django.contrib.auth.decorators import login_required
# Create your views here.

def create_plan(request):
    """
    View to create a new plan.
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        visibility = request.POST.get('visibility') == 'public'
        height = request.POST.get('height')
        weight = request.POST.get('weight')
        start_date = request.POST.get('startDate')
        end_date = request.POST.get('endDate')
        month_goal = request.POST.get('monthGoal')
        final_goal = request.POST.get('finalGoal')
        description = request.POST.get('description')

        Plan.objects.create(
            name=name,
            private=not visibility,
            height=float(height),
            weight=float(weight),
            start_time=start_date,
            end_time=end_date,
            month_target=float(month_goal),
            final_target=float(final_goal),
            description=description,
            user=request.user
        )
    
        return redirect('create_plan')
        # Handle form submission and plan creation logic here
    else:
        # Render the plan creation form
        return render(request, 'plan/create_plan.html')
    


@login_required
def view_plan(request):
    """
    View to display a specific plan.
    """
    user = request.user
    plans = Plan.objects.filter(user=user).order_by('-start_time')
    if not plans:
        return redirect('create_plan')

    return render(request, 'plan/view_plan.html', {'plans': plans})