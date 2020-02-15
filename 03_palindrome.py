user = raw_input("Enter text: ")
user_lower = str.lower(user)
user_space = user_lower.replace(" ", "")
punctuations = '''!()-{};:'"\,<>=?@[/^]_|~#$%&*'''
new_text = ""

for char in user_space:
    if char not in punctuations:
        new_text = new_text + char

palindrome_user_reverse = (new_text[::-1])

if new_text == palindrome_user_reverse:
    print("This is a palindrome")

else:
    print("This is not a palindrome")

