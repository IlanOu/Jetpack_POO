from displayer import Displayer
import time
from debug import Debug
from displayer import ResultCodes

class CheckableClass:
    def __init__(self):
        pass

    def test(self):
        pass
    

class Checker:
    def __init__(self):
        pass
    
    @staticmethod
    def allResultsAreSuccess(results):
        for result in results:
            print(ResultCodes.getType(result["result"]))
            if not ResultCodes.getType(result["result"]) == "success":
                return False
        return True
    
    @staticmethod
    def check(allObjects):
        Debug.LogWhisper("Start setup verification")
        resultsOfDelegates = []
        for delegate in allObjects:
            results = delegate.test()
            resultsOfDelegates.append(results)
            for result in results:
                if result.get("class") != None:
                    Displayer.raiseResult(result["result"], result["class"])
                else:
                    Displayer.raiseResult(result["result"])
                time.sleep(1)
        
        Debug.LogWhisper("End setup verification")
        
        for result in resultsOfDelegates:
            print(Checker.allResultsAreSuccess(result))
            if Checker.allResultsAreSuccess(result) == False:
                return False

        return True