import re

text = "My email is xyz@gmail.com and phone is +92-3123-456789"

# Basic patterns
pattern = r"\w+@\w+\.\w+"
match = re.search(pattern, text)
if match:
    print(match.group())    # xyz@gmail.com

# Common patterns
email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
phone_pattern = r"\d{2}-\d{4}-\d{5}"

# Find all
emails = re.findall(r"\w+@\w+\.\w+", text)

# Substitution
new_text = re.sub(r"\d{2}-\d{4}-\d{5}", "XXX-XXX-XXXX", text)

# Splitting
words = re.split(r"\s+", "Hello   world  test")

# Groups
date_pattern = r"(\d{2})-(\d{2})-(\d{4})"
match = re.search(date_pattern, "19-06-2026")
if match:
    day, month, year = match.groups()
