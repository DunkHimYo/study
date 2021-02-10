from sklearn import datasets

from sklearn.model_selection import train_test_split

iris = datasets.load_iris()

x = iris.data

y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

print(f'x_train : {x_train.shape}')
print(f'x_train : {x_test.shape}')
print(f'x_train : {y_train.shape}')
print(f'x_train : {y_test.shape}')
