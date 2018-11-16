# Bai 2
'''
1> pip install validate_email
2> pip install py3dns
'''

import re
from validate_email import validate_email


# This's function check email address really registered
def validate_email_exists(str_email):
    if str_email is None or str_email == '': return False
    try:
        return True if validate_email(str_email, verify=True) else False
    except BaseException as be:
        print(be)
        return False


lst_emails = ['adamparker@gmail.com', 'adamparker@facebook.com.vn', 'adamparkerfacebook.com.vn',
              'adam parker@facebook.com.vn', 'adamparker@face book.com.vn', '@hushmail.com', 'adamparker',
              'adamparker@', 'adamparker@gmail', 'adamparker@7zip.com', 'adamparker123@gmail.com',
              'adam_parker@gmail.com', 'adam.parker@gmail.com', 'adam.parker123@gmail.com', 'adam.parker_123@gmail.com',
              'adamparker@gmail.com4', 'adamparker@7_zip.com']

str_pattern = r'^([a-zA-Z0-9._]+)@([a-zA-Z0-9_]+)\.([a-zA-Z]+)([\.a-zA-Z]*)$'

for str_email in lst_emails:
    if re.match(str_pattern, str_email):
        if validate_email_exists(str_email):
            print(str_email, '->', 'Correct format', '->', 'This email address really exists')
        else:
            print(str_email, '->', 'Correct format', '->', "This email address doesn't exists")
    else:
        print(str_email, '->', 'Wrong format')
