from fuzzywuzzy import fuzz

# compare cell values in the columns to find duplicates

def same_phone(r1, r2):
    return r1['phone'] == r2['phone']

def same_area_code(r1, r2):
    return r1['phone'].split(' ')[0] == r2['phone'].split(' ')[0]

def same_name(r1, r2):
    return fuzz.ratio(r1['name'], r2['name']) > 75

def similar_address(r1, r2):
    return (
            fuzz.ratio(r1['address'], r2['address']) > 55 or
            fuzz.partial_ratio(r1['address'], r2['address']) > 75
    )

def similar_name(r1, r2):
    return fuzz.partial_ratio(r1['name'], r2['name']) > 50

def same_restaurant(r1, r2):
    return (
            (
                    same_phone(r1, r2) and
                    similar_name(r1, r2)
            ) or
            (
                    same_area_code(r1, r2) and
                    same_name(r1, r2) and
                    similar_address(r1, r2)
            )
    )

