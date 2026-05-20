# Derivation of the Frequency Response

Repeating Eq. (9.11), the frequency response of the LTI system in Fig. 9.1 or Fig. 9.3 is

$$y _ {\mathrm{ss}} (t) = G (j \omega) U (j \omega) e ^ {j \omega t} \tag {9.12}$$

where the subscript ss denotes “steady state.” The sinusoidal transfer function $G ( j \omega )$ is a complex function of frequency ?? and (generally) consists of real and imaginary parts. Figure 9.4 shows the sinusoidal transfer function $G ( j \omega )$ as a point in the complex plane with real and imaginary components. The reader should recall that the complex plane shown in Fig. 9.4 is essentially a Cartesian coordinate frame where the horizontal axis consists of real numbers and the vertical axis consists of imaginary numbers. Therefore, we can represent the complex value $G ( j \omega )$ using either Cartesian or polar coordinates. Referring to Fig. 9.4, the complex value of $G ( j \omega )$ is

Cartesian form: $G ( j \omega ) = A + j B$

$\mathrm { P o l a r ~ f o r m : } \quad G ( j \omega ) = | G ( j \omega ) | e ^ { j \phi } = | G ( j \omega ) | ( \cos \phi + j \sin \phi )$

![](image/f23ce91b3eb9561aa75a6d2f6798f31d4d28f64562f31546dd0ae3be4ab624d0.jpg)

<details>
<summary>text_image</summary>

Imaginary
Magnitude
|G(jω)|
Phase angle
φ = ∠G(jω)
0
A
Real
B
</details>

Figure 9.4 Magnitude and phase of the sinusoidal transfer function $G ( j \omega )$ .

where the magnitude (or absolute value) and phase (or argument) of $G ( j \omega )$ are

$$\text { Magnitude: } \quad | G (j \omega) | = \sqrt {A ^ {2} + B ^ {2}} \tag {9.13}\text { Phase angle: } \quad \phi = \angle G (j \omega) = \tan^ {- 1} \left(\frac {B}{A}\right) \tag {9.14}$$

Computing the magnitude and phase angle of a complex number is relatively easy in MATLAB using the abs (absolute value) and angle commands. As a quick example, consider the complex number $X = 4 + j 2$ and the following MATLAB commands:

$$
\begin{array}{l} > > X = 4 + j * 2; \quad \% \text { define the complex number } X = 4 + j 2 \\ > > \operatorname{mag} X = \text {abs} (X) \quad \% \text {compute the magnitude (absolute value) of} X \\ > > \text { phaseX } = \text { angle } (X) \quad \% \text { compute   the   phase   angle   of } X (\text { rad }) \\ \end{array}
$$

After executing these commands we obtain

$$\operatorname{magX} = 4. 4 7 2 1 \text { and } \operatorname{phaseX} = 0. 4 6 3 6 (\text { or }, 2 6. 5 7 ^ {\circ})$$

Next, we can replace $G ( j \omega )$ in Eq. (9.12) with its polar form and hence the frequency response becomes
