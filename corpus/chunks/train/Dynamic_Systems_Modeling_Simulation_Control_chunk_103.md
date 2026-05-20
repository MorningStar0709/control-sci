# Inductor

A simple coil of wire forms an inductor. Inductors store energy in the magnetic field that results from current flowing through the coil of wire. Figure 3.3 shows the symbol for a two-terminal inductor with current $I _ { L }$ and voltage potential $e _ { L }$ across the two terminals. Ideal inductors exhibit a linear relationship between current $I _ { L }$ and magnetic flux linkage ??

$$\lambda = L I _ {L} \tag {3.8}$$

where L is the inductance in webers/ampere (Wb/A) or henries (H). Magnetic flux linkage ?? has units of webers (Wb), and it is the product of magnetic flux density (Wb/m2), coil area (m2), and the number of turns (or loops) in the coil of wire. Inductance L depends on material and geometric properties, such as the number of loops (turns) and area of the coil. If the coil is wrapped around a ferromagnetic core, the inductance becomes a nonlinear function.

Faraday’s law of magnetic induction states that a coil of wire will have a voltage difference induced across it if the magnetic flux changes with time. The time derivative of flux linkage is equal to the voltage across the inductor

$$\dot {\lambda} = e _ {L} \tag {3.9}$$

For a fixed inductor with constant inductance L, we can substitute the time derivative of Eq. (3.8) into Eq. (3.9) to yield

$$e _ {L} = L \dot {I} _ {L} \tag {3.10}$$

Inductors can store energy in their magnetic field due to current

$$\xi_ {L} = \frac {1}{2} L I _ {L} ^ {2} \tag {3.11}$$

The time derivative of Eq. (3.11) yields the power

$$\dot {\xi} _ {L} = L I _ {L} \dot {I} _ {L} \tag {3.12}$$

Substituting Eq. (3.10) for $L \dot { I } _ { L }$ in Eq. (3.11), we see that power is voltage × current.

![](image/75dab18be0400f0a7f85d3f7e55216b9d4d9a4fc39f9ac722ce76f067641c24e.jpg)

<details>
<summary>chemical</summary>

Electrical circuit diagram showing inductor with voltage and current labels
</details>

Figure 3.3 Inductor element.

![](image/dadbfb4aba1a418583577f32489cbbe90f27fc808d578e724b76eca7270032e5.jpg)  
Figure 3.4 Ideal electrical sources: (a) voltage source and (b) current source.
