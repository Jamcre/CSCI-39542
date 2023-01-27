"""
    Name: James Michael Crespo
    Email: james.crespo64@myhunter.cuny.edu
    Resources:  Internet
"""


def make_dictionary(data, kind="min"):
    """
    Creating a dictionary with a key of the remote unit ID + turnstile unit number.
    Depending on kind, the resulting dictionary will store the minimum entry
    number seen (as an integer), the maximum entry number seen (as an integer),
    or the station name (as a string).
    Returns the resulting dictionary.

    Keyword arguments:
    type -- type of dictionary to be created:  min, max, station
    """

    # Placeholder-- replace with your code
    new_dict = {}
    for line in data:
        # columns for data: C/A,UNIT,SCP,STATION,LINENAME,DIVISION,DATE,TIME,DESC,ENTRIES,EXITS
        line_column = line.split(",")
        # create key for dictionary, Remote Unit ID + turnstile unit number
        key = line_column[1] + "," + line_column[2]
        # add key:value to dictionary, when kind = "station". values are station names
        if kind == "station":
            new_dict[key] = line_column[3]
        # for when kind = "min" or kind = "max"
        else:
            # add value if dictionary is empty or key is not repeat in dictionary
            if not (new_dict) or not key in new_dict:
                new_dict[key] = int(line_column[9])
            else:
                # check if old entry value is more than new entry value, if so replace for new min
                if (new_dict[key] > int(line_column[9])) and kind == "min":
                    new_dict[key] = int(line_column[9])
                # check if old entry value is less than new entry value, if so replace for new max
                if (new_dict[key] < int(line_column[9])) and kind == "max":
                    new_dict[key] = int(line_column[9])

    return new_dict


def get_turnstiles(station_dict, stations=None):
    """
    If stations is None, returns the names of all the turnstiles stored as keys
    in the inputted dictionary.
    If non-null, returns the keys which have value from station in the inputed dictionary.
    Returns a list.

    Keyword arguments:
    stations -- None or list of station names.
    """

    # Placeholder-- replace with your code
    lst = []
    if stations is not None:
        for key in station_dict.keys():
            if station_dict[key] in stations:
                lst.append(key)
    else:
        lst = list(station_dict.keys())
    return lst


def compute_ridership(min_dict, max_dict, turnstiles=None):
    """
    Takes as input two dictionaries and a list, possibly empty, of turnstiles.
    If no value is passed for turnstile, the default value of None is used
    (that is, the total ridership for every station in the dictionaries).
    Returns the ridership (the difference between the minimum and maximum values)
    across all turnstiles specified.

    Keyword arguments:
    turnstiles -- None or list of turnstile names
    """

    # Placeholder-- replace with your code
    total = 0
    if turnstiles is None:
        for keys in max_dict:
            total = total + max_dict[keys] - min_dict[keys]
    else:
        for keys in max_dict:
            if keys in turnstiles:
                total = total + max_dict[keys] - min_dict[keys]

    return total


def main():
    """
    Opens a data file and computes ridership, using functions above.
    """
    file_name = 'turnstile_220611.txt'
    # Store the file contents in data:
    with open(file_name, encoding='UTF-8') as file_d:
        lines = file_d.readlines()
    # Discard first line with headers:
    data = lines[1:]

    # Set up the three dictionaries:
    min_dict = make_dictionary(data, kind="min")
    max_dict = make_dictionary(data, kind="max")
    station_dict = make_dictionary(data, kind="station")

    # Print out the station names, alphabetically, without duplicates:
    print(f'All stations: {sorted(list(set(station_dict.values())))}')

    # All the turnstiles from the data:
    print(f'All turnstiles: {get_turnstiles(station_dict)}')
    # Only those for Hunter & Roosevelt Island stations:
    print(get_turnstiles(station_dict, stations=[
          '68ST-HUNTER CO', 'ROOSEVELT ISLND']))

    # Checking the ridership for a single turnstile
    ridership = compute_ridership(
        min_dict, max_dict, turnstiles=["R051,02-00-00"])
    print(f'Ridership for turnstile, R051,02-00-00:  {ridership}.')

    # Checking the ridership for a station
    hunter_turns = get_turnstiles(station_dict, stations=['68ST-HUNTER CO'])
    ridership = compute_ridership(min_dict, max_dict, turnstiles=hunter_turns)
    print(f'Ridership for Hunter College: {ridership}.')


if __name__ == "__main__":
    main()
