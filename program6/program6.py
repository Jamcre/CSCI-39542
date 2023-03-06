"""
    Name: James Michael Crespo
    Email: james.crespo64@myhunter.cuny.edu
    Resources:  Internet
"""
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def import_data(file_name):
    """
    reads file into dataframe, drops the columns in the list,
    and drops rows with non-positive 'total_amount' values

    :param file_name: name of csv file containing data from OpenData NYC
    """
    df = pd.read_csv(file_name)
    drop_lst = ['VendorID', 'RatecodeID', 'store_and_fwd_flag', 'payment_type',
                'extra', 'mta_tax', 'tolls_amount', 'improvement_surcharge', 'congestion_surcharge']
    df = df.drop(drop_lst, axis=1)
    df = df[df['total_amount'] > 0]
    return df


def add_tip_time_features(df):
    """
    computes 3 new columns, percent_tip = 100 * tip_ammount/(total_amount-tip_amount)
    duration = time of trip in seconds, dayofweek = day of week represented as 0 to 6

    :param df: a Dataframe contianing Yellow Taxi Trip Data
    """
    df['percent_tip'] = 100 * df['tip_amount'] / \
        (df['total_amount']-df['tip_amount'])
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])
    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])

    df['duration'] = (df['tpep_dropoff_datetime'] -
                      df['tpep_pickup_datetime']).dt.total_seconds()
    df['dayofweek'] = df['tpep_pickup_datetime'].dt.dayofweek
    return df


def impute_numeric_cols(df):
    """
    Missing data in the numeric columns, are replaced with respective column's median

    :param df: a df containing Yellow Taxi Trip Data from OpenDataN NYC
    """
    medians = df[['passenger_count', 'trip_distance', 'fare_amount',
                  'tip_amount', 'total_amount', 'duration', 'dayofweek']].median()
    df = df.fillna(value=medians)
    return df


def add_boro(df, file_name) -> pd.DataFrame:
    """
    creates a df from file_name, and creates 2 new columns in param_df using info from new_df

    :param df: df containing Yellow Taxi trip data from NYC OpenData
    :param file_name: name of csv file for Taxi Zones from NYC OpenData
    """
    temp_df = pd.read_csv(file_name)
    id_and_borough = dict(zip(temp_df['LocationID'], temp_df['borough']))
    df['PU_borough'] = df['PULocationID'].map(id_and_borough)
    df['DO_borough'] = df['DOLocationID'].map(id_and_borough)
    return df.reset_index(drop=True)


def encode_categorical_col(col, prefix):
    """
    Too much to explain, just run it and look at what is returned

    :param col: a column of categorical data
    :param prefix: a prefix to use for the labels of the resulting columns
    """
    # Encoded df
    df = pd.get_dummies(col, prefix=prefix, prefix_sep='')
    # Sort colums alphabetically
    df = df.sort_index(axis=1)
    # return df with last col dropped
    return df.iloc[:, :-1]


def split_test_train(df, xes_col_names, y_col_name, test_size=0.25, random_state=1870):
    """
    uses sklearn train_test_split function to split data into a training and test subset.
    remaining subsets are returned, x_train, x_test, y_train, y_test

    :param df: df of NYC Yellow Tax Trip Data from OpenData NYC to which add_boro() has been used
    :param xes_col_names: list of columns that contain independent variables
    :param y_col_name: name of the column of dependent variables
    :param test_size: accepts float(0 to 1), is proportion of data for training. default = 0.25
    :param random_state: Used as seed for randomization. default = 1870
    """
    x_data = df[xes_col_names]
    y_data = df[y_col_name]
    x_train, x_test, y_train, y_test = train_test_split(
        x_data, y_data, test_size=test_size, random_state=random_state)
    return x_train, x_test, y_train, y_test


def fit_linear_regression(x_train, y_train):
    """
    Fits a linear model to x_train and y_train, using sklearn.linear_model.LinearRegression.
    The resulting model should be returned as bytestream, using pickle (see Lecture 4).

    :param x_train: an array of numeric columns with no null values.
    :param y_train: an array of numeric columns with no null values.
    """
    model = LinearRegression().fit(x_train, y_train)
    return pickle.dumps(model)


def predict_using_trained_model(mod_pkl, xes, yes):
    """
    Computes and returns the mean squared error and r2 score,
    between the values predicted by the model (mod_pkl on x) and the actual values (y).
    sklearn.metrics contains two functions that may be of use: mean_squared_error and r2_score.


    :param mod_pkl: a trained model for the data, stored in pickle format.
    :param xes: an array or DataFrame of numeric columns with no null values.
    :param yes: an array or DataFrame of numeric columns with no null values.
    """
    model = pickle.loads(mod_pkl)
    y_pred = model.predict(xes)
    mse = mean_squared_error(yes, y_pred)
    r2_val = r2_score(yes, y_pred)

    return mse, r2_val


def main():
    """test, deleted because didn't want to deal with pylint for submissions"""


if __name__ == "__main__":
    main()
