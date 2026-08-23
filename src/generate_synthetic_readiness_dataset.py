import pandas as pd
import random

# Define synthetic skill pools
skills_pool = ["Python", "SQL", "Tableau", "Machine Learning", "Java", "Spring Boot",
               "Docker", "AWS", "Excel", "Power BI", "Communication", "Statistics"]

labels = ["Highly Ready", "Moderately Ready", "Needs Improvement", "Not Ready Yet"]

def generate_student_profile():
    # Randomly select skills
    resume_skills = random.sample(skills_pool, random.randint(3, 6))
    jd_skills = random.sample(skills_pool, random.randint(4, 7))
    critical_skills = random.sample(jd_skills, random.randint(1, 2))

    matched = set(resume_skills) & set(jd_skills)
    missing = set(jd_skills) - set(resume_skills)
    critical_missing = set(critical_skills) - set(resume_skills)

    # Features
    skill_match_percentage = len(matched)/len(jd_skills)*100
    critical_skill_match_percentage = (len(critical_skills)-len(critical_missing))/len(critical_skills)*100
    missing_skills_count = len(missing)
    critical_missing_skills_count = len(critical_missing)

    # Assign synthetic readiness label
    if skill_match_percentage > 75 and critical_skill_match_percentage == 100:
        label = "Highly Ready"
    elif skill_match_percentage > 50:
        label = "Moderately Ready"
    elif skill_match_percentage > 30:
        label = "Needs Improvement"
    else:
        label = "Not Ready Yet"

    return {
        "resume_skills": resume_skills,
        "jd_skills": jd_skills,
        "critical_skills": critical_skills,
        "skill_match_percentage": skill_match_percentage,
        "critical_skill_match_percentage": critical_skill_match_percentage,
        "missing_skills_count": missing_skills_count,
        "critical_missing_skills_count": critical_missing_skills_count,
        "readiness_label": label
    }

# Generate synthetic dataset
synthetic_data = [generate_student_profile() for _ in range(100)]

# Convert to DataFrame
df = pd.DataFrame(synthetic_data)

# Save to CSV
df.to_csv("../data/processed/features.csv", index=False)

print("Synthetic readiness dataset generated successfully!")
print(df.head())