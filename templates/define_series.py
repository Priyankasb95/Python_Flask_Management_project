#Define Series in Pandas?
'''
Answer

Pandas series is a One-dimensional ndarray with axis labels. The labels need not be unique but must be a hashable type. The object supports both integer- and label-based indexing and provides a host of methods for performing operations involving the index. The row labels in a Series are called the index. In layman terms, Pandas Series is nothing but a column in an excel sheet.

A Pandas Series can be created out of a Python list or NumPy array. It has to be remembered that unlike Python lists, a Series will always contain data of the same type. This makes NumPy array a better candidate for creating a pandas series.

Just as while creating the Pandas DataFrame, the Series also generates by default row index numbers which is a sequence of incremental numbers starting from ‘0’
As you might have guessed that it’s possible to have our own row index values while creating a Series. We just need to pass index parameters which take a list of the same type or a NumPy array.

Though Pandas Series is extremely useful in itself for doing data analysis and provides many useful helper functions, most of the time, however, the analytic requirements will force us to use DataFrame and Series together.
'''

Any list, tuple and dictionary can be converted in to Series using ’series’ method as shown below.
l=[‘Priyanka’, ‘13-Feb-1995’, 95]
l=pd.Series(l,index=[‘name’, ‘dob’, ‘score’])
print(l)

'''
Output:-
name            Priyanka
dob              13-Feb-1995
score            95
dtype:  object

'''

