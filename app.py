from flask import Flask, request, render_template
import re

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('input_data.html')

@app.route('/submit_form', methods=['POST'])
def handle_form():
    id_number = request.form.get('id')
    name = request.form.get('name')
    gender = request.form.get('gender')
    email = request.form.get('email')

    # Validate ID number (assuming 台灣ID)
    if len(id_number)!=10:
        return "身分證號碼應該為10碼", 400
        
    if not id_number[0].isalpha():
        return "第一個字元應該為英文字母碼", 400
        
    if not id_number[1:].isdigit():
        return "身分證號碼後九個字元應該為數字", 400

    def letter_to_number(letter):
    letter = letter.upper()
    if letter == 'A':
        return 10
    elif letter == 'B':
        return 11
    elif letter == 'C':
        return 12
    elif letter == 'D':
        return 13
    elif letter == 'E':
        return 14
    elif letter == 'F':
        return 15
    elif letter == 'G':
        return 16
    elif letter == 'H':
        return 17
    elif letter == 'I':
        return 34
    elif letter == 'J':
        return 18
    elif letter == 'K':
        return 19
    elif letter == 'L':
        return 20
    elif letter == 'M':
        return 21
    elif letter == 'N':
        return 22
    elif letter == 'O':
        return 35
    elif letter == 'P':
        return 23
    elif letter == 'Q':
        return 24
    elif letter == 'R':
        return 25
    elif letter == 'S':
        return 26
    elif letter == 'T':
        return 27
    elif letter == 'U':
        return 28
    elif letter == 'V':
        return 29
    elif letter == 'W':
        return 32
    elif letter == 'X':
        return 30
    elif letter == 'Y':
        return 31
    elif letter == 'Z':
        return 33
    else:
        return "身分證號碼第一個英文字母應該轉換為對應數字", 400






    # Validate name (assuming it's alphabetic)
    if not re.match(r'^[A-Za-z\s]+$', name):
        return "Invalid name", 400

    # Validate gender
    if gender not in ['Male', 'Female']:
        return "Invalid gender", 400

    # Validate email
    if not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
        return "Invalid email", 400

    return "All entries are valid", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Listen on all available network interfaces and port 80

