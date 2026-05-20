# 5.24 Figure P5.24 shows an electrical system known as a buck converter, which is a circuit used to step the source voltage $e _ { \mathrm { i n } } ( t )$ “down” to a lower desired output voltage (see Problem 3.27 in Chapter 3). The stepdown voltage converter uses a switch to connect and disconnect the voltage supply $e _ { \mathrm { i n } } ( t )$ from the remainder of the circuit until output voltage $e _ { O } = e _ { C }$ is equal to the desired voltage. Obtain a complete SSR of the buck

converter circuit where the states are the dynamic variables associated with the energy-storage elements, $e _ { O }$ is the system output, and $e _ { \mathrm { i n } } ( t )$ is the input.

![](image/82ae259fe2b4248e5696d95831f4a96675ce1419f2db37acb8efb279e7853f32.jpg)

<details>
<summary>text_image</summary>

1
L
+
2
e_in(t)
-
C
e_O
+
-
R
</details>

Figure P5.24

5.25 Figure P5.25 shows the electrical system (band-stop or notch filter) from Problem 3.29. These circuits are used to “filter out” or attenuate input signals within a particular frequency band. For example, notch filters are used on aerospace vehicles to remove the mechanical vibrations that are transmitted to the onboard sensors such as gyroscopes and accelerometers. Derive the transfer function G(s) of the band-stop or notch filter where voltage $e _ { O }$ is the desired output and source voltage $e _ { \mathrm { i n } } ( t )$ is the input.

![](image/0d0972d36625a936ab239ac16c29c80721a61c3713c650bcccd471f049ec349b.jpg)

<details>
<summary>text_image</summary>

R
+
e_in(t)
-
I
L
Output voltage
e_O
C
</details>

Figure P5.25

5.26 Obtain a complete SSR of the band-stop filter described in Problem 5.25 where the states are the dynamic variables associated with the energy-storage elements, $e _ { O }$ is the system output, and $e _ { \mathrm { i n } } ( t )$ is the input.   
5.27 A simplified, linear representation of an electrohydraulic actuator (EHA) consists of a power amplifier, a solenoid model, and a mechanical valve model. The linear I/O equations for each subsystem are

$$\text { Power amplifier: } \tau_ {a} \dot {e} _ {0} + e _ {0} = K _ {a} e _ {\text { in }} (t)\text { Solenoid actuator: } \tau_ {s} \dot {f} + f = K _ {s} e _ {0}\text { Spool valve: } m \ddot {z} + b \dot {z} + k z = f$$
