def isEven(value):
    return value & 1 == 0

def isEven2(value):
    return value % 2 == 0

import dis

dis.dis(isEven)
dis.dis(isEven2)
