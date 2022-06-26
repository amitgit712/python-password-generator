from flask import Flask, render_template, \
                    request

import random
import string

app = Flask(__name__)

ASCII_UPPERCASE = string.ascii_uppercase
ASCII_LOWERCASE = string.ascii_lowercase
DIGITS = string.digits
PUNCTUATION = string.punctuation

PASSWORD_LENGTH = [
    '6','7','8','9','10',
    '11','12','13','14','15',
    '16','17','18','19','20'
]

### Web aplication

@app.route('/', methods=['GET','POST'])
def gen_pass():
    if request.method == 'POST':
        is_cap = request.form.get('uppercase') != None
        is_lower = request.form.get('lowercase') != None
        is_digits = request.form.get('digits') != None
        is_punctuation = request.form.get('specialcharacters') != None
        pass_length = int(request.form['pass_length'])
        
        arguments = []

        if is_cap:
            arguments.append(ASCII_UPPERCASE)

        if is_lower:
            arguments.append(ASCII_LOWERCASE)

        if is_digits:
            arguments.append(DIGITS)

        if is_punctuation:
            arguments.append(PUNCTUATION)

        if arguments == []:
            arguments.append(string.ascii_letters)
        else:
            pass
        password = ''.join(random.choices(''.join(arguments), k=pass_length))
        return render_template('genPass.html',generated_password=password,password_length=PASSWORD_LENGTH)
    return render_template('genPass.html',password_length=PASSWORD_LENGTH)

### Using Terminal

# def set_input(user_input):
#     if user_input.upper() == 'Y' or user_input.upper() == 'YES':
#         return True
#     return False




# def generate_password():
#     pass_length = int(input("Password Length : "))
#     if pass_length < 6:
#         print(f"\n Please provide password length greater than or equal to 6\n")
#         generate_password()
#     is_cap = set_input(input("Uppercase (Yes/No or Y/N) : "))
#     is_lower = set_input(input("Lowercase (Yes/No or Y/N) : "))
#     is_digits = set_input(input("Numbers (Yes/No or Y/N) : "))
#     is_punctuation = set_input(input("Special Char (Yes/No or Y/N) : "))

#     arguments = []

#     if is_cap:
#         arguments.append(ASCII_UPPERCASE)

#     if is_lower:
#         arguments.append(ASCII_LOWERCASE)

#     if is_digits:
#         arguments.append(DIGITS)

#     if is_punctuation:
#         arguments.append(PUNCTUATION)

#     password = ''.join(random.choices(''.join(arguments), k=pass_length))

#     print(f"\n Your Password Is : \n {password}")

#     return password


# generate_password()


if __name__ == '__main__':

    app.run(host="0.0.0.0",debug=True, port=5000)
