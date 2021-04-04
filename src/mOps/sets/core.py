import inspect
from mOps.sets import symbols as symbols
from mOps.core import number_generators

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

    def innerSet(self):
        return set(self.items())

    def copy(self):
        return Set(*self.items())

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

    def get_cardinality(self):
        return self.__len__()


    def fromGenerator(self,*args,generator=None,gen_size=5):
        if (generator is None):
            generator = number_generators.rangeGenerator(size=gen_size)

        for x in generator:
            cond = True
            if(len(args)>=1):
                y_offset = 0
                if (len(inspect.getfullargspec(args[0]).args) == 2):
                    cond = args[0](x,args[1])
                    y_offset += 1
                else:
                    cond = args[0](x)

                for y in range(1, len(args)-y_offset, 2):
                    b = args[y + y_offset + 1]
                    cond = args[y+y_offset](cond, b(x))
            if(cond):
                self.add(x)
        return self

    def hasSubset(self,subSet):
        '''
        try:
            subSet.backing == symbols.EmptySet
            return True
        except:
            pass
        '''
        return subSet.innerSet().issubset(self.innerSet())

    def hasMember(self,element):
        return self.contains(element)
