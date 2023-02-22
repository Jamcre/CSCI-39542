"""
    Name: James Michael Crespo
    Email: james.crespo64@myhunter.cuny.edu
    Resources:  Internet
"""
import pandas as pd


def parse_datetime(df, column='DATE'):
    """
    creates 3 columns in df, 'timestamp' with date in YYYY-MM-DD format,
    'month' with numeric month value,
    'year' with year value

    :param df: a dataframe contatining column 'column'
    :param column: name of a column, default value of 'DATE'
    """
    df['timestamp'] = pd.to_datetime(df[column])
    df['month'] = pd.to_datetime(df[column]).dt.month
    df['year'] = pd.to_datetime(df[column]).dt.year
    return df


def compute_lin_reg(xes, yes):
    return 0, 1


def predict(xes, theta_0, theta_1):
    return 0, 1


def mse_loss(y_actual, y_estimate):
    return 0


def rmse_loss(y_actual, y_estimate):
    return 0


def compute_error(y_actual, y_estimate, loss_fnc=mse_loss):
    return 0


def compute_ytd(df):
    return []


def compute_year_over_year(df):
    return []


def main():
    df_1yr = pd.read_csv('program5/fred_info_2022_1yr.csv')
    df_1yr = parse_datetime(df_1yr)
    print(df_1yr)


if __name__ == "__main__":
    main()
