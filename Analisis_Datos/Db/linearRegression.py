import matplotlib.pyplot as plt



class LinearRegression:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = len(x)
        self.x_mean = sum(x) / self.n
        self.y_mean = sum(y) / self.n
        self.m = self.slope()
        self.b = self.intercept()

    def slope(self):
        numerator = sum([xi*yi for xi, yi in zip(self.x, self.y)]) - self.n * self.x_mean * self.y_mean
        denominator = sum([xi**2 for xi in self.x]) - self.n * self.x_mean**2
        return numerator / denominator
    
    def intercept(self):
        return self.y_mean - self.m * self.x_mean
    
    def predict(self, x):
        return self.m * x + self.b
    
    def r_squared(self):
        y_pred = [self.predict(xi) for xi in self.x]
        ssr = sum((yi - y_pred) ** 2 for yi, y_pred in zip(self.y, y_pred))
        sst = sum((yi - self.y_mean) ** 2 for yi in self.y)
        return 1 - ssr / sst
    
    def plot(self):
        plt.scatter(self.x, self.y)
        plt.plot(self.x, [self.predict(xi) for xi in self.x], color='red')
        plt.show()



#Example of use:
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 6, 5]
lr = LinearRegression(x, y)
lr.plot()
print(lr.r_squared())
print(lr.predict(6))
print(lr.predict(7))
print(lr.predict(8))
print(lr.predict(9))
        