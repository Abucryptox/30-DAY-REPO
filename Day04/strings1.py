#STRINGS
first_name = "abubakar"
last_name = "auwal"
space =  " "
full_name = first_name + space + last_name
print(full_name)
language = "python"
a, b, c, d, e, f = language   #unpacking
print(a)
print(b)
print(c)
programming_type = "python programming"
print(programming_type[0])   #accesing element using index
print(programming_type[-1])
print(programming_type[5])
print(programming_type[6])
print(programming_type[0:3])   #slicing
print(programming_type[2:5])
print(programming_type[6:12])
print(programming_type[8:15])
print(programming_type[::-1])   #reverse string

#STRIGS METHODS
school = "bayero university kano"
sub_string = "sity"
challenge = "246"
print(school.capitalize())
print(school.upper())
print(school.lower())
print(school.count("o"))
print(school.endswith("kano"))
print(school.find("uni"))
print(school.rfind("n"))
print(school.index(sub_string))    # returns lowest indexof substring
print(school.isalnum())
print(sub_string.isalnum())
print(school.isalpha())
print(challenge.isdecimal())
print(challenge.isdigit())
print(school.islower())
result =' '.join(school)
print(school.strip("kan"))
print(school.replace("bayero", "maryam abacha"))
print(school.split())
print(school.title())
print(school.swapcase())
print(school.startswith("bay"))


#EXERCISES
# 1. Concatenate 'Thirty', 'Days', 'Of', 'Python'
a, b, c, d = "Thirty", "Days", "Of", "Python"
sentence = a + " " + b + " " + c + " " + d
print(sentence)

# 2. Concatenate 'Coding', 'For', 'All'
e, f, g = "Coding", "For", "All"
topic = e + " " + f + " " + g
print(topic)

# 3. Declare company
company = "Coding For All"

# 4. Print company
print(company)

# 5. Length
print(len(company))

# 6-8. Case methods
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9. First word
print(company.split()[0])   # Coding

# 10. Contains 'Coding'?
print("Coding" in company)         # True
print(company.find("Coding"))      # 0

# 11. Replace Coding -> Python
print(company.replace("Coding", "Python"))

# 12. "Python for Everyone" -> "Python for All"
phrase = "Python for Everyone"
print(phrase.replace("Everyone", "All"))

# 13. Split on space
print(company.split())

# 14. Split on comma
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(","))

# 15-17. Indexing
print(company[0])    # C
print(len(company) - 1)  # 13 (last index)
print(company[10])   # o

# 18-19. Acronyms
print("".join(w[0] for w in "Python For Everyone".split()).upper())  # PFE
print("".join(w[0] for w in company.split()).upper())                 # CFA

# 20-21. index of C, F
print(company.index("C"))
print(company.index("F"))

# 22. rfind 'l'
sentence2 = "Coding For All People"
print(sentence2.rfind("l"))

# 23-27. 'because' sentence
sent = "You cannot end a sentence with because because because is a conjunction"
print(sent.find("because"))              # 23/26 first occurrence
print(sent.rindex("because"))            # 24 last occurrence
start = sent.find("because")
end = sent.rindex("because") + len("because")
print(sent[start:end])                   # 25/27 slice

# 28-29. startswith/endswith
print(company.startswith("Coding"))  # True
print(company.endswith("coding"))    # False

# 30. Strip
padded = "   Coding For All      "
print(padded.strip())

# 31. isidentifier
print("30DaysOfPython".isidentifier())        # False
print("thirty_days_of_python".isidentifier()) # True

# 32. Join libraries
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" # ".join(libraries))

# 33. Newline
print("I am enjoying this challenge.\nI just wonder what is next.")

# 34. Tab
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# 35. Circle area
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

# 36. Arithmetic
num_one = 8
num_two = 6
print(f"{num_one} + {num_two} = {num_one + num_two}")
print(f"{num_one} - {num_two} = {num_one - num_two}")
print(f"{num_one} * {num_two} = {num_one * num_two}")
print(f"{num_one} / {num_two} = {round(num_one / num_two, 2)}")
print(f"{num_one} % {num_two} = {num_one % num_two}")
print(f"{num_one} // {num_two} = {num_one // num_two}")
print(f"{num_one} ** {num_two} = {num_one ** num_two}")













