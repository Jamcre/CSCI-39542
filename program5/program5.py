"""
    Name: James Michael Crespo
    Email: james.crespo64@myhunter.cuny.edu
    Resources:  Internet
"""
import pandas as pd
import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt


def parse_datetime(df, column='DATE'):
    """
    creates 3 columns in df, 'timestamp' with date in YYYY-MM-DD format,
    'month' with numeric month value,
    'year' with year value, returns new df

    :param df: a dataframe contatining column 'column'
    :param column: name of a column, default value of 'DATE'
    """
    df['timestamp'] = pd.to_datetime(df[column])
    df['month'] = pd.to_datetime(df[column]).dt.month
    df['year'] = pd.to_datetime(df[column]).dt.year
    return df


def compute_lin_reg(xes, yes):
    """
    computes the slope and y-intercept of linear regression line,
    using ordinary least squares

    :param xes: iterables of numeric values representing independent variable
    :param yes: iterables of numeric values representing dependent variable
    """
    sd_x = np.std(xes)
    sd_y = np.std(yes)
    r_val = xes.corr(yes)
    print(r_val)
    theta_1 = r_val * sd_y/sd_x
    theta_0 = yes.mean() - theta_1 * xes.mean()
    return theta_0, theta_1


def predict(xes, theta_0, theta_1):
    """
    returns the predicted values of the dependent variable xes,
    under the linear regression sodel with y-intercept theta_0 and slope theta_1

    :param xes: an iterables of numeric values representing the independent variable
    :param theta_0: the y-intercept of the linear regression model
    :param theta_1: the slope of the linear regression model
    """
    lst = []
    for x_val in xes:
        lst.append(theta_0 + theta_1 * x_val)
    return lst


def mse_loss(y_actual, y_estimate):
    """
    computes and returns the Mean Squared Error of 'y_actual' and 'y_estimate'

    :param y_actual: a Series containing numeric values
    :param y_estimate: a Series containing numeric values
    """
    return pow((y_actual-y_estimate), 2).mean()


def rmse_loss(y_actual, y_estimate):
    """
    computes and returns square root of the Mean Squared Error of 'y_actual' and 'y_estimate'

    :param y_actual: a Series containing numeric values
    :param y_estimate: a Series containing numeric values
    """
    mse_value = mse_loss(y_actual, y_estimate)
    return pow(mse_value, 0.5)


def compute_error(y_actual, y_estimate, loss_fnc=mse_loss):
    """
    :param y_actual: a Series containing numeric values
    :param y_estimate: a Series containing numeric values
    :param loss_fnc=mse_loss: function that takes numeric series as input paramters
                              , and returns amumeric value. Default equal mse_loss
    """
    return loss_fnc(y_actual, y_estimate)


def compute_ytd(df):
    """
    returns a Series with the number of jobs since the beginning of the year for that entry.
    Ex: for the January 2022 row, the number would be 0 since January is the beginning of the year.
    For July 2022, the number is difference between 'USINFO' for July and 'USINFO' for January.

    :param df: Dataframe contatining columns 'month', 'year', and 'USINFO'
    """
    # create loop to iterate through entire df
    # get 'USINFO' value of current row
    # get 'USINFO' value of row where 'month' = 1 and year = current_row.year
    # find the difference between current 'USINFO' value and 'USINFO' beginning of year value
    # append to list

    curr_row_jobs = 0
    start_year_jobs = 0
    result_lst = []
    for index, row in df.iterrows():
        curr_row_jobs = row['USINFO']
        start_year_jobs = df.loc[(df['year'] == row['year']) & (
            df['month'] == 1), 'USINFO'].iloc[0]
        result_lst.append(curr_row_jobs - start_year_jobs)
    return pd.Series(result_lst)


def compute_year_over_year(df):
    """
    returns a Series with the percent change from previous year 'USINFO'.
    You can assume that the DataFrame is ordered by date, with earlier dates coming first in the DF

    :param df: Dataframe containing columns 'month', 'year', and 'USINFO'
    """
    return df['USINFO'].pct_change(periods=12) * 100


def main():
    """
    test functions
    """
    # parse_datetime() test
    df_1yr = pd.read_csv('program5/fred_info_2022_1yr.csv')
    df_1yr = parse_datetime(df_1yr)
    print(df_1yr)

    # visualization
    # sns.lineplot(data=df_1yr, x='month', y='USINFO')
    # plt.ylabel('Number of Jobs')
    # plt.xticks(range(1, 13),
    #  ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    # plt.title('Information Services Employment, 2022')
    # plt.show()

    # compute_line_reg() test
    theta_0, theta_1 = compute_lin_reg(df_1yr['month'], df_1yr['USINFO'])
    xes = np.array([0, 12])
    yes = theta_1*xes + theta_0

    # predict() test
    months_2023 = np.array([13, 14, 15, 16, 17])
    print(predict(months_2023, theta_0, theta_1))

    df_5yr = pd.read_csv('program5/fred_info_2022_5yr.csv')
    df_5yr = parse_datetime(df_5yr)
    print(df_5yr[:30])
    print(df_5yr.index.to_series())

    # compute_ytd() test
    df_all = pd.read_csv('program5/fred_info_2022_1yr.csv')
    df_all = parse_datetime(df_all)
    print(df_all)
    df_all['YTD'] = compute_ytd(df_all)
    print(df_all)
    print('DONE')


if __name__ == "__main__":
    main()
