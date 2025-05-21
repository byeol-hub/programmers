# str = input()

# if 1 <= len(str) <= 20:
#     if "A" <= str <= "Z":
#         print(lowper(str))
#     if "a" <= str <= "z":
#         print(upper(str))
        
# str = input()

# if 1 <= len(str) <= 20:
#     if "A" <= str <= "Z":
#         print(str.lower())
#     elif "a" <= str <= "z":
#         print(str.upper())
        
# str = []
# str = input()

# i = 0

# if 1<= len(str) <=20:
#     for i in str:
#         if "A" <= str[i] <= "Z":
#             str[i] = str[i].lower()
#             i += 1
#         elif "a" <= str[i] <= "z":
#             str[i] = str[i].upper()
#             i += 1
        
# print(str)

result = ''

str = input()

if 1 <= len(str) <= 20:
    for i in str:
        if "A" <= i <= "Z":
            result += i.lower()
        elif "a" <= i <= "z":
            result += i.upper()
            
print(result)
        