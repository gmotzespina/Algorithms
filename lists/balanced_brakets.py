brackets = ['{{([])}}','{{)[](}}']

def are_brackets_balanced(brackets):
    brackets_array = list(brackets)
    
    left_brackets = []
    right_brackets = []

    brackets_a_length = len(brackets_array)

    if brackets_a_length%2 != 0:
        return 'NO'

    index = 0
    # print(brackets_a_length-2)
    for _ in range(brackets_a_length-2):
      #  print(index)
        if index > brackets_a_length-1:
            break

        if is_left_bracket(brackets_array[index]):

            result = bracket_matches(brackets_array[index], brackets_array[index+1])

            if result == False:
                if is_left_bracket(brackets_array[index]):
                    left_brackets.append(brackets_array[index])
                else:
                    right_brackets.insert(0, brackets_array[index])
            else:
                index += 1

        else:
            right_brackets.insert(0, brackets_array[index])

            if index == brackets_a_length-2:
                if is_left_bracket(brackets_array[index+1]):
                        return 'NO'
                else:
                    right_brackets.insert(0, brackets_array[index+1])
                break

        index += 1

    print('Right brackets {}'.format(right_brackets))
    print('Left brackets {}'.format(left_brackets))

    index = 0
    right_b_length = len(right_brackets)
    left_b_length = len(left_brackets)

    print(right_b_length)
    print(left_b_length)

    if right_b_length != left_b_length:
        return 'NO'

    for _ in range(right_b_length):
        if bracket_matches(left_brackets[index], right_brackets[index]) == False:
            return 'NO'
    
   #  print('Right brackets {}'.format(right_brackets))
   #  print('Left brackets {}'.format(left_brackets))

    return 'YES'

def get_left_bracket(bracket):

    matching_bracket = {
            ')': '(',
            ']': '[',
            '}': '{'
            }

    return matching_brackets[bracket];

def is_left_bracket(bracket):
    left_brackets = ['{', '(', '[']
    return bracket in left_brackets


def bracket_matches(bracket1, bracket2):

    matching_brackets = {
            '{': '}',
            '[': ']',
            '(': ')'
            }

    if matching_brackets[bracket1] == bracket2:
        return True

    return False

for bracket_string in brackets:
    result = are_brackets_balanced(bracket_string)
    print(result)
