"""
    Name: James Michael Crespo
    Email: james.crespo64@myhunter.cuny.edu
    Resources: Internet
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def make_dog_df(license_file, zipcode_file):
    return df


def make_bite_df(file_name):
    return df


def clean_age(age_str):
    return 0


def clean_breed(breed_str):
    return "STUB"


def impute_age(df):
    return df


def impute_zip(boro, zipcode):
    return "STUB"


def parse_datetime(df, column='LicenseIssuedDate'):
    return df


def main():
    """
    function tests
    """
    # make_dog_df() test
    dog_df = make_dog_df("NYC_Dog_Licensing_Dataset_2021.csv",
                         "nyc_zip_borough_neighborhoods_pop.csv")
    print(dog_df)

    # parse_datetime() test
    dog_df = parse_datetime(dog_df)
    print(dog_df)

    print('Most popular names are:')
    print(dog_df['AnimalName'].value_counts()[:10])

    sns.histplot(data=dog_df, x="Borough")

    plt.title('Dog Bites, 2021')
    plt.show()

    bite_df = make_bite_df("DOHMH_Dog_Bite_Data_2021.csv")
    print(bite_df)

    sns.histplot(data=bite_df, x="Borough")
    plt.show()

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

    sns.histplot(data=bite_df, x="month", discrete=True)

    plt.xticks(range(1, 13),
               ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
    plt.title('Dog Bites, 2021')
    plt.show()

    sns.histplot(data=bite_df, x="day_of_week")
    plt.xticks(range(7), ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    plt.title('Dog Bites, 2021')
    plt.show()


if __name__ == "__main__":
    main()
