"""
    Name: James Michael Crespo
    Email: james.crespo64@myhunter.cuny.edu
    Resources: Internet
"""


def clean_df(df, year=2015):  # not done
    """
    modifies dataframes by dropping or rewriting columns, based on the year the data set
    returns the modified dataframe

    :param df: dataframe that contains tree census data
    :param year: year of the data set, three possible values 1995, 2005, 2015
    """


def make_nta_df(file_name):  # not done
    """
    opens file 'file_name' as a dataframe, and returns a dataframe containing columns
    'nta_code','nta_name', and 'population'

    :param file_name: name of a CSV file containing population,
                      and names for neighborhood tabulation areas
    """


def count_by_area(df):  # not done
    """
    modifies dataframe to have columns 'nta' and 'num_trees', returns modified df

    :param df: dataframe with 'nta' column
    """


def neighborhood_trees(tree_df, nta_df):  # not done
    """
    joins to input dataframes, 'tree_df' as left table. join should be on NTA code.
    resulting dataframe should have columns in order
    'nta','num_trees','nta_name','population', and trees_per_capita'

    :param tree_df: dataframe containing column 'nta'
    :param nta_df: dataframe containing columsn 'NTACode' and 'NTAName'
    """


def compute_summary_stats(df, col):  # not done
    """
    returns mean and median of series df[col]

    :param df: dataframe containing column 'col'
    :param col: name of numeric-valued col in dataframe
    """


def mse_loss(theta, y_vals):  # not done
    """
    computes the Mean Squared Error of param 'theta' and series 'y_vals'

    :param theta: a numeric value
    :param y_vals: a Series containing numeric values
    """


def mae_loss(theta, y_vals):  # not done
    """
    computes the Mean Absolute Error of param 'theta and Series 'y_vals'

    :param theta: a numeric value
    :param y_vals: a Series containing numeric values
    """


def test_mse(loss_fnc=mse_loss):  # not done
    """
    used to test whether the loss_fnc returning 'True',
    if the loss_fnc performs correctly, and 'False' otherwise

    :param loss_fnc: a function that takes in two input parameters,
                     (a numeric value and a Series of numeric values),
                     and returns a numeric value. It has a default value of mse_loss.
    """


def main():
    # function tests
    print("Tests:")


if __name__ == "__main__":
    main()
