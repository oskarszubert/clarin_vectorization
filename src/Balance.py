import pandas as pd
from sklearn.utils import resample


def balance_dataset(df):
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

    return df
