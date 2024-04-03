from displayer import Displayer


class CheckableClass:
    def __init__(self):
        pass

    def test(self):
        pass
    

class Checker:
    def __init__(self):
        pass
    
    @staticmethod
    def check(delegate):
        result = delegate.test()
        if result.get("class") != None:
            Displayer.raiseResult(result["result"], result["class"])
        else:
            Displayer.raiseResult(result["result"])