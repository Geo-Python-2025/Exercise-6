
#!/usr/bin/env python
from points_decorator import points
import inspect
import pandas as pd
import os

class TestProblem1:
    @points(0.5, "Problem 1, Part 1: Did you correctly read the csv file into the dataframe 'data'?")
    def test_problem_1_part_1_fuction(self, problem1):
        section_data, namespace = problem1
        section = "Part 1"  # Define the section key

        # Check if section exists in the dictionary
        assert section in section_data, f"Section '{section}' not found in section_data"

        # Extract variables from section data
        variables = section_data[section]['variables']

        # Assert that 'data' is a DataFrame
        assert isinstance(namespace['data'], pd.DataFrame)

    @points(0.5, "Problem 1, Part 2: Does 'data' contain the correct columns, is the first row right and nan values removed?")
    def test_problem_1_part_2(self, problem1):
        section_data, namespace = problem1
        section = "Part 1"  # Define the section key

        # Check if section exists in the dictionary
        #assert section in section_data, f"Section '{section}' not found in section_data"

        # Extract variables from section data
        variables = section_data[section]['variables']
        data = variables['data']   

        # Assert the length of 'data'
        assert(data.columns.tolist()) == ['STATION', 'ELEVATION', 'LATITUDE', 'LONGITUDE', 'DATE', 'PRCP', 'TAVG', 'TMAX', 'TMIN']
        assert list(data.loc[0].values) == ['GHCND:FIE00142080', 51, 60.3269, 24.9603, 19520101, 0.31, 37.0, 39.0, 34.0]
        assert pd.isna(data.tail(1)[['TMIN']].values[0][0])

    @points(0.1, "Problem 1, Part 2: Incorrect amount of NaN values in the TAVG column!")
    def test_problem_1_part_2_tavg(self, problem1):
        section_data, namespace = problem1
        section = "Part 2"  # Define the section key
        assert namespace['tavg_nodata_count'] == 3308

        
    @points(0.1, "Problem 1, Part 2: Incorrect amount of NaN values in the TMIN column!")
    def test_problem_1_part_2_tmin(self, problem1):
        section_data, namespace = problem1
        section = "Part 2"  # Define the section key
        assert namespace['tmin_nodata_count'] == 365
    
    @points(0.1, "Problem 1, Part 2: Variable 'day_count' is not correctly defined!")
    def test_problem_1_part_2_daycount(self, problem1):
        section_data, namespace = problem1
        section = "Part 2"  # Define the section key
        assert namespace['day_count'] == 23716

    @points(0.1, "Problem 1, Part 2: Variable 'first_obs' is not correctly defined!")
    def test_problem_1_part_2_firstobs(self, problem1):
        section_data, namespace = problem1
        section = "Part 2"  # Define the section key
        assert namespace['first_obs'] == 19520101

    @points(0.1, "Problem 1, Part 2: Variable 'last_obs' is not correctly defined!")
    def test_problem_1_part_2_lastobs(self, problem1):
        section_data, namespace = problem1
        section = "Part 2"  # Define the section key
        assert namespace['last_obs'] == 20171004

    @points(0.1, "Problem 1, Part 2: Variable 'avg_temp' is not correctly defined!")
    def test_problem_1_part_2_avgtemp(self, problem1):
        section_data, namespace = problem1
        section = "Part 2"  # Define the section key
        assert round(namespace['avg_temp']),2 == 41.32

    @points(0.4, "Problem 1, Part 2: Variable 'avg_temp_1969' is not correctly defined!")
    def test_problem_1_part_2_avgtemp1969(self, problem1):
        section_data, namespace = problem1
        section = "Part 2"  # Define the section key
        assert round(namespace['avg_temp_1969']),2 == 67.82     


    ###Problem 2###

    @points(3.0, "Problem 2, Part 1: Did you correctly read the csv file into the dataframe 'data'?")
    def test_problem_2_part_1_df(self, problem1):
        section_data, namespace = problem1
        section = "Part 3"  # Define the section key

        # Check if section exists in the dictionary
        assert section in section_data, f"Section '{section}' not found in section_data"

        # Extract variables from section data
        variables = section_data[section]['variables']

        # Assert that 'data' is a DataFrame
        assert isinstance(namespace['monthly_data'], pd.DataFrame)


    @points(3.0, "Problem 2, Part 1: Did you create a DataFrame 'monthly_data' ?")
    def test_problem_2_part_1_df(self, problem1):
        section_data, namespace = problem1
        section = "Part 3"  # Define the section key

        # Check if section exists in the dictionary
        assert section in section_data, f"Section '{section}' not found in section_data"

        # Extract variables from section data
        variables = section_data[section]['variables']

        # Assert that 'data' is a DataFrame
        assert isinstance(namespace['monthly_data'], pd.DataFrame)


    @points(1.0, "Problem 2, Part 1: Did you create a DataFrame 'monthly_data' ?")
    def test_problem_2_part_1_df(self, problem1):
        section_data, namespace = problem1
        section = "Part 3"  # Define the section key

        # Check if section exists in the dictionary
        assert section in section_data, f"Section '{section}' not found in section_data"

        # Extract variables from section data
        variables = section_data[section]['variables']

        # Assert that 'data' is a DataFrame
        assert isinstance(namespace['monthly_data'], pd.DataFrame)


    @points(1.0, "Problem 2, Part 1: Something is wrong with the 'monthly_data' DataFrame!")
    def test_problem_2_part_1_monthly_data(self, problem1):
        section_data, namespace = problem1
        section = "Part 3"  # Define the section key

        # Check if section exists in the dictionary
        assert section in section_data, f"Section '{section}' not found in section_data"

        # Extract variables from section data
        variables = section_data[section]['variables']

        monthly_data = variables['monthly_data']

        # Assert that 'data' is a DataFrame
        assert len(monthly_data) == 790


    @points(1.0, "Problem 2, Part 1: Something is wrong with the 'temp_celsius' column!")
    def test_problem_2_part_1_temp_celsius(self, problem1):
        section_data, namespace = problem1
        section = "Part 3"  # Define the section key

        # Check if section exists in the dictionary
        assert section in section_data, f"Section '{section}' not found in section_data"

        # Extract variables from section data
        variables = section_data[section]['variables']

        monthly_data = variables['monthly_data']
        assert round(monthly_data['temp_celsius'].mean(), 2) == 5.1

        assert round(monthly_data['temp_celsius'].median(), 2) == 4.73



    @points(1.0, "Problem 3, Part 1: Does the 'monthly_data' DataFrame contain the correct columns?")
    def test_problem_3_part_1_temp_celsius(self, problem1):
        section_data, namespace = problem1
        section = "Part 4"  # Define the section key

        # Check if section exists in the dictionary
        assert section in section_data, f"Section '{section}' not found in section_data"

        # Extract variables from section data
        variables = section_data[section]['variables']

        monthly_data = variables['monthly_data']
        
        answer_columns = list(monthly_data.columns.str.lower())
        assert 'month' in answer_columns and 'diff' in answer_columns and 'ref_temp' in answer_columns

    
    @points(1.0, "Problem 3, Part 2: Something is wrong with the values of the 'diff' column!")
    def test_problem_3_part_2_diff(self, problem1):
        section_data, namespace = problem1
        section = "Part 5"  # Define the section key

        # Check if section exists in the dictionary
        assert section in section_data, f"Section '{section}' not found in section_data"

        # Extract variables from section data
        variables = section_data[section]['variables']

        monthly_data = variables['monthly_data']
        
        assert(str(monthly_data['diff'].mean())[:5] == '0.722')
               
        assert(str(monthly_data['diff'].min())[:6] == '-12.13')
                      
        assert(int(monthly_data['diff'].max()) == 8)

    @points(1.0, "Problem 3, Part 2: Something is wrong with the maximum and minimum values of the 'diff' column!")
    def test_problem_3_part_2_anomalies(self, problem1):
        section_data, namespace = problem1
        section = "Part 5"  # Define the section key

        # Check if section exists in the dictionary
        assert section in section_data, f"Section '{section}' not found in section_data"

        # Extract variables from section data
        variables = section_data[section]['variables']

        monthly_data = variables['monthly_data']

        assert round(monthly_data["diff"].abs().max(),2) == 12.14

        assert round(monthly_data["diff"].max(),2) == 8.23

        assert round(monthly_data["diff"].min(),2) == -12.14
        
        
