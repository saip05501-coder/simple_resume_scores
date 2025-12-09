from flask import Flask, request, jsonify
from flask_cors import CORS
import os

from resume_parser import extract_resume_text
from keyword_extractor import extract_skills
from jd_loader import load_all_jds
from skill_matcher import calculate_resume_score

app = Flask(__name__)
CORS(app)  # allow frontend to access backend

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load all JDs at startup
print("Loading all JDs...")
JD_DATA = load_all_jds("samples/jd")
print(f"Loaded JD roles: {list(JD_DATA.keys())}")

@app.route("/upload", methods=["POST"])
def upload_resume():
    if 'file' not in request.files or 'job_role' not in request.form:
        return jsonify({"error": "File or job role missing"}), 400

    file = request.files['file']
    job_role = request.form['job_role'].replace(" ", "_").lower()

    if job_role not in JD_DATA:
        return jsonify({"error": f"Job role '{job_role}' not found"}), 400

    # Save uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # Extract resume text
    text = extract_resume_text(file_path)

    # Extract skills from resume
    resume_skills = extract_skills(text)

    # Load JD skills for this role
    jd_skills = JD_DATA[job_role]

    # Calculate score and missing skills
    score, matched_skills, missing_skills = calculate_resume_score(resume_skills, jd_skills)

    return jsonify({
        "resume_skills": resume_skills,
        "job_role": job_role,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "score": score
    })

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)