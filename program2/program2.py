"""
Name:  James Michael Crespo
Email: james.crespo64@myhunter.cuny.edu
Resources: the internet
"""


def clean_df(df, year=2015):  # done

    # lists with all columns that shouldn't be dropped for each possible year
    lst_2015 = ['tree_dbh', 'health', 'spc_latin', 'spc_common', 'address', 'zipcode', 'boroname',
                'nta', 'latitude', 'longitude', 'council_district', 'census_tract']
    lst_2005 = ['tree_dbh', 'status', 'spc_latin', 'spc_common', 'address', 'zipcode', 'boroname',
                'nta', 'latitude', 'longitude', 'cncldist', 'census_tract']
    lst_1995 = ['diameter', 'condition', 'spc_latin', 'spc_common', 'address', 'zip_original',
                'borough', 'nta_2010', 'latitude', 'longitude', 'council_district',
                'censustract_2010']

    # cleaning the df for 2015
    if year == 2015:
        df = df.loc[:, lst_2015]

    # cleaning the df for 2005
    if year == 2005:
        df = df.loc[:, lst_2005]
        df.rename(columns={'status': 'health',
                  'cncldist': 'council_district'}, inplace=True)

    # cleaning the df for 1995
    if year == 1995:
        df = df.loc[:, lst_1995]
        df.rename(columns={'diameter': 'tree_dbh', 'condition': 'health', 'zip_original': 'zipcode',
                  'borough': 'boroname', 'nta_2010': 'nta', 'censustract_2010': 'census_tract'},
                  inplace=True)

    # return clean dataframe
    return df


def filter_health(df, keep):  # done
    df = df.loc[df['health'].isin(keep)]
    return df


def add_indicator(row):  # done
    if (row[0] > 10) & (row[1] != 'Poor'):
        return 1
    else:
        return 0


def find_trees(df, species):  # not done
    lst = []
    df = df[df['spc_latin'].str.contains(species)]
    if df.empty:
        return lst
    lst = list(df['address'])
    return lst


def count_by_area(df, area='boroname'):  # not done
    total = 0
    return total
