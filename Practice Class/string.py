instr= "3*qaz, 1*q, 4*tr, 2*pop"

# opstr = "qazqazqazqtrtrtrtrpoppop"

# newstring=""
# for i in instr.split(','):
#     newstring+=int(i.strip().split("*")[0])*i.strip().split("*")[1]
# print(newstring)

print("".join([int(i.strip().split("*")[0])*i.strip().split("*")[1] for i in instr.split(',')]))