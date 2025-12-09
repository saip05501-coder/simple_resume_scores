from resume_parser import extract_resume_text
from keyword_extractor import extract_skills

resume_path = "samples/resumes/resume1.pdf"

text = extract_resume_text(resume_path)
skills = extract_skills(text)

print("Extracted Skills:")
print(skills)