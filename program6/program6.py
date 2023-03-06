"""
    Name: James Michael Crespo
    Email: james.crespo64@myhunter.cuny.edu
    Resources:  Internet
"""
import pandas as pd
import numpy as np
import datetime as dt
import pickle as pkl
import sklearn as sk


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
    return df


def fit_linear_regression(x_train, y_train):
    return 0


def predict_using_trained_model(mod_pkl, xes, yes):
    return 0, 1


def main():
    """test"""
    df = import_data("program6/taxi_jfk_june2020.csv")
    df = add_tip_time_features(df)
    print(df[['trip_distance', 'duration', 'dayofweek',
          'total_amount', 'percent_tip']].head())

    print(df[['passenger_count', 'trip_distance']].head(10))
    df = impute_numeric_cols(df)
    print(df[['passenger_count', 'trip_distance']].head(10))

    df = add_boro(df, 'program6/taxi_zones.csv')
    print('\nThe locations and borough columns:')
    print(f"{df[['PULocationID','PU_borough','DOLocationID','DO_borough']]}")

    df_do = encode_categorical_col(df['DO_borough'], 'DO_')
    print(df_do.head())


if __name__ == "__main__":
    main()
