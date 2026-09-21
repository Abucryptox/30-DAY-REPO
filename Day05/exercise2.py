ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# 1. Sort the list and find the min and max age
ages.sort()
min_age = min(ages)
max_age = max(ages)
print(ages)      # [19, 19, 20, 22, 24, 24, 24, 25, 25, 26]
print(min_age)   # 19
print(max_age)   # 26

# 2. Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
ages.sort()      # sort again so the median is correct
print(ages)      # [19, 19, 19, 20, 22, 24, 24, 24, 25, 25, 26, 26]

# 3. Median (12 items, so two middle items divided by two)
n = len(ages)
if n % 2 == 1:
    median = ages[n // 2]
else:
    median = (ages[n // 2 - 1] + ages[n // 2]) / 2
print(median)    # 24.0

# 4. Average
average = sum(ages) / len(ages)
print(average)   # 22.75

# 5. Range
age_range = max(ages) - min(ages)
print(age_range) # 7

# 6. Compare abs(min - average) and abs(max - average)
print(abs(min(ages) - average))  # 3.75
print(abs(max(ages) - average))  # 3.25
# min is further from the average than max is

# 7. Middle country
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
mid = len(countries) // 2
print(countries[mid])   # Finland

# 8. Split into two lists (first half gets the extra one if odd)
split_point = (len(countries) + 1) // 2
first_half = countries[:split_point]
second_half = countries[split_point:]
print(first_half)   # ['China', 'Russia', 'USA', 'Finland']
print(second_half)  # ['Sweden', 'Norway', 'Denmark']

# 9. Unpack the first three and the rest as Scandinavian countries
china, russia, usa, *scandic_countries = countries
print(china)              
print(russia)             
print(usa)                
print(scandic_countries)  

