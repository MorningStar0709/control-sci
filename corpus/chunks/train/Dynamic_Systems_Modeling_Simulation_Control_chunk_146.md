3.27 Figure P3.27 shows an electrical system known as a buck converter, which is a circuit used to step the source voltage $e _ { \mathrm { i n } } ( t )$ “down” to a lower desired output voltage $e _ { O } = e _ { C }$ (voltage across the capacitor). The step-down voltage converter uses a switch to connect and disconnect the voltage supply $e _ { \mathrm { i n } } ( t )$ from the remainder of the circuit until $e _ { C }$ is equal to the desired voltage. Derive the mathematical model of this system in terms of the appropriate dynamic variables and include the switching effect.

![](image/dbc18a545d6ba5d7184dbdb7916582b48beecacd6a6a593d530e59aaf8e3208e.jpg)

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

Figure P3.27

3.28 A series RC circuit known as a washout filter is shown in Fig. P3.28. This circuit (or filter) will “pass” the initial part of the dynamic output voltage response $e _ { O }$ (voltage across the resistor) but will eventually “wash out” (i.e., reduce to zero) a constant input voltage. These filters are often used in control systems such as an aircraft’s automatic flight control system. Derive the mathematical model with $e _ { O }$ (voltage across the resistor) as the dynamic variable and source voltage $e _ { \mathrm { i n } } ( t )$ as the input.

![](image/e672a6965207b8cc30c24d2fb3c79394316595bf9bdcedf655fbcc10f16a0427.jpg)

<details>
<summary>text_image</summary>

C
+
e_in(t)
-
I
Output voltage
e_O
</details>

Figure P3.28

3.29 Figure P3.29 shows an electrical circuit known as a band-stop filter or notch filter, which attenuates (reduces) the amplitude of input signals that have a certain frequency band and “passes” all other signals without alteration. These electrical circuits are used to remove signals with undesirable frequencies; for example, notch filters are used on aerospace vehicles to remove mechanical vibrations that are transmitted to sensors such as gyroscopes and accelerometers.

![](image/23cbc29475325831a46ea78f02b970d7b775c83f241bcf03a0dcbce474ac5216.jpg)

<details>
<summary>text_image</summary>

R
+
e_in(t)
-
I
Output voltage
e_O
L
C
</details>

Figure P3.29
