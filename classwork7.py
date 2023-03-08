"""
    Name: James Michael Crespo
    Email: james.crespo64@myhunter.cuny.edu
    Resources: the internet
    I attended lecture today.
    Row: 9
    Seat: 93
"""
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import datasets, svm, metrics
from sklearn import datasets
import matplotlib as plt


def binary_digit_clf(data, target, test_size=0.25, random_state=21):
    """
    data: a numpy array that includes rows of equal size flattend arrays,
    target a numpy array that takes values 0 or 1 corresponding to the rows of data.
    test_size: the size of the test set created when the data is divided into test and training sets with train_test_split. The default value is 0.25.
    random_state: the random seed used when the data is divided into test and training sets with train_test_split. The default value is 21.
    """


# Import datasets, classifiers and performance metrics:
# Using the digits data set from sklearn:
digits = datasets.load_digits()
print(digits.target)
print(type(digits.target), type(digits.data))
# flatten the images
n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))
print(data[0:5])
print(f'The targets for the first 5 entries: {digits.target[:5]}')
# Make a DataFrame with just the binary digits:
binaryDigits = [(d, t) for (d, t) in zip(data, digits.target) if t <= 1]
bd, bt = zip(*binaryDigits)
print(f'The targets for the first 5 binary entries: {bt[:5]}')

confuse_mx = binary_digit_clf(bd, bt, test_size=0.95)
print(f'Confusion matrix:\n{confuse_mx}')
disp = metrics.ConfusionMatrixDisplay(confusion_matrix=confuse_mx)
# Use a different color map since the default is garish:
disp.plot(cmap="Purples")
plt.title("Logistic Regression Classifier for Binary Digits")
plt.show()
