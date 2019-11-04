def contains_type(s, validator):
    return any(map(validator, list(s)))
    
def solution(s):
    print(contains_type(s, str.isalnum))
    print(contains_type(s, str.isalpha))
    print(contains_type(s, str.isdigit))
    print(contains_type(s, str.islower))
    print(contains_type(s, str.isupper))
    
