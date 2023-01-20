import csv
from itertools import groupby


def get_data_from_csv_file(filename: str, sep: str=",") -> dict:
    """Returns data from a csv file"""
    
    with open(filename, mode="r") as f:
        data = list(csv.DictReader(f))
    return data
     
     
def get_schools_by_column(schools: dict, column: str) -> groupby: 
    """Returns a groupby object with schools grouped by given column"""
    
    schools.sort(key=lambda x: x[column])
    return groupby(schools, lambda x: x[column])
    
    
def print_total_schools(schools: dict) -> None:
    """Prints the school list length"""
    
    print(f"\nTotal Schools: {len(schools)}")
    
    
def print_schools_by_column(schools: dict, column: str, column_title: str) -> None:
    """Prints how many schools are in each value of the given column"""
    
    schools_by_column = get_schools_by_column(schools, column) 
    print(f"\nSchools by {column_title}: \n")
    for column_value, school_list in schools_by_column:
        print(f"{column_value} : {sum(1 for x in school_list)} \n") 
    

def print_city_most_schools(schools):
    """Prints the city with most number of schools in it"""
    
    schools_by_cities = get_schools_by_column(schools, "LCITY05")
    max_schools = 0
    for city, school_list in schools_by_cities:
        quantity = sum(1 for x in school_list)
        if quantity > max_schools:
            max_schools = quantity
            city_max = city
    
    print(f"City with most schools: {city_max} ({max_schools} schools)")


def print_cities_with_one_more_schools(schools):
    """Prints the cities with have one o more schools in it"""
    
    schools_by_cities = get_schools_by_column(schools, "LCITY05")
    cities = sum(1 for x in schools_by_cities)
    print(f"Unique cities with at least one school {cities}")


def print_counts(schools) -> None:
    """Solves the challenge's tasks"""
             
    print_total_schools(schools)
    print_schools_by_column(schools, "LSTATE05", "State")
    print_schools_by_column(schools, "MLOCALE", "Metro-centric")
    print_city_most_schools(schools)
    print_cities_with_one_more_schools(schools)
    

