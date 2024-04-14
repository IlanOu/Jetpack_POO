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
        from pydub import AudioSegment
        import simpleaudio as sa
        import os
        
        speech = gtts.gTTS(text, lang='fr')
        speech.save('sample.mp3')
        
        # Convertir le fichier MP3 en WAV
        audio = AudioSegment.from_file("sample.mp3", format="mp3")
        audio.export("sample.wav", format="wav")
        
        wave_obj = sa.WaveObject.from_wave_file('sample.wav')
        play_obj = wave_obj.play()
        play_obj.wait_done()
        
        os.remove('sample.mp3')
        os.remove('sample.wav')

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
        
