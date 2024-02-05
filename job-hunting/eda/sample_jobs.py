# This file will contain job postings and top AI-picked candidates, based on one of the resume hiring tool's
# sample data generated
import re
from typing import List, Dict, NamedTuple

job_1 = '''Job preview: Account Executive

On-site · London, United Kingdom · Full time

Description
We are looking for a competent Account Executive to find business opportunities and manage customer relationships. You’ll be directly responsible for the preservation and expansion of our customer base. The ideal candidate will have talent in sales and experience in customer service. We expect you to be a reliable professional able to achieve balance between customer orientation and a results-driven approach. The goal is to find opportunities and turn them in long-term profitable relationships based on trust and mutual satisfaction.

Responsibilities

Create detailed business plans to facilitate the attainment of goals and quotas
Manage the entire sales cycle from finding a client to securing a deal
Present products to prospective clients
Provide professional after-sales support to enhance the customers’ dedication
Remain in frequent contact with the clients in your responsibility to understand their needs
Negotiate agreements and keep records of sales and data
Requirements

Proven experience as an Account Executive, or in other sales/customer service role
Knowledge of market research, sales and negotiating principles
Outstanding knowledge of MS Office; knowledge of CRM software (e.g. Salesforce) is a plus
Excellent communication/presentation skills and ability to build relationships
Organizational and time-management skills
A business acumen
Enthusiastic and passionate
Benefits

Health Care Plan (Medical, Dental & Vision)
Retirement Plan (401k, IRA)
Paid Time Off (Vacation, Sick & Public Holidays)
Family Leave (Maternity, Paternity)
Training & Development
Stock Option Plan'''

# summary, education, skills, resume, contact details, contact preferences, social profiles (automatically retrieved)

class Education(NamedTuple):
    start_year: int
    end_year: int
    degree: str
    institution: str

    def __repr__(self) -> str:
        return (f"{self.degree} at {self.institution}, "
                f"{self.start_year} - {self.end_year}")

def parse_education(raw_education: str) -> Education:
    # Example of a basic parser, can be expanded based on the format of raw data
    match = re.match(r"(\d{4}) - (\d{4})\n(.*) at (.*)", raw_education)
    if match:
        start_year, end_year, degree, institution = match.groups()
        return Education(int(start_year), int(end_year), degree, institution)
    else:
        raise ValueError("Invalid education format")

class Candidate:
    def __init__(self, 
                 summary: str, 
                 raw_education: str, 
                 skills: str, 
                 resume: str, 
                 contact_details: Dict[str, str], 
                 contact_preferences: Dict[str, str], 
                 social_profiles: List[str]) -> None:
        self.summary = summary
        self.education = parse_education(raw_education)
        self.skills = skills.split(', ')
        self.resume = resume
        self.contact_details = contact_details
        self.contact_preferences = contact_preferences
        self.social_profiles = social_profiles

    def __repr__(self) -> str:
        return (f"Candidate(summary={self.summary}, education={self.education}, "
                f"skills={self.skills}, resume={self.resume}, "
                f"contact_details={self.contact_details}, "
                f"contact_preferences={self.contact_preferences}, "
                f"social_profiles={self.social_profiles})")
    
raw_education_data = "2005 - 2009\nB.A. Business Management at University of Arizona"

candidate = Candidate(
    summary="Experienced professional",
    raw_education=raw_education_data,
    skills="Project Management, Data Analysis",
    resume="resume.pdf",
    contact_details={"phone": "555-0100", "email": "candidate@example.com"},
    contact_preferences={"texting": "enabled", "phone": "disabled"},
    social_profiles=["linkedin.com/in/example"]
)

print(candidate)

# sourced_candidates_data = [
#     (
#      """Colleagues know me as highly creative, someone who can always be trusted to come up with a new approach. I know the client’s business comes first, so I spend time to understand how best my work can create a positive result for clients. I can work well alone, but I’m at my best collaborating with others.""", # summary i.e. something about who the person is etc.
#      """""", # education e.g. start, end, what is it
#      """""", # skills "skill 1, skill 2, ..., skill n" they"re comma separated strings
#      """""", # resume
#      {}, # contact details e.g. { address: "", phone: "", email: "" }
#      {}, # contact preferences e.g. texting: enabled/disabled, phone: enabled/disabled
#      [] # social profiles
#      ),
#      ()
# ]


# sourced_candidates = [Candidate(*data) for data in sourced_candidates_data]