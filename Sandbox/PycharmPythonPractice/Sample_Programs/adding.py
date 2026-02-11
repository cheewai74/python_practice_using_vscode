def main():
    amt = 0
    while True:
        x = get_num()
        if x is None:
        #b, n = get_num()
        #if not b:
            break
        #amt += n
        amt += x
    print('The total is :', amt)

#def get_num(num = 0.0):
def get_num():
    s = input('Input number (ENTER to quit): ')
    if not s:
        # return False, num
        return None
    else:
        #return True, float(s)
        return float(s)

main()