import os

def extract_jd_skills(jd_file_path):
    jd_skills = []
    with open(jd_file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        skills_section = False
        for line in lines:
            line = line.strip()
            if line.startswith("Required Skills"):
                skills_section = True
                continue
            if skills_section:
                if line.startswith("- "):
                    jd_skills.append(line[2:])
                elif line == "" or not line.startswith("- "):
                    break
    return jd_skills

def load_all_jds(jd_folder="samples/jd"):
    jd_dict = {}
    for jd_file in os.listdir(jd_folder):
        if jd_file.endswith(".txt"):
            role_name = jd_file.replace(".txt", "").lower().replace(" ", "_")
            jd_path = os.path.join(jd_folder, jd_file)
            jd_dict[role_name] = extract_jd_skills(jd_path)
    return jd_dict