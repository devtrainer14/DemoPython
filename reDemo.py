import re
#x=re.search('ab','Here is ab absolute string')
"""x=re.match('Here','Here is ab absolute string')
print(x.group())	# another additional methods work with match object.
print(x.start())
print(x.end())
print(x.span())"""

x = re.match(r"(...)+","edureka")
print(x.group(1))