# A program for IP validation

# Example:

# 192.168.1.1 is valid

# 999.999.999.999 is invalid

def ip(s):
    arr = s.split(".")
    new_arr = []
    octet_count = None
    octet_value = None
    octet_range = None
    length = len(arr)
    
    if length == 4:
        octet_count = True
    else:
        octet_count = False
        print("4 Octet do not exist")

    if octet_count == True:
        try:
            for elm in arr:
                new_arr.append(int(elm))
            octet_value = True
        except ValueError:
            octet_value = False
            print("Integer value not present")

    if octet_value == True:
        for elm in new_arr:
            if ((elm < 0) or (elm > 255)):
                print('Invalid IP Address')
                octet_range = False
                break
            else:
                octet_range = True
    
    if octet_range == True:
        print("Valid IP address")


ip("192.168.a.1")