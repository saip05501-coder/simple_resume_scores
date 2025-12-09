from resume_parser import extract_resume_text
from keyword_extractor import extract_skills
from jd_loader import get_jd_skills
from skill_matcher import compare_skills

def evaluate_resume(resume_path, role):
    # 1. Extract text from resume
    text = extract_resume_text(resume_path)

    # 2. Extract skills from resume
    resume_skills = extract_skills(text)

    # 3. Load job description skills
    jd_skills = get_jd_skills(role)

    # 4. Compare (match / missing / score)
    result = compare_skills(resume_skills, jd_skills)

    return {
        "resume_skills": resume_skills,
        "jd_skills": jd_skills,
        "matched": result["matched_skills"],
        "missing": result["missing_skills"],
        "score": result["resume_score"]
    }