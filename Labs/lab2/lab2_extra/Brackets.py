

'''
Nicolas Van der Werf.

Worked Alone on this
'''
def Brackets(s):
    tracker = {'(':0,')':0,'[':0,']':0,'{':0,'}':0}
    for char in s:
        if tracker.get(char) != None:
            tracker[char] += 1
    if tracker['['] != tracker[']']:
        return False
    if tracker['{'] != tracker['}']:
        return False
    if tracker['('] != tracker[')']:
        return False
    return True
