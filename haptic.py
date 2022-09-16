from machine import PWM as _PWM
from machine import Timer as _Timer

class Haptic():
    '''A simple haptic feedback motor driver module.
    Control the motor through pwm and timer to simulate the effect of haptic feedback.

    :param Pin pin: pin is the entity on which the PWM is output, which is usually a machine.Pin object
    :param int freq: Frequency of PWM output
    '''
    _timer = None
    def __init__(self, pin, freq: int = 100) -> None:
        self._pwm = _PWM(pin, freq=freq, duty_u16=0)
        if self._timer is None:
            self._timer = _Timer(3)

    def once(self, duration: int = 50) -> None:
        '''Play the haptic effect once on the motor.
        :param int duration: The duration of the haptic effect, in milliseconds.
        '''
        self._timer.init(period=duration, mode=_Timer.ONE_SHOT, callback=self._cb)
        self._pwm.duty_u16(32768)

    def deint(self) -> None:
        '''Disabled Haptic Driver.
        '''
        self._timer.deinit()
        self._pwm.deinit()

    def _cb(self, timer) -> None:
        self._pwm.duty_u16(0)
