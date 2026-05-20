# 7.6 The Modulation Model

A characteristic feature of computer-controlled systems with zero-order hold is that the control signal is constant over the sampling period. This fact is used in Chapter 2 to describe how the system changes from one sampling instant to the next by integrating the system equations over one sampling period; this section attempts to describe what happens between the sampling instants. Other mathematical models are then needed, because it is no longer sufficient to model signals as sequences (functions that map Z to R); instead they must be modeled as continuous-time functions (functions that map R to R).

![](image/cae8a745555ff6db95e9df9770a3513d98da5713e3d1ce22ecee97f41105d1c5.jpg)

<details>
<summary>text_image</summary>

Clock
i
R
C
u
y
</details>

Figure 7.15 Schematic diagram of a sample-and-hold circuit.

The central theme is to develop the modulation model. This model is more complicated than the stroboscopic model discussed in Chapter 2. The main difficulty is that the periodic nature of sampled-data systems must be taken into account. The system can be described as an amplitude modulator followed by a linear system. The modulation signal is a pulse train. A further idealization is obtained by approximating the pulses by impulses. The model has its origin in early work on sampled-data systems by MacColl (1945), Linvill (1951), and others.

In the special case of computer control with a unit-gain algorithm and negligible time delay, the combined action of the A-D converter, the computer, and the D-A converter can be described as a system that samples the analog signal and produces another analog signal that is constant over the sampling periods. Such a circuit is called a sample-and-hold circuit. An A-D converter can also be described as a sample-and-hold circuit. The hold circuit keeps the analog voltage constant during the conversion to a digital representation. A more detailed model for the sample-and-hold circuit will first be developed.
