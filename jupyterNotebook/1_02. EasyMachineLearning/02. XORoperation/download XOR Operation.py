#!/usr/bin/env python
# coding: utf-8

# In[6]:


#!
#! Library import
#!
# LinearSVC algorithm 
from sklearn.svm import LinearSVC
# Evaluate test results
from sklearn.metrics import accuracy_score

#!
#! Prepare data and results for training.
#!
# X, Y (traning data)
learn_data = [[0,0], [1,0], [0,1], [1,1]]
# X XOR Y (result data)
learn_label = [0, 1, 1, 0]

#!
#! Algorithm selection.(LinearSVC)
#!
# Creatting objects.
clf = LinearSVC()

#!
#! Learning data and results for training. 
#!
# fit() = Machine Learning.
clf.fit(learn_data, learn_label)

#!
#! Predictions from test data.
#!
test_data = [[0,0], [1,0], [0,1], [1,1]]
# predict() = Machine predictions.
test_label = clf.predict(test_data)

#! 
#! Evaluation of prediction results.
#! 
print(test_data, "の予測結果: ", test_label)
# accuracy_score = Outputs the correct answer rate.
print("正解率 = ", accuracy_score([0, 1, 1, 0], test_label))



# - 今回のプログラムではXORの機械学習はできない。
#  - アルゴリズムはそのままで、アルゴリズムに指定するパラメータを調整
#  - アルゴリズムを変更する。

# - 今回はアルゴリズムをアルゴリズム チートシートから変更して再トライする。

# In[10]:


#!
#! Library import
#!
"""
Update **NeighborsClassifier** algorithm 
"""
from sklearn.neighbors import KNeighborsClassifier

# Evaluate test results
from sklearn.metrics import accuracy_score

#!
#! Prepare data and results for training.
#!
# X, Y (traning data)
learn_data = [[0,0], [1,0], [0,1], [1,1]]
# X XOR Y (result data)
learn_label = [0, 1, 1, 0]

#!
#! Algorithm selection.("KneighborsClassifier")
#!
# Creatting objects.
"""
Update **KNeighborsClassifier** algorithm 
"""
clf = KNeighborsClassifier(n_neighbors = 1)

#!
#! Learning data and results for training. 
#!
# fit() = Machine Learning.
clf.fit(learn_data, learn_label)

#!
#! Predictions from test data.
#!
test_data = [[0,0], [1,0], [0,1], [1,1]]
# predict() = Machine predictions.
test_label = clf.predict(test_data)

#! 
#! Evaluation of prediction results.
#! 
print(test_data, "の予測結果: ", test_label)
# accuracy_score = Outputs the correct answer rate.
print("正解率 = ", accuracy_score([0, 1, 1, 0], test_label))


# In[ ]:




