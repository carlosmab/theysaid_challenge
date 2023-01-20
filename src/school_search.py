import time


common_words = ["school", "of", "the", "and"]


def search_schools(schools: dict, query: str) -> list:
    start_time = time.time()
    keywords = query.lower().split(" ")
    found_schools = []
    
    for school in schools:
        search_string = f'{school["SCHNAM05"]} {school["LCITY05"]} {school["LSTATE05"]}'.lower() 
        match_score = sum(1 for kw in keywords if kw in search_string and kw not in common_words)
        
        if match_score >= 0:
            found_schools.append({
                "name": school["SCHNAM05"], 
                "city": school["LCITY05"], 
                "state": school["LSTATE05"],
                "match_score": match_score
            })
    
    # prioritizing by match_score by score and then alphabetically sorting
    found_schools.sort(key=lambda x: (x['match_score'], x['name']), reverse=True)
    
    end_time = time.time()    
    runtime_ms = (end_time - start_time) * 1000  
    
    print(f"\nResults found for '{query}'. (search took: {runtime_ms:.2f} ms)")  
         
    for index, value in enumerate(found_schools):
        if index > 2:
            print(f"{index + 1}. [Next Best Hit]")
            break
        print(f"{index + 1}. {value['name']}, {value['city']}, {value['state']}")
    
        