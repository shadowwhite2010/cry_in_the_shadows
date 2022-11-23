import random
# test_str = "DaeQGMLoJeIeL1uddcikWJ8l4uNm1wvKQfkxxVfCp0U="
def rand_str(c):
    cnt = ord(c)
    return ''.join(random.choices("01", k=cnt))

def BinaryToDecimal(binary):
    # binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return (decimal)



# enrypts the message according to user name
def encpt_pswd(e_str, u_name):
    res = ''.join(format(ord(i), '08b') for i in e_str)
    # print(res, type(res))
    t_res = ""
    s = 0
    for i in range(0, len(res), 8):
        t_res = t_res + rand_str(u_name[s]) + res[i:i + 8]
        s+=1
        s%=len(u_name)
    return t_res
    
# print(type(t_res), t_res)
# enrypts the message according to user name
def dcpt_pswd(pswd):
    s = 0
    i = 0
    tstr_data = ""
    try:
        while(i<len(pswd)):
            i+=ord(u_name[s])
            temp_data = int(pswd[i:i + 8])
            i = i+8
            decimal_data = BinaryToDecimal(temp_data)
            tstr_data = tstr_data + chr(decimal_data)
            s+=1
            s%=len(u_name)
    except: pass
    return tstr_data


if __name__ == "__main__":
    # pswd = encpt_pswd(test_str)
    # with open("test_fld/magic.txt", "w") as fl:
    #     fl.write(pswd)
    u_name = "Ojas"
    # u_name = os.getlogin()
    test_str = "I am Shadow White"
    pswd = encpt_pswd(test_str, u_name)
    with open("test_fld/pswd_ojas.txt", "w") as fl:
        fl.write(pswd)
    print(dcpt_pswd(pswd))



# this code decodes the binary string to normal string
# str_data = ""
# for i in range(0, len(res), 8):
#     temp_data = int(res[i:i + 8])
#     decimal_data = BinaryToDecimal(temp_data)
#     str_data = str_data + chr(decimal_data)
# print(str_data)
