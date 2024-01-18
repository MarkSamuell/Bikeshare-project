import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city_selection = input('To view the available bikeshare data, kindly choose\n -Chicago\n -New York City\n -Washington\n').lower()
            if city_selection in ['chicago', 'new york city', 'washington']:
                city = city_selection
                break
        except KeyboardInterrupt:
            print('\nNO Input Taken!')
        else:
            print('Invalid month choice!!')


    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday', 'sunday', 'all']

    month = input('\n\nTo filter {}\'s data by a particular month, please type the month name or all for not filtering by month: \n-January\n-February\n-March\n-April\n-May\n-June\n-All\n\n:'.format(city.title())).lower()

    while month not in months:
        print("That's invalid choice, please type a valid month name or all.")
        month = input('\n\nTo filter {}\'s data by a particular month, please type the month name or all for not filtering by month: \n-January\n-February\n-March\n-April\n-May\n-June\n-All\n\n:'.format(city.title())).lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('\n\nTo filter {}\'s data by a particular day, please type the day name or all for not filtering by day: \n-Sunday\n-Monday\n-Tuesday\n-Wednesday\n-Thursday\n-Friday\n-Sturday\n-All\n\n:'.format(city.title())).lower()

    while day not in days:
        print("That's invalid choice, please type a valid day name or all.")
        day = input('\n\nTo filter {}\'s data by a particular day, please type the day name or all for not filtering by day: \n-Sunday\n-Monday\n-Tuesday\n-Wednesday\n-Thursday\n-Friday\n-Sturday\n-All\n\n:'.format(city.title())).lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month_name()

    common_month = df['month'].mode()[0]
    print('the most common month is :', common_month)


    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('the most common day is:', common_day)

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour

    common_hour = df['start_hour'].mode()[0]
    print('the most common start hour is:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('the most common start station is :', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('the most common end station is :', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['common_stations'] = pd.concat([df['Start Station'],df['End Station']], ignore_index=True)
    common_station = df['common_stations'].mode()[0]
    print('the most frequent station is:', common_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

     # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('total travel time:', total_time, 'sec')

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('mean of travel time:', mean_time, 'sec')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('counts of user types:', user_types, '\n')

    # TO DO: Display counts of gender
    if city == 'washington':
        print('gender data is not available in Washington')
    else:
        gender_types = df['Gender'].value_counts()
        print('counts of gender:', gender_types, '\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if city == 'washington':
        print('birth data is not available in Washington')
    else:
        early_date = int(np.min(df['Birth Year']))
        recent_date = int(np.max(df['Birth Year']))
        most_common = int(df['Birth Year'].mode()[0])
        print('earliest year : {}\n most recent year: {}\n most common year:{}\n'.format(early_date, recent_date, most_common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(city):
    print('\n Raw data is available to check... \n')
    display_raw = input('May you want to have a look on the raw data? Type y or n\n')

    while display_raw == 'y':
        try:
            for chunk in pd.read_csv(CITY_DATA[city], chunksize=5):
                print(chunk)

                # repeating the question

                display_raw = input('May you want to have a look on more raw data? Type y or n\n')
                if display_raw != 'y':
                    break
            break
        except KeyboardInterrupt:
            print('Thank you.')
    if display_raw == 'n':
        print('Thank you.')
    else:
        print('\n')
        print('invalid choice please type y or n\n')
        display_raw_data(city)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
