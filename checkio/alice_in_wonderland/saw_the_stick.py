def build_tri_num_list(limit):
    result = []
    last_number = 1
    counter = 2
    while last_number <= limit:
        result.append(last_number)
        last_number += counter
        counter += 1
    return result

def checkio(number):
    tri_nums = build_tri_num_list(number)
    len_tri_nums = len(tri_nums)
    
    for left_end in range(len_tri_nums):
        for right_end in range(left_end, len_tri_nums):
            subarr = tri_nums[left_end:right_end]
            sum_subarr = sum(subarr)
            
            if sum_subarr == number:
                return subarr
            elif sum_subarr > number:
                continue
    return []

def test():
    assert checkio(64) == [15, 21, 28], "1st example"
    assert checkio(371) == [36, 45, 55, 66, 78, 91], "1st example"
    assert checkio(225) == [105, 120], "1st example"
    assert checkio(882) == [], "1st example"
