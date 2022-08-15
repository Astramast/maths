class Number:
    def __init__(self, base=10, value=0):
        self.base = base
        power = 0
        while value >= base**power:
            power += 1
        self.value = []
        for i in range(power-1, -1, -1):
            self.value.append(value//base**i)
            value %= base**i
        self.value.reverse()

    def __repr__(self):
        return f"{self.value}"

    def __str__(self):
        e = ""
        for i in reversed(self.value):
            e += str(i) + ' '
        return e

    def getValue(self):
        return self.value

    def getOrder(self):
        return len(self.value)

    def getBase(self):
        return self.base

    def getValue10(self):
        val10 = 0
        for i in range(len(self.value)):
            val10 += self.value[i]*(self.base**i)
        return val10

    def __add__(self, other):
        if type(other) is Number:
            add = self.getValue10() + other.getValue10()
        elif type(other) is int:
            add = self.getValue10() + other
        else:
            raise TypeError(f"unsupported operand type(s) for +: 'Number' and '{type(other)}'")
        add = Number(self.base, add)
        return add

    def __iadd__(self, other):
        if type(other) is Number:
            add = self.getValue10() + other.getValue10()
        elif type(other) is int:
            add = self.getValue10() + other
        else:
            raise TypeError(f"unsupported operand type(s) for +=: 'Number' and '{type(other)}'")
        add = Number(self.base, add)
        self.value = add.getValue()
        return self

    def __radd__(self, other):
        if type(other) is int:
            return other+self.getValue10()
        else:
            raise TypeError(f"unsupported operand type(s) for +: '{type(other)}' and 'Number'")

    def __eq__(self, other):
        if type(other) is Number:
            return self.getValue10() == other.getValue10()
        elif type(other) is int:
            return self.getValue10() == other
        else:
            return False
