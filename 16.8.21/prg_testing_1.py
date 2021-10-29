# import time
# def sep(l1 , x, l2, length, y):

#     if type(l1[x]) is list:
#         length = len(l1[x])
#         x = 0
#         sep(l1[x], x, l2, length, y+1)
#         print("l2: ", l2)

#     while type(l1[x]) is int and x < length:
#         l2.append(l1[x])
#         print("X : ", x)
#         x+=1
#         print("l2: ", l2)
#         print("X : ", x)
#         print("\nlength : ", length)
#     else:
#         x = y
#         lenth = len(l1)
#         sep(l1[y] , x, l2, length, y+1)
#         print("l2: ", l2)
def converInSimpleList(l1):
    l2 = []
# l1 = [1,2,[3,4,5],[ [6], [ [ [7, [None] ],[8,9]]]]]
    for x in l1:
        if type(x) is list:
            l2 = l2 + converInSimpleList(x)
            print(l2)
        else:
            l2.append(x)
            print(l2)
    return l2
l1 = [1,2,[3,4,5],[ [6], [ [ [7, [None] ],[8,9]]]]]
lenth = len(l1)
print("length: ", lenth)
l2 = []
print(converInSimpleList(l1))





