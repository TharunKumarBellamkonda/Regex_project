from flask import Flask, request, render_template
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
    User_name = request.form.get('User_name')
    User_mail = request.form.get('User_mail')
    func = request.form.get('func')

    if func == "findall":
        result = re.findall(User_name, User_mail)
    elif func == "search":
        match = re.search(User_name, User_mail)
        result = f'The text is located in position: {match.start()}' if match else 'No Match found, please try again'
    elif func == "split":
        result = re.split(User_name, User_mail)
    elif func == "sub":
        result = re.sub(User_name, User_mail)
    else:
        result = 'Invalid function'

    return render_template('result.html', result=result, User_name=User_name, User_mail=User_mail, func=func)

@app.route('/validate_email', methods=['POST'])
def validate_email():
    email = request.form.get('email')
    is_valid = re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}$', email)
    return render_template('home.html', email=email, email_address="Valid email address" if is_valid else "Invalid email address", condition=is_valid)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
