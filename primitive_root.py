def primitive_root(number, border):
    list = []
    counter = 0
    for num in range(1, number):
        s = set()
        if(counter == border): break
        for i in range(0, number):
            elem = pow(num, i, number)
            if (elem not in s):
                s.add(elem)
            else:
                break
        if(len(s) ==  number - 1):
            print(num)
            list.append(num)
            counter+=1

    return list

def main():
    number = input()
    print(primitive_root(int(number), 9))

if __name__ == '__main__':
    main()