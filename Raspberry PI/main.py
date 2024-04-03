import RPi.GPIO as GPIO
import time


class DistanceDelegate:
    def __init__(self):
        pass
        
    def far_away(self):
        pass
    
    def close(self):
        pass


class DistanceTestDelegate(DistanceDelegate):
    def __init__(self):
        super().__init__()
        self.verbose = True
        
    def far_away(self):
        if self.verbose:
            print("Le capteur est loin")
    
    def close(self):
        if self.verbose:
            print("Le capteur est proche")


class DistanceSensor:
    def __init__(self, trigger_pin, echo_pin, delegate):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        self.setup_gpio()
        self.delegate = delegate

    def setup_gpio(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)

    def measure_distance(self):
        # Trigger le signal ultrason
        GPIO.output(self.trigger_pin, True)
        time.sleep(0.00001)
        GPIO.output(self.trigger_pin, False)

        # Mesurer le temps d'echo
        start_time = time.time()
        while GPIO.input(self.echo_pin) == 0:
            start_time = time.time()
        while GPIO.input(self.echo_pin) == 1:
            end_time = time.time()

        pulse_duration = end_time - start_time

        # Calculer la distance
        distance = pulse_duration * 17000 / 2.0
        
        if distance > 20:
            self.delegate.far_away()
        else:
            self.delegate.close()

        return distance

    def run(self):
        try:
            while True:
                distance = self.measure_distance()
                print("Distance:", distance, "cm")
                time.sleep(0.25)
        except KeyboardInterrupt:
            # Nettoyer les broches GPIO
            self.cleanup()

    def cleanup(self):
        GPIO.cleanup()



# ----------------------------------- Websockets

import websocket


class Client:
    def __init__(self, url, trigger_pin=14, echo_pin=15):
        # URL du serveur WebSocket auquel se connecter
        self.url = url
        
        # Definir les broches GPIO
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin
        
        self.isOpened = False
        
    def initialize(self):
        # Initialisation du client WebSocket
        ws = websocket.WebSocketApp(self.url,
                                    on_message=self.on_message,
                                    on_error=self.on_error,
                                    on_close=self.on_close)
        ws.on_open = self.on_open
                
        # Lancement de la boucle d'événements
        ws.run_forever()
    
    def on_message(self, ws, message):
        print(f"Message reçu : {message}")
        ws.send("Bonjour, serveur WebSocket!")

    def on_error(self, ws, message):
        print(f"Erreur : {message}")
        self.isOpened = False

    def on_close(self, msg, a, b):
        print("Connexion fermée")
        self.isOpened = False

    def on_open(self, ws):
        print("Connexion ouverte")
        self.isOpened = True



if __name__ == "__main__":
    client = Client("ws://192.168.40.62:3000", 14, 15)
    client.initialize()
    
    # Creer une instance du capteur de distance
    sensor = DistanceSensor(self.trigger_pin, self.echo_pin)
    
    while True:
        if client.isOpened:
            # Executer la mesure
                distance = sensor.measure_distance()
                distance = str(int(distance * 100)/100)
                ws.send("dist-" + distance)
                print("Send distance : " + distance)
                time.sleep(0.25)
    
    
