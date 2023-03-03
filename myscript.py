import argparse

parser = argparse.ArgumentParser()
parser.add_argument("fullName", help="the fullName to greet")
parser.add_argument("height", help="the height of the person being greeted", type=float)
parser.add_argument("weight", help="the weight of the person being greeted", type=float)
parser.add_argument("age", help="the age of the person being greeted", type=int)
args = parser.parse_args()

print("Your FullName is " + str(args.fullName))
print("Your Height is " + str(args.height))
print("Your Weight is " + str(args.weight))
print("Your Age is " + str(args.age))
