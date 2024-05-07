
import pandas as pd, numpy as np

from sklearn.preprocessing import MinMaxScaler

from Stocks import *
import os
import math
import datetime as dt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


import matplotlib.pyplot as plt
from itertools import cycle
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

class LSTM_model:
    import tensorflow as tf
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense, Dropout
    from tensorflow.keras.layers import LSTM 

    def __init__(self, df):
        self.df = df
        self.closeddf = [[]]
    def data_prepation(self):
        # if not df.isnull().values.any():

        self.df = self.df.drop(self.df[['Adj Close', 'Volume']], axis=1)
        self.df = self.df.dropna(thresh=2)

        self.closeddf = self.df.drop(self.df[['Open', 'High', 'Low']], axis=1)
        # if not df.isnull().values.any():
        
        return self.closeddf

    def create_dataset(self, dataset, time_step=1):
        dataX, dataY = [], []
        for i in range(len(dataset)-time_step-1):
            a = dataset[i:(i+time_step), 0]
            dataX.append(a)
            dataY.append(dataset[i + time_step, 0])
        return np.array(dataX), np.array(dataY)

    def prediction(self):
        closed_value = self.closeddf['Close']
        scaler = MinMaxScaler(feature_range=(0,1))
        closed_value = scaler.fit_transform(np.array(closed_value).reshape(-1,1))

        training_size = int(len(closed_value)*0.80)
        test_size = len(closed_value)-training_size
        train_data, test_data = closed_value[0:training_size,:], closed_value[training_size:len(closed_value), :1]

        time_step = 15
        X_train, y_train = self.create_dataset(train_data, time_step)
        X_test, y_test = self.create_dataset(test_data, time_step)

        X_train = X_train.reshape((X_train.shape[0], X_train.shape[1], 1))
        X_test = X_test.reshape(X_test.shape[0], X_test.shape[1], 1)
        model = tf.keras.models.Sequential()
        dense = tf.keras.layers.Dense()
        dropout = tf.keras.layers.Dropout()
        LSTM = tf.keras.layers.LSTM()

        model.add(LSTM(10, input_shape=(None, 1), activation="relu"))
        model.add(dense(1))
        model.compile(loss = "mean_squared_error", optimizer = "adam")

        history = model.fit(X_train, y_train, validation_data = (X_test, y_test), epochs = 200, batch_size = 32, verbose = 1)

        loss = history.history['loss']
        val_loss = history.history['val_loss']

        epochs = range(len(loss))

        plt.plot(epochs, loss, 'r', label='Training loss')
        plt.plot(epochs, val_loss, 'b', label='Validation loss')
        plt.title('Training and validation loss')
        plt.legend(loc=0)
        plt.figure()
        plt.show()

        train_predict=model.predict(X_train)
        test_predict=model.predict(X_test)
        train_predict.shape, test_predict.shape

        x_input=test_data[len(test_data)-time_step:].reshape(1,-1)
        temp_input=list(x_input)
        temp_input=temp_input[0].tolist()

        from numpy import array

        lst_output=[]
        n_steps=time_step
        i=0
        pred_days = 30
        while(i<pred_days):
            
            if(len(temp_input)>time_step):
                
                x_input=np.array(temp_input[1:])
                #print("{} day input {}".format(i,x_input))
                x_input = x_input.reshape(1,-1)
                x_input = x_input.reshape((1, n_steps, 1))
                
                yhat = model.predict(x_input, verbose=0)
                #print("{} day output {}".format(i,yhat))
                temp_input.extend(yhat[0].tolist())
                temp_input=temp_input[1:]
                #print(temp_input)
            
                lst_output.extend(yhat.tolist())
                i=i+1
                
            else:
                
                x_input = x_input.reshape((1, n_steps,1))
                yhat = model.predict(x_input, verbose=0)
                temp_input.extend(yhat[0].tolist())
                
                lst_output.extend(yhat.tolist())
                i=i+1
        # print("Output of predicted next days: ", len(lst_output))

        temp_mat = np.empty((len(last_days)+pred_days+1,1))
        temp_mat[:] = np.nan
        temp_mat = temp_mat.reshape(1,-1).tolist()[0]

        last_original_days_value = temp_mat
        next_predicted_days_value = temp_mat

        last_original_days_value[:time_step+1] = scaler.inverse_transform(closedf[len(closedf)-time_step:]).reshape(1,-1).tolist()[0]
        next_predicted_days_value[time_step+1:] = scaler.inverse_transform(np.array(lst_output).reshape(-1,1)).reshape(1,-1).tolist()[0]

        new_pred_plot = pd.DataFrame({
            'last_original_days_value':last_original_days_value,
            'next_predicted_days_value':next_predicted_days_value
        })

        names = cycle(['Last 15 days close price','Predicted next 30 days close price'])

        fig = px.line(new_pred_plot,x=new_pred_plot.index, y=[new_pred_plot['last_original_days_value'],
                                                            new_pred_plot['next_predicted_days_value']],
                    labels={'value': 'Stock price','index': 'Timestamp'})
        fig.update_layout(title_text='Compare last 15 days vs next 30 days',
                        plot_bgcolor='white', font_size=15, font_color='black',legend_title_text='Close Price')

        fig.for_each_trace(lambda t:  t.update(name = next(names)))
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        fig.show()

        lstmdf=closedf.tolist()
        lstmdf.extend((np.array(lst_output).reshape(-1,1)).tolist())
        lstmdf=scaler.inverse_transform(lstmdf).reshape(1,-1).tolist()[0]

        names = cycle(['Close price'])

        fig = px.line(lstmdf,labels={'value': 'Stock price','index': 'Timestamp'})
        fig.update_layout(title_text='Plotting whole closing stock price with prediction',
                        plot_bgcolor='white', font_size=15, font_color='black',legend_title_text='Stock')

        fig.for_each_trace(lambda t:  t.update(name = next(names)))

        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False)
        fig.show()





class random_forest:
    def __init__(self):
        self.df = pd.read_csv(r'Stocks Statistics\Overall_statistics_uptoCipla.csv')
    def data_prepation(self):
        self.df = self.df.drop(self.df[['DATE']], axis=1)
        self.df = self.df.dropna(thresh=2)
        return self.df
    def prediction(self, features):
        x = self.df[['PRESET Y SALES', 'NEXT Y SALES', 'EXPENSES', 'NET PROFIT', 'EPS', 'DIVIDEND PAYOUT', 'EQUITY', 'RESERVES', 'ROCE', 'PROMOTERS', 'FII', 'DII']]
        y = self.df['DECISION']

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

        rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
        rf_classifier.fit(x_train, y_train)
        y_pred = rf_classifier.predict(x_test)

        accuracy = accuracy_score(y_test, y_pred)
        print(f"Accuracy: {accuracy: .2f}")

        # print("Classification Report: ")
        # print(classification_report(y_test, y_pred))
        #
        # print("Confusion Matrix: ")
        # print(confusion_matrix(y_test, y_pred))
        pred = rf_classifier.predict([features])
        return pred[0]


def stock_data(symbol):
    match symbol:
        case 'ADANIPORTS':
            stk = ADANIPORTS()

            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()

        case 'ASIANPAINT':
            stk = ASIANPAINT()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()

        case 'AXISBANK':
            stk = AXISBANK()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'BAJAJ_AUTO':
            stk = BAJAJ_AUTO()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'BAJAJFINSV':
            stk = BAJAJFINSV()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'BAJFINANCE':
            stk = BAJFINANCE()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'BHARTIARTL':
            stk = BHARTIARTL()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'BPCL':
            stk = BPCL()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'BRITANNIA':
            stk = BRITANNIA()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'CIPLA':
            stk = CIPLA()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'COALINDIA':
            stk = COALINDIA()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'DIVISLAB':
            stk = DIVISLAB()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'DRREDDY':
            stk = DRREDDY()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'EICHERMOT':
            stk = EICHERMOT()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'GRASIM':
            stk = GRASIM()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'HCLTECH':
            stk = HCLTECH()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'HDFCBANK':
            stk = HDFCBANK()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'HDFCLIFE':
            stk = HDFCLIFE()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'HEROMOTOCO':
            stk = HEROMOTOCO()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'HINDALCO':
            stk = HINDALCO()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'HINDUNILVR':
            stk = HINDUNILVR()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'ICICIBANK':
            stk = ICICIBANK()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'INDUSINDBK':
            stk = INDUSINDBK()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'INFY':
            stk = INFY()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'ITC':
            stk = ITC()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'JSWSTEEL':
            stk = JSWSTEEL()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'KOTAKBANK':
            stk = KOTAKBANK()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'LT':
            stk = LT()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'MnM':
            stk = MnM()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'MARUTI':
            stk = MARUTI()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'NESTLEIND':
            stk = NESTLEIND()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'NTPC':
            stk = NTPC()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'ONGC':
            stk = ONGC()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'POWERGRID':
            stk = POWERGRID()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'RELIANCE':
            stk = RELIANCE()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'SBIN':
            stk = SBIN()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'SBILIFE':
            stk = SBILIFE()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'SHREECEM':
            stk = SHREECEM()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'SUNPHARMA':
            stk = SUNPHARMA()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'TCS':
            stk = TCS()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'TATACONSUM':
            stk = TATACONSUM()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'TATAMOTORS':
            stk = TATAMOTORS()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'TATASTEEL':
            stk = TATASTEEL()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'TECHM':
            stk = TECHM()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'TITAN':
            stk = TITAN()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'ULTRACEMCO':
            stk = ULTRACEMCO()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'UBL':
            stk = UBL()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'WIPRO':
            stk = WIPRO()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'ZEEL':
            stk = ZEEL()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()
        case 'ADANIGREEN':
            stk = ADANIGREEN()
            return stk.historical_data(), stk.current_price(), stk.NSE_symbol(), stk.value_parameters(), stk.shareholding_pattern()

def main():
    stk_dict = stocks_dictionary()
    symbol_dict = stk_dict.symbols()
    stk = 'Adani Ports and Special Economic Zone Ltd'
    stk_sym = symbol_dict[stk]
    hst_data, curr_prize, sym, vp, shp = stock_data(stk_sym)
    # print(vp[0])
    # lstm = LSTM_model(hst_data)
    # print(lstm.data_prepation())
    # lstm.prediction()
    
    df = pd.read_csv(r'Stocks Statistics\Overall_statistics_uptoCipla.csv')
    rf = random_forest(df)
    rf.data_prepation()
    features = [vp[2], None, vp[3], vp[4], vp[8], vp[12], vp[6], vp[7], vp[5], shp[2], shp[0], shp[1]]
    print(rf.prediction(features))



if __name__ == '__main__':
    main()