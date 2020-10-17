import pickle
income_data = []
with (open(r"C:\Users\Szymon\Desktop\Hackathon\Skrypty pyton\codeplay\user_loans_ policy\dane_od_macka.py", "rb")) as openfile:
    while True:
        try:
            income_data.append(pickle.load(openfile))
        except EOFError:
            break

spending_data = []
with (open(r"C:\Users\Szymon\Desktop\Hackathon\Skrypty pyton\codeplay\user_loans_ policy\dump.py", "rb")) as openfile:
    while True:
        try:
            spending_data.append(pickle.load(openfile))
        except EOFError:
            break

service_data = []
with (open(r"C:\Users\Szymon\Desktop\Hackathon\Skrypty pyton\codeplay\user_loans_ policy\user_loan_policy.py", "rb")) as openfile:
    while True:
        try:
            service_data.append(pickle.load(openfile))
        except EOFError:
            break
list_of_incomes=[]
list_of_spendings=[]
income_dic={}
spending_dic={}
for user in income_data:
    for u in user:
        list_of_incomes.append(u[0])
        item = u[1:]
        income_dic[u[0]] = u[1:]

for user in spending_data:
    for u in user:
        list_of_spendings.append(u[0])
        item = u[1:]
        spending_dic[u[0]] = u[1:]

output_list=[]
for user in service_data:
    for u in user:
        if (u in list_of_incomes) and (u in list_of_spendings):
            final_list= spending_dic[u][0] + income_dic[u]
            output_list.append((u, service_data[0][u],final_list))

print(output_list)
file = open('final_data.py', 'wb')
pickle.dump(output_list, file, -1)

