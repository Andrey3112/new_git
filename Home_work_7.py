#######1
start = int(input())
end = int(input())
def sum_range(start, end):
    if start > end:
        start, end = end, start
    counter = 0
    for i in range(start, end + 1):
        counter += i
    return counter
print(sum_range(start, end))


#######2
mesyac = int(input())
def season(mesyac):

    if mesyac in [1, 2, 12]:
        return "Zima"
    elif mesyac in [3, 4, 5]:
        return "Vesna"
    elif mesyac in [6, 7, 8]:
        return "Leto"
    elif mesyac in [9, 10, 11]:
        return "Osen"
    else:
        return "Takogo mesyaca v godu net"
print(season(mesyac))


#######3
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
def get_filtered(a):
    for i in a:
        if i < 5:
            print(i)
get_filtered(a)


#######4
def num1(x):
    def num2(y):
        return x * y
    return num2
resultat = num1(3)(4)
print(resultat)
