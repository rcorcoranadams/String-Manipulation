# Rachel Corcoran-Adams
# September 25, 2020
# This exercise produces the output below using string manipulation techniques:
  # Tonight: Clear, Low: 55 F
  # Thursday: Sunny then Chance Showers, High: 77 F
  # Friday: Sunny, High: 73 F
  # Saturday: Mostly Sunny, High: 77 F
  # Sunday: Mostly Sunny, High: 71 F

# This part tells the computer what encoding the string is stored in 
forecast = '''

Tonight
ClearLow: 55 F

Thursday
Sunny thenChanceShowersHigh: 77 F

Friday
SunnyHigh: 73 F

Saturday
Mostly SunnyHigh: 77 F

Sunday
Mostly SunnyHigh: 71 F
'''
# This reates a list item at every instance of separator
forecast_list = forecast.split('\n\n')
# This line creates a for loop to edit the strings in the list
for day in forecast_list:
    # These lines replace the strings and add spaces or commas to mimic the desired output
    day = day.replace('\n',' ')
    day = day.replace('High',', High')
    day = day.replace('Chance',' Chance')
    day = day.replace('Showers',' Showers')
    day = day.replace('Low',', Low')
    # This line prints the output
    print(day)
