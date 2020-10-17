import os

import numpy as np
import pandas as pd
import pickle

pd.set_option('display.max_columns', None)
loan_file = pd.read_csv(r"user_loans_ policy/loan_clients.csv", sep='\t', delimiter=',', encoding ="ISO-8859-1", error_bad_lines=False)
policy_file = pd.read_csv(r"user_loans_ policy/policy_clients.csv", sep='\t', delimiter=',', encoding ="ISO-8859-1", error_bad_lines=False)
output = pd.DataFrame(columns=['user', 'komunikacyjne', 'mieszkanie', 'rolne', 'upraw', 'NNW', 'firm','OC','zwierzat', 'inne', 'na_zycie', 'grupowe', 'travel', '<5000', '<10000','<50000','<100000','+100000','high','low',])

for user in loan_file.values:
    try:
        if user[3] <= 5000:
           if user[4] <= 10:
               new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                  '<5000': 1,
                                  'low':1
                                  })
           if user[4] > 10:
               new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                   '<5000': 1,
                                   'high': 1
                                   })
           output = output.append(new_df,ignore_index=True)

        if 5000 < user[3] <= 10000:
            if user[4] <= 10:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    '<10000': 1,
                                    'low': 1
                                    })
            if user[4] > 10:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    '<10000': 1,
                                    'high': 1
                                    })

            output = output.append(new_df, ignore_index=True)
        if 10000 < user[3] <= 50000:
            if user[4] <= 10:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    '<50000': 1,
                                    'low': 1
                                    })
            if user[4] > 10:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    '<50000': 1,
                                    'high': 1
                                    })
            output = output.append(new_df, ignore_index=True)
        if 50000 < user[3] <= 100000:
            if user[4] <= 10:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    '<100000': 1,
                                    'low': 1
                                    })
            if user[4] > 10:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    '<100000': 1,
                                    'high': 1
                                    })
            output = output.append(new_df, ignore_index=True)
        if 100000 < user[3]:
            if user[4] <= 10:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    '+100000': 1,
                                    'low': 1
                                    })
            if user[4] > 10:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    '+100000': 1,
                                    'high': 1
                                    })

                output = output.append(new_df, ignore_index=True)
    except ValueError:
       pass
output.fillna('0')
for user in loan_file.values:
    try:
        if user[4] == 1:
           new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                   'komunikacyjne': 1,
                                   })
           output = output.append(new_df, ignore_index=True)
        if user[4] == 2:
           new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                   'mieszkanie': 1
                                   })
           output = output.append(new_df, ignore_index=True)

        if user[4] == 3:
            new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'rolne': 1
                                    })

            output = output.append(new_df, ignore_index=True)
        if user[4] == 5:
            new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'upraw': 1
                                    })
            output = output.append(new_df, ignore_index=True)
        if user[4] == 6:
            new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'NNW': 1
                                    })

            output = output.append(new_df, ignore_index=True)
        if user[4] == 7:
            new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'firm': 1
                                    })

            output = output.append(new_df, ignore_index=True)
        if user[4] == 8:
            new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'OC': 1
                                    })


            output = output.append(new_df, ignore_index=True)
        if user[4] == 9:
            new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'zwierzat': 1
                                    })


            output = output.append(new_df, ignore_index=True)
        if user[4] == 10:
            new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'inne': 1
                                    })


            output = output.append(new_df, ignore_index=True)
        if user[4] == 13:
            new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'na_zycie': 1
                                    })

            output = output.append(new_df, ignore_index=True)
        if user[4] == 14:
            new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'grupowe': 1
                                    })

            output = output.append(new_df, ignore_index=True)
        if user[4] == 15:
            new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'travel': 1
                                })
            output = output.append(new_df, ignore_index=True)
    except ValueError:
       pass

output.fillna(0)
output_dict = {}
pd.DataFrame(output).fillna(0).to_csv('all_together.csv')
print(output)
for user in output.values:
    val_list=[]
    for val in user[1:]:
        if val == 1:
            val_list.append(1)
        else:
            val_list.append(0)

    output_dict[str(user[0])] = val_list


print(output_dict)
file = open('user_loan_policy.py', 'wb')
pickle.dump(output_dict, file, -1)

