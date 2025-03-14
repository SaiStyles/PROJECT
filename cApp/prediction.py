import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from pathlib import Path
# Load the dataset
BASE_DIR = Path(__file__).resolve().parent.parent
def main_rape():
    crime_data = pd.read_csv(f'{BASE_DIR}/dataset/20_Victims_of_rape.csv')  # Replace 'crime_data.csv' with the actual file path
    # Assuming you have already preprocessed the data and created features
    # For simplicity, let's use 'year' as the only feature
    X = crime_data[['Year']]
    y = crime_data['Rape_Cases_Reported']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test data
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')

    # Predict future crime rate
    future_year = 2025  # Change this to the desired future year
    predicted_crime_rate = model.predict([[future_year]])
    res = round(predicted_crime_rate[0])
    if res < 0:
        res = 0
    print(f'Predicted crime rate for {future_year}: {res}')
    result = f'Predicted crime rate for {future_year}: {res}'
    return result

def state_rape(state='Kerala'):
    crime_data = pd.read_csv(f'{BASE_DIR}/dataset/20_Victims_of_rape.csv')  # Replace 'crime_data.csv' with the actual file path
    crime_data = crime_data[crime_data['Area_Name'] == state]
    crime_data = crime_data[crime_data['Subgroup'] == 'Victims of Incest Rape']
    # Assuming you have already preprocessed the data and created features
    # For simplicity, let's use 'year' as the only feature
    X = crime_data[['Year']]
    y = crime_data['Rape_Cases_Reported']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test data
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')

    # Predict future crime rate
    future_year = 2025  # Change this to the desired future year
    predicted_crime_rate = model.predict([[future_year]])
    res = round(predicted_crime_rate[0])
    if res < 0:
        res = 0
    print(f'Predicted crime rate for {future_year}: {res}')
    result = f'Predicted crime rate for {future_year}: {res}'
    return result

def main_murder():
    crime_data = pd.read_csv(f'{BASE_DIR}/dataset/32_Murder_victim_age_sex.csv')  # Replace 'crime_data.csv' with the actual file path
    # Assuming you have already preprocessed the data and created features
    # For simplicity, let's use 'year' as the only feature
    X = crime_data[['Year']]
    y = crime_data['Victims_Total']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test data
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')

    # Predict future crime rate
    future_year = 2025  # Change this to the desired future year
    predicted_crime_rate = model.predict([[future_year]])
    res = round(predicted_crime_rate[0])
    if res < 0:
        res = 0
    print(f'Predicted crime rate for {future_year}: {res}')
    result = f'Predicted crime rate for {future_year}: {res}'
    return result

def state_murder(state='Kerala'):
    crime_data = pd.read_csv(f'{BASE_DIR}/dataset/32_Murder_victim_age_sex.csv')  # Replace 'crime_data.csv' with the actual file path
    crime_data = crime_data[crime_data['Area_Name'] == state]
    # Assuming you have already preprocessed the data and created features
    # For simplicity, let's use 'year' as the only feature
    X = crime_data[['Year']]
    y = crime_data['Victims_Total']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test data
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')

    # Predict future crime rate
    future_year = 2025  # Change this to the desired future year
    predicted_crime_rate = model.predict([[future_year]])
    res = round(predicted_crime_rate[0])
    if res < 0:
        res = 0
    print(f'Predicted crime rate for {future_year}: {res}')
    result = f'Predicted crime rate for {future_year}: {res}'
    return result

def main_police_hr():
    crime_data = pd.read_csv(f'{BASE_DIR}/dataset/35_Human_rights_violation_by_police.csv')  # Replace 'crime_data.csv' with the actual file path
    # Assuming you have already preprocessed the data and created features
    # For simplicity, let's use 'year' as the only feature
    X = crime_data[['Year']]
    y = crime_data['Cases_Registered_under_Human_Rights_Violations']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test data
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')

    # Predict future crime rate
    future_year = 2025  # Change this to the desired future year
    predicted_crime_rate = model.predict([[future_year]])
    res = round(predicted_crime_rate[0])
    if res < 0:
        res = 0
    print(f'Predicted crime rate for {future_year}: {res}')
    result = f'Predicted crime rate for {future_year}: {res}'
    return result

def state_police_hr(state='Kerala'):
    crime_data = pd.read_csv(f'{BASE_DIR}/dataset/35_Human_rights_violation_by_police.csv')  # Replace 'crime_data.csv' with the actual file path
    crime_data = crime_data[crime_data['Area_Name'] == state]
    # Assuming you have already preprocessed the data and created features
    # For simplicity, let's use 'year' as the only feature
    X = crime_data[['Year']]
    y = crime_data['Cases_Registered_under_Human_Rights_Violations']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the linear regression model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Make predictions on the test data
    y_pred = model.predict(X_test)

    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')

    # Predict future crime rate
    future_year = 2025  # Change this to the desired future year
    predicted_crime_rate = model.predict([[future_year]])
    res = round(predicted_crime_rate[0])
    if res < 0:
        res = 0
    print(f'Predicted crime rate for {future_year}: {res}')
    result = f'Predicted crime rate for {future_year}: {res}'
    return result

main_police_hr()
state_police_hr()