# import machine
import poc_tools
from checker import CheckableClass
from debug import Debug

class AccelDelegate:
    def __init__(self):
        pass
        
    def right(self):
        pass
        
    def left(self):
        pass



class AccelTestDelegate(AccelDelegate):
    def __init__(self):
        super().__init__()
        self.verbose = False
        
    def right(self):
        if self.verbose:
            Debug.LogWhisper("Direction : Droite")
        
    def left(self):
        if self.verbose:
            Debug.LogWhisper("Direction : Gauche")

class AccelTraductor:
    def __init__(self):
        self.orientations = {
            "up": False,
            "down": False,
            "right": False,
            "left": False
        }
        
        self.points_x = 0
        self.points_y = 0
        
        self.max_points = 20000
        
        self.sensibility = 1500
        
        self.init_decrement_speed = 100
        self.decrement_speed_x = 100
        self.decrement_speed_y = 100
        self.lerp = 1.2
    
    def traduce(self, values):
        """
        values looks like :
        { "AcX":..., "AcY":..., "AcZ":..., "Tmp":..., "GyX":..., "GyY":..., "Gyz":... }
        """
        
        if values:
            if values["GyX"]:
                if values["GyX"] > self.sensibility:
                    self.orientations["right"] = True
                    if (self.points_x < self.max_points):
                        self.points_x += values["GyX"]
                if values["GyX"] < -self.sensibility:
                    self.orientations["left"] = True
                    if (self.points_x > -self.max_points):
                        self.points_x += values["GyX"]
                if values["GyY"] > self.sensibility:
                    self.orientations["up"] = True
                    if (self.points_y < self.max_points):
                        self.points_y += values["GyY"]
                if values["GyY"] < -self.sensibility:
                    self.orientations["down"] = True
                    if (self.points_y > -self.max_points):
                        self.points_y += values["GyY"]
                else:
                    self.orientations = {
                        "up": False,
                        "down": False,
                        "right": False,
                        "left": False
                    }
                
                    if self.points_x > self.decrement_speed_x:
                        self.points_x -= self.decrement_speed_x
                        self.decrement_speed_x *= self.lerp
                    elif self.points_x < -self.decrement_speed_x:
                        self.points_x += self.decrement_speed_x
                        self.decrement_speed_x *= self.lerp
                    else:
                        self.points_x = 0
                        self.decrement_speed_x = self.init_decrement_speed
                        
                    if self.points_y > self.decrement_speed_y:
                        self.points_y -= self.decrement_speed_y
                        self.decrement_speed_y *= self.lerp
                    elif self.points_y < -self.decrement_speed_y:
                        self.points_y += self.decrement_speed_y
                        self.decrement_speed_y *= self.lerp
                    else:
                        self.points_y = 0
                        self.decrement_speed_y = self.init_decrement_speed
                    
                
                mapped_values = {
                    "x": poc_tools.map_value(self.points_x, -self.max_points, self.max_points, 0, 100),
                    "y": poc_tools.map_value(self.points_y, -self.max_points, self.max_points, 0, 100)
                }
                
                return mapped_values
        
        return None

class Accel(CheckableClass):
    def __init__(self, i2c, addr=0x68, delegate=None):
        self.iic = i2c
        self.addr = addr
        
        self.exception = False
        
        try:
            self.iic.start()
            self.iic.writeto(self.addr, bytearray([107, 0]))
            self.iic.stop()
        except:
            self.exception = True
        
        
        self.delegate = delegate
        
        self.traductor = AccelTraductor()
    
    
    def test(self):
        Debug.LogWhisper("Start testing button")
        result_code = "100"
        
        if self.exception:
            result_code = "300"
        
        Debug.LogWhisper("Stop testing button")
        
        return [{
            "result": result_code,
            "class": self.__class__
        }]

    def get_raw_values(self):
        self.iic.start()
        datas = self.iic.readfrom_mem(self.addr, 0x3B, 14)
        self.iic.stop()
        return datas

    def get_ints(self):
        values = self.get_raw_values()
        values_array = []
        for value in values:
            values_array.append(value)
        return values_array

    def bytes_to_int(self, firstbyte, secondbyte):
        if not firstbyte & 0x80:
            return firstbyte << 8 | secondbyte
        return - (((firstbyte ^ 255) << 8) | (secondbyte ^ 255) + 1)

    def get_values(self):
        raw_ints = self.get_raw_values()
        vals = {}
        vals["AcX"] = self.bytes_to_int(raw_ints[0], raw_ints[1])
        vals["AcY"] = self.bytes_to_int(raw_ints[2], raw_ints[3])
        vals["AcZ"] = self.bytes_to_int(raw_ints[4], raw_ints[5])
        vals["Tmp"] = self.bytes_to_int(raw_ints[6], raw_ints[7]) / 340.00 + 36.53
        vals["GyX"] = self.bytes_to_int(raw_ints[8], raw_ints[9])
        vals["GyY"] = self.bytes_to_int(raw_ints[10], raw_ints[11])
        vals["GyZ"] = self.bytes_to_int(raw_ints[12], raw_ints[13])
        return vals  # returned in range of Int16
        # -32768 to 32767
        
    def process(self):
        values = self.get_values()
        
        mapped_values = self.traductor.traduce(values)
        
        if mapped_values["x"] > 50:
            self.delegate.right()
        else:
            self.delegate.left()
        
        return mapped_values
        
