def get_formatted_name(first_name, last_name, middle_name = ''):
    """Return a full name, neatly formatted"""


    full_name = (f"{first_name}  {last_name}")

    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q)' at any time to quit")
if
    f_name = input("first_name: ")
    if f_name == "q":
       break

    l_name = input("last_name: ")

    if f_name == 'q':
        break
    formatted_name =get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}")

