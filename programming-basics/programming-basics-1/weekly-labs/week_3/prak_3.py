# while True:
#     r = input()
    
#     match r:
#         case "SS":
#             print("False | False")
#         case "RR":
#             print("False | False")
#         case "PP":
#             print("False | False")
#         case "SP" | "RS" | "PR":
#             print("True")
#         case "PS" | "SR" | "RP":
#             print("False")
#         case _:
#             break

n=5
width = 3
print(f'{n:{width}}')
print(f'{n:0{width}}')
print(f'{n:b}')