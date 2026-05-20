# Parametric Sensitivity Analysis

The objective of the vibration isolation system is to suppress the motion of the vehicle cabin floor $z _ { 0 } ( t )$ that is transmitted to the driver. The previous sections presented the impulse and frequency responses for the nominal seat-suspension parameters in Table 11.1. It is useful for the design engineer to understand the effect each parameter has on the performance of the system. A parametric sensitivity analysis is a standard engineering method where each free parameter is varied and the sensitivity (or lack thereof) of the system’s performance metric is determined. Such information will aid the design engineer in optimizing system performance in the context of operating constraints.

Transmissibility is the performance measure of the parametric analysis, and it is defined by the amplitude ratio of the frequency-response output $z _ { 2 } ( t )$ and sinusoidal input $z _ { 0 } ( t )$ . Transmissibility is essentially the magnitude plot from the Bode diagram for output $y = z _ { 2 }$ . It can be computed using the MATLAB command where w is the input frequency in rad/s. MATLAB M-file script 11.1 computes the transmissibility for input frequencies ranging from 0.1 to 5 Hz. Previous studies have shown that the human body is most sensitive to relatively low-frequency vibrations in the 0.5–5 Hz range [2].

Figure 11.10 shows the transmissibility $| z _ { 2 } ( t ) | / | z _ { 0 } ( t ) |$ for three parametric variations in seat-cushion stiffness: nominal $k _ { 2 } = 8 2 3 0 \mathrm { N } / \mathrm { m }$ , 50% reduction in $k _ { 2 } .$ , and 50% increase in $k _ { 2 }$ . The input frequencies range from 0.1 to 5 Hz (or, 0.63–31.41 rad/s). Stiffer seat cushions suppress the peak transmissibility and increase the resonant frequency where the peak transmissibility occurs. Increasing stiffness $k _ { 2 }$ also increases the transmitted vibrations at the higher frequencies. Vehicle vibrations are predominantly in the 2.5 Hz (15.7 rad/s) range [2], and therefore the seat-cushion stiffness must be selected so that a good trade-off exists between low peak transmissibility and low transmissibility around 2.5 Hz. In light of these constraints, the nominal

MATLAB M-file 11.1   
```matlab
% M-file for computing transmissibility for
% the seat-suspension system
