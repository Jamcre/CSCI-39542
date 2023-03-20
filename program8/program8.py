"""
Name:  James Michael Crespo
Email: james.crespo64@myhunter.cuny.edu
Resources: the internet
"""
import pickle
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


def clean_reg(reg):
    """
    If reg is passenger 'PAS' or commercial 'COM', return those values. Otherwise, return 'OTHER'.

    :param reg: a string containing the registration status of the vehicle.
    """
    if reg in ('PAS', 'COM'):
        return reg
    return 'OTHER'


def clean_color(col):
    """
    takes a string, and replaces to a value based on input, if not a value, change to other

    :param col: a string containing the color of the vehicle.
    """
    if col.upper() in ['GY', 'GRAY', 'GREY', 'SILVE', ' SIL', 'SL']:
        temp = 'GRAY'
    elif col.upper() in ['WH', 'WHITE']:
        temp = 'WHITE'
    elif col.upper() in ['BK', 'BLACK', 'BL']:
        temp = 'BLACK'
    elif col.upper() in ['BLUE']:
        temp = 'BLUE'
    elif col.upper() in ['RED', 'RD']:
        temp = 'RED'
    elif col.upper() in ['GR', 'GREEN']:
        temp = 'GREEN'
    elif col.upper() in ['BROWN', 'TAN']:
        temp = 'BROWN'
    else:
        temp = 'OTHER'
    return temp


def add_indicators(df, cols=['Registration', 'Color', 'State']):
    """
    Returns df with additional indicator col generated by get_dummies for specified columns.
    The drop_first flag is set to True to drop extraneous columns.

    :param df: a DataFrame that including the columns specified in cols.
    :param col: a list of names of cols in df. default = ['Registration', 'Color', 'State'].
    """
    for col in cols:
        new_col = pd.get_dummies(df[col], prefix=col, drop_first=True)
        df = pd.concat([df, new_col], axis=1)
    return df


def add_excessive_flag(df, threshold=5):
    """
    Returns the df with a new col, 'Excessive Tickets', is 0 if there's less threshold # of tickets,
    else it is 1.

    :param df: a DataFrame that including the columns specified in cols.
    :param threshold: a numeric value. The default value is 5.
    """
    df['Excessive Tickets'] = (df['Tickets'] >= threshold).astype(int)
    return df


def split_data(df, x_cols, y_col, test_size=0.25, random_state=2023):
    """
    Returns  data split into 4 subsets, corresponding to those returned by
    train_test_split: x_train, x_test, y_train, and y_test.
    where units is the "x" column and the input parameter, y_col_name is the "y" column.

    :param df: a DataFrame containing with a columns units.
    :param x_cols: a list of the names of the column of the independent variable.
    :param y_col: the name of the column of the dependent variable.
    :param test_size: accepts a float between 0 and 1,
                      and is the proportion of the data set to use for training. default = 0.25
    :param random_state: Used as a seed to the randomization. default = 1870.
    """
    x_data = df[x_cols]
    y_data = df[y_col]
    x_train, x_test, y_train, y_test = train_test_split(
        x_data, y_data, test_size=test_size, random_state=random_state)
    return x_train, x_test, y_train, y_test


def fit_model(x_train, y_train, model_type='logreg'):
    """
    Fits the specifed model to the x_train and y_train data, using sklearn.
    The resulting model should be returned as bytestream, using pickle.

    :param x_train: the independent variable(s) for the analysis.
    :param y_train: the dependent variable for the analysis.
    :param model_type: type of model to use such as'logreg', 'svm', 'nbayes', and 'rforest'.
                       default='logreg'
    """
    if model_type == 'logreg':
        model = LogisticRegression(penalty='l2', solver='saga', max_iter=5000)
    if model_type == 'nbayes':
        model = GaussianNB()
    if model_type == 'svm':
        model = SVC(kernel='rbf')
    if model_type == 'rforest':
        model = RandomForestClassifier(n_estimators=100, random_state=0)
    model.fit(x_train, y_train)
    return pickle.dumps(model)


def score_model(mod_pkl, xes, yes):
    """
    Returns the confusion matrix for the model.

    :param mod_pkl: a object serialization of a trained model. possible models:
                    logistic regression, support vector machine, naive Bayes, and random forest.
    :param xes: the independent variable(s) for analysis with same dimensions as model.
    :param yes: the dependent variable(s) for analysis with same dimensions as model.
    """
    model = pickle.loads(mod_pkl)
    y_pred = model.predict(xes)
    con_matrix = confusion_matrix(yes, y_pred)
    return con_matrix


def compare_models(x_test, y_test, models):
    """
    For specified models in models, calls score() on each model on x_test and y_test.
    The function returns the index of the model with highest accuracy score and its accuracy score
    (i.e. 0 if it is the first model in the list, 1 if it is the second model in the list, etc).
    In case of ties for the best score, return the first one that has that value.

    :param x_test: a numpy array that includes rows of equal size flattened arrays,
    :param y_test a numpy array that takes values 0 or 1 corresponding to the rows of x_test.
    :param models: a list of pickled models constructed from fit_model.
    """
    best_score = -1.5
    best_index = -1.5

    for index, model in enumerate(models):
        model = pickle.loads(model)
        score = model.score(x_test, y_test)

        if score > best_score:
            best_score = float(score)
            best_index = float(index)

    return best_index, best_score
