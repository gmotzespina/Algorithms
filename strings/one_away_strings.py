def one_away_strings(string1, string2) -> bool:
    
    if string1 == string2:
        return True

    size_difference = abs(len(string1) - len(string2)) 

    if size_difference > 1:
        return False
    
    if(count_different_words(string1, string2) > 1):
        return False

    return True

def count_different_words(s1, s2) -> int:
    diff = abs(len(s1) - len(s2))
    s1 = list(s1)
    s2 = list(s2)
    shortest = s1 if len(s1) < len(s2) else s2
    longest = s2 if len(s2) > len(s1) else s1
    inserted = False if diff > 0 else True
    for index, char in enumerate(longest):
        if index == len(shortest):
            return True

        if shortest[index] != char:
            if diff == 1 and not inserted:
                shortest.insert(index, char)
                inserted = True
            else:
                diff += 1
    return diff




s1 = 'Holeb'
s2 = 'Heaeb'

print(one_away_strings(s1, s2))
