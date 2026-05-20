# Engineering Applications

9.24 Figure P9.24 shows the band-stop or notch filter discussed in Problems 3.29 and 5.25. As discussed in these prior problems, band-pass filters are used to suppress signals that contain an undesirable frequency. For example, the frames of aerospace vehicles (e.g., aircraft, missiles, rockets) vibrate at known frequencies and these frequencies can be inadvertently measured by onboard sensors such as gyroscopes and accelerometers. Hence band-stop filters are used to remove an unwanted frequency component from the measurement signal.

![](image/398ffd74f360d07641e14ed3aa69337881ed28b130c3cf9dae0ac77468856ab0.jpg)

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

Figure P9.24

The transfer function for the band-stop filter is

$$G (s) = \frac {L C s ^ {2} + 1}{L C s ^ {2} + R C s + 1} = \frac {E _ {O} (s)}{E _ {\mathrm{in}} (s)}$$

The electrical parameters for the band-stop filter are inductance $L = 0 . 0 0 5 \ : \mathrm { H }$ , capacitance C = 0.02 F, and $R = 1 \ \Omega$ .

a. Using MATLAB plot the Bode diagram of the band-stop filter. Show that the band-stop filter essentially removes an input voltage signal with a frequency equal to the “notch” frequency $\omega _ { N } = \sqrt { 1 / ( L C ) }$ rad/s.   
b. Using the Bode plot, estimate the “stop band” or input frequency range where the amplitude of the filter’s output signal is reduced to less than one-half of the amplitude of the input signal.   
c. If the resistance is changed to $R = 0 . 2 \ : \Omega$ describe how the performance of the band-stop filter changes and estimate the band-stop frequency range for one-half amplitude reduction [i.e., repeat part (b)].

9.25 A vibration isolation system has the transfer function $G ( s ) = F _ { T } ( s ) / F _ { \mathrm { i n } } ( s )$ where $f _ { \mathrm { i n } } ( t )$ is the applied force from an unbalanced rotating machine (the input) and $f _ { T } ( t )$ is the transmitted force to the base (the output). Figure P9.25 shows the Bode diagram of the vibration isolation system.

![](image/86a54329492da3594175608b41d170ef3c28b3579c010e10d1fb87fb15ef96b7.jpg)

<details>
<summary>line</summary>

| Frequency, ω, rad/s | Magnitude, dB |
| --- | --- |
| 1 | 0 |
| 10 | 5 |
| 100 | -25 |
| 1000 | -50 |
</details>

![](image/24b004124cc86b8fe84b830fb3d1cd6cc00d676574b2802d3ad79802296827f2.jpg)

<details>
<summary>line</summary>
