import numpy as np 
class MAPE: 
        def __init__(self, y, y_predict):
                self.y = y
                self.y_predict = y_predict
        
        def MAPE(self):
                self.y, self.y_predict = np.array(self.y), np.array(self.y_predict)
                return (np.mean(np.abs((self.y - self.y_predict) / self.y)) * 100)