from tabulate import tabulate

from GPTResParser import ResumeParser

# Initialize the parser with the resume path
parser = ResumeParser.Parse("resources\ATSResume.pdf")

# Extract candidate information
name = parser.get_name()
email = parser.get_email()
phone_number = parser.get_phoneNumber()
skills_list = parser.get_skills()
schools_dict = parser.get_schools()
experience_dict = parser.get_experience()

# Store the extracted information in a dictionary
resume_data = {
    "Candidate's Name": name,
    "Email Address": email,
    "Phone Number": phone_number,
    "Skills List": skills_list,
    "Schools Dict": schools_dict,
    "Experience Dict": experience_dict
}

# Convert the dictionary to a list of tuples
data_as_list = [(field, value) for field, value in resume_data.items()]

# Print the information in a tabular format
table = tabulate(data_as_list, headers=["Field", "Value"], tablefmt="grid")
print(table)

