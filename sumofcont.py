cont=[1,4,2,5,2,5,6,1]


def sumofc(container):
    s=0
    for el in container:
        s=s+el
    return s


if __name__ == '__main__':
    print(sumofc(cont))