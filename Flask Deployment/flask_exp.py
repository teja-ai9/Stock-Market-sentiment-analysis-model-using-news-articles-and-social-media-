from flask import Flask, render_template, request
import csv

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('emotions_form.html')

@app.route('/predict', methods=['POST'])
def search():
  date = request.form['Date']
  data = []
  with open('final_5thjan.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      if row['Date'] == date:
        data.append(row)
  return render_template('search_results_sp.html', data=data)

@app.route('/emotions', methods=['POST'])
def emotions():
  date = request.form['Date']
  data = []
  with open('final_5thjan.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
      if row['Date'] == date:
        data.append(row)
  return render_template('emotions_results.html', data=data)

if __name__ == '__main__':
  app.run()
