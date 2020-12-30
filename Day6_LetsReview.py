for i in range(int(input())):
    s = input()
    print (''.join(s[c] for c in range(0,len(s), 2)), ''.join(s[c] for c in range(1,len(s), 2)))
