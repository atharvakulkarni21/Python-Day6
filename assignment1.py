#Assignment1 list to dict
list1 = [1, 2, 3, 4, 5, 6, 7, 8]
list2 = ["a", "b","c","d","e"]
dicty = {list1[i]:list2[i] for i in range(len(list2))}
print(dicty)