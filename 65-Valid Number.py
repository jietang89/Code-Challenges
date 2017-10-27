# -*- coding: utf-8 -*-
# @Author: jietang
# @Date:   2017-10-27 15:57:13
# @Last Modified by:   jietang
# @Last Modified time: 2017-10-27 17:07:52

import re

def isNumber(s):
    """
    :type s: str
    :rtype: bool
    """
####solution 1: use regular expression
#     s = s.strip()
    # result1 = re.fullmatch('[\+\-]?[0-9]+\.?[0-9]*(e[\+\-]?[0-9]+)?',s)
#     if result1:
#     	return True
#     result2 = re.fullmatch('[\+\-]?\.[0-9]+(e[\+\-]?[0-9]+)?',s)
#     if result2:
#     	return True
#     return False

# ####solution 2: direct
# 	try: float(s)
# 	except ValueError: return False
# 	else: return True

####solution 3: re
    
    regex1 = re.compile('^[+-]?\d+$') #integer
    regex2 = re.compile('^[+-]?((\d*\.\d+)|(\d+\.\d*))$') #float
    regex3 = re.compile('^[+-]?((\d*\.\d+)|(\d+(\.\d*)?))e[+-]?\d+$') #scientific
    regex = re.compile('^[+-]?((\.\d+)|(\d+\.?\d*))(e[+-]?d+)?$') #numeric
    # ^:start $:at the end |:or
    return bool(regex.match(s.strip()))
    
    # return bool(self.regex.match(s.strip()))
# isNumber('1jkhk')
print(isNumber("1e"))