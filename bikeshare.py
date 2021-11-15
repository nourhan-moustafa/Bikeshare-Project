import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')

    city = input("Which city would you like to analyze: chicago, new york city, washington?").lower()
    while city not in CITY_DATA.keys():
        print("invalid", " ", "input".title())
        city = input("kindly, enter a valid city: chicago, new york city, washington?").lower()
        
    month = input('Which month would you like to visualize data from?').lower()
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while month not in months:
        print("invalid", " ", "input".title())
        month = input('Which month would you like to visualize data from?').lower()
    
    day = input('which day would you like to know about?').lower()
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while day not in days:
        print("invalid", " ", "input".title())
        day = input('which day would you like to know about?').lower()

        print('-' * 40)

    return city, month.title(), day.title()


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df['month'] = df['Start Time'].dt.month_name()
    if month != 'all':
        df = df[df['month'] == month]
        
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if day != 'all':
        df = df[df['day_of_week'] == day] 
        
    df['hour'] = df['Start Time'].dt.hour

    return df


def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    mc_month = df['month'].mode()[0]
    print('Most Common Month is:', mc_month)
  
    mc_day = df['day_of_week'].mode()[0]
    print('Most Common Day of The Week is:', mc_day)

    df['hour'] = df['Start Time'].dt.hour
    mc_hour = df['hour'].mode()[0]
    print('Most Common Hour of the Day is:', mc_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    mc_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station is:', mc_start_station)

    mc_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station is:', mc_end_station)

    df["Most Frequent Route Trip"] = df['Start Station'] + "-" + df['End Station']
    mf_route_trip = df["Most Frequent Route Trip"].mode()[0]
    print('Most Frequent Combination of Start Station and End Station Trip is:', mf_route_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time is:', total_travel_time)

    average_travel_time = df['Trip Duration'].mean()
    print('Average Travel Time is:', average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    user_types = df['User Type'].value_counts()
    print(user_types)

    if "Gender" in df.columns:
        gender = df['Gender'].value_counts()
        print(gender)
    else:
        print('There is no Gender Information Provided in this City')

    if "Birth Year" in df.columns:
        earliest_birth_year = df["Birth Year"].min()
        print(earliest_birth_year)
    else:
        print('There is No Birth Year Data Provided in this City')

    if "Birth Year" in df.columns:
        most_recent_birth_year = df["Birth Year"].max()
        print(most_recent_birth_year)
    else:
        print('There is No Birth Year Data Provided in this City')

    if "Birth Year" in df.columns:
        most_common_birth_year = df["Birth Year"].mode()[0]
        print(most_common_birth_year)
    else:
        print('There is No Birth Year Data Provided in this City')

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-' * 40)


def display_raw_data(df):
    start_loc = 0
    raw_data = input('\nWould You Like to See More Raw Data? Enter yes or no.\n').lower()
    while raw_data == 'yes':
        print(df.iloc[start_loc: start_loc + 5])
        start_loc += 5
        raw_data = input('\nWould You Like to See More Raw Data? Enter yes or no.\n').lower()
    print('All Desired Data are Displayed')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
    
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Thank You for Using Our Data Analysis System')
            break

if __name__ == '__main__':
        main()
