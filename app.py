# app.py
from flask import Flask, render_template, request
import csv

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/filter', methods=['POST'])
def filter_results():
    n = int(request.form['n'])
    budget = request.form['budget']

    budget2 = budget.split('-')

    if budget2[1] == '10000':
        csv_file = 'company_based_ranking_below10k.csv'
    elif budget2[1] == '20000':
        csv_file = 'company_based_ranking_below20k.csv'
    elif budget2[1] == '30000':
        csv_file = 'company_based_ranking_below30k.csv'
    elif budget2[1] == '40000':
        csv_file = 'company_based_ranking_below40k.csv'
    elif budget2[1] == '50000':
        csv_file = 'company_based_ranking_below50k.csv'
    elif budget2[1] == '60000':
        csv_file = 'company_based_ranking_below60k.csv'

    rows = []

    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        i = 1
        for row in csv_reader:
            rows.append(row)
            if i == n:
                break
            i = i+1

    return render_template('resultsCompany.html', results=rows)


@app.route('/filter2', methods=['POST'])
def filter_results2():
    n = int(request.form['n'])
    budget = request.form['budget']

    budget2 = budget.split('-')

    if budget2[1] == '10000':
        csv_file = 'product_based_ranking_below10k.csv'
    elif budget2[1] == '20000':
        csv_file = 'product_based_ranking_below20k.csv'
    elif budget2[1] == '30000':
        csv_file = 'product_based_ranking_below30k.csv'
    elif budget2[1] == '40000':
        csv_file = 'product_based_ranking_below40k.csv'
    elif budget2[1] == '50000':
        csv_file = 'product_based_ranking_below50k.csv'
    elif budget2[1] == '60000':
        csv_file = 'product_based_ranking_below60k.csv'

    rows = []

    with open(csv_file, 'r') as file:
        csv_reader = csv.reader(file)
        i = 1
        for row in csv_reader:
            rows.append(row)
            if i == n:
                break
            i = i+1

    return render_template('resultsProducts.html', results=rows)


if __name__ == '__main__':
    app.run(debug=True)
