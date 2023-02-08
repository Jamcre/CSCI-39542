"""
    Name: James Michael Crespo
    Email: james.crespo64@myhunter.cuny.edu
    Resources: Internet
"""
import pandas as pd


def clean_df(df, year=2015):  # done
    """
    modifies dataframes by dropping or rewriting columns, based on the year the data set
    returns the modified dataframe

    :param df: dataframe that contains tree census data
    :param year: year of the data set, three possible values 1995, 2005, 2015
    """
    lst_2015 = ['tree_dbh', 'health', 'spc_latin',
                'spc_common', 'nta', 'latitude', 'longitude']
    lst_2005 = ['tree_dbh', 'status', 'spc_latin',
                'spc_common', 'nta', 'latitude', 'longitude']
    lst_1995 = ['diameter', 'condition', 'spc_latin',
                'spc_common', 'nta_2010', 'latitude', 'longitude']

    if year == 2015:  # cleaning 2015 df
        df = df.loc[:, lst_2015]

    if year == 2005:  # cleaning 2005 df
        df = df.loc[:, lst_2005]
        df.rename(columns={'status': 'health'}, inplace=True)

    if year == 1995:  # cleaning 1995
        df = df.loc[:, lst_1995]
        df.rename(columns={'diameter': 'tree_dbh', 'condition': 'health',
                  'nta_2010': 'nta'}, inplace=True)

    return df


def make_nta_df(file_name):  # might done
    """
    opens file 'file_name' as a dataframe, and returns a dataframe containing columns
    'nta_code','nta_name', and 'population'

    :param file_name: name of a CSV file containing population,
                      and names for neighborhood tabulation areas
    """
    df = pd.read_csv(file_name)
    target_columns = ['nta_code', 'nta_name', 'population']
    df = df.loc[:, target_columns]
    return df


def count_by_area(df):  # not done
    """
    modifies dataframe to have columns 'nta' and 'num_trees', returns modified df

    :param df: dataframe with 'nta' column
    """
    return df


def neighborhood_trees(tree_df, nta_df):  # might be done
    """
    joins to input dataframes, 'tree_df' as left table. join should be on NTA code.
    resulting dataframe should have columns in order
    'nta','num_trees','nta_name','population', and trees_per_capita'

    :param tree_df: dataframe containing column 'nta'
    :param nta_df: dataframe containing columns 'NTACode' and 'NTAName'
    """
    merged_df = pd.merge(tree_df, nta_df, how='left', on='NTACode')
    return merged_df


def compute_summary_stats(df, col):  # not done
    """
    returns mean and median of series df[col]

    :param df: dataframe containing column 'col'
    :param col: name of numeric-valued col in dataframe
    """
    return 1, 0


def mse_loss(theta, y_vals):  # not done
    """
    computes the Mean Squared Error of param 'theta' and series 'y_vals'

    :param theta: a numeric value
    :param y_vals: a Series containing numeric values
    """
    return 0


def mae_loss(theta, y_vals):  # not done
    """
    computes the Mean Absolute Error of param 'theta and Series 'y_vals'

    :param theta: a numeric value
    :param y_vals: a Series containing numeric values
    """
    return 0


def test_mse(loss_fnc=mse_loss):  # not done
    """
    used to test whether the loss_fnc returning 'True',
    if the loss_fnc performs correctly, and 'False' otherwise

    :param loss_fnc: a function that takes in two input parameters,
                     (a numeric value and a Series of numeric values),
                     and returns a numeric value. It has a default value of mse_loss.
    """
    return False


def main():
    """
    function tests
    """
    df_si = pd.read_csv('trees_si_2015.csv')
    df_si = clean_df(df_si)
    print(df_si)


if __name__ == "__main__":
    main()
