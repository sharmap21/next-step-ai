from django.shortcuts import render,redirect
from .utils import match_career
from django.template.loader import render_to_string
from .forms import CareerForm
from .utils import match_career

# Create your views here.

def home_page(request):
    return render(request,'career/main.html')


def recommend_career(request):
    recommendations = None

    if request.method == "POST":
        skills = request.POST.get("skills", "").split(",")  # Get skills from input
        education = request.POST.get("education", "")
        field_of_study = request.POST.get("field_of_study", "")

        # Get recommendations based on user input
        recommendations = match_career(skills, education, field_of_study)

        # Redirect to result page with recommendations
        return render(request, "career/result.html", {"recommendations": recommendations})

    return render(request, "career/career_recommendation.html")

