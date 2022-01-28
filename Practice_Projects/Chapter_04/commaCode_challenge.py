spam = ['Riker', 46, 'lumbar spine', True]

def groceries(note):
    string_list = ''

    for item in note:
        if item == note[-1]:
            string_list += f'and {item}'
            return str(string_list)
        elif item != note[-1]:
            string_list += f'{item}, '

phrase = groceries(spam)
print(phrase)
