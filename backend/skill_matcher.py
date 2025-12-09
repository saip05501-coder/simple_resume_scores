from fuzzywuzzy import fuzz

def calculate_resume_score(resume_skills, jd_skills):
    """
    Compare resume skills with JD skills and return:
    - score (percentage)
    - matched skills
    - missing skills
    """
    matched_skills = []
    for skill in jd_skills:
        for r_skill in resume_skills:
            if fuzz.ratio(skill.lower(), r_skill.lower()) > 80:  # 80% similarity
                matched_skills.append(skill)
                break

    score = len(matched_skills) / len(jd_skills) * 100 if jd_skills else 0
    missing_skills = [skill for skill in jd_skills if skill not in matched_skills]

    return score, matched_skills, missing_skills