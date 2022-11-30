import numpy as np

class OnlineMean:
    def __init__(self):
        self._mean:float = 0
        self._counter:int = 0

    def push(self, value:float):
        self._counter += 1
        self._mean = self._mean + (value-self._mean)/self._counter

    def get_mean(self):
        return self._mean

    def __repr__(self):
        return f"<OnlineMean mean:{self._mean}>"

class OnlineVariance(OnlineMean):
    # https://datagenetics.com/blog/november22017/index.html
    def __init__(self):
        OnlineMean.__init__(self)
        self._s_var:float = 0

    def push(self, value:float):
        mean_old = self._mean
        OnlineMean.push(self, value)
        var_old = self._s_var
        self._s_var = var_old + (value - mean_old)*(value - self._mean)

    def get_variance(self):
        return self._s_var/self._counter

    def get_std(self):
        return np.sqrt(self.get_variance())

    def __repr__(self):
        return f"<OnlineVariance mean:{self._mean}, std:{self.get_std()}>"


def main():
    data = [2,4,4,4,5,5,7,9]
    online_mean = OnlineMean()
    online_variance = OnlineVariance()
    for i in range(len(data)):
        online_mean.push(data[i])
        online_variance.push(data[i])
        pass
    pass

if __name__ == '__main__':
    main()
