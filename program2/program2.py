"""
Name:  James Michael Crespo
Email: james.crespo64@myhunter.cuny.edu
Resources: the internet
"""
import pandas as pd


def clean_df(df, year=2015):  # done
    """
    modifies dataframes by dropping or rewriting columns, based on the year the data set
    returns the modified dataframe

    :param df: dataframe that contains tree census data
    :param year: year of the data set, three possible values 1995, 2005, 2015
    """
    # lists with all columns to keep for each possible year
    lst_2015 = ['tree_dbh', 'health', 'spc_latin', 'spc_common', 'address', 'zipcode', 'boroname',
                'nta', 'latitude', 'longitude', 'council_district', 'census_tract']
    lst_2005 = ['tree_dbh', 'status', 'spc_latin', 'spc_common', 'address', 'zipcode', 'boroname',
                'nta', 'latitude', 'longitude', 'cncldist', 'census_tract']
    lst_1995 = ['diameter', 'condition', 'spc_latin', 'spc_common', 'address', 'zip_original',
                'borough', 'nta_2010', 'latitude', 'longitude', 'council_district',
                'censustract_2010']

    if year == 2015:  # cleaning the df for 2015
        df = df.loc[:, lst_2015]

    if year == 2005:  # cleaning the df for 2005
        df = df.loc[:, lst_2005]
        df.rename(columns={'status': 'health',
                  'cncldist': 'council_district'}, inplace=True)

    if year == 1995:  # cleaning the df for 1995
        df = df.loc[:, lst_1995]
        df.rename(columns={'diameter': 'tree_dbh', 'condition': 'health', 'zip_original': 'zipcode',
                  'borough': 'boroname', 'nta_2010': 'nta', 'censustract_2010': 'census_tract'},
                  inplace=True)

    return df


def filter_health(df, keep):  # done
    """
    returns dataframe which only contains rows whose 'health' column,
    contains a value from list 'keep'

    :param df: dataframe that contains 'health' column
    :param keep: a list of values for 'health' column
    """
    df = df.loc[df['health'].isin(keep)]
    return df


def add_indicator(row):  # done
    """
    returns 1 if 'health' != 'Poor' and 'tree_dbh' > 10. otherwise, return 0

    :param row: a Series(row) containing values from 'tree_dbh' and 'health'
    """
    if (row[0] > 10) & (row[1] != 'Poor'):
        return 1
    return 0


def find_trees(df, species):  # done
    """
    returns a list of 'address' for all trees in dataframe whose 'spc_latin' column matches species

    :param df: dataframe that contains 'spc_latin' and 'address' column
    :param species: string containing the latin name of a tree
    """
    lst = []  # initialize list

    # make dataframe with species, use lower to match case to compare
    df = df.loc[(df['spc_latin'].str.lower() == species.lower())]

    if df.empty:
        return lst

    # add 'address' values to list, and return
    lst = list(df['address'])
    return lst


def count_by_area(df, area='boroname'):  # not done
    """
    returns sum of the number of trees, grouped by area

    :param df: dataframe that contains 'area' column
    :param area: name of a column in df. The default value is "boroname"
    """
    total = 0
    return total
