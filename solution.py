import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Please Select A City To Explore: chicago, new york city, washington: \n  ').lower()
    
    while city not in CITY_DATA.keys():
        print("invalid input, please re-enter the city name")
        city = input('Please Select A City To Explore: Chicago, new york city, washington: \n ').lower()
   
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january' , 'february', 'march', 'april', 'may', 'june', 'all']
    month = input('please select month to explore from January:June, or All for six months \n').lower()
    
    while month not in months:
        print("Invalid month input, please try again")
        
        month = input('please select amonth to explore from January:June, or All for all six months').lower()
    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input("Please select a week day to explore, or all to explore all week days \n ").lower()
    
    while day not in days:
        print("invalid input")
        day = input("Please select a week day to explore, or all to explore all week days \n ").lower()

    print('-'*40)
    return city, month, day 

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1 
        df = df[df['month']==month]
        
    if day != 'all':
        df = df[df['day_of_week'].str.startswith(day.title())]
        
        
    
    return df

def time_stats(df):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    common_month = df['month'].mode()[0]
    print('Most popular month: ', common_month)
    
    common_day = df['day_of_week'].mode()[0]
    print('most common day of week: ', common_day)
    
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('the most common hour: ', common_hour)
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
   
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()  
    
    common_start_station = df['Start Station'].mode()[0]
    print(' the most common start station is:  ', common_start_station)
    
    common_end_station = df['End Station'].mode()[0]
    print(' the most common end station is: ', common_end_station)
    
    df['combination'] = df['Start Station'] + ' - ' + df['End Station']
    common_combination = df['combination'].mode()[0]
    print(' the most common combination of start station and end station trip is: ', common_combination)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def trip_duration_stats(df):
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    
    total_travel_time = df['Trip Duration'].sum()
    print('total travel time is: ', total_travel_time)
    
    mean_travel_time = df['Trip Duration'].mean()
    print('mean travel time is: ', mean_travel_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
   
    print('\nCalculating User Stats...\n')
    start_time = time.time()  
    count_user_types = df['User Type'].count()
    print('the count of user type is:', count_user_types)
    
    try:
        print('the count of gender is:', df['Gender'].value_counts())
        print('earliest year of birth:', df['Birth Year'].min())
        print('most recent year of birth:', df['Birth Year'].max())
        print('most commom year of birth:', df['Birth Year'].mode()[0])      
    except KeyError:
        print('column not exist')
      
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def view_data(df):
    start_location = 0
    answer = ['yes', 'no']
    question = input('\nWould you like to view 5 rows of trip data? Enter Yes or No: \n').lower()
    while question not in answer:
        print('invalid response, Would you like to view 5 rows of trip data? Enter Yes or No: \n').lower()  
    if question == 'no':
        print("end")
    while question == 'yes':
        print(df.iloc[start_location : start_location + 5])
        start_location += 5
        question = input('Do you want to continue displaying data?')
    
            
                       
               
      
    
    
    
    


                  
                     
              
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        view_data(df)
                  
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
