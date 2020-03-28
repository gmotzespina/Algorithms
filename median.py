class Statistics:

    def __init__(self):
        self.hi = []
        self.lo = []

    def add_num(self, num):
        if len(self.lo) > 0:
            if num > self.lo[0]:
                self.add_to_hi(num)
                return

            self.add_to_lo(num)
            return

        self.lo.append(num)
        return

    def add_to_hi(self, num):
        if len(self.hi) == 0:
            self.hi.append(num)
            return
        
        if len(self.lo) == 1 and len(self.hi) == 1:
            self.add_to_lo(self.hi[0])
            self.hi[0] = num
            return

        index = 0
        while num > self.hi[index] and index < len(self.hi):
            index += 1
            if index == len(self.hi):
                break

        self.hi.insert(index, num)
        print('len: {}'.format(len(self.hi)))
        if len(self.hi) == 3:
            print('here')
            print(self.hi)
            self.add_to_lo(self.hi[0])
            del self.hi[0:1]
            print(self.hi)
            print('deleting')
            print(self.hi)


    def add_to_lo(self, num):
        lo_len = len(self.lo)
        if lo_len == 0:
            self.lo.append(num)
            return
        
        if len(self.hi) == 0:
            self.add_to_hi(self.lo[0])
            self.lo[0] = num
            return
        
        index = 0
        while num < self.lo[index] and index < len(self.lo):
            index += 1
            if index == len(self.lo):
                break

        self.lo.insert(index, num)
        
        if len(self.lo) == 3 and len(self.hi) == 2:
            self.lo.pop()
            self.lo.pop()
        elif len(self.lo) == 3:
            self.add_to_hi(self.lo[0])
            del self.lo[0]
            
    def median(self):
        if (len(self.lo) + len(self.hi)) % 2 == 0:
            return (self.lo[0] + self.hi[0])/2

        return self.lo[0]

    def print_nums(self):
        print("lo: {}".format(self.lo))
        print("hi: {}".format(self.hi))


stat = Statistics()

stat.add_num(1)
print(stat.median())
stat.add_num(2)

stat.print_nums()
print(stat.median())

stat.add_num(3)
stat.print_nums()
print(stat.median())
stat.add_num(4)
stat.print_nums()
print(stat.median())
stat.add_num(5)
stat.print_nums()
print(stat.median())

