from sklearn.datasets import load_iris
iris = load_iris()
x = iris.data
y = iris.target
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_suze = 0.3, random_state=1
)

print(X_train.shape) # (105, 4)
print(X_train.shape) # (45, 4)

print(X_train.shape) # (105,)
print(X_train.shape) # (45,)