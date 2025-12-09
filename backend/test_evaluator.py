from resume_evaluator import evaluate_resume

path = "samples/resumes/resume1.pdf"
role = "ML Engineer"

result = evaluate_resume(path, role)
print(result)