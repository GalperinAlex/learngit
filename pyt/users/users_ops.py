
# This is how users will be stored:
# {
#     15:{'name': "yuval", 'pass': '12345678', 'email':'a@b.com'},
#     29.4:{'name': "moshe", 'pass': '99999999', 'email':'x@y.com'}
# }


def init_all_users():
    return {}

def add_new_user(user_id, user_name, user_password, user_email, all_users):
    retval = {}
    if user_id in all_users:
        retval['code'] = -1
        retval['description'] = "user exists"
    else:
        all_users[user_id] = {'name':user_name, 'mail':user_email, 'pass':user_password}
        retval['code'] = 0
        retval['description']  = "inserted"
    return retval


def delete_users(user_id, all_users):
    if user_id in all_users:
        del all_users[user_id]
        status = 'deleted'
    else:
        status = 'no such user'
    return status


def get_user(user_id, all_users):
    if user_id in all_users:
        user_details = all_users[user_id]
    else:
        raise ValueError
    
    return user_details


