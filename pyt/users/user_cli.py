import users_ops

#
#  users>  
#  users>  add 
    #   enter id:  101
    #   enter name:  moshe
    #   enter pass:  12345678
    #   enter email:  a@b.c
    # added1!
#  users>  

def start_all():

    all_commands = make_commands_dict()
    all_users = users_ops.init_all_users()

    while(True):
        print('users> ', end='')
        user_command = input()
        if user_command == 'quit':
            break
        else:
            run_command(user_command, all_commands, all_users)


def run_command(command, all_commands, all_users):
    words = command.split()
    if words:
        if words[0] in all_commands:
            all_commands[words[0]] (all_users)
        else:
            print('no such command')


def handle_add_command(all_users):
    uid = input('enter id: ')
    uname = input('enter name: ')
    upass = input('enter password: ')
    umail = input('enter email: ')
    retval = users_ops.add_new_user(uid, uname, upass, umail, all_users)
    print(retval['description'])


def handle_delete_command(all_users):
    print('delete')

def handle_show_command(all_users):
    uid = input('enter user to print:')
    try:
        user_data = users_ops.get_user(uid, all_users)
        print('name: ', user_data['name']) 
        print('pass: ', user_data['pass'])
        print('email: ', user_data['mail'])
    except:
        print('no such user')





def make_commands_dict():
    commands_dict = {}
    commands_dict['add'] = handle_add_command
    commands_dict['del'] = handle_delete_command
    commands_dict['show'] = handle_show_command
    return commands_dict


start_all()