

l = list()
for i in range(5):
    a = input("Intro un nom:")
    l.append(a)
for e in l:
    if "a" not in e:
        print(e)