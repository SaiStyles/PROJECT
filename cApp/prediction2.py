import pandas as pd # type: ignore
from sklearn.model_selection import train_test_split# type: ignore
from sklearn.linear_model import LinearRegression# type: ignore
from sklearn.metrics import mean_squared_error# type: ignore
from pathlib import Path# type: ignore
# Load the dataset
BASE_DIR = Path(__file__).resolve().parent.parent
def main(case,year):
    crime_data = pd.read_csv(f'{BASE_DIR}/dataset/Crimes.csv')  
    
    crime = crime_data[crime_data['DISTRICT'] == 'TOTAL']
    print(crime)
    X = crime[['YEAR']]
    y = crime[case]
    print("==============================")
    print(y)
    print("==============================")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}') 

    future_year = year
    predicted_crime_rate = model.predict([[future_year]])
    res = round(predicted_crime_rate[0])
    if res < 0:
        res = 0
    result = f'Predicted crime rate for {future_year}: {res}'
    print(result)

    crime_year = crime_data[crime_data['DISTRICT'] == 'TOTAL']
    print(crime_year)
    total_cases = pd.DataFrame(crime_year.groupby(['YEAR'])[case].sum().reset_index())
    print(total_cases)



    return result, total_cases

# main("KIDNAPPING & ABDUCTION",2026)

def state_main(state,case,year):
    crime_data = pd.read_csv(f'{BASE_DIR}/dataset/Crimes.csv')  
    
    crime = crime_data[crime_data['DISTRICT'] != 'TOTAL']
    crime = crime[crime['STATE'] == state]
    print(crime)
    X = crime[['YEAR']]
    y = crime[case]
    print("==============================")
    print(y)
    print("==============================")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}') 

    future_year = year
    predicted_crime_rate = model.predict([[future_year]])
    res = round(predicted_crime_rate[0])
    if res < 0:
        res = 0
    result = f'Predicted crime rate for {future_year}: {res}'
    print(result)

    crime_year = crime_data[crime_data['DISTRICT'] == 'TOTAL']
    crime_year = crime_year[crime_year['STATE'] == state]
    print(crime_year)
    total_cases = pd.DataFrame(crime_year.groupby(['YEAR'])[case].sum().reset_index())
    print(total_cases)
    return result, total_cases

# state_main("Bihar","OTHER IPC CRIMES",2026)