import numpy as np
import pickle
import pandas as pd

df = pd.read_csv('infiltered.csv')

df.drop(['protocol', 'tot_fwd_pkts', 'tot_bwd_pkts',
       'totlen_fwd_pkts', 'totlen_bwd_pkts', 'fwd_pkt_len_max',
       'fwd_pkt_len_min', 'fwd_pkt_len_mean', 'fwd_pkt_len_std',
       'bwd_pkt_len_max', 'bwd_pkt_len_min', 'bwd_pkt_len_mean',
       'bwd_pkt_len_std', 'flow_pkts_s', 'flow_iat_std',
       'flow_iat_max', 'fwd_iat_mean',
       'fwd_iat_std', 'fwd_iat_max', 'fwd_iat_min', 'bwd_iat_tot',
       'bwd_iat_mean', 'bwd_iat_std', 'bwd_iat_max', 'bwd_iat_min',
       'fwd_psh_flags', 'bwd_psh_flags', 'fwd_urg_flags', 'bwd_urg_flags',
       'bwd_header_len', 'fwd_pkts_s',
       'pkt_len_min', 'pkt_len_max', 'pkt_len_mean', 'pkt_len_std',
       'pkt_len_var', 'fin_flag_cnt', 'syn_flag_cnt', 'rst_flag_cnt',
       'psh_flag_cnt', 'ack_flag_cnt', 'urg_flag_cnt', 'cwe_flag_count',
       'ece_flag_cnt', 'down_up_ratio', 'pkt_size_avg', 'fwd_seg_size_avg',
       'bwd_seg_size_avg', 'fwd_byts_b_avg', 'fwd_pkts_b_avg',
       'fwd_blk_rate_avg', 'bwd_byts_b_avg', 'bwd_pkts_b_avg',
       'bwd_blk_rate_avg', 'subflow_fwd_pkts', 'subflow_fwd_byts',
       'subflow_bwd_pkts', 'subflow_bwd_byts',
       'init_bwd_win_byts', 'fwd_act_data_pkts', 
       'active_std', 'active_max', 'active_min', 'idle_mean',
       'idle_std', 'idle_max', 'idle_min'],axis=1, inplace=True)


X=df.drop('label', axis=1)
y=df['label']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

pickle.dump(model, open('models.pkl','wb'))
models = pickle.load(open('models.pkl','rb'))