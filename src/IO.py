import redisHandler
import Taqqiq
import utils


def new_service():
    print('New Service')
    serv_login = dict()
    serv_name = input("New service name: ")
    r = utils.init_redis()
    if redisHandler.chk_serv_exists(serv_name, r):
        print("An entry for this service already exists")
        do_edit = (input("Do you wish to edit this entry? [y/N]: ")).lower()
        while do_edit not in ['y', 'n', 'yes', 'no']:
            do_edit = (input("Do you wish to edit this entry? [y/N]: ")).lower()
        if do_edit in ['y', 'yes']:
            utils.kill_redis_conn(r)
            edit_service()
        else:
            utils.kill_redis_conn(r)
            Taqqiq.entry()
    else:
        serv_login['serv_name'] = serv_name
        serv_login['user_name'] = utils.encrypt_val(input("Username: "))
        serv_login['passwd'] = utils.encrypt_val(input("Password: "))
        if redisHandler.chk_password(utils.decrypt_val(serv_login['passwd']), r):
            print("This password is in use for a different account. It is not recommended to re-use passwords.")
            new_pass_q = input("Do you wish to create a new password? [y/N]: ").lower()
            while new_pass_q not in ['y', 'n', 'yes', 'no']:
                new_pass_q = input("Do you wish to create a new password? [y/N]: ").lower()
            if new_pass_q in ['y', 'yes']:
                print("Remember to change the password at the account preferences as well!")
                serv_login['passwd'] = utils.encrypt_val(input("New Password: "))
        num_secq = int(input("How many security questions: "))
        if num_secq > 0:
            for i in range(num_secq):
                serv_login['secq' + str(i + 1)] = utils.encrypt_val(input("Security question " + str(i + 1) + ": "))
                serv_login['sec_ans' + str(i + 1)] = utils.encrypt_val(input("Answer: "))
        serv_login['numq'] = num_secq
        redisHandler.put(serv_login, r)
        utils.kill_redis_conn(r)
        Taqqiq.entry()


def retrieve_service():
    print('Retrieve Service')
    serv_name = input("Service name: ")
    r = utils.init_redis()
    if redisHandler.chk_serv_exists(serv_name, r):
        key = redisHandler.get(serv_name, r)
        print('Service: ' + key['serv_name'.encode()].decode())
        print('Username: ' + utils.decrypt_val(key['user_name'.encode()]).decode())
        print('Password: ' + utils.decrypt_val(key['passwd'.encode()]).decode())
        num_ques = int(key['numq'.encode()].decode())
        if num_ques:
            for n in range(num_ques):
                print('Security question ' + str(n + 1) + ': '
                      + utils.decrypt_val(key[('secq' + str(n + 1)).encode()]).decode())
                print('Security Answer ' + str(n + 1) + ': '
                      + utils.decrypt_val(key[('sec_ans' + str(n + 1)).encode()]).decode())
        ret_entry = input("return to entry screen? [y]: ").lower()
        while ret_entry not in ['y', 'yes']:
            ret_entry = input("return to entry screen? [y]: ").lower()
        if ret_entry in ['y', 'yes']:
            utils.kill_redis_conn(r)
            Taqqiq.entry()
    else:
        utils.kill_redis_conn(r)
        print("No entry exists for " + serv_name)
        new_entry = input("Would you like to create one? [y/N]: ").lower()
        while new_entry not in ['y', 'n', 'yes', 'no']:
            new_entry = input("Would you like to create one? [y/N]: ").lower()
        if new_entry in ['y', 'yes']:
            utils.kill_redis_conn(r)
            new_service()
        else:
            utils.kill_redis_conn(r)
            Taqqiq.entry()


def edit_service():
    print('Edit Service')
    serv_name = input("Service name: ")
    r = utils.init_redis()
    if redisHandler.chk_serv_exists(serv_name, r):
        print("Which fields do you wish to edit:")
        serv_keys = redisHandler.get(serv_name, r).keys()
        for k in serv_keys:
            print(k.decode())
        print("Enter the fields you wish to edit, separated by commas")
        fields_to_edit = input("Example: serv_name,secq1,user_name: ")
        fields = fields_to_edit.split(",")
        for f in fields:
            print('Current ' + f + ": " + utils.decrypt_val(redisHandler.get(serv_name)[f.encode()]).decode())
            new_field_val = utils.encrypt_val(input("Enter the new " + f + ": "))
            redisHandler.edit(serv_name, f, new_field_val, r)
        utils.kill_redis_conn(r)
        Taqqiq.entry()
    else:
        print("No entry exists for " + serv_name)
        utils.kill_redis_conn(r)
        Taqqiq.entry()


def delete_service():
    print('Delete Service')
    serv_name = input("Service name: ")
    r = utils.init_redis()
    if redisHandler.chk_serv_exists(serv_name, r):
        confirm = (input("Are you sure you wish to delete " + serv_name + " [y/N]: ")).lower()
        while confirm not in ['y', 'n', 'yes', 'no']:
            confirm = (input("Are you sure you wish to delete " + serv_name + " [y/N]: ")).lower()
        if confirm in ['y', 'yes']:
            redisHandler.delete(serv_name, r)
            print("Entry for " + serv_name + " has been deleted.")
            utils.kill_redis_conn(r)
            Taqqiq.entry()
        else:
            utils.kill_redis_conn(r)
            Taqqiq.entry()
    else:
        print("No entry exists for " + serv_name)
        utils.kill_redis_conn(r)
        Taqqiq.entry()


def delete_all():
    print('Delete All')
    print("Are you sure? This is will delete all entries in the Taqqiq.")
    print("This action is irreversible.")
    del_all = input("[y/N]: ").lower()
    while del_all not in ['y', 'n', 'yes', 'no']:
        del_all = input("[y/N]: ").lower()
    if del_all in ['y', 'yes']:
        r = utils.init_redis()
        redisHandler.erase_all(r)
        utils.kill_redis_conn(r)
        print("All entries in Taqqiq have been deleted.")
        Taqqiq.entry()
    else:
        Taqqiq.entry()


def retrieve_all():
    print('Retrieve All')
    r = utils.init_redis()
    key_list = redisHandler.get_all(r)
    key_list.sort()
    if key_list:
        for k in key_list:
            print(k[0].decode())
        ret_entry = input("return to entry screen? [y]: ").lower()
        while ret_entry not in ['y', 'yes']:
            ret_entry = input("return to entry screen? [y]: ").lower()
        if ret_entry in ['y', 'yes']:
            utils.kill_redis_conn(r)
            Taqqiq.entry()
    else:
        print("No entries in Taqqiq")
        utils.kill_redis_conn(r)
        ret_entry = input("return to entry screen? [y]: ").lower()
        while ret_entry not in ['y', 'yes']:
            ret_entry = input("return to entry screen? [y]: ").lower()
        if ret_entry in ['y', 'yes']:
            Taqqiq.entry()


def Taqqiq_exit():
    pass

