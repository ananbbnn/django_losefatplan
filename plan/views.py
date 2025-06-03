from django.shortcuts import render

# Create your views here.

def create_plan(request):
    """
    View to create a new plan.
    """
    if request.method == 'POST':
        # Handle form submission and plan creation logic here
        pass
    else:
        # Render the plan creation form
        return render(request, 'plan/create_plan.html')