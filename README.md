# Haptic feedback motor driver

A simple haptic feedback motor driver module for micropython.

## 验证与测试

- LILYGO T-Watch

## 使用指南

### class Haptic

A simple haptic feedback motor driver module.
Control the motor through pwm and timer to simulate the effect of haptic feedback.

Usage Model:

```python
from machine import Pin
from haptic import  Haptic

touch = Pin(38, Pin.IN)

h = Haptic(Pin(4))

while True:
    if touch.value() == 0:
        h.once()
```

#### 构造

##### haptic.Haptic(pin, freq: int = 100)

使用以下参数构造并返回一个新的 Haptic 对象：

- pin: pin is the entity on which the PWM is output, which is usually a machine.Pin object.
- freq: Frequency of PWM output

#### 方法

##### Haptic.once(duration: int = 50)

Play the haptic effect once on the motor.

- duration: The duration of the haptic effect, in milliseconds.

##### Haptic.deint()

Disabled Haptic Driver.
