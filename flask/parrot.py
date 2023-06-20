def build_profile(first,last, **user_info):
    """BUild  a dictionary containing everything we know about the user"""

    user_info['first_name'] = first
    user_info['last_name'] = last

    return user_info 



user_profile  = build_profile('albert', 'einstein', location = 'princeton',
                             field = 'Physics')

print(user_profile)

