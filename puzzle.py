# зад.2б вар.7 KTO+KOT=TOK
for a in range(1, 10):
    for b in range(10):
        for c in range(1, 10):
            if 200 * a + 11 * b + 11 * c == 100 * c + 10 * b + a:
                print('a=' + str(a) + ' b=' + str(b) + ' c=' + str(c))
