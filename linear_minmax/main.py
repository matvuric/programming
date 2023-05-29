from datetime import date

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler


def rev_min_max_func(scaled_val, target):
    max_val = max(data[target])
    min_val = min(data[target])
    og_val = (scaled_val*(max_val - min_val)) + min_val
    return og_val


if __name__ == '__main__':
    data = pd.read_csv('web-traffic.csv', sep=';', on_bad_lines='skip')
    cols = ['users', 'visits', 'pageviews']

    # 1 задание
    df = data.groupby(data.date)[cols].sum()
    df.plot(kind='area', stacked=False, color=['b', 'r', 'y'])
    plt.xticks(rotation=23)

    # 2 задание
    data_sct = data.copy()
    data_sct['sum'] = data_sct[cols].sum(axis=1)
    df = data_sct.groupby(data_sct.date)[['sum']].sum()
    df.plot(style='.')
    plt.xticks(rotation=23)

    # 3 задание
    data_bar = data.copy()
    data_bar.date = pd.to_datetime(data_bar.date).dt.to_period('M')
    df = data_bar.groupby(data_bar.date)[cols].sum()
    df.plot(kind='bar')
    plt.xticks(rotation=23)
    plt.show()

    # 4 задание
    data_pred = data.copy()
    data_pred.date = pd.to_datetime(data_pred.date)
    data_pred.date = data_pred.date.map(date.toordinal)
    df = data_pred.groupby(data_pred.date)[['users', 'visits']].sum().reset_index()

    scaler = MinMaxScaler()
    model = LinearRegression()

    # Normalize the 'users' and 'visits' columns using the Min-Max scaler
    df[['users', 'visits']] = scaler.fit_transform(df[['users', 'visits']])

    # Create a linear regression model for the 'users' column
    model_users = LinearRegression()
    X_users = df.date.values.reshape(-1, 1)
    y_users = df.users.values.reshape(-1, 1)
    model_users.fit(X_users, y_users)

    # Create a linear regression model for the 'visits' column
    model_visits = LinearRegression()
    X_visits = df.date.values.reshape(-1, 1)
    y_visits = df.visits.values.reshape(-1, 1)
    model_visits.fit(X_visits, y_visits)

    # Define a date value to make a prediction
    new_date = '2020-10-09'

    # Normalize the new 'users' and 'visits' values using the same scaler
    new_data = df.copy()
    new_data.loc[len(new_data)] = [new_date, 0, 0]
    new_data.date = pd.to_datetime(new_data.date)
    new_data.date = new_data.date.map(date.toordinal)
    new_data[['users', 'visits']] = scaler.transform(new_data[['users', 'visits']])
    new_data = new_data.tail(1)

    # Make a prediction for the 'users' column
    new_X_users = new_data.date.values.reshape(-1, 1)
    new_prediction_users = model_users.predict(new_X_users)

    # Make a prediction for the 'visits' column
    new_X_visits = new_data.date.values.reshape(-1, 1)
    new_prediction_visits = model_visits.predict(new_X_visits)

    # Print the predictions
    print(f'Prediction for users on {new_date}: {int(rev_min_max_func(new_prediction_users[0][0], "users"))}')
    print(f'Prediction for visits on {new_date}: {int(rev_min_max_func(new_prediction_visits[0][0], "visits"))}')
