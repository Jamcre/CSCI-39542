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
    r = xes.corr(yes)
    print(r)
    theta_1 = r * sd_y/sd_x
    theta_0 = yes.mean() - theta_1 * xes.mean()
    return theta_0, theta_1


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
    # parse_datetime() test
    df_1yr = pd.read_csv('program5/fred_info_2022_1yr.csv')
    df_1yr = parse_datetime(df_1yr)
    print(df_1yr)

    # visualization
    # sns.lineplot(data=df_1yr, x='month', y='USINFO')
    # plt.ylabel('Number of Jobs')
    # plt.xticks(range(1, 13),
    #            ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    # plt.title('Information Services Employment, 2022')
    # plt.show()

    # compute_line_reg() test
    theta_0, theta_1 = compute_lin_reg(df_1yr['month'], df_1yr['USINFO'])
    xes = np.array([0, 12])
    yes = theta_1*xes + theta_0


if __name__ == "__main__":
    main()
