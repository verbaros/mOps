from mOps.sets import symbols as symbols

#https://www.oreilly.com/library/view/python-cookbook/0596001673/ch05s18.html
class Set:

    def __init__(self,  *args, varName=None, displayType='unicode',maxDisplay=10):

        self._dict = {}

        if len(args)==0:
            self.backing = symbols.EmptySet
        else:
            [self.add(arg) for arg in args]

        if varName is None:
            #TO DO
            pass
        else:
            self.varName = varName

        self.displayType = displayType
        self.maxDisplay = maxDisplay

    def __hash__(self):
        return hash(' '.join(str(v) for v in list(self._dict.keys())))

    def __getitem__(self, index):
        return self._dict.keys(  )[index]

    def __iter__(self):
        return iter(sorted(self._dict.copy(  )))

    def __len__(self):
        return len(self._dict)

    def copy(self):
        return Set(*self.items())

    def __str__(self):
        if len(self._dict) == 0:
            return '{ }'
        else:
            set_list = list(self._dict)
            if (len(set_list) > self.maxDisplay):
                return f'{{{", ".join(str(v) for v in sorted(set_list))}}}'
            else:
                return f'{{{", ".join(str(v) for v in sorted(set_list[0:self.maxDisplay]))}}}'

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return set(self.items()) == set(other.items())

    def __lt__(self, other):
        return len(self) < len(other)

    def __gt__(self, other):
        return len(self) > len(other)


    def items(self):
        result = self._dict.keys()
        return result

    def extend(self, args):
        for arg in args:
            self.add(arg)

    def add(self, item):
        self._dict[item] = item

    def remove(self, item):
        del self._dict[item]

    def contains(self, item):
        return self._dict.has_key(item)


