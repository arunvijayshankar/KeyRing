import utils


def put(serv_login, r):
    r.setnx('new_serv_id', 0)
    r.incr('new_serv_id')
    serv_id = 'serv:' + str(r.get('new_serv_id'))
    r.hmset(serv_id, serv_login)
    r.hset('services', serv_login['serv_name'], serv_id)


def get(serv_name, r):
    serv_id = r.hget('services', serv_name)
    return r.hgetall(serv_id)


def get_all(r):
    key_list = list()
    for s in r.hvals('services'):
        key_list.append(r.hmget(s, 'serv_name'))
    return key_list


def delete(serv_name, r):
    serv_id = r.hget('services', serv_name)
    r.delete(serv_id)
    r.hdel('services', serv_name)
    r.decr('new_serv_id')


def edit(serv_name, field, val, r):
    serv_id = r.hget('services', serv_name)
    r.hset(serv_id, field, val)


def erase_all(r):
    r.flushdb()


def chk_password(passwd, r):  # move to redisHandler
    passwd_list = []
    serv_id_list = r.hvals('services')
    for sid in serv_id_list:
        passwd_list.append(utils.decrypt_val(r.hmget(sid, 'passwd'.encode())[0]).decode())
    if passwd.decode() in passwd_list:
        return True
    else:
        return False


def chk_serv_exists(serv_name, r):
    if r.hexists('services', serv_name):
        return True
    else:
        return False
