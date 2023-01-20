import time
from src.count_schools import print_counts, get_data_from_csv_file
from src.school_search import search_schools

def main():
    schools = get_data_from_csv_file("data/school_data.csv") 
    print("\n\n************************ Printing Counts ***********************")
    print_counts(schools)
    
    print("\n\n************************ Running Queries ***********************")
    queries = [
        "elementary school highland park",
        "jefferson belleville",
        "riverside school 44",
        "granada charter school",
        "foley high alabama",
        "KUSKOKWIM",
    ]
    
    for query in queries:
        search_schools(schools, query)        

if __name__=='__main__':
    main()