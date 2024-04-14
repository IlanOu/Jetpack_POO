from abc import ABC, abstractmethod

class TTSEngine(ABC):
    """
    Classe abstraite définissant l'interface pour les moteurs de synthèse vocale.
    """
    @abstractmethod
    def say(self, text: str):
        pass

class Pyttsx3Engine(TTSEngine):
    """
    Implémentation de TTSEngine utilisant la bibliothèque pyttsx3.
    """
    def say(self, text: str):
        import pyttsx3
        
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

class GttsEngine(TTSEngine):
    """
    Implémentation de TTSEngine utilisant la bibliothèque Google Text-to-Speech (gTTS).
    """
    def say(self, text: str):
        import gtts
        from playsound import playsound
        import os
        
        tts = gtts.gTTS(text, lang='fr')
        
        port = 1
        while os.path.exists(f"temp{port}.mp3"):
            port += 1
        os.rename("temp.mp3", f"temp{port}.mp3")
        
        playsound(f"temp{port}.mp3")
        os.remove(f"temp{port}.mp3")

class Speaker:
    """
    Classe permettant de lire du texte à haute voix en utilisant différents moteurs de synthèse vocale.
    """
    @staticmethod
    def say(text: str, engine: TTSEngine = Pyttsx3Engine()):
        """
        Lit le texte donné à haute voix en utilisant le moteur de synthèse vocale spécifié.
        
        Args:
            text (str): Le texte à lire.
            engine (TTSEngine, optional): Le moteur de synthèse vocale à utiliser. Par défaut, Pyttsx3Engine est utilisé.
        """
        engine.say(text)
        
