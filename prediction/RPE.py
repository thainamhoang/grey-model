class RPE:
        def __init__(self, y_point, y_point_predict):
                self.y_point = y_point
                self.y_point_predict = y_point_predict
        
        def RPE(self):
                return (((self.y_point_predict - self.y_point) / self.y_point) * 100)