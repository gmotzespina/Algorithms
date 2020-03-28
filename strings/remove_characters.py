given_string = 'This is a test tring'
characters_to_remove = 'aeiou'

given_string = list(given_string)
characters_to_remove = set(characters_to_remove)

for index in range(len(given_string)):
    if given_string[index] in characters_to_remove:
        given_string.pop(index)

print(given_string)
