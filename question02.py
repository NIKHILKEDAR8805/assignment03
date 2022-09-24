from shutil import register_unpack_format


def reverse(s):
    
    return s[::-1]
s = "1234abcd"
print('original string :',s)
print('reversed string :',reverse(s))