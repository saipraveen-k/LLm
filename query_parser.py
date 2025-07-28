import re

def extract_info(query):
    age = re.search(r'(\d+)[ ]*[-]*[ ]*(year|yr)', query, re.I)
    surgery = re.search(r'(knee surgery|hip surgery|heart surgery|surgery)', query, re.I)
    location = re.search(r'in (\w+)', query)
    policy_age = re.search(r'(\d+)[ ]*[-]*[ ]*(month|yr)', query)

    return {
        "age": age.group(1) if age else None,
        "procedure": surgery.group(1) if surgery else None,
        "location": location.group(1) if location else None,
        "policy_duration": policy_age.group(1) + " months" if policy_age else None
    }
