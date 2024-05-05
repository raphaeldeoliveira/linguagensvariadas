from sklearn.datasets import load_iris
iris = load_iris()
x = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names
print("Feature names: ", feature_names)
print("Target names: ", target_names)
print("\nFirst 10 rows of X:\n", X[:10])


Feature names: ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
Target names: ['setosa', 'versicolor', 'virginica']
First 10 rows of X:
[
    [5.1, 3.5, 1.4, 0.2]
    [5.1, 3.5, 1.4, 0.2]
    [5.1, 3.5, 1.4, 0.2]
    [5.1, 3.5, 1.4, 0.2]
    [5.1, 3.5, 1.4, 0.2]
    [5.1, 3.5, 1.4, 0.2]
    [5.1, 3.5, 1.4, 0.2]
    [5.1, 3.5, 1.4, 0.2]
    [5.1, 3.5, 1.4, 0.2]
    [5.1, 3.5, 1.4, 0.2]
]

