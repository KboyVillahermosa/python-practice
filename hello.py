# Step 1: Define six variables
var1 = 10
var2 = 15
var3 = 10
var4 = 20
var5 = 15
var6 = 25

# Step 2: Store these variables in a list
data = [var1, var2, var3, var4, var5, var6]

# Step 3: Calculate the mean
mean = sum(data) / len(data)

data.sort()  
n = len(data)

if n % 2 == 0:
    median = (data[n//2 - 1] + data[n//2]) / 2
else:
    median = data[n//2]

mode = max(data, key=data.count)


print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Mode: {mode}")
