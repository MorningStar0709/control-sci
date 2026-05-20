$$\frac {E _ {o} (s)}{E _ {i} (s)} = - \frac {1}{R _ {1} C _ {1} R _ {2} C _ {2} s ^ {2} + \left[ R _ {2} C _ {2} + R _ {1} C _ {2} + \left(R _ {1} / R _ {3}\right) R _ {2} C _ {2} \right] s + \left(R _ {1} / R _ {3}\right)}$$

![](image/aebc0cbf31d03244e1b62eb111326f1ce323b733e3ba42954dc005cc32d00764.jpg)

<details>
<summary>text_image</summary>

i1
R1
A
i2
i4
R2
B
i5
C2
-
+
ei
C1
i3
eo
</details>

Figure 3–28   
Operationalamplifier circuit.

A–3–9. Consider the servo system shown in Figure 3–29(a).The motor shown is a servomotor,a dc motor designed specifically to be used in a control system.The operation of this system is as follows:A pair of potentiometers acts as an error-measuring device. They convert the input and output positions into proportional electric signals. The command input signal determines the angular position r of the wiper arm of the input potentiometer.The angular position r is the reference input to the system, and the electric potential of the arm is proportional to the angular position of the arm. The output shaft position determines the angular position c of the wiper arm of the output potentiometer.The difference between the input angular position r and the output angular position c is the error signal e, or

$$e = r - c$$

The potential difference $e _ { r } - e _ { c } = e _ { v }$ is the error voltage, where $e _ { r }$ is proportional to r and $e _ { c }$ is proportional to c; that is, $e _ { r } = K _ { 0 } r$ and $e _ { c } = K _ { 0 } c$ where, $K _ { 0 }$ is a proportionality constant. The error voltage that appears at the potentiometer terminals is amplified by the amplifier whose gain constant is $K _ { 1 }$ . The output voltage of this amplifier is applied to the armature circuit of the dc motor.A fixed voltage is applied to the field winding. If an error exists, the motor develops a torque to rotate the output load in such a way as to reduce the error to zero. For constant field current, the torque developed by the motor is

$$T = K _ {2} i _ {a}$$

where $K _ { 2 }$ is the motor torque constant and $i _ { a }$ is the armature current.

When the armature is rotating, a voltage proportional to the product of the flux and angular velocity is induced in the armature. For a constant flux, the induced voltage $e _ { b }$ is directly proportional to the angular velocity ordudt,

$$e _ {b} = K _ {3} \frac {d \theta}{d t}$$

where $e _ { b }$ is the back emf, $K _ { 3 }$ is the back emf constant of the motor, and u is the angular displacement of the motor shaft.
