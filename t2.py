import os
from cryptography.fernet import Fernet

key = b"DaeQGMLoJeIeL1uddcikWJ8l4uNm1wvKQfkxxVfCp0U="

# with open('mykey.key', 'wb') as mykey:
#     mykey.write(key)
f = Fernet(key)

def fl_encrpt(fl_name, i):
    with open(fl_name, 'rb') as original_file:
        original = original_file.read()

    encrypted = f.encrypt(original)
    flnm_encrpt = f.encrypt(bytes(fl_name, "utf-8"))
    # with open(os.path.dirname(fl_name) + '/cry_in_shadow'+str(i)+'.png', 'wb') as encrypted_file:
    #     encrypted_file.write(encrypted + b"<$$<cry_in_shadow>$$>" + flnm_encrpt)
    with open(fl_name, 'wb') as encrypted_file:
        encrypted_file.write(encrypted + b"<$$<cry_in_shadow>$$>" + flnm_encrpt)
    os.replace(fl_name, os.path.dirname(fl_name) + '/cry_in_shadow'+str(i)+'.png')

def fl_dcrpt(fl_name):
    with open(fl_name, "rb") as encrypted_file:
        encrypted = encrypted_file.read()
    encrypted_data = encrypted.split(b"<$$<cry_in_shadow>$$>")[0]
    encrypted_fl_name = encrypted.split(b"<$$<cry_in_shadow>$$>")[1]
    original = f.decrypt(encrypted_data)
    or_name = f.decrypt(encrypted_fl_name)
    # with open(str(or_name, encoding="utf-8"), "wb") as original_file:
    #     original_file.write(original)
    with open(fl_name, "wb") as original_file:
        original_file.write(original)
    os.replace(fl_name, str(or_name, encoding="utf-8"))

def enc_fl(fl_path):
    cnt = 0
    for fl in os.listdir(fl_path):
        fl_encrpt(fl_path + "/" + fl, cnt)
        cnt+=1
        # print(fl)

def dec_fl(fl_path):
    for fl in os.listdir(fl_path):
        # if "cry_in_shadow" in fl_path:
        fl_dcrpt(fl_path + "/" + fl)

print(os.getcwd())
# enc_fl("encrypt_me")
dec_fl("encrypt_me")