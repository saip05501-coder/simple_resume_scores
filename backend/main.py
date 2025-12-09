from resume_parser import extract_resume_text
from keyword_extractor import extract_skills
from jd_loader import load_all_jds
from jd_loader import load_all_jds
from skill_matcher import calculate_resume_score

# Path to resume PDF
resume_path = "samples/resumes/resume1.pdf"

# Step 1: Extract resume text
resume_text = extract_resume_text(resume_path)

# Step 2: Extract skills from resume
resume_skills = extract_skills(resume_text)
print("Resume Skills Extracted:", resume_skills)

# Step 3: Load all JD files
jd_dict = load_all_jds("samples/jd")

# Step 4: Compare resume with all roles and store results
results = []
for role, jd_skills in jd_dict.items():
    score, matched, missing = calculate_resume_score(resume_skills, jd_skills)
    results.append({
        "role": role,
        "score": score,
        "matched": matched,
        "missing": missing
    })

# Step 5: Sort roles by score (highest first)
results = sorted(results, key=lambda x: x["score"], reverse=True)

# Step 6: Display ranked roles
print("\n=== Resume Evaluation Results ===")
for r in results:
    print(f"\nRole: {r['role']}")
    print(f"Score: {r['score']:.2f}%")
    print(f"Matched Skills: {r['matched']}")
    print(f"Missing Skills: {r['missing']}")