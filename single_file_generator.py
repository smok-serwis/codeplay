import os

import numpy as np
import pandas as pd


pd.set_option('display.max_columns', None)
loan_file = pd.read_csv(r"C:\Users\Szymon\Desktop\Hackathon\Skrypty pyton\codeplay\loan_clients.csv", sep='\t', delimiter=',', encoding ="ISO-8859-1", error_bad_lines=False)
policy_file = pd.read_csv(r"C:\Users\Szymon\Desktop\Hackathon\Skrypty pyton\codeplay\policy_clients.csv", sep='\t', delimiter=',', encoding ="ISO-8859-1", error_bad_lines=False)
output = pd.DataFrame(columns=['user', 'komunikacyjne', 'mieszkanie', 'rolne', 'upraw', 'NNW', 'firm','OC','zwierzat', 'inne', 'na_zycie', 'grupowe', 'travel', '<5000', '<10000','<50000','<100000','+1000000','5%','10%','20%',
                               '50%','p_100','p_300','p_500','p_1000','p_+1000'])

for user in loan_file.values:
    try:
        if user[3] <= 5000:
           if user[4] <= 5:
               new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                  '<5000': 1,
                                  '5%':1
                                  })
           if user[4] <= 10:
               new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                   '<5000': 1,
                                   '10%': 1
                                   })
           if user[4] <= 20:
               new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                   '<5000': 1,
                                   '20%': 1
                                   })
           if user[4] <= 50:
               new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                   '<5000': 1,
                                   '50%': 1
                                   })
           output = output.append(new_df,ignore_index=True)

        if 5000 < user[3] <= 10000:
            if user[4] <= 5:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    '<10000': 1,
                                    '5%': 1
                                    })
            if user[4] <= 10:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    '<10000': 1,
                                    '10%': 1
                                    })
            if user[4] <= 20:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    '<10000': 1,
                                    '20%': 1
                                    })
            if user[4] <= 50:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    '<10000': 1,
                                    '50%': 1
                                    })
            output = output.append(new_df, ignore_index=True)
        if 10000 < user[3] <= 50000:
            if user[4] <= 5:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    '<50000': 1,
                                    '5%': 1
                                    })
            if user[4] <= 10:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    '<50000': 1,
                                    '10%': 1
                                    })
            if user[4] <= 20:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    '<50000': 1,
                                    '20%': 1
                                    })
            if user[4] <= 50:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    '<50000': 1,
                                    '50%': 1
                                    })
            output = output.append(new_df, ignore_index=True)
        if 50000 < user[3] <= 100000:
            if user[4] <= 5:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    '<100000': 1,
                                    '5%': 1
                                    })
            if user[4] <= 10:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    '<100000': 1,
                                    '10%': 1
                                    })
            if user[4] <= 20:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    '<100000': 1,
                                    '20%': 1
                                    })
            if user[4] <= 50:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    '<100000': 1,
                                    '50%': 1
                                    })
            output = output.append(new_df, ignore_index=True)
        if 100000 < user[3]:
            if user[4] <= 5:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    '+100000': 1,
                                    '5%': 1
                                    })
            if user[4] <= 10:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    '+100000': 1,
                                    '10%': 1
                                    })
            if user[4] <= 20:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    '+100000': 1,
                                    '20%': 1
                                    })
            if user[4] <= 50:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    '+100000': 1,
                                    '50%': 1
                                    })
                output = output.append(new_df, ignore_index=True)
    except ValueError:
       pass
print(output.fillna('0'))
for user in loan_file.values:
    try:
        if user[4] == 1:
           if user[3] <= 100:
               new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                   'komunikacyjne': 1,
                                   'p_100':1
                                   })
           if 100 < user[3] <= 300:
               new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                   'komunikacyjne': 1,
                                   'p_300': 1
                                   })
           if 300 < user[3] <= 500:
               new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                   'komunikacyjne': 1,
                                   'p_500': 1
                                   })
           if 500 < user[3] <= 1000:
               new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                   'komunikacyjne': 1,
                                   'p_1000': 1
                                   })
           if 1000 < user[3]:
               new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                   'komunikacyjne': 1,
                                   'p_+1000': 1
                                   })

           output = output.append(new_df, ignore_index=True)
        if user[4] == 2:
           if user[3] <= 100:
               new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                   'mieszkanie': 1,
                                   'p_100': 1
                                   })
           if 100 < user[3] <= 300:
               new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                   'mieszkanie': 1,
                                   'p_300': 1
                                   })
           if 300 < user[3] <= 500:
               new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                   'mieszkanie': 1,
                                   'p_500': 1
                                   })
           if 500 < user[3] <= 1000:
               new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                   'mieszkanie': 1,
                                   'p_1000': 1
                                   })
           if 1000 < user[3]:
               new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                   'mieszkanie': 1,
                                   'p_+1000': 1
                                   })

           output = output.append(new_df, ignore_index=True)
        if user[4] == 3:
            if user[3] <= 100:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'rolne': 1,
                                    'p_100': 1
                                    })
            if 100 < user[3] <= 300:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'rolne': 1,
                                    'p_300': 1
                                    })
            if 300 < user[3] <= 500:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'rolne': 1,
                                    'p_500': 1
                                    })
            if 500 < user[3] <= 1000:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'rolne': 1,
                                    'p_1000': 1
                                    })
            if 1000 < user[3]:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'rolne': 1,
                                    'p_+1000': 1
                                    })

            output = output.append(new_df, ignore_index=True)
        if user[4] == 5:
            if user[3] <= 100:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'upraw': 1,
                                    'p_100': 1
                                    })
            if 100 < user[3] <= 300:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'upraw': 1,
                                    'p_300': 1
                                    })
            if 300 < user[3] <= 500:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'upraw': 1,
                                    'p_500': 1
                                    })
            if 500 < user[3] <= 1000:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'upraw': 1,
                                    'p_1000': 1
                                    })
            if 1000 < user[3]:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'upraw': 1,
                                    'p_+1000': 1
                                    })

            output = output.append(new_df, ignore_index=True)
        if user[4] == 6:
            if user[3] <= 100:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'NNW': 1,
                                    'p_100': 1
                                    })
            if 100 < user[3] <= 300:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'NNW': 1,
                                    'p_300': 1
                                    })
            if 300 < user[3] <= 500:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'NNW': 1,
                                    'p_500': 1
                                    })
            if 500 < user[3] <= 1000:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'NNW': 1,
                                    'p_1000': 1
                                    })
            if 1000 < user[3]:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'NNW': 1,
                                    'p_+1000': 1
                                    })

            output = output.append(new_df, ignore_index=True)
        if user[4] == 7:
            if user[3] <= 100:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'firm': 1,
                                    'p_100': 1
                                    })
            if 100 < user[3] <= 300:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'firm': 1,
                                    'p_300': 1
                                    })
            if 300 < user[3] <= 500:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'firm': 1,
                                    'p_500': 1
                                    })
            if 500 < user[3] <= 1000:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'firm': 1,
                                    'p_1000': 1
                                    })
            if 1000 < user[3]:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'firm': 1,
                                    'p_+1000': 1
                                    })

            output = output.append(new_df, ignore_index=True)
        if user[4] == 8:
            if user[3] <= 100:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'OC': 1,
                                    'p_100': 1
                                    })
            if 100 < user[3] <= 300:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'OC': 1,
                                    'p_300': 1
                                    })
            if 300 < user[3] <= 500:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'OC': 1,
                                    'p_500': 1
                                    })
            if 500 < user[3] <= 1000:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'OC': 1,
                                    'p_1000': 1
                                    })
            if 1000 < user[3]:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'OC': 1,
                                    'p_+1000': 1
                                    })

            output = output.append(new_df, ignore_index=True)
        if user[4] == 9:
            if user[3] <= 100:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'zwierzat': 1,
                                    'p_100': 1
                                    })
            if 100 < user[3] <= 300:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'zwierzat': 1,
                                    'p_300': 1
                                    })
            if 300 < user[3] <= 500:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'zwierzat': 1,
                                    'p_500': 1
                                    })
            if 500 < user[3] <= 1000:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'zwierzat': 1,
                                    'p_1000': 1
                                    })
            if 1000 < user[3]:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'zwierzat': 1,
                                    'p_+1000': 1
                                    })

            output = output.append(new_df, ignore_index=True)
        if user[4] == 10:
            if user[3] <= 100:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'inne': 1,
                                    'p_100': 1
                                    })
            if 100 < user[3] <= 300:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'inne': 1,
                                    'p_300': 1
                                    })
            if 300 < user[3] <= 500:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'inne': 1,
                                    'p_500': 1
                                    })
            if 500 < user[3] <= 1000:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'inne': 1,
                                    'p_1000': 1
                                    })
            if 1000 < user[3]:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'inne': 1,
                                    'p_+1000': 1
                                    })

            output = output.append(new_df, ignore_index=True)
        if user[4] == 13:
            if user[3] <= 100:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'na_zycie': 1,
                                    'p_100': 1
                                    })
            if 100 < user[3] <= 300:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'na_zycie': 1,
                                    'p_300': 1
                                    })
            if 300 < user[3] <= 500:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'na_zycie': 1,
                                    'p_500': 1
                                    })
            if 500 < user[3] <= 1000:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'na_zycie': 1,
                                    'p_1000': 1
                                    })
            if 1000 < user[3]:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'na_zycie': 1,
                                    'p_+1000': 1
                                    })

            output = output.append(new_df, ignore_index=True)
        if user[4] == 14:
            if user[3] <= 100:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'grupowe': 1,
                                    'p_100': 1
                                    })
            if 100 < user[3] <= 300:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'grupowe': 1,
                                    'p_300': 1
                                    })
            if 300 < user[3] <= 500:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'grupowe': 1,
                                    'p_500': 1
                                    })
            if 500 < user[3] <= 1000:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'grupowe': 1,
                                    'p_1000': 1
                                    })
            if 1000 < user[3]:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'grupowe': 1,
                                    'p_+1000': 1
                                    })
            output = output.append(new_df, ignore_index=True)
        if user[4] == 15:
            if user[3] <= 100:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'travel': 1,
                                    'p_100': 1
                                    })
            if 100 < user[3] <= 300:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'travel': 1,
                                    'p_300': 1
                                    })
            if 300 < user[3] <= 500:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'travel': 1,
                                    'p_500': 1
                                    })
            if 500 < user[3] <= 1000:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'travel': 1,
                                    'p_1000': 1
                                    })
            if 1000 < user[3]:
                new_df = pd.Series({'user': str(user[0]) + '-' + user[1][0:2],
                                    'travel': 1,
                                    'p_+1000': 1
                                    })
            output = output.append(new_df, ignore_index=True)
    except ValueError:
       pass

output.set_index('user', inplace=True)
print(output.fillna(int('0')))
pd.DataFrame(output).fillna(0).to_csv('all_together.csv')