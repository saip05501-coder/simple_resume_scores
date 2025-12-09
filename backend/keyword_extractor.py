import re

# Predefined skills list
SKILLS_LIST = [
    # Programming Languages
    "Python", "Java", "C++", "C", "C#", "JavaScript", "TypeScript", "R", "SQL", "MATLAB", "Go", "Ruby", "PHP", "Scala",

    # Web Development
    "HTML", "CSS", "React", "ReactJS", "Angular", "Vue.js", "Node.js", "Express", "Django", "Flask", "Spring Boot", "Bootstrap", "Tailwind CSS",

    # Databases
    "MySQL", "PostgreSQL", "MongoDB", "SQLite", "Oracle", "Redis", "Cassandra", "MariaDB", "Firebase",

    # Machine Learning & AI
    "Machine Learning", "Deep Learning", "NLP", "Computer Vision", "Data Analysis", "Data Mining", "Scikit-learn",
    "TensorFlow", "Keras", "PyTorch", "OpenCV", "LightGBM", "XGBoost", "CatBoost", "MLlib", "FastAI",

    # Data Science & Analytics
    "Pandas", "NumPy", "Matplotlib", "Seaborn", "Plotly", "Tableau", "Power BI", "Excel", "Data Visualization", "Statistics",

    # Cloud & DevOps
    "AWS", "Azure", "GCP", "Docker", "Kubernetes", "CI/CD", "Jenkins", "Terraform", "Ansible", "Git", "GitHub", "GitLab",

    # Big Data
    "Hadoop", "Spark", "Kafka", "Hive", "Pig", "Flink", "NoSQL",

    # Tools & Platforms
    "VS Code", "PyCharm", "Jupyter Notebook", "Colab", "Linux", "Linux Shell", "Unix", "REST API", "GraphQL", "Postman", "Swagger",

    # Other Skills
    "Agile", "Scrum", "Kanban", "Problem Solving", "Communication", "Teamwork", "Leadership", "Project Management",

    # Optional/Popular libraries
    "Streamlit", "Flask-RESTful", "BeautifulSoup", "Selenium", "Requests", "NLTK", "SpaCy", "Gensim", "OpenAI API"
]

ABBREVIATIONS = {
    "ML": "Machine Learning",
    "DL": "Deep Learning",
    "CV": "Computer Vision",
    "NLP": "NLP"
}

def clean_text(text):
    text = text.replace("\n", " ")  # merge lines
    text = re.sub(r"[^a-zA-Z0-9\s\.\-+]", " ", text)  # remove weird chars
    text = re.sub(r"\s+", " ", text)  # multiple spaces → 1 space
    return text.lower()

def extract_skills(text):
    """
    Extract skills from resume text using predefined skills list.
    Works for multi-word skills.
    """
    text_lower = text.lower()
    extracted_skills = []

    for skill in SKILLS_LIST:
        pattern = r'\b' + re.escape(skill.lower()) + r'\b'
        if re.search(pattern, text_lower):
            extracted_skills.append(skill)

    return extracted_skills