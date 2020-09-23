import csv
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def welcome_page():
    return render_template('index.html')


@app.route('/thankyou')
def thankyou_page():
    return render_template('thankyou.html')


@app.route('/favicon.ico')
def icon():
    app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon.ico'))


def write_to_txt_file(data: dict):
    with open('database.txt', mode='a') as database:
        database.write(f'\n{"-"*150}\nName: {data["name"]}\nEmail ID: {data["email"]}\nSubject: {data["subject"]}\nMessage: {data["message"]}')


def write_to_csv_file(data: dict):
    with open('database.csv', mode='a', newline='\n') as database2:
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        name = data['name']
        email_id = data['email']
        subject = data['subject']
        msg = data['message']

        csv_writer.writerow([name, email_id, subject, msg])


@app.route('/query_submitted', methods=["POST", "GET"])
def get_data():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_txt_file(data)
        write_to_csv_file(data)
        return redirect('thankyou')
    else:
        return 'Something went wrong! Please try again later!'
