from skill_matcher import compare_skills

resume_skills = ["Python", "Java", "ML", "SQL"]
job_skills = ["Python", "SQL", "Machine Learning", "Deep Learning"]

result = compare_skills(resume_skills, job_skills)
print(result)