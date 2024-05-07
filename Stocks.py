import pandas as pd

class stocks_dictionary:
    def symbols(self):
        symbol = {
            'Adani Ports and Special Economic Zone Ltd': 'ADANIPORTS',
            'Asian Paints Ltd': 'ASIANPAINT',
            'Axis Bank Ltd': 'AXISBANK',
            'Bajaj Auto Ltd': 'BAJAJ_AUTO',
            'Bajaj Finserv Ltd': 'BAJAJFINSV',
            'Bajaj Finance Ltd': 'BAJFINANCE',
            'Bharti Airtel Ltd': 'BHARTIARTL',
            'Bharat Petroleum Corporation Ltd': 'BPCL',
            'Britannia Industries Ltd': 'BRITANNIA',
            'Cipla Ltd': 'CIPLA',
            'Coal India Ltd': 'COALINDIA',
            "Divi's Laboratories Ltd": 'DIVISLAB',
            "Dr. Reddy's Laboratories Ltd": 'DRREDDY',
            'Eicher Motors Ltd': 'EICHERMOT',
            'Grasim Industries Ltd': 'GRASIM',
            'HCL Technologies Ltd': 'HCLTECH',
            'HDFC Bank Ltd': 'HDFCBANK',
            'HDFC Life Insurance Company Ltd': 'HDFCLIFE',
            'Hero MotoCorp Ltd': 'HEROMOTOCO',
            'Hindalco Industries Ltd': 'HINDALCO',
            'Hindustan Unilever Ltd': 'HINDUNILVR',
            'ICICI Bank Ltd': 'ICICIBANK',
            'IndusInd Bank Ltd': 'INDUSINDBK',
            'Infosys Ltd': 'INFY',
            'ITC Ltd': 'ITC',
            'JSW Steel Ltd': 'JSWSTEEL',
            'Kotak Mahindra Bank Ltd': 'KOTAKBANK',
            'Larsen & Toubro Ltd': 'LT',
            'Mahindra & Mahindra Ltd': 'MnM',
            'Maruti Suzuki India Ltd': 'MARUTI',
            'Nestle India Ltd': 'NESTLEIND',
            'NTPC Ltd': 'NTPC',
            'Oil and Natural Gas Corporation Ltd': 'ONGC',
            'Power Grid Corporation of India Ltd': 'POWERGRID',
            'Reliance Industries Ltd': 'RELIANCE',
            'State Bank of India': 'SBIN',
            'SBI Life Insurance Company Ltd': 'SBILIFE',
            'Shree Cement Ltd': 'SHREECEM',
            'Sun Pharmaceutical Industries Ltd': 'SUNPHARMA',
            'Tata Consultancy Services Ltd': 'TCS',
            'Tata Consumer Products Ltd': 'TATACONSUM',
            'Tata Motors Ltd': 'TATAMOTORS',
            'Tata Steel Ltd': 'TATASTEEL',
            'Tech Mahindra Ltd': 'TECHM',
            'Titan Company Ltd': 'TITAN',
            'UltraTech Cement Ltd': 'ULTRACEMCO',
            'United Breweries Ltd': 'UBL',
            'Wipro Ltd': 'WIPRO',
            'Zee Entertainment Enterprises Ltd': 'ZEEL',
            'Adani Green Energy Ltd': 'ADANIGREEN'
        }
        return symbol



class ADANIPORTS:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\ADANIPORTS.NS.csv')
        return df

    def current_price(self):
        price = 1320
        return price

    def NSE_symbol(self):
        symbol = 'ADANIPORTS'
        return symbol

    def value_parameters(self):
        self.year_high = 1424.95 #0
        self.year_low = 656.75 #1
        self.mkt_cap = 236196 #2
        self.expenses = 1121 #3
        self.netprofit = 10094 #4
        self.roce = 12.9 #5
        self.equity = 432 #6
        self.reserve = 48261 #7
        self.EPS = 10.22 #8
        self.PERatio = 32.5 #9
        self.bookvalue = 225 #10
        self.PBRatio = 5.88 #11
        self.dividend_yield = 0.38 #12
        self.facevalue = 2 #13
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce,self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 14.98
        self.institution = 11.84
        self.promoter = 65.89
        self.public = 7.30
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others


class ASIANPAINT:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\ASIANPAINT.NS.csv')
        return df

    def current_price(self):
        price = 2930
        return price

    def NSE_symbol(self):
        symbol = 'ASIANPAINT'
        return symbol

    def value_parameters(self):
        self.year_high = 3568
        self.year_low = 2766.15
        self.mkt_cap = 281021
        self.expanses = 27793
        self.netprofit = 5541
        self.roce = 34
        self.equity = 96
        self.reserve = 16466
        self.EPS = 56.69
        self.PERatio = 50.6
        self.bookvalue = 173
        self.PBRatio = 16.7
        self.dividend_yield = 0.89
        self.facevalue = 1
        return self.year_high, self.year_low, self.mkt_cap, self.expanses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 15.89
        self.institution = 11.61
        self.promoter = 52.63
        self.public = 19.78
        self.others = 0.04
        return self.foreign, self.institution, self.promoter, self.public ,self.others

class AXISBANK:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\AXISBANK.NS.csv')
        return df

    def current_price(self):
        price = 1142
        return price

    def NSE_symbol(self):
        symbol = "AXISBANK"
        return symbol

    def value_parameters(self):
        self.year_high = 1182.90
        self.year_low = 854.05
        self.mkt_cap = 359942
        self.expenses = 61391
        self.netprofit = 35178
        self.roce = 9
        self.equity = 615
        self.reserve = 129166
        self.EPS = 85.49
        self.PERatio = 13.4
        self.bookvalue = 422
        self.PBRatio = 2.71
        self.dividend_yield = 0.09
        self.facevalue = 2
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 53.84
        self.institution = 30.12
        self.promoter = 8.22
        self.public = 7.81
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class BAJAJ_AUTO:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\BAJAJ-AUTO.NS.csv')
        return df

    def current_price(self):
        price = 9106
        return price

    def NSE_symbol(self):
        symbol = 'BAJAJ AUTO'
        return symbol

    def value_parameters(self):
        self.year_high = 3568
        self.year_low = 2766.15
        self.mkt_cap = 281020
        self.expenses = 36109
        self.netprofit = 7708
        self.roce = 26
        self.equity = 279
        self.reserve = 28683
        self.EPS = 72.05
        self.PERatio = 33
        self.bookvalue = 1037
        self.PBRatio = 8.78
        self.dividend_yield = 0.88
        self.facevalue = 10
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce,self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 14.53
        self.institution = 8.47
        self.promoter = 55.06
        self.public = 21.88
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class BAJAJFINSV:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\BAJAJFINSV.NS.csv')
        return df

    def current_price(self):
        price = 1627
        return price

    def NSE_symbol(self):
        symbol = 'BAJAJFINSV'
        return symbol

    def value_parameters(self):
        self.year_high = 1741
        self.year_low = 1330
        self.mkt_cap = 259634
        self.expenses = 69716
        self.netprofit = 15595
        self.roce = 11.6
        self.equity = 159
        self.reserve = 60169
        self.EPS = 51.07
        self.PERatio = 31.9
        self.bookvalue = 378
        self.PBRatio = 4.3
        self.dividend_yield = 0.06
        self.facevalue = 1
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce,self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 8.42
        self.institution = 7.33
        self.promoter = 60.69
        self.public = 23.38
        self.others = 0.18
        return self.foreign, self.institution, self.promoter, self.public, self.others

class BAJFINANCE:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\BAJFINANCE.NS.csv')
        return df

    def current_price(self):
        price = 6932
        return price

    def NSE_symbol(self):
        symbol = 'BAJFINANCE'
        return symbol

    def value_parameters(self):
        self.year_high = 8192
        self.year_low = 6155.95
        self.mkt_cap = 429057
        self.expenses = 16273
        self.netprofit = 14451
        self.roce = 11.9
        self.equity = 124
        self.reserve = 76572
        self.EPS = 233.46
        self.PERatio = 29.7
        self.bookvalue = 1239
        self.PBRatio = 5.59
        self.dividend_yield = 0.52
        self.facevalue = 2
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 20.55
        self.institution = 14.33
        self.promoter = 54.69
        self.public = 10.19
        self.others = 0.16
        return self.foreign, self.institution, self.promoter, self.public, self.others

class BHARTIARTL:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\BHARTIARTL.NS.csv')
        return df

    def current_price(self):
        price = 1277
        return price

    def NSE_symbol(self):
        symbol = 'BHARTIARTL'
        return symbol

    def value_parameters(self):
        self.year_high = 1354
        self.year_low = 773.65
        self.mkt_cap = 759133
        self.expenses = 148392
        self.netprofit = 10716
        self.roce = 12.3
        self.equity = 2858
        self.reserve = 74627
        self.EPS = 15.01
        self.PERatio = 66.6
        self.bookvalue = 138
        self.PBRatio = 9.27
        self.dividend_yield = 0.31
        self.facevalue = 5
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce,self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 24.35
        self.institution = 19.20
        self.promoter = 53.48
        self.public = 2.80
        self.others = 0.05
        return self.foreign, self.institution, self.promoter, self.public, self.others

class BPCL:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\BPCL.NS.csv')
        return df

    def current_price(self):
        price = 630
        return price

    def NSE_symbol(self):
        symbol = 'BPCL'
        return symbol

    def value_parameters(self):
        self.year_high = 687.95
        self.year_low = 331.45
        self.mkt_cap = 136630
        self.expenses = 449644
        self.netprofit = 28940
        self.roce  = 6.86
        self.equity = 2129
        self.reserve = 68853
        self.EPS = 133.41
        self.PERatio = 4.49
        self.bookvalue = 327
        self.PBRatio = 1.92
        self.dividend_yield = 3.33
        self.facevalue = 10
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 16.79
        self.institution = 21.30
        self.promoter = 522.98
        self.public = 8
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class BRITANNIA:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\BRITANNIA.NS.csv')
        return df

    def current_price(self):
        price = None
        return 4745

    def NSE_symbol(self):
        symbol = 'BRITANNIA'
        return symbol

    def value_parameters(self):
        self.year_high = 5386.05
        self.year_low = 4347.7
        self.mkt_cap = 114282
        self.expenses = 13603
        self.netprofit = 2134
        self.roce = 48.9
        self.equity = 24
        self.reserve = 3917
        self.EPS = 88.84
        self.PERatio = 53.5
        self.bookvalue = 164
        self.PBRatio = 29
        self.dividend_yield = 1.52
        self.facevalue = 1
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 18.23
        self.institution = 15.63
        self.promoter = 50.55
        self.public = 15.57
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class CIPLA:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\CIPLA.NS.csv')
        return df

    def current_price(self):
        price = 1425
        return price

    def NSE_symbol(self):
        symbol = 'CIPLA'
        return symbol

    def value_parameters(self):
        self.year_high = 1519
        self.year_low = 896.30
        self.mkt_cap = 115034
        self.expenses = 19201
        self.netprofit = 3743
        self.roce = 18
        self.equity = 161
        self.reserve = 24664
        self.EPS = 45.93
        self.PERatio = 29.1
        self.bookvalue = 307
        self.PBRatio = 4.63
        self.dividend_yield = 0.6
        self.facevalue = 2
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 25.82
        self.institution = 24.15
        self.promoter = 33.46
        self.public = 16.36
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class COALINDIA:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\COALINDIA.NS.csv')
        return df

    def current_price(self):
        price = 475
        return price

    def NSE_symbol(self):
        symbol = 'COALINDIA'
        return symbol

    def value_parameters(self):
        self.year_high = 487.6
        self.year_low = 223.25
        self.mkt_cap = 292483
        self.expenses= 94352
        self.netprofit = 37369
        self.roce = 65.1
        self.equity = 6163
        self.reserve = 76567
        self.EPS = 60.69
        self.PERatio = 7.83
        self.bookvalue = 134
        self.PBRatio = 3.54
        self.dividend_yield = 5.11
        self.facevalue = 10
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce,self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 8.41
        self.institution = 23.18
        self.promoter = 63.13
        self.public = 5.16
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class DIVISLAB:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\DIVISLAB.NS.csv')
        return df

    def current_price(self):
        price = 3951
        return price

    def NSE_symbol(self):
        symbol = 'DIVISLAB'
        return symbol

    def value_parameters(self):
        self.year_high = 4100
        self.year_low = 3051
        self.mkt_cap = 104885
        self.expanses = 5534
        self.netprofit = 1383
        self.roce = 19.4
        self.equity = 53
        self.reserve = 12624
        self.EPS = 52.10
        self.PERatio = 75.8
        self.bookvalue = 478
        self.PBRatio = 8.27
        self.dividend_yield = 0.76
        self.facevalue = 2
        return self.year_high, self.year_low, self.mkt_cap, self.expanses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 14.68
        self.institution = 22.1
        self.promoter = 51.92
        self.public = 11.19
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class DRREDDY:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\DRREDDY.NS.csv')
        return df

    def current_price(self):
        price = 6350
        return price

    def NSE_symbol(self):
        symbol = 'DRREDDY'
        return symbol

    def value_parameters(self):
        self.year_high = 6505.9
        self.year_low = 4384.05
        self.mkt_cap = 105922
        self.expenses = 19585
        self.netprofit = 5228
        self.roce = 26.7
        self.equity = 83
        self.reserve = 25413
        self.EPS = 313.66
        self.PERatio = 20.3
        self.bookvalue = 1528
        self.PBRatio = 4.15
        self.dividend_yield = 0.63
        self.facevalue = 5
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce,self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 29.13
        self.institution = 18.31
        self.promoter = 26.65
        self.public = 25.73
        self.others = 0.17
        return self.foreign, self.institution, self.promoter, self.public, self.others


class EICHERMOT:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\EICHERMOT.NS.csv')
        return df

    def current_price(self):
        price = 4588
        return price

    def NSE_symbol(self):
        symbol = 'EICHERMOT'
        return symbol

    def value_parameters(self):
        self.year_high = 4689.95
        self.year_low = 3160
        self.mkt_cap = 125623
        self.expenses = 11952
        self.netprofit = 3836
        self.roce = 27.4
        self.equity = 27
        self.reserve = 15904
        self.EPS = 140.19
        self.PERatio = 32.7
        self.bookvalue = 582
        self.PBRatio = 7.9
        self.dividend_yield = 0.79
        self.facevalue = 1
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 28.95
        self.institution = 11.04
        self.promoter = 49.14
        self.public = 10.77
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class GRASIM:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\GRASIM.NS.csv')
        return df

    def current_price(self):
        price = 2433
        return price

    def NSE_symbol(self):
        symbol = 'GRASIM'
        return symbol

    def value_parameters(self):
        self.year_high = 2489.75
        self.year_low = 1667
        self.mkt_cap = 162814
        self.expenses = 101286
        self.netprofit = 9560
        self.roce = 9.97
        self.equity = 132
        self.reserve = 83039
        self.EPS = 82.64
        self.PERatio = 28.9
        self.bookvalue = 1222
        self.PBRatio = 2
        self.dividend_yield = 0.41
        self.facevalue = 2
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 12.7
        self.institution = 16.69
        self.promoter = 43.05
        self.public = 27.24
        self.others = 0.31
        return self.foreign, self.institution, self.promoter, self.public, self.others

class HCLTECH:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\HCLTECH.NS.csv')
        return df

    def current_price(self):
        price = 1333
        return price

    def NSE_symbol(self):
        symbol = 'HCLTECH'
        return symbol

    def value_parameters(self):
        self.year_high = 1697.35
        self.year_low = 1055
        self.mkt_cap = 361623
        self.expenses = 85715
        self.netprofit = 15710
        self.roce = 29.8
        self.equity = 543
        self.reserve = 67720
        self.EPS = 57.86
        self.PERatio = 23
        self.bookvalue = 252
        self.PBRatio = 5.35
        self.dividend_yield = 3.89
        self.facevalue = 2
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 19.65
        self.institution = 14.95
        self.promoter = 60.82
        self.public = 4.35
        self.others = 0.21
        return self.foreign, self.institution, self.promoter, self.public, self.others

class HDFCBANK:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\HDFCBANK.NS.csv')
        return df

    def current_price(self):
        price = 1508
        return price

    def NSE_symbol(self):
        symbol = 'HDFCBANK'
        return symbol

    def value_parameters(self):
        self.year_high = 1757.50
        self.year_low = 1363.55
        self.mkt_cap = 1145880
        self.expenses = 283649
        self.netprofit = 65449
        self.roce = 9.5
        self.equity = 558
        self.reserve = 288880
        self.EPS = 84.33
        self.PERatio = 17.8
        self.bookvalue = 519
        self.PBRatio = 2.91
        self.dividend_yield = 1.28
        self.facevalue = 1
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 47.83
        self.institution = 33.33
        self.promoter = 0
        self.public = 18.64
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class HDFCLIFE:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\HDFCLIFE.NS.csv')
        return df

    def current_price(self):
        price = 557
        return price

    def NSE_symbol(self):
        symbol = 'HDFCLIFE'
        return symbol

    def value_parameters(self):
        self.year_high = 710.6
        self.year_low = 540
        self.mkt_cap = 119808
        self.expenses = 101029
        self.netprofit = 1574
        self.roce = 6.61
        self.equity = 2151
        self.reserve = 12515
        self.EPS = 7.32
        self.PERatio = 76.1
        self.bookvalue = 68.2
        self.PBRatio = 8.1
        self.dividend_yield = 0.35
        self.facevalue = 10
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 30.03
        self.institution = 7.93
        self.promoter = 50.37
        self.public = 11.64
        self.others = 0.03
        return self.foreign, self.institution, self.promoter, self.public, self.others

class HEROMOTOCO:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\HEROMOTOCO.NS.csv')
        return df

    def current_price(self):
        price = 4444
        return price

    def NSE_symbol(self):
        symbol = 'HEROMOTOCO'
        return symbol

    def value_parameters(self):
        self.year_high = 4949.05
        self.year_low = 2566
        self.mkt_cap = 88859
        self.expenses = 31655
        self.netprofit = 3610
        self.roce = 22.7
        self.equity = 40
        self.reserve = 17634
        self.EPS = 180.87
        self.PERatio = 23.9
        self.bookvalue = 884
        self.PBRatio = 5.03
        self.dividend_yield = 2.22
        self.facevalue = 2
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 28.93
        self.institution = 27.76
        self.promoter = 34.76
        self.public = 8.55
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class HINDALCO:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\HINDALCO.NS.csv')
        return df

    def current_price(self):
        price = 620
        return price

    def NSE_symbol(self):
        symbol = 'HINDALCO'
        return symbol

    def value_parameters(self):
        self.year_high = 661.6
        self.year_low = 397.8
        self.mkt_cap = 139738
        self.expenses = 215825
        self.netprofit = 9392
        self.roce = 11.3
        self.equity = 223
        self.reserve = 45836
        self.EPS = 41.79
        self.PERatio = 14.9
        self.bookvalue = 443
        self.PBRatio = 1.4
        self.dividend_yield = 0.48
        self.facevalue = 1
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce,self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 26.82
        self.institution = 25.64
        self.promoter = 34.65
        self.public = 12.08
        self.others = 0.46
        return self.foreign, self.institution, self.promoter, self.public, self.others

class HINDUNILVR:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\HINDUNILVR.NS.csv')
        return df

    def current_price(self):
        price = 2379
        return price

    def NSE_symbol(self):
        symbol = 'HINDUNILVR'
        return symbol

    def value_parameters(self):
        self.year_high = 2769.65
        self.year_low = 2172.05
        self.mkt_cap = 559272
        self.expenses = 47237
        self.netprofit = 10282
        self.roce = 27.2
        self.equity = 235
        self.reserve = 50983
        self.EPS = 43.74
        self.PERatio = 54.4
        self.bookvalue = 218
        self.PBRatio = 10.9
        self.dividend_yield = 1.77
        self.facevalue = 1
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 12.67
        self.institution = 13.21
        self.promoter = 61.9
        self.public = 12.19
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class ICICIBANK:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\ICICIBANK.NS.csv')
        return df

    def current_price(self):
        price = 1132
        return price

    def NSE_symbol(self):
        symbol = 'ICICIBANK'
        return symbol

    def value_parameters(self):
        self.year_high = 1169.55
        self.year_low = 899
        self.mkt_cap = 793574
        self.expenses = 101495
        self.netprofit = 46081
        self.roce = 8.37
        self.equity = 1397
        self.reserve = 213101
        self.EPS = 63.02
        self.PERatio = 17.9
        self.bookvalue = 307
        self.PBRatio = 3.68
        self.dividend_yield = 0.71
        self.facevalue = 2
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 44.77
        self.institution = 45.10
        self.promoter = 0
        self.public = 9.84
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class INDUSINDBK:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\INDUSINDBK.NS.csv')
        return df

    def current_price(self):
        price = 1453
        return price

    def NSE_symbol(self):
        symbol = 'INDUSINDBK'
        return symbol

    def value_parameters(self):
        self.year_high = 1694.5
        self.year_low = 1087
        self.mkt_cap = 112996
        self.expenses = 18062
        self.netprofit = 8950
        self.roce = 8.42
        self.equity = 776
        self.reserve = 538846
        self.EPS = 114.99
        self.PERatio = 12.6
        self.bookvalue = 704
        self.PBRatio = 2.06
        self.dividend_yield = 0.96
        self.facevalue = 10
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 40.25
        self.institution = 28.09
        self.promoter = 16.4
        self.public = 14.9
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class INFY:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\INFY.NS.csv')
        return df

    def current_price(self):
        price = 1441
        return price

    def NSE_symbol(self):
        symbol = 'INFY'
        return symbol

    def value_parameters(self):
        self.year_high = 1733
        self.year_low = 1239.05
        self.mkt_cap = 598161
        self.expenses = 117245
        self.netprofit = 26248
        self.roce = 40
        self.equity = 2071
        self.reserve = 86045
        self.EPS = 63.2
        self.PERatio = 23
        self.bookvalue = 212
        self.PBRatio = 6.79
        self.dividend_yield = 2.64
        self.facevalue = 5
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 34.11
        self.institution = 35.62
        self.promoter = 14.71
        self.public = 15.06
        self.others = 0.29
        return self.foreign, self.institution, self.promoter, self.public, self.others

class ITC:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\ITC.NS.csv')
        return df

    def current_price(self):
        price = 440
        return price

    def NSE_symbol(self):
        symbol = 'ITC'
        return symbol

    def value_parameters(self):
        self.year_high = 499.7
        self.year_low = 399.35
        self.mkt_cap = 549954
        self.expenses = 44341
        self.netprofit = 20803
        self.equity = 1247
        self.reserve = 67852
        self.EPS = 16.47
        self.roce = 39
        self.PERatio = 26.9
        self.bookvalue = 55.4
        self.PBRatio = 7.95
        self.dividend_yield = 2.9
        self.facevalue = 1
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 40.95
        self.institution = 43.76
        self.promoter = 0
        self.public = 15.23
        self.others = 0.04
        return self.foreign, self.institution, self.promoter, self.public, self.others

class JSWSTEEL:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\JSWSTEEL.NS.csv')
        return df

    def current_price(self):
        price = 857
        return price

    def NSE_symbol(self):
        symbol = 'JSWSTEEL'
        return symbol

    def value_parameters(self):
        self.year_high = 914
        self.year_low = 681.05
        self.mkt_cap = 209828
        self.expenses = 145730
        self.netprofit = 11392
        self.roce = 8.33
        self.equity = 305
        self.reserve = 73653
        self.EPS = 46
        self.PERatio = 19.4
        self.bookvalue = 302
        self.PBRatio = 2.83
        self.dividend_yield = 0.4
        self.facevalue = 1
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce,self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 26.06
        self.institution = 9.81
        self.promoter = 44.81
        self.public = 18.44
        self.others = 0.37
        return self.foreign, self.institution, self.promoter, self.public, self.others

class KOTAKBANK:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\KOTAKBANK.NS.csv')
        return df

    def current_price(self):
        price = 1644
        return price

    def NSE_symbol(self):
        symbol = 'KOTAKBANK'
        return symbol

    def value_parameters(self):
        self.year_high = 2064.4
        self.year_low = 1543.85
        self.mkt_cap = 326704
        self.expenses = 47843
        self.netprofit = 18213
        self.roce = 8.75
        self.equity = 953
        self.reserve = 49535
        self.EPS = 91.62
        self.PERatio = 17.9
        self.bookvalue = 563
        self.PBRatio = 2.92
        self.dividend_yield = 0.09
        self.facevalue = 5
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue


    def shareholding_pattern(self):
        self.foreign = 37.59
        self.institution = 23.4
        self.promoter = 25.9
        self.public = 13.11
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class LT:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\LT.NS.csv')
        return df

    def current_price(self):
        price = 3428
        return price

    def NSE_symbol(self):
        symbol = 'LT'
        return symbol

    def value_parameters(self):
        self.year_high = 3860
        self.year_low = 2168.5
        self.mkt_cap = 471365
        self.expenses = 212369
        self.netprofit = 14993
        self.roce = 11.6
        self.equity = 275
        self.reserve = 78137
        self.EPS = 91
        self.PERatio = 37.3
        self.bookvalue = 570
        self.PBRatio = 6.01
        self.dividend_yield = 0.7
        self.facevalue = 2
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 24.36
        self.institution = 38.08
        self.promoter = 0
        self.public = 37.33
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class MnM:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\M&M-BL.NS.csv')
        return df

    def current_price(self):
        price = 2192
        return price

    def NSE_symbol(self):
        symbol = 'M&M'
        return symbol

    def value_parameters(self):
        self.year_high = 2240
        self.year_low = 1213.7
        self.mkt_cap = 272550
        self.expenses = 112222
        self.netprofit = 12143
        self.roce = 12.7
        self.equity = 557
        self.reserve = 59929
        self.EPS = 89.67
        self.PERatio = 24.5
        self.bookvalue = 486
        self.PBRatio = 4.51
        self.dividend_yield = 0.74
        self.facevalue = 5
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 41.75
        self.institution = 26.13
        self.promoter = 18.58
        self.public = 9.7
        self.others = 3.75
        return self.foreign, self.institution, self.promoter, self.public, self.others

class MARUTI:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\MARUTI.NS.csv')
        return df

    def current_price(self):
        price = 12364
        return price

    def NSE_symbol(self):
        symbol = 'MARUTI'
        return symbol

    def value_parameters(self):
        self.year_high = 13073.95
        self.year_low = 8960
        self.mkt_cap = 388921
        self.expenses = 12332
        self.netprofit = 13488
        self.roce = 23.7
        self.equity = 157
        self.reserve = 85479
        self.EPS = 429.01
        self.PERatio = 28.8
        self.bookvalue = 2724
        self.PBRatio = 4.54
        self.dividend_yield = 0.73
        self.facevalue = 5
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 19.64
        self.institution = 18.86
        self.promoter = 58.19
        self.public = 3.24
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class NESTLEIND:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\NESTLEIND.NS.csv')
        return df

    def current_price(self):
        price = 2509
        return price

    def NSE_symbol(self):
        symbol = 'NESTLEIND'
        return symbol

    def value_parameters(self):
        self.year_high = 1065.6
        self.year_low = 478.1
        self.mkt_cap = 241814
        self.expenses = 14839
        self.netprofit = 3196
        self.roce = 153
        self.equity = 96
        self.reserve = 1822
        self.EPS = 33.15
        self.PERatio = 75.8
        self.bookvalue = 34.6
        self.PBRatio = 72.4
        self.dividend_yield = 0.67
        self.facevalue = 1
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 12.1
        self.institution = 9
        self.promoter = 62.76
        self.public = 16.14
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class NTPC:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\NTPC.NS.csv')
        return df

    def current_price(self):
        price = 349
        return price

    def NSE_symbol(self):
        symbol = 'NTPC'
        return symbol

    def value_parameters(self):
        self.year_high = 380.4
        self.year_low = 171.85  
        self.mkt_cap = 338701
        self.expenses = 126736
        self.netprofit = 19714
        self.roce = 9.83
        self.equity = 9697
        self.reserve = 1413980
        self.EPS = 20.12
        self.PERatio = 17.4
        self.bookvalue = 158
        self.PBRatio = 2.2
        self.dividend_yield = 2.08
        self.facevalue = 10
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 17.86
        self.institution = 27.55
        self.promoter = 51.1
        self.public = 3.37
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class ONGC:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\ONGC.NS.csv')
        return df

    def current_price(self):
        price = 274
        return price

    def NSE_symbol(self):
        symbol = 'ONGC'
        return symbol

    def value_parameters(self):
        self.year_high = 292.95
        self.year_low = 150.05
        self.mkt_cap = 344380
        self.expenses = 542473
        self.netprofit = 50386
        self.roce = 13.9
        self.equity = 6290
        self.reserve = 303337
        self.EPS = 33.33
        self.PERatio = 7.51
        self.bookvalue = 246
        self.PBRatio = 1.11
        self.dividend_yield = 4.11
        self.facevalue = 5
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce , self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 8.88
        self.institution = 18.88
        self.promoter = 58.89
        self.public = 3.05
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class POWERGRID:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\POWERGRID.NS.csv')
        return df

    def current_price(self):
        price = 295
        return price

    def NSE_symbol(self):
        symbol = 'POWERGRID'
        return symbol

    def value_parameters(self):
        self.year_high = 317.25
        self.year_low = 172.50
        self.mkt_cap = 274556
        self.expenses = 6081
        self.netprofit = 15730
        self.roce = 13.1
        self.equity = 9301
        self.reserve = 77585
        self.EPS = 16.92
        self.PERatio = 17.4
        self.bookvalue = 93.4
        self.PBRatio = 3.16
        self.dividend_yield = 3.75
        self.facevalue = 10
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 29.82
        self.institution = 15.26
        self.promoter = 51.34
        self.public = 3.58
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class RELIANCE:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\RELIANCE.NS.csv')
        return df

    def current_price(self):
        price = 2803
        return price

    def NSE_symbol(self):
        symbol = 'RELIANCE'
        return symbol

    def value_parameters(self):
        self.year_high = 3024.9
        self.year_low = 2220.3
        self.mkt_cap = 1896422
        self.expenses = 738831
        self.netprofit = 79020
        self.roce = 10
        self.equity = 6766
        self.reserve = 786715
        self.EPS = 102.9
        self.PERatio = 27.2
        self.bookvalue = 1173
        self.PBRatio = 2.39
        self.dividend_yield = 0.32
        self.facevalue = 10
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 22.06
        self.institution = 16.98
        self.promoter = 50.31
        self.public = 10.46
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class SBIN:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\SBIN.NS.csv')
        return df

    def current_price(self):
        price = 802
        return price

    def NSE_symbol(self):
        symbol = 'SBIN'
        return symbol

    def value_parameters(self):
        self.year_high = 836.2
        self.year_low = 543.2
        self.mkt_cap = 715665
        self.expenses = 231046
        self.netprofit = 66109
        self.roce = 5.2
        self.equity = 892
        self.reserve = 358039
        self.EPS = 71.48
        self.PERatio = 10.4
        self.bookvalue = 402
        self.PBRatio = 1.99
        self.dividend_yield = 1.41
        self.facevalue = 1
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 11.09
        self.institution = 23.96
        self.promoter = 57.54
        self.public = 7.37
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class SBILIFE:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\SBILIFE.NS.csv')
        return df

    def current_price(self):
        price = 1450
        return price

    def NSE_symbol(self):
        symbol = 'SBILIFE'
        return symbol

    def value_parameters(self):
        self.year_high = 1569.4
        self.year_low = 1142.55
        self.mkt_cap = 145228
        self.expenses = 131588
        self.netprofit = 1894
        self.roce = 14.9
        self.equity = 1001
        self.reserve = 13907
        self.EPS = 18.91
        self.PERatio = 76.7
        self.bookvalue = 149
        self.PBRatio = 9.74
        self.dividend_yield = 0.19
        self.facevalue = 10
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 25.16
        self.institution = 15.4
        self.promoter = 55.42
        self.public = 4.01
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class SHREECEM:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\SHREECEM.NS.csv')
        return df

    def current_price(self):
        price = 25396
        return price

    def NSE_symbol(self):
        symbol = 'SHREECEM'
        return symbol

    def value_parameters(self):
        self.year_high = 30737.75
        self.year_low = 22605.6
        self.mkt_cap = 91629
        self.expenses = 15341
        self.netprofit = 2353
        self.roce = 8.99
        self.equity = 36
        self.reserve = 19135
        self.EPS = 652.13
        self.PERatio = 38.9
        self.bookvalue = 5313
        self.PBRatio = 4.78
        self.dividend_yield = 0.39
        self.facevalue = 10
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 12.47
        self.institution = 12.14
        self.promoter = 62.56
        self.public = 12.64
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class SUNPHARMA:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\SUNPHARMA.NS.csv')
        return df

    def current_price(self):
        price = 1515
        return price

    def NSE_symbol(self):
        symbol = 'SUNPHARMA'
        return symbol

    def value_parameters(self):
        self.year_high = 1638.85
        self.year_low = 922.45
        self.mkt_cap =  363583
        self.expenses = 34655
        self.netprofit = 8934
        self.roce = 16.4
        self.equity = 240
        self.reserve = 59586
        self.EPS = 37.12
        self.PERatio = 38.8
        self.bookvalue = 249
        self.PBRatio = 6.08
        self.dividend_yield = 0.76
        self.facevalue = 1
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 17.72
        self.institution = 18.71
        self.promoter = 54.48
        self.public = 8.97
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class TCS:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\TCS.NS.csv')
        return df

    def current_price(self):
        price = 3979
        return price

    def NSE_symbol(self):
        symbol = 'TCS'
        return symbol

    def value_parameters(self):
        self.year_high = 4254.75
        self.year_low = 3156
        self.mkt_cap = 1439619
        self.expenses = 176597
        self.netprofit = 46099
        self.roce = 64.3
        self.equity = 362
        self.reserve = 90127
        self.EPS = 126.88
        self.PERatio = 30.9
        self.bookvalue = 250
        self.PBRatio = 15.9
        self.dividend_yield = 1.38
        self.facevalue = 1
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 12.7
        self.institution = 10.61
        self.promoter = 71.77
        self.public = 4.86
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class TATACONSUM:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\TATACONSUM.NS.csv')
        return df

    def current_price(self):
        price = 1099
        return price

    def NSE_symbol(self):
        symbol = 'TATACONSUM'
        return symbol

    def value_parameters(self):
        self.year_high = 1269
        self.year_low = 756.45
        self.mkt_cap = 104755
        self.expenses = 12922
        self.netprofit =1215
        self.roce = 10.9
        self.equity = 95
        self.reserve = 15962
        self.EPS = 12.07
        self.PERatio = 76.2
        self.bookvalue = 169
        self.PBRatio = 6.52
        self.dividend_yield = 0.77
        self.facevalue = 1
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 25.46
        self.institution = 17.39
        self.promoter = 33.55
        self.public = 23.58
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class TATAMOTORS:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\TATAMOTORS.NS.csv')
        return df

    def current_price(self):
        price = 989
        return price

    def NSE_symbol(self):
        symbol = 'TATAMOTORS'
        return symbol

    def value_parameters(self):
        self.year_high = 1065.6
        self.year_low = 478.1
        self.mkt_cap = 362241
        self.expenses = 368356
        self.netprofit = 19774
        self.roce = 5.95
        self.equity = 766
        self.reserve = 52877
        self.EPS = 58.39
        self.PERatio = 18
        self.bookvalue = 161
        self.PBRatio = 6.12
        self.dividend_yield = 0.2
        self.facevalue = 2
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 19.2
        self.institution = 16.01
        self.promoter = 46.36
        self.public = 18.31
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class TATASTEEL:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\TATASTEEL.NS.csv')
        return df

    def current_price(self):
        price = 164
        return price

    def NSE_symbol(self):
        symbol = 'TATASTEEL'
        return symbol

    def value_parameters(self):
        self.year_high = 170.75
        self.year_low = 104.05
        self.mkt_cap = 205042
        self.expenses = 233445
        self.netprofit = -3898
        self.roce = 12.6
        self.equity = 1221
        self.reserve = 87976
        self.EPS = -2.74
        self.PERatio = 106
        self.bookvalue = 72.5
        self.PBRatio = 2.26
        self.dividend_yield = 2.19
        self.facevalue = 1
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 19.61
        self.institution = 23.51
        self.promoter = 33.19
        self.public = 23.52
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class TECHM:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\TECHM.NS.csv')
        return df

    def current_price(self):
        price = 1292
        return price

    def NSE_symbol(self):
        symbol = 'TECHM'
        return symbol

    def value_parameters(self):
        self.year_high = 1416.3
        self.year_low = 1034.05
        self.mkt_cap = 126247
        self.expenses = 47489
        self.netprofit = 2397
        self.roce = 11.9
        self.equity = 441
        self.reserve = 26228
        self.EPS = 24.14
        self.PERatio = 53.5
        self.bookvalue = 273
        self.PBRatio = 4.73
        self.dividend_yield = 2.48
        self.facevalue = 5
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 24.15
        self.institution = 29.42
        self.promoter = 35.08
        self.public = 11.16
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class TITAN:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\TITAN.NS.csv')
        return df

    def current_price(self):
        price = 3271
        return price

    def NSE_symbol(self):
        symbol = 'TITAN'
        return symbol

    def value_parameters(self):
        self.year_high = 3886.95
        self.year_low = 2670
        self.mkt_cap = 290386
        self.expenses = 45792
        self.netprofit = 3496
        self.roce = 22.7
        self.equity = 89
        self.reserve = 9304
        self.EPS = 39.38
        self.PERatio = 83.1
        self.bookvalue = 106
        self.PBRatio = 30.9
        self.dividend_yield = 0.31
        self.facevalue = 1
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 19.01
        self.institution = 10.29
        self.promoter = 52.9
        self.public = 17.57
        self.others = 0.08
        return self.foreign, self.institution, self.promoter, self.public, self.others

class ULTRACEMCO:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\ULTRACEMCO.NS.csv')
        return df

    def current_price(self):
        price = 9682
        return price

    def NSE_symbol(self):
        symbol = 'ULTRACEMCO'
        return symbol

    def value_parameters(self):
        self.year_high = 10526
        self.year_low = 7585.1
        self.mkt_cap = 279528
        self.expenses = 57940
        self.netprofit = 7004
        self.roce = 15.3
        self.equity = 289
        self.reserve = 59939
        self.EPS = 242.65
        self.PERatio = 39.6
        self.bookvalue = 2086
        self.PBRatio = 4.64
        self.dividend_yield = 0.39
        self.facevalue = 10
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 17.74
        self.institution = 14.14
        self.promoter = 59.96
        self.public = 7.92
        self.others = 0.17
        return self.foreign, self.institution, self.promoter, self.public, self.others

class UBL:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\UBL.NS.csv')
        return df

    def current_price(self):
        price = 2005
        return price

    def NSE_symbol(self):
        symbol = 'UBL'
        return symbol

    def value_parameters(self):
        self.year_high = 2106
        self.year_low = 1373
        self.mkt_cap = 53019
        self.expenses = 7426
        self.netprofit = 411
        self.roce = 13.5
        self.equity = 26
        self.reserve = 4152
        self.EPS = 15.51
        self.PERatio = 129
        self.bookvalue = 158
        self.PBRatio = 12.7
        self.dividend_yield = 0.37
        self.facevalue = 1
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 6.63
        self.institution = 6.12
        self.promoter = 70.84
        self.public = 5.25
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class WIPRO:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\WIPRO.NS.csv')
        return df

    def current_price(self):
        price = 464
        return price

    def NSE_symbol(self):
        symbol = 'WIPRO'
        return symbol

    def value_parameters(self):
        self.year_high = 545.9
        self.year_low = 375.05
        self.mkt_cap = 242489
        self.expenses = 73008
        self.netprofit = 11112
        self.roce = 17.2
        self.equity = 1045
        self.reserve = 73488
        self.EPS = 21.14
        self.PERatio = 22
        self.bookvalue = 143
        self.PBRatio = 3.25
        self.dividend_yield = 0.22
        self.facevalue = 2
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 6.96
        self.institution = 8.28
        self.promoter = 72.89
        self.public = 1.76
        self.others = 0.11
        return self.foreign, self.institution, self.promoter, self.public, self.others

class ZEEL:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\ZEEL.NS.csv')
        return df

    def current_price(self):
        price = 134
        return price

    def NSE_symbol(self):
        symbol = 'ZEEL'
        return symbol

    def value_parameters(self):
        self.year_high = 299.7
        self.year_low = 132.5
        self.mkt_cap = 12842
        self.expenses = 8579
        self.netprofit = -68
        self.roce = 7.94
        self.equity = 96
        self.reserve = 10694
        self.EPS = -0.71
        self.PERatio = 59
        self.bookvalue = 112
        self.PBRatio = 1.19
        self.dividend_yield = 0
        self.facevalue = 1
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 19.18
        self.institution = 35.3
        self.promoter = 3.99
        self.public = 41.38
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others

class ADANIGREEN:
    def historical_data(self):
        df = pd.read_csv(r'Stocks historical data\ADANIGREEN.NS.csv')
        return df

    def current_price(self):
        price = 1726
        return price

    def NSE_symbol(self):
        symbol = 'ADANIGREEN'
        return symbol

    def value_parameters(self):
        self.year_high = 2018.95
        self.year_low = 815.55
        self.mkt_cap = 273404
        self.expenses = 1923
        self.netprofit = 1260
        self.roce = 9.22
        self.equity = 1584
        self.reserve = 8250
        self.EPS = 6.94
        self.PERatio = 219
        self.bookvalue = 62.1
        self.PBRatio = 27.8
        self.dividend_yield = 0
        self.facevalue = 10
        return self.year_high, self.year_low, self.mkt_cap, self.expenses, self.netprofit, self.roce, self.equity, self.reserve, self.EPS, self.PERatio, self.bookvalue, self.PBRatio, self.dividend_yield, self.facevalue

    def shareholding_pattern(self):
        self.foreign = 18.15
        self.institution = 1.55
        self.promoter = 56.37
        self.public = 23.93
        self.others = 0
        return self.foreign, self.institution, self.promoter, self.public, self.others


def main():
    sd = stocks_dictionary()
    sym = sd.symbols()
    print(sym['Asian Paints Ltd'])
    ADP = 'ADANIPORTS'
    adp = ADANIPORTS()
    print(adp.stats())


if __name__ == '__main__':
    main()