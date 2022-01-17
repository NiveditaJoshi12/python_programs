# Collect an email address from the user and
# then find out if the user has a custom domain name or a popular domain name.
# Get user email address
popular_domains = {
"gmail": "Google",
"hotmail":"Microsoft",
"yahoo":"Yahoo",
"outlook":"Microsoft"}

user_email = input("What is your email address? ")

user_name = user_email.split('@')[0]
user_domain = user_email.split('@')[-1]
user_domain = user_domain.split('.')[0]

if user_domain in popular_domains.keys():
    print(f"Hey {user_name} it seems like your email is registered with {popular_domains[user_domain]}!")
else:
    print(f"Hey {user_name} it seems like you have your own custom domain at {user_domain}!")