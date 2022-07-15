import codecs

def encode(s):
    if not isinstance(s,str):
        raise TypeError
    origlen = len(s)
    crypted = ""
    digitmapping = dict(zip('1234567890!"#€%&/()=','!"#€%&/()=1234567890'))
    banned = 'öäåÖÄÅ '
    #banned2 = '+'
    if len(s) > 1000:
        raise ValueError
    new_s = s.ljust(1000, "a") 
    for c in new_s:
        if c.isalpha():
            if c.islower():
                c=c.upper()
                if c in banned:
                    raise ValueError
            # Rot13 the character for maximum security
            crypted+=codecs.encode(c,'rot13')
        elif c in digitmapping:
          crypted+=digitmapping[c]
        else:
            raise ValueError
            
    return crypted[:origlen]

def decode(s):
    if not isinstance(s,str):
         raise TypeError
    origlen = len(s)
    crypted = ""
    digitmapping = dict(zip('!"#€%&/()=1234567890','1234567890!"#€%&/()='))
    banned = 'öäåÖÄÅ'
    #banned2 = '+'
    if len(s) > 1000:
        raise ValueError
    new_s = s.ljust(1000, "a") 
    for c in new_s:
        if c.isalpha():
            if c.isupper():
                c=c.lower()
                if c in banned:
                    raise ValueError
            # Rot13 the character for maximum security
            crypted+=codecs.decode(c,'rot13')
        elif c in digitmapping:
          crypted+=digitmapping[c]
        else:
            raise ValueError
            
    return crypted[:origlen]

