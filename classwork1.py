"""
    Name: James Michael Crespo
    Email: james.crespo64@myhunter.cuny.edu
    Resources: the internet
    I attended lecture today.
    Row: 7
    Seat: 93
"""


def make_dict(file_name, sep=": "):
    """
    Opens and reads from file_name, and returns a dictionary.

    Keyword arguments:
    sep -- the delimanators for splitting up the data (default ': ')
    """

    new_d = {}
    with open(file_name, encoding="utf8") as filed:
        for line in filed:
            if line.find(sep) > -1:
                words = line[:-1].split(sep)
                new_d[words[0]] = words[1]
    return new_d
