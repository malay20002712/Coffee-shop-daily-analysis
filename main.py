import time
from turtle import *
import heroes
import pyodbc as pyodbc
import pandas as p
import statistics as s

name_2 = heroes.gen()
name_1 = heroes.gen()
t = Turtle()
sc = Screen()
for i in range(10):
    t.penup()
    t.forward(100)
    t.pendown()
    t.penup()
    t.left(90)
    t.forward(100)
    t.pendown()
    t.left(90)
    t.penup()
    t.forward(100)
    t.pendown()
    t.left(90)
    t.forward(90)

sc.exitonclick()
expresso = {
    "water": 50,
    "coffee": 18
}

latte = {
    "water": 200,
    "coffee": 24,
    "milk": 150
}

cuppucino = {

    "water": 250,
    "coffee": 24,
    "milk": 100

}

coldcoffee = {

    "icecubes": 2,
    "coldcreammilk": 2

}


def setTemperature(setTemp, coffee):
    settemp = int(input("enter the temperature at which you want to set the coffee maker into: "))
    boolean = False
    if coffee == "coldcoffee":
        while not boolean:
            if settemp > 20:
                print("set the temperature below 20")
                boolean = False
        else:
            boolean = True

    while not boolean:
        if settemp < 30:
            print("Not sufficient please increase: ")
            boolean = False
        elif (settemp > 30) and (settemp < 50):
            print("suitable temperature.")
            boolean = True
        else:
            print("Not a suitable temperature")


file = p.read_csv("dataRefreshsample.csv")
print(file)
print(file["Profit"])
event = False
while not event:
    coffeeChose = input("enter the coffe you want to have: ").lower()
    if coffeeChose == "expresso":

        sumElement = 0
        for i in expresso:
            sumElement += expresso[i]
        print("Your expresso is ready")
    elif coffeeChose == "latte":
        for i in latte:
            sumElement += latte[i]
        print("Your Latte is ready")
    elif coffeeChose == "cuppucino":
        for i in cuppucino:
            sumElement += cuppucino[i]
        print("Your Cuppucino is ready")

    else:
        for i in coldcoffee:
            sumElement += coldcoffee[i]
        print("Your cold coffee!!")

    print("Thankyou!! have a good day")
    condition = input("do you still want to access coffee: ").lower()
    if condition == "yes":
        event = False
    else:
        event = True
import statistics as s

import pandas as p
import statistics as s

# with open("weather_data.csv") as file:
#     li = file["temp"].to_list()
#     s = sum(li)
#     avg = s / len(li)
#     print("Average: ", avg)

file = p.read_csv("weather_data.csv")
li = file["temp"].to_list()
avg = s.mean(li)
totalSum = round(sum(li) / len(li), 2)
print("Average element: ", totalSum)
import random as r
import pandas as p

student = input().strip().split(" ")
dataDict = {
    student: r.randint(10, 100) for student in student
}

passedStudentDict = {
    student: score for (student, score) in dataDict.items() if score >= 60
}

# ps = p.DataFrame(passedStudentDict)
# ps.to_csv("passedstudents.csv")

file = p.read_csv("weather_data.csv")
li = file["temp"].to_list()
maxElement, minElement = max(li), min(li)
mv = s.median(li)
medianValue = (maxElement + minElement) // 2
print("Average element: ", medianValue, " median value: ", mv)

file = p.read_csv("refreshdata.csv")
li = file["Profit"]
sum, x = 0, 0
for i in li:
    sum += i
    x += 1
avgData = round(sum / x, 2)
print(avgData)
l = file["Shipping Cost"]
avgData = round(s.mean(l), 2)
print("Average data: ", avgData)
li = []


def get_mouse_click_coor(x, y):
    string = str(x) + " " + str(y)
    li.append(string)


names = []
n = int(input("enter how many names you want to give into the data: "))
for _ in range(0, n):
    name = input()
    names.append(name)

getwebdata = input("enter the websites name: ").strip().split(
    " ")  # get the name of the websites used frequently by the developers

website_info = {}
for _ in range(0, len(getwebdata)):
    website_info[getwebdata[_]] = int(input())

updated_dict_data = {

    student: data for (student, data) in website_info.items() if data > 30

}

print(updated_dict_data)

# print(new_dict_data_student)
t.onscreenclick(get_mouse_click_coor)

screen = t.Screen()
screen.title("USA map and find its coordinates")
screen.addshape("blank_states_img.gif")
t.shape("blank_states_img.gif")
t.mainloop()
try:
    t.onscreenclick(get_mouse_click_coor)
except Exception:
    print("continue")
data = p.DataFrame(li)
data.to_csv("newMapCoordinates.csv")
screen.exitonclick()
import turtle

import pandas as p
import turtle as t

li = []

screen = t.Screen()
screen.title("USA map and find its coordinates")
screen.addshape("blank_states_img.gif")
t.shape("blank_states_img.gif")
f = p.read_csv("50_states.csv")

# def get_mouse_click_coor(x, y):
#     print(x, " ", y)
#
#
# t.onscreenclick(get_mouse_click_coor)
# t.mainloop()

state_list = f.state.to_list()

tu = t.Turtle()
tu.hideturtle()
tu.penup()

while not False:
    answer_state = screen.textinput(title="Find out the state:", prompt="Write down your state which you want to write "
                                                                        "in "
                                                                        "the chat box: ")
    if answer_state in state_list:
        state_data = f[f.state == answer_state]
        tu.goto(int
                (state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()

file = p.read_csv("refreshdata.csv")
li = file["Profit"]
sum, x = 0, 0
for i in li:
    sum += i
    x += 1
avgData = round(sum / x, 2)
print(avgData)
l = file["Shipping Cost"]
avgData = round(s.mean(l), 2)
print("Average data: ", avgData)
datadict = file.to_json()
print(datadict)

li = input().strip().split(" ")
dict_data = {}
for i in range(len(li)):
    print("enter the ", i + 1, "th data: ")
    data = int(input())
    dict_data[li[i]] = data

updated_Data = {

    student: data for (student, data) in
    dict_data.items() if data > 30
    # get the student data and update the dictionary so that it could be further used in the future

}
df = p.DataFrame(df)
print(df)


class newNode:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# function to find left most node in a tree
def leftMostNode(node):
    while node is not None and node.left is not None:
        node = node.left
    return node


# function to find right most node in a tree
def rightMostNode(node):
    while node is not None and node.right is not None:
        node = node.right
    return node


# recursive function to find the Inorder Scuccessor
# when the right child of node x is None
def findInorderRecursive(root, x):
    if not root:
        return None
    if (root == x or (findInorderRecursive(root.left, x)) or
            (findInorderRecursive(root.right, x))):
        if findInorderRecursive(root.right, x):
            temp = findInorderRecursive(root.right, x)
        else:
            temp = findInorderRecursive(root.left, x)
        if temp:

            if root.left == temp:
                print("Inorder Successor of",
                      x.data, end="")
                print(" is", root.data)
                return None
        return root
    return None


a = int(input("enter the data: "))
sumElement = 0
while a != 0:
    sumElement += (a % 10)
    a /= 10
print("the total sum element are: ", sumElement)


def inorderSuccessor(root, x):
    # Case1: If right child is not None
    if x.right is not None:
        inorderSucc = leftMostNode(x.right)
        print("Inorder Successor of", x.data,
              "is", end=" ")
        print(inorderSucc.data)

    # Case2: If right child is None
    if (x.right == None):
        f = 0
        rightMost = rightMostNode(root)

        # case3: If x is the right most node
        if (rightMost == x):
            print("No inorder successor!",
                  "Right most node.")
        else:
            findInorderRecursive(root, x)


# Driver Code
"""

News paper data that we need 
to take out of the website of the website: 

"""
# newspaper data and the grievance of the following are the rest data of the times of India
li = [i for i in input().split(" ")]
dict_data = {}
# newspaper websites that are best in form:
constant_value = [int(i) for i in input().split(" ")]
for i in range(len(li)):
    dict_data[li[i]] = constant_value[i]

updated_Data = {

    student: data for (student, data) in
    dict_data.items() if data > 15
    # get the student data and update the dictionary so that it could be further used in the future

}
csv_file = p.read_csv("HackerEarthFinancialdataanalysis(ChinaBranch).csv")
d = csv_file[csv_file.Country == "United States of America"]
print(max(d["Units Sold"]))
file = open("dataEntry.csv", 'w')
w = csv.writer(file)
for key, value in updated_Data.items():
    w.writerow([key, value])

"""

'OVER' : News paper data retrieve from the website
that the user targeted and the streamed data that are not at par

"""

if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.right = newNode(6)

    # Case 1
    inorderSuccessor(root, root.right)

    # case 2
    inorderSuccessor(root, root.left.left)

    # case 3
    inorderSuccessor(root, root.right.right)


class Node:

    # Constructor to create a
    # new binary tree node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def diagonalPrintUtil(root, d, diagonalPrintMap):
    # Base Case
    if root is None:
        return

    # Store all nodes of same line
    # together as a vector
    try:
        diagonalPrintMap[d].append(root.data)
    except KeyError:
        diagonalPrintMap[d] = [root.data]

    # Increase the vertical distance
    # if left child
    diagonalPrintUtil(root.left,
                      d + 1, diagonalPrintMap)

    # Vertical distance remains
    # same for right child
    diagonalPrintUtil(root.right,
                      d, diagonalPrintMap)


# driving licence
age = int(input("enter the age of the person: "))
if 16 <= age < 18:
    print("You have a licence to drive only non-gear vehicle: like Scooty or luna")
elif age >= 18:
    print("you are now eligible to drive any motorised any motorised vehicle")
else:
    print("you are not eligible to drive any motorised vehicle you will be eligible to ride non gear motorised "
          "vehicle once you reach the age of 16")

inputEmails = input("email of the person: ")
inputEmails = inputEmails.split(" ")
userName, domain = [], []
for i in inputEmails:
    l = i.split(" ")
    userName.append(l[0])
    domain.append(l[1])
print(userName, domain)

file = open("sample.txt", mode='w')
stringInput = input("enter the string: ")
stringInput = stringInput.split(" ")
string = ''
for i in stringInput:
    string += (i + " ")
file.write(string)
window = t.Tk()
# wi = t.Tk()
window.minsize(width=1000, height=1000)
window.title("Black lives matters")
label = t.Label(text="What's your favourite Video on the platform of Google ??",
                font=("Arial", '24', "bold"), fg='red')

label.pack(expand=True)
t.mainloop()


# Print diagonal traversal of given binary tree
def diagonalPrint(root):
    # Create a dict to store diagonal elements
    diagonalPrintMap = dict()

    # Find the diagonal traversal
    diagonalPrintUtil(root, 0, diagonalPrintMap)

    print
    "Diagonal Traversal of binary tree : "
    for i in diagonalPrintMap:
        for j in diagonalPrintMap[i]:
            print
            j,
        print
        """I a calling the function"""


s = Screen()
s.setup(width=1000, height=500)
s.bgcolor("black")
s.title("Play the game")
starting_color = [(0, 0), (0, -20), (-1, -10), (0, 10)]

segments = []
for pos in starting_color:
    # pos means the position of the snake in the game
    t = Turtle("square")
    t.color("white")
    t.goto(pos)
    segments.append(t)
game_is_on = True
while game_is_on:
    for p in segments:
        p.forward(100)
        p.left(90)
        p.forward(100)
        p.left(90)
        p.forward(100)
        p.left(90)
        p.forward(100)
        p.left(90)
    s.exitonclick()
    s.title("Run as module")
# Driver Program
root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
root.right.right.left = Node(13)
root.left.right.left = Node(4)
root.left.right.right = Node(7)

diagonalPrint(root)

"""
called out the first name and the last name of the given shape and started the streaming
and thanks a lot you are watching our streaming
"""


def add_func(args):
    return sum(args)


li = [int(i) for i in input().split(' ')]
x = add_func(li)
print(x)
t = Turtle()
s = Screen()
typeShape = input("input the which type of polygon you want to get to know: ").lower()

from tkinter import *

window = Tk()
window.title("BMI calculator.")
window.minsize(width=1000, height=500)
label = Label(text="enter the weight", font=('Arial', '24', 'bold'), fg='red', bg='black')
label.pack()


def clickButton():
    weight, height = float(spinbox.get()), float(s.get())
    BMI = weight // height
    st = f"the BMI is : {BMI}"
    label.config(text=st)


spinbox = Spinbox(from_=0, to=1000)
spinbox.insert(END, "enter weight.")
spinbox.pack()

s = Spinbox(from_=0, to=1000)
s.insert(END, "enter the height in m^2")
s.pack()

b = Button(text="BMI", command=clickButton)

mainloop()

shapeDict = {

    "pentagon": 5,
    "hexagon": 6,
    "heptagon": 7,
    "octagon": 8,
    "nonagon": 9,
    "decagon": 10

}
# pt
predictSize = 360 // shapeDict[typeShape]

for i in range(shapeDict[typeShape]):
    t.right(predictSize)
    t.forward(100)

s.exitonclick()

import random as r

turtle_2 = Turtle()
screen_2 = Screen()

randDirection = [0, 90, 270, 360]
for i in range(10):
    turtle_2.forward(100)
    turtle_2.setheading(r.choice(randDirection))


def chooseRandomColor():
    red, blue, green = r.randint(0, 255), r.randint(0, 255), r.randint(0, 255)
    randomColor = (red, blue, green)
    return randomColor


turtle_3, screen_3 = Turtle(), Screen()


class SQLserverDataBase:
    pass


def getServerRequest(serverConnection):
    string = SQLserverDataBase(str1, str2)


getServerRequest(serverConnection=None)
pyodbc.connect('''DRIVER={SQL Server};
                      SERVER=tcp:<myServer_name>;
                      PORT=1433;
                      DATABASE=<myDB_name>;
                      UID=personsUser;
                      PWD=personsPassword
                   ''')

"""

getting the automatic server down to the pole of magnitude
so that the program will run as fast as possible
possibly the program will not run as fast as possible
and the program will take as input or drivers will
work as good as possible at that rate

"""

for i in range(50):
    turtle_3.color(chooseRandomColor())
    turtle_3.setheading(r.choice(randDirection))


class newNode:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


# Function to compute height and
# size of a binary tree
def heighAndSize(node, size):
    if (node == None):
        return 0

    # compute height of each subtree
    l = heighAndSize(node.left, size)
    r = heighAndSize(node.right, size)

    # increase size by 1
    size[0] += 1

    # return larger of the two
    return l + 1 if (l > r) else r + 1


from smtplib import *

window = Tk()
window.title('email sending app')
window.minsize(width=1000, height=1000)


def command_send():
    subject = t.get()
    from_email = t1.get()
    to_email = t2.get()
    text_data = te.get("1.0", "end")
    with SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=from_email, password='very secret password')
        message = 'Subject: ' + subject + '\n\n' + text_data
        connection.sendmail(from_addr=from_email,
                            to_addrs=to_email,
                            msg=message)


t = Entry(master=window, fg='red')
t.insert(END, 'Subject')
t.pack()

t1 = Entry(master=window, fg='red')
t1.insert(END, 'FROM')
t1.pack()

t2 = Entry(master=window, fg='red')
t2.insert(END, 'TO')
t2.pack()

te = Text(master=window, width=50, height=30, fg='red', bg='violet')
te.insert(END, 'body')
te.pack()

b = Button(text='send', command=command_send, fg='red', bg='black')
b.pack()
mainloop()


# function to calculate density
# of a binary tree
def density(root):
    if (root == None):
        return 0

    size = [0]  # To store size

    # Finds height and size
    _height = heighAndSize(root, size)

    return size[0] / _height


# Driver Code
if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)

    print("Density of given binary tree is ",
          density(root))

""" utility that allocates a new Node
with the given key """


class newNode:

    # Construct to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Function to find sum of all the element
def addBT(root):
    if (root == None):
        return 0
    return (root.key + addBT(root.left) +
            addBT(root.right))


# Driver Code
if __name__ == '__main__':
    root = newNode(1)
    root.left = newNode(2)
    root.right = newNode(3)
    root.left.left = newNode(4)
    root.left.right = newNode(5)
    root.right.left = newNode(6)
    root.right.right = newNode(7)
    root.right.left.right = newNode(8)

    sumElement = addBT(root)

    print("Sum of all the nodes is:", sumElement)


# Node class
class Node:

    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class
class LinkedList:

    # Function to initialize the Linked List object
    def __init__(self):
        self.head = None


# This function is in LinkedList class
# Function to insert a new node at the beginning
def push(self, new_data):
    # 1 & 2: Allocate the Node &
    new_node = Node(new_data)

    # 3. Make next of new Node as head
    new_node.next = self.head

    # 4. Move the head to point to new Node
    self.head = new_node
