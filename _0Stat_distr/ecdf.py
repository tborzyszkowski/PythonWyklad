import matplotlib.pyplot as plt

class ECDF:

    def __init__(self, observations):
        self.observations = observations

    def __call__(self, x):
        counter = 0.0
        for obs in self.observations:
            if obs <= x:
                counter += 1
        return counter / len(self.observations)

    def plot(self, a=None, b=None):
        if a == None:
            # Set up some reasonable default
            a = self.observations.min() - self.observations.std()
        if b == None:
            # Set up some reasonable default
            b = self.observations.max() + self.observations.std()
        X = np.linspace(a, b, 100)
        f = np.vectorize(self.__call__)
        plt.plot(X, f(X))
        plt.show()
