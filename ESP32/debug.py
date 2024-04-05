class Colors:
    HEADER = '\033[95m'
    OK_BLUE = '\033[94m'
    OK_CYAN = '\033[96m'
    
    OK_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    
    RED = '\033[31m'
    BLACK = '\033[30m'
    GREEN = '\033[32m'
    ORANGE = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    LIGHT_GREY = '\033[37m'
    DARK_GRAY = '\033[90m'
    
    BOLD = '\033[1m'
    DIM = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    
    ENDC = '\033[0m'

class Debug():
    def __init__(self):
        pass
    
    verbose = True
    
    @staticmethod
    def Log(message):
        print(Colors.DARK_GRAY, end="")
        print(message, end="")
        print(Colors.ENDC)
    
    
    @staticmethod
    def LogWhisper(message):
        if Debug.verbose:
            print(Colors.DARK_GRAY + Colors.DIM + Colors.ITALIC, end="")
            print(message, end="")
            print(Colors.ENDC)
    
    
    @staticmethod
    def LogSuccess(message):
        print(Colors.OK_GREEN, end="")
        print(message, end="")
        print(Colors.ENDC)
    
    
    @staticmethod
    def LogWarning(message):
        print(Colors.WARNING, end="")
        print(message, end="")
        print(Colors.ENDC)
    
    
    @staticmethod
    def LogError(message):
        print(Colors.FAIL + Colors.BOLD, end="")
        print(message, end="")
        print(Colors.ENDC)