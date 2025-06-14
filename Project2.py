email=input("Enter email:")
def valid_email(email):
    if  email.count('@') != 1:
        return False
    local_part, domain_part = email.split('@')
    if not local_part or not domain_part:
        return False
    if '.' not in domain_part or domain_part.startswith('.') or domain_part.endswith('.'):
        return False
    return True
if valid_email(email):
    print('Valid')
else:
    print('Invalid')
