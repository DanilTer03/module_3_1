calls = 0

def count_calls():
    global calls
    calls += 1
    
def string_info(string):
    count_calls()
    return  (len(string)), (string.upper()), (string.lower())

def is_contains(string, list_to_search):
    count_calls()

    for i in range(len(list_to_search)):
        flag = False
        for j in range(len(list_to_search)):
            if string.upper() in list_to_search[i].upper():
                flag = True
    return flag






print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic'])) # No matches
print(calls)