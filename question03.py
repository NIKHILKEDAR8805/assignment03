sample_string ='The quick Brow Fox'
upper_counter = 0
lower_counter = 0
for i in sample_string:
    if i.isupper():
     upper_counter += 1
    elif i.islower():
        lower_counter += 1
print(upper_counter)
print(lower_counter)

