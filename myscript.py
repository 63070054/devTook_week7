import argparse

parser = argparse.ArgumentParser()
parser.add_argument("firstName", help="the firstName to greet")
parser.add_argument("height", help="the height of the person being greeted", type=int)
parser.add_argument("weight", help="the weight of the person being greeted", type=int)
parser.add_argument("age", help="the age of the person being greeted", type=int)
args = parser.parse_args()

print("Your FirstName is " + str(args.firstName))
print("Your Height is " + str(args.height))
print("Your Weight is " + str(args.weight))
print("Your Age is " + str(args.age))
