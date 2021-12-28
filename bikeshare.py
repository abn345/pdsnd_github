"""
Amanda Norman
"""
import time
import pandas as pd
import numpy as np



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # Get user input for city (Chicago, New York City, Washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please input a city name from the following: New York City, Chicago, Washington.').lower()
    
    if city == 'Washington':
	print("Warning: This city does not have a lot of user data.")

    while city not in ['chicago','new york city','washington']:
        city = input("Invalid city name. Please put Chicago, New York City, or Washington")
        
    # Get user input for month (all, january, february, ... , june)
    month = input('Please input a month from the following: January, February, March, April, May, June.').lower()
    
    while month not in ['january','february','march','april','may','june']:
        month = input('Invalid month. Please put a month from January-June.')
        
    # Get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('From what weekday(s) do you want to filter the data? Use commas to list the names.').lower()

    while day not in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday']:
        day = input('Invalid day. Please enter a weekday')
        
    print('-'*40)
    return city, month, day

    
#Shorten the list for months and day of week
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
    df = pd.read_csv("{}.csv".format(city.replace(" ","_")))

    # Convert the Start and End Time columns to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].apply(lambda x: x.month)
    df['day_of_week'] = df['Start Time'].apply(lambda x: x.strftime('%A').lower())


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month,:]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day,:]

    return df
   


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_common_month= str(df['month'].mode()[0])
    print('The most common month: '+ most_common_month)

    # display the most common day of week
    most_common_day= str(df['day_of_week'].mode()[0])
    print('The most common day of the week: ' + most_common_day)

    # display the most common start hour
    df['start_hour']=df['Start Time'].dt.hour
    most_common_start_hour= str(df['start_hour'].mode()[0])
    print('The most common start hour: ' + most_common_start_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station=str(df['Start Station'].mode()[0])
    print('The most common used Start Station: '+ most_common_start_station)

    # display most commonly used end station
    most_common_end_station=str(df['End Station'].mode()[0])
    print("The most common End Station: " + most_common_end_station)

    # display most frequent combination of start station and end station trip
    df["Start-End Combo"] = (df['Start Station'] + '-' + df['End Station'])
    most_frequent_combo = str(df['Start-End Combo'].mode()[0])
    print('The most frequent combonation of start station and end station trip: ' + most_frequent_combo)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    df['duration']=df['End Time']-df['Start Time']
    # display total travel time
    total_travel_time = str(df['duration'].sum())
    print("Total travel time: " + total_travel_time)

    # display mean travel time
    mean_travel_time = str(df['duration'].mean())
    print("Mean travel time: " + mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # Display counts of user types
    user_types = str(df['User Type'].value_counts())
    print("Counts of user types: " + user_types)
    
    # Display counts of gender
    gender_count = str(df['Gender'].value_counts())
    print("Counts of gender: " + gender_count)

    # Display earliest, most recent, and most common year of birth
    earliest_birth_year = str(df['Birth Year'].min())
    print("Earliest birth year: " + earliest_birth_year)
        
    most_recent_birth_year = str(df['Birth Year'].max())
    print("Most recent birth year: " + most_recent_birth_year)
        
    most_common_birth_year = str(df['Birth Year'].mode()[0])
    print("Most common birth year: " + most_common_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


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
