import pandas as pd
from sklearn.utils import resample
from sklearn.model_selection import train_test_split


def balance_dataset(df, df_y):
    df.insert(0, "value", df_y, True) 

    single_label_df_list = []
    class_labels = set(df['value'])
    for label in class_labels:
        tmp_df = df[df['value'] == label]
        single_label_df_list.append( [tmp_df.shape, tmp_df ])
    df = df.iloc[0:0]

    single_label_df_list.sort(reverse=True)
    n_samples = single_label_df_list[0][0][0]


    tmp_list = [single_label_df_list[0][1]]
    for tmp_df in single_label_df_list[1:]:
        tmp_list.append(resample(   tmp_df[1], 
                                    replace=True,            # sample with replacement
                                    n_samples=n_samples,     # to match majority class
                                    random_state=123)   )        # reproducible results
    single_label_df_list = tmp_list

    for tmp_df in single_label_df_list:
        df = pd.concat( [df, tmp_df] )

    X = df.drop(columns=['value'])
    Y = df['value'].values

    return X, Y


# EXAMPLE USAGE:
# if __name__ == '__main__':
#     filename = 'data.csv'
#     df = pd.read_csv(filename, sep=',')
#     print('before:', df.shape)
#     X = df.drop(columns=['value'])
#     Y = df['value'].values
#     X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)
#     X_train, Y_train = balance_dataset(X_train, Y_train)
