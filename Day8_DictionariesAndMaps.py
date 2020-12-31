dt = {}
for _ in range(int(input())):
    name, ph = input().split()
    dt[name] = ph

while True:
    try:
        name = input()
        if name in dt:
            print('%s=%s' % (name, dt[name]))
        else:
            print('Not found')
    except EOFError:
        break
