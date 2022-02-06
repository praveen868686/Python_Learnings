#https://python.plainenglish.io/what-is-python-bytecode-e03a2f2d9263
#article on python being interpreted language or not


import dis
#
# def get_empty_dict():
#     return {}
#
# dis.dis(get_empty_dict)



def get_empty_dict():
    return dict()

dis.dis(get_empty_dict)
