#Say you have a list value like this:
#spam = ['apples', 'bananas', 'tofu', 'cats']
#Write a function that takes a list value as an argument and returns
#a string with all the items separated by a comma and a space, with and inserted before the last item.
#For example, passing the previous spam list to the function would return 'apples, bananas, tofu, and cats'.
#But your func- tion should be able to work with any list value passed to it.
#Be sure to test the case where an empty list [] is passed to your function.

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
