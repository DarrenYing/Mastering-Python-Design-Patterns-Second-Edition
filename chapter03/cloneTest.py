from copy import copy, deepcopy


class Item:
    def __init__(self, attr, name):
        self.attr = attr
        self.name = name

    def __str__(self):
        desp = self.name + ' '
        for k, v in self.attr.items():
            desp += ' ' + k + ' ' + str(v)
        return desp


a = Item({'age': 18, 'gender': 'male'}, 'John')
b = copy(a)

# 不会影响a
b.name = 'Mike'
print(a)
print(b)

# 会影响a
b.attr['age'] = 19
print(a)
print(b)

# 不会影响a
c = deepcopy(a)
c.attr['age'] = 20
print(a)
print(c)
