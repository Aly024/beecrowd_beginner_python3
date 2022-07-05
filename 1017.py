#Taking input for time taken and avg speed
time = int(input())
avg_speed = int(input())

#Calculating the distance
dist = avg_speed * time

#Calculating the fuel spent
fuel = dist / 12

print('%0.3f'%fuel)
