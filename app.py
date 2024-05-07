from flask import Flask, render_template, request, jsonify
from Stocks import *
from Report import *


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("landing_page.html")

@app.route("/report", methods=['POST'])
def report():
    
    stock = request.form.get("stocks")

    sd = stocks_dictionary()
    symbol = sd.symbols()

    stock_symbol = symbol[stock]

    hst_data, curr_prize, sym, vp, shp = stock_data(stock_symbol)
    rf = random_forest()
    rf.data_prepation()
    features = [vp[2], None, vp[3], vp[4], vp[8], vp[12], vp[6], vp[7], vp[5], shp[2], shp[0], shp[1]]
    decision = rf.prediction(features)

    return render_template("stats.html", Stock_name = stock, Decision = decision, Curr_prize = curr_prize, Symbol = stock_symbol, year_high = vp[0], year_low = vp[1],
                     mkt_cap = vp[2], equity = vp[6], reserve = vp[7], eps = vp[8], PEratio = vp[9], bookvalue = vp[10], 
                     PBratio = vp[11], dividend = vp[12], facevalue = vp[13], FII = shp[0], DII = shp[1], 
                     promoter = shp[2], public = shp[3], other = shp[4])

  
    