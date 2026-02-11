users = [
    {
        "name": "svinci",
        "salt": "098u n4v04",
        "hashed_password": "q423uinf9304fh2u4nf3410uth1394hf"
    },
    {
        "name": "admin",
        "salt": "0198234nva",
        "hashed_password": "3894tumn13498ujc843jmcv92384vmqv"
    }
]


def all_users():
    def discard_passwords(user):
        u = user.copy()
        del u["salt"]
        del u["hashed_password"]
        return u

    return list(map(discard_passwords, users))
    print(str(all_users()))


if __name__ == "__main__":
    us = all_users()
    for u in us:
        print(str(u))