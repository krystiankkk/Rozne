def count(string,specifc):
    counter=0
    for c in string:
        if str(specifc) in c:
            counter+=1
    return counter


if __name__=='__main__':
    print(count('pozdrawiam', 'a'))