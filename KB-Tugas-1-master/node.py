class Node:
    def __init__(self, goal, state, parent=None, stateSet=set(), gen=0, amt=[0]):
        self.goal = goal
        self.state = state
        self.zeroIndex = self.findZero()
        self.parent = parent
        self.stateSet = stateSet
        self.gen = gen
        if self.parent:
            self.gen = self.parent.gen + 1
        self.children = []
        self.amt = amt
        self.amt[0] += 1

        self.stateSet.add(self.arrString(self.state))
        self.h1 = self.H1()
        self.h2 = self.H2()


    def findZero(self):
        for i in range(len(self.state)):
            if not self.state[i]:
                return i


    def toString(self):
        # print(f"""{self.gen}-th GEN\n 
        # goal is {self.goal}\n
        # state is {self.state}\n
        # zeroIndex is {self.zeroIndex}\n
        # self is {self}\n
        # parent is {self.parent}\n
        # children are {self.children}\n
        # amt of nodes is {self.amt[0]}\n\n""")

        print(f"""--------{self.gen}-th GEN(step)--------""")
        print(" ---+---+---")
        for y in range(3):
            for x in range(3):
                print(f"""| {self.state[x+y*3]}""", end=" ")
                if x == 2:
                    print("", end="|")
            print("")
            if y < 2:
                print(" ---+---+---")
        print(" ---+---+---")
        print("")

    def upChild(self):
        if self.zeroIndex / 3 != 0 and self.zeroIndex - 3 >= 0:
            temp = self.state.copy()
            temp[self.zeroIndex] = temp[self.zeroIndex - 3]
            temp[self.zeroIndex - 3] = 0
            if self.arrString(temp) not in self.stateSet:
                self.children.append(Node(self.goal, temp, parent=self, stateSet=self.stateSet, amt=self.amt))


    def downChild(self):
        if self.zeroIndex / 3 != 2 and self.zeroIndex + 3 < len(self.state):
            temp = self.state.copy()
            temp[self.zeroIndex] = temp[self.zeroIndex + 3]
            temp[self.zeroIndex + 3] = 0
            if self.arrString(temp) not in self.stateSet:
                self.children.append(Node(self.goal, temp, parent=self, stateSet=self.stateSet, amt=self.amt))


    def rightChild(self):
        if self.zeroIndex % 3 != 2:
            temp = self.state.copy()
            temp[self.zeroIndex] = temp[self.zeroIndex + 1]
            temp[self.zeroIndex + 1] = 0
            if self.arrString(temp) not in self.stateSet:
                self.children.append(Node(self.goal, temp, parent=self, stateSet=self.stateSet, amt=self.amt))


    def leftChild(self):
        if self.zeroIndex % 3 != 0:
            temp = self.state.copy()
            temp[self.zeroIndex] = temp[self.zeroIndex - 1]
            temp[self.zeroIndex - 1] = 0
            if self.arrString(temp) not in self.stateSet:
                self.children.append(Node(self.goal, temp, parent=self, stateSet=self.stateSet, amt=self.amt))


    def arrString(self, arr):
        tempstr = ''
        for i in range(len(arr)):
            tempstr += str(arr[i])
        return tempstr

    
    def isGoal(self):
        for i in range(len(self.state)):
            if self.state[i] != self.goal[i]:
                return False
        return True


    def reproduce(self):
        if not self.isGoal():
            self.leftChild()
            self.upChild()
            self.rightChild()
            self.downChild()


    def H1(self):
        h1 = 0
        for i in range(len(self.goal)):
            if bool(self.goal[i]) and not self.goal[i] == self.state[i]:
                h1 += 1
        return h1


    def find_manhattan_distance(self, goal, state, number):
        g=0
        s=0
        for i in range(len(goal)):
            if goal[i] == number:
                g = i
            if state[i] == number:
                s = i
        g_row = int(g / 3)
        g_col = g % 3
        s_row = int(s / 3)
        s_col = s % 3
        # print(f"n={number} g={g} s={s} gr={g_row} gc={g_col} sr={s_row} sc={s_col}")
        return abs(s_row - g_row) + abs(s_col - g_col)


    def H2(self):
        h2 = 0
        for i in range(1, len(self.goal)):
            h2 += self.find_manhattan_distance(self.goal, self.state, i)
        return h2