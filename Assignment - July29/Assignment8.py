def get_domain(email):
    if "@" not in email:
        return "Invalid"

    domain = email.split("@")[1]
    company = domain.split(".")[0]

    return company.title()


email = "developer_99@microsoft.com"

print(get_domain(email))