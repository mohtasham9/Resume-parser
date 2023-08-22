from GPTResParser import ResumeParser

# Initialize the parser with the resume path
parser = ResumeParser.Parse("resources\Dublin.pdf")

# Extract candidate information
name = parser.get_name()
email = parser.get_email()
phone_number = parser.get_phoneNumber()
skills_list = parser.get_skills()
schools_dict = parser.get_schools()
experience_dict = parser.get_experience()

# Print the extracted information
print("Candidate's Name:", name)
print("Email Address:", email)
print("Phone Number:", phone_number)
print("Skills List:", skills_list)
print("Schools Dict", schools_dict)
print("Experience Dict", experience_dict)