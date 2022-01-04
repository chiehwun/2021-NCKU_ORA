def bridge_torch_probelm(s):
    s.sort()
    if len(s) > 3:
        a = s[0] + s[-1] + min(2*s[1], s[0] + s[-2])
        print(f'a = {a}')
        return a + bridge_torch_probelm(s[:-2])
    else:
        print(s[len(s) == 2:])
        return sum(s[len(s) == 2:])


if __name__ == '__main__':
    input = [1, 2, 5, 10]
    print(input, '=>', bridge_torch_probelm(input))
