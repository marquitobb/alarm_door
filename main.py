import RPi.GPIO as GPIO
import time


class Alarm:
    """ "base class to execute alarm on function and notify otherwise"""

    @classmethod
    def activate_alarm(cls):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(24, GPIO.IN)
        GPIO.setup(18, GPIO.OUT)

        try:
            while True:
                GPIO.output(18, GPIO.HIGH)
                inputValue = GPIO.input(24)
                if inputValue == True:
                    # TODO: send notification for a certain time to say that the alarm is still active
                    # time.sleep(0.5)
                    pass
                else:
                    cls.send_notification()
                    GPIO.cleanup()
                    break
        except KeyboardInterrupt:
            print("se cancelo alarma!")
            GPIO.cleanup()

    @classmethod
    def send_notification(cls):
        # TODO: send notification with the telegram app or some email
        print("Se desactivo alarma x_x")
        pass


if __name__ == "__main__":
    print("Alarma activate...")
    Alarm.activate_alarm()
