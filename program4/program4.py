"""
    Name: James Michael Crespo
    Email: james.crespo64@myhunter.cuny.edu
    Resources: Internet
"""
import pandas as pd


def make_dog_df(license_file, zipcode_file):
    """
    takes 2 input files, left merges to license_file on zipcode, drops specified columns,
    drops rows with NaN values in Borough, capitalizes animal names

    :param license_file: name of CSV file, with NYC Dog Licensing Data
    :param zipcode_file: name of CSV file, with BetaNYC's Zipcode by Borough data
    """
    drop_lst = ['LicenseExpiredDate', 'Extract Year',
                'population', 'density', 'neighborhood', 'post_office']
    license_df = pd.read_csv(license_file)
    zipcode_df = pd.read_csv(zipcode_file)
    zipcode_df = zipcode_df.rename(
        columns={'zip': 'ZipCode', 'borough': 'Borough'})
    merged_df = pd.merge(license_df, zipcode_df, how='left', on='ZipCode')
    merged_df = merged_df.drop(drop_lst, axis=1)
    merged_df['AnimalName'] = merged_df['AnimalName'].str.capitalize()
    return merged_df.dropna(subset=['Borough'])


def make_bite_df(file_name):
    """
    opens file_name and drops the 'Species' column

    :param file_name: name of CSV file, with DOHMH Dog Bite Data
    """
    df = pd.read_csv(file_name)
    return df.drop(['Species'], axis=1)


def clean_age(age_str):
    """
    if age_str is NaN, return age_str.
    if age_str ends with Y, return the number as year.
    if age_str ends with M, convert from months and return as year.
    if str_age has only numeric, return the number

    :param age_str: a string containing age of the dog
    """

    if pd.isna(age_str):
        return age_str

    age_str = str(age_str).strip()

    if age_str.isdigit():
        return float(age_str)

    last_letter = age_str[-1]

    if last_letter == 'Y':
        return float(age_str[:-1])
    if last_letter == 'M':
        return float(age_str[:-1]) / 12

    return None


def clean_breed(breed_str):
    """
    if breed_str is empty, return 'Unknown'. else return the string as title

    :param breed_str: a string containing breed of dog
    """
    if pd.isna(breed_str):
        return 'Unknown'
    return breed_str.title()


def impute_age(df):
    """
    replaces missing value of 'Age Num', with the median of the same column

    :param df: a dataframe containing column 'Age Num'
    """
    return df


def impute_zip(boro, zipcode):
    """
    if zipcode is empty, impute value based on boro (see dictionary below).
    return None, if boro is not in the dictionary

    :param boro: a non-empty string containing the borough
    :param zipcode: a possibly empty string containing zipcode
    """
    zip_dict = {'Bronx': '10451', 'Brooklyn': '11201',
                'Manhattan': '10001', 'Queens': '11431', 'Staten Island': '10341'}
    if pd.isna(zipcode):
        zipcode = zip_dict.get(boro)
    return zipcode


def parse_datetime(df, column='LicenseIssuedDate'):
    """
    creates 3 columns in df, 'timestamp' with date in YYYY-MM-DD format,
    'month' with numeric month value,
    'day_of_week' with numeric weekday (0-6)

    :param df:
    :param column:
    """
    df['timestamp'] = pd.to_datetime(df[column])
    df['month'] = pd.to_datetime(df[column]).dt.month
    df['day_of_week'] = pd.to_datetime(df[column]).dt.dayofweek
    return df


def main():
    """
    function tests
    """
    dog_df = make_dog_df("NYC_Dog_Licensing_Dataset_2021.csv",
                         "nyc_zip_borough_neighborhoods_pop.csv")
    print(dog_df)

    dog_df = parse_datetime(dog_df)
    print(dog_df)

    bite_df = make_bite_df("DOHMH_Dog_Bite_Data_2021.csv")
    print(bite_df)

    df_drop = bite_df.dropna()
    print(f'The full DataFrame has {len(bite_df)} entries.')
    print(f'Dropping undefined values leaves {len(df_drop)} entries.')

    bite_df['Age Num'] = bite_df['Age'].apply(clean_age)
    print(bite_df[['Age', 'Age Num']])

    bite_df['Breed'] = bite_df['Breed'].apply(clean_breed)
    print(bite_df)

    bite_df = impute_age(bite_df)
    bite_df['ZipCode'] = bite_df.apply(
        lambda row: impute_zip(row['Borough'], row['ZipCode']), axis=1)
    print(bite_df)

    bite_df = parse_datetime(bite_df, column='DateOfBite')
    print(bite_df)


if __name__ == "__main__":
    main()
