import json
import os
from django.conf import settings

def load_career_data():
    data_path = os.path.join(settings.BASE_DIR, "data/career_data.json")
    with open(data_path, "r") as file:
        return json.load(file)

def match_career(skills, education, field_of_study):
    career_data = load_career_data()
    recommendations = []

    # Convert inputs to lowercase for case-insensitive matching
    skills = {skill.lower().strip() for skill in skills if skill.strip()}
    education = education.lower().strip()
    field_of_study = field_of_study.lower().strip()

    for career in career_data:
        career_skills = {s.lower() for s in career["skills"]}
        career_education = {e.lower() for e in career["education"]}
        career_title = career["career"].lower()

        # Count matching skills
        matching_skills = skills.intersection(career_skills)
        skill_match_count = len(matching_skills)

        # Ensure at least 50% of the user's skills match
        if skill_match_count < max(1, len(skills) // 2):
            continue  

        score = skill_match_count * 3  # Higher weight for skills

        # Ensure education is an exact match
        if education in career_education:
            score += 4  # Increased weight for education relevance

        # Ensure field of study is highly relevant
        if field_of_study in career_title or any(field_of_study in s for s in career_skills):
            score += 3  

        # Only include careers with strong relevance (score must be 6+)
        if score >= 6:
            recommendations.append((career, score))

    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations
