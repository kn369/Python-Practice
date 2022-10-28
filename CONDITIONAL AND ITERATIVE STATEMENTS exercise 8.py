
num_subjects=int(input("How many subjects are you taking ? "))

sum=0

for index in range (num_subjects):
    prompt="Enter marks for subject #" + str(index+1) + ":"
    marks= int(input("Enter the marks you have obtained :"))
    sum=sum+marks

average= sum/num_subjects
print ("your average marks in ",num_subjects,"subjects are ",average)
