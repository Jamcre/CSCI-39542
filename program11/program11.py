"""
Name:  James Michael Crespo
Email: james.crespo64@myhunter.cuny.edu
Resources: the internet
"""
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.mixture import GaussianMixture

def make_df(file_name):
    """
    This function takes one input:
    file_name: the name of a CSV file containing 911 System Calls from OpenData NYC.
    The data is read into a DataFrame. Rows that are have null values for the type description, incident date, incident time, latitute and longitude are dropped. Only rows that contain AMBULANCE as part of the TYP_DESC are kept. The resulting DataFrame is returned.
    Hint: see DS 100: Chapter 13 for using string methods within pandas.
    See Classwork 9.
    """
    df = pd.read_csv(file_name)
    # Dropping rows
    drop_lst = ['TYP_DESC','INCIDENT_DATE','INCIDENT_TIME','Latitude','Longitude']
    df = df.dropna(subset=drop_lst)
    # Keep TYPE_DESC rows with AMBULANCE
    df = df[df['TYP_DESC'].str.contains('AMBULANCE', case=False)]
    return df

def add_date_time_features(df):
    """
    This function takes one input:
    df: a DataFrame containing 911 System Calls from OpenData NYC created by make_df.
    An additional column WEEK_DAY is added with the day of the week (0 for Monday, 1 for Tuesday, ..., 6 for Sunday) of the date in INCIDENT_DATE is added. Another column, INCIDENT_MIN, that takes the time from INCIDENT_TIME and stores it as the number of minutes since midnight. The resulting DataFrame is returned.
    Hint: see Lecture 3 for using datetime methods with pandas, including computing the day of the week (of datetime objects) and the total seconds (of timedelta objects).
    """
    # Convert column to datetime objects
    df['INCIDENT_DATE'] = pd.to_datetime(df['INCIDENT_DATE'])
    # Add week day column as number, 0-6
    df['WEEK_DAY'] = df['INCIDENT_DATE'].dt.dayofweek
    # Add column that calculates minutes from midnight
    df['INCIDENT_MIN'] = pd.to_timedelta(df['INCIDENT_TIME']).dt.seconds / 60
    return df

def filter_by_time(df, days=None, start_min=0, end_min=1439):
    """
    This function takes four inputs:
    df: a DataFrame containing 911 System Calls from OpenData NYC.
    days: a list of integers ranging from 0 to 6, representing the days of the week. The default value is None and is equivalent to the list containing all days: [0,1,2,3,4,5,6].
    start_min: a non-negative integer value representing the starting time. With end_min, it representing the range, inclusive, for the time, in minutes, that should be selected. The default value give the range of [0,1439] which ranges from midnight (0 minutes) to (1439 representing 23:59 since 23 hours + 59 minutes = 23*60+59 minutes = 1439 minutes).
    end_min: a non-negative integer value representing the ending time. With start_min, it representing the range, inclusive, for the time, in minutes, that should be selected. The default value give the range of [0,1439] which ranges from midnight (0 minutes) to (1439 representing 23:59 since 23 hours + 59 minutes = 23*60+59 minutes = 1439 minutes).
    Returns a DataFrame with entries restricted to weekdays in days (or all weekdays if None is given) and incident times in [start_min, end_min] inclusive (e.g. contains the endpoints).
    """
    # Create default mask if param 'days' is none
    if days is None:
        days = [0, 1, 2, 3, 4, 5, 6]
    # perform filtering
    filtered_df = df[(df['WEEK_DAY'].isin(days)) &  (df['INCIDENT_MIN'] >= start_min) & (df['INCIDENT_MIN'] <= end_min)]
    return filtered_df

def compute_kmeans(df, num_clusters = 8, n_init = 'auto', random_state = 2022):
    """
    This function takes four inputs:
    df: a DataFrame containing 911 System Calls from OpenData NYC.
    n_init: Number of times the k-means algorithm is run with different centroid seeds. The final results is the best output of n_init consecutive runs in terms of inertia. The default value is auto.
    num_clusters: an integer representing the number of clusters. The default value is 8.
    random_state: the random seed used for KMeans. The default value is 2022.
    Runs the KMeans model with num_clusters on the latitude and longitude data of the provided DataFrame. Returns the cluster centers and predicted labels computed via the model.
    A similar, but not identical function was part of Classwork 9.
    """
    # Get the latitude and longitude data
    lat_lon_data = df[['Latitude', 'Longitude']].values
    # Initialize the KMeans model
    kmeans = KMeans(n_clusters=num_clusters, n_init=n_init, random_state=random_state)
    # Fit the model to the data and get the cluster centers and labels
    kmeans.fit(lat_lon_data)
    return kmeans.cluster_centers_, kmeans.labels_

def compute_gmm(df, num_clusters = 8, random_state = 2022):
    """
    This function takes three input:
    df: a DataFrame containing 911 System Calls from OpenData NYC.
    num_clusters: an integer representing the number of clusters. The default value is 8.
    random_state: the random seed used for GaussianMixture. The default value is 2022..
    Runs the GaussianMixture model with num_clusters on the latitude and longitude data of the provided DataFrame. Returns the array of the predicted labels computed via the model.
    """
    # Get the latitude and longitude data
    lat_lon_data = df[['Latitude', 'Longitude']].values
    # Initialize the GaussianMixture model
    gmm = GaussianMixture(n_components=num_clusters, random_state=random_state)
    # Fit the model to the data and get the predicted labels
    gmm.fit(lat_lon_data)
    return gmm.predict(lat_lon_data)

def compute_agglom(df, num_clusters = 8, linkage='ward'):
    """
    This function takes three input:
    df: a DataFrame containing 911 System Calls from OpenData NYC.
    num_clusters: an integer representing the number of clusters. The default value is 8.
    linkage: the linkage criterion used determining distances between sets for AgglomerativeClustering. The default value is 'ward'.
    Runs the Agglomerative model with num_clusters on the latitude and longitude data of the provided DataFrame and default linkage (i.e. ward). Returns the array of the predicted labels computed via the model.
    """
    # Get the latitude and longitude data
    lat_lon_data = df[['Latitude', 'Longitude']]
    # Initialize the Agglomerative model and get get predicted labels
    agg = AgglomerativeClustering(n_clusters=num_clusters, linkage=linkage)
    return agg.fit_predict(lat_lon_data)

def compute_explained_variance(df, K =[1,2,3,4,5], random_state = 55):
    """
    This function takes three inputs:
    df: a DataFrame containing 911 System Calls from OpenData NYC.
    K: a list of integers representing values for the number of clusters. The default value is [1,2,3,4,5].
    random_state: the random seed used for KMeans. The default value is 55.
    Returns a list of the sum of squared distances of samples to their closest cluster center for each value of K. This can be computed manually or via the inertia_ attribute of the KMeans model.
    """
    # Get the latitude and longitude data
    lat_lon_data = df[['Latitude', 'Longitude']].values
    # Initiliaze empty list for sum of squared distances
    sum_squ_dist = []
    # For all values in K, create KMeans model and compute sum of square distances
    for integer in K:
        kmeans = KMeans(n_clusters=integer, random_state=random_state)
        kmeans.fit(lat_lon_data)
        sum_squ_dist.append(kmeans.inertia_)
    return sum_squ_dist

def main():
    df = make_df('program11/NYPD_Calls_Manhattan_4Jul2021.csv')
    print(df[['INCIDENT_TIME','TYP_DESC','Latitude','Longitude']])

    df = add_date_time_features(df)
    print(df[['INCIDENT_DATE','WEEK_DAY','INCIDENT_TIME','INCIDENT_MIN']])

    df_early_am = filter_by_time(df,days=[6], start_min=0,end_min=360)
    print(df_early_am[['INCIDENT_DATE','WEEK_DAY','INCIDENT_TIME','INCIDENT_MIN']])

if __name__ == "__main__":
    main()
