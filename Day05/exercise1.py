# 1-4
empty = list()
subjects = ["math", "english", "physics", "chemistry", "biology", "data processing"]
print(len(subjects))
print(subjects[0], subjects[len(subjects) // 2], subjects[-1])

# 5
mixed_data_types = ['daddy', 19, 17.8, 'single', 'gashua']

# 6-9
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0], it_companies[len(it_companies) // 2], it_companies[-1])

# 10
it_companies[0] = "Meta"
print(it_companies)

# 11-12
it_companies.append("Remita")
it_companies.insert(len(it_companies) // 2, "Interswitch")
print(it_companies)

# 13
it_companies[0] = it_companies[0].upper()
print(it_companies)

# 14
print('#;  '.join(it_companies))

# 15
print("Amazon" in it_companies)

# 16-17
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)

# 18-20
print(it_companies[:3])
print(it_companies[-3:])



# 21-23
it_companies.pop(0)
mid = len(it_companies) // 2
print(mid)


# 24-25
it_companies.clear()
print(it_companies)
del it_companies

# 26-27
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
joined = front_end + back_end
print(joined)

full_stack = joined.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)



