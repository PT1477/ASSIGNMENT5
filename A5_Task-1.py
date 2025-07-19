d = {'meet':85,'rohit':76,'rahul':89,'sanjay':69,'pt':98}
n = input("Enter the student's name :")
if n in d:
    print("{}'s marks {}".format(n,d.get(n)))
else:
    print('not found')