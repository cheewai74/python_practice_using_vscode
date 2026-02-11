name_for_userid = {
    382: 'Alice',
    950: 'Bob',
    590: 'Dilbert',
}


def greeting(userid):
    return 'Hi %s!' % name_for_userid[userid]

greeting(382)


def greeting(userid):
    try:
        return 'Hi %s!' % name_for_userid[userid]
    except KeyError:
        return 'Hi there\n'


def greeting(userid):
    return 'Hi %s!' % name_for_userid.get(userid, 'there')