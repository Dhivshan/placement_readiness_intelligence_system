from fpdf import FPDF
import os

# Create directories if they don't exist
os.makedirs("../data/sample_resumes", exist_ok=True)
os.makedirs("../data/sample_jds", exist_ok=True)

# -------------------------------
# Generate Synthetic Resume PDFs
# -------------------------------
def create_resume(filename, name, education, skills, projects, experience):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt=f"Resume - {name}", ln=True, align="C")
    pdf.ln(10)

    pdf.cell(200, 10, txt=f"Education: {education}", ln=True)
    pdf.cell(200, 10, txt=f"Skills: {', '.join(skills)}", ln=True)
    pdf.cell(200, 10, txt=f"Projects: {', '.join(projects)}", ln=True)
    pdf.cell(200, 10, txt=f"Experience: {experience}", ln=True)

    pdf.output(filename)

# Example resumes
create_resume("../data/sample_resumes/resume1.pdf",
              "John Doe",
              "B.Tech Computer Science",
              ["Python", "Machine Learning", "Data Visualization"],
              ["Predictive Analytics Project"],
              "Data Analyst Intern at XYZ Corp")

create_resume("../data/sample_resumes/resume2.pdf",
              "Jane Smith",
              "M.Sc Data Science",
              ["SQL", "Tableau", "R", "Statistics"],
              ["Customer Segmentation Analysis"],
              "Business Intelligence Intern at ABC Ltd")

create_resume("../data/sample_resumes/resume3.pdf",
              "Arun Kumar",
              "B.E Information Technology",
              ["Java", "Spring Boot", "Docker", "AWS"],
              ["E-commerce Web Application"],
              "Software Developer Intern at DEF Tech")

# -------------------------------
# Generate Synthetic JD Text Files
# -------------------------------
jd1 = """Job Title: Data Analyst
Required Skills: Python, SQL, Tableau, Machine Learning
Critical Skills: SQL, Tableau
Optional Skills: Power BI, Docker
Responsibilities: Data cleaning, Visualization, Business Intelligence
"""

jd2 = """Job Title: Software Engineer
Required Skills: Java, Spring Boot, Docker, AWS
Critical Skills: Java, Spring Boot
Optional Skills: Kubernetes, React
Responsibilities: Backend development, API integration, Cloud deployment
"""

jd3 = """Job Title: Business Analyst
Required Skills: Excel, SQL, Power BI, Communication
Critical Skills: SQL, Communication
Optional Skills: Tableau, Python
Responsibilities: Requirement gathering, Stakeholder analysis, Reporting
"""

with open("../data/sample_jds/jd1.txt", "w") as f:
    f.write(jd1)

with open("../data/sample_jds/jd2.txt", "w") as f:
    f.write(jd2)

with open("../data/sample_jds/jd3.txt", "w") as f:
    f.write(jd3)

print("Synthetic resumes and job descriptions generated successfully!")