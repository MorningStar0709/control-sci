A–4–7. Figure 4–34 shows a hydraulic jet-pipe controller. Hydraulic fluid is ejected from the jet pipe. If the jet pipe is shifted to the right from the neutral position, the power piston moves to the left, and vice versa. The jet-pipe valve is not used as much as the flapper valve because of large null flow, slower response, and rather unpredictable characteristics. Its main advantage lies in its insensitivity to dirty fluids.

Suppose that the power piston is connected to a light load so that the inertia force of the load element is negligible compared to the hydraulic force developed by the power piston. What type of control action does this controller produce?

Solution. Define the displacement of the jet nozzle from the neutral position as x and the displacement of the power piston as y. If the jet nozzle is moved to the right by a small displacement x, the oil flows to the right side of the power piston, and the oil in the left side of the power piston is returned to the drain. The oil flowing into the power cylinder is at high pressure; the oil flowing out from the power cylinder into the drain is at low pressure. The resulting pressure difference causes the power piston to move to the left.

Figure 4–33 (a) Uncovered-portarea-A-versus displacement-x curve for the overlapped valve; (b) uncoveredport-area-A-versusdisplacement-x curve for the underlapped valve.   
![](image/39d226b5755219c8567a6cfed6bd117eb0a7fc829a73ba8773d7e46a790f24ef.jpg)

<details>
<summary>text_image</summary>

A
x
x₀/2
</details>

![](image/892db92e4ff3dba385edac9859f1212ee2ccecb5f203b18d199beeb4622ba93f.jpg)

<details>
<summary>text_image</summary>

A
Effective area
Area exposed to high pressure
x
x₀/2
Area exposed to low pressure
</details>

(b)

![](image/c2406b2e6183cea83fcaedcbf38666d2433138cf1c11dfca10b7842aff82b107.jpg)

<details>
<summary>text_image</summary>

A
y
x
Oil under pressure
</details>

Figure 4–34 Hydraulic jet-pipe controller.

For a small jet-nozzle displacement x, the flow rate q to the power cylinder is proportional to x; that is,

$$q = K _ {1} x$$

For the power cylinder,

$$A \rho d y = q d t$$

where A is the power-piston area and $\rho$ is the density of oil. Hence

$$\frac {d y}{d t} = \frac {q}{A \rho} = \frac {K _ {1}}{A \rho} x = K x$$

where $K = K _ { 1 } / ( A \rho ) =$ constant. The transfer function= $Y ( s ) / X ( s )$ is thus

$$\frac {Y (s)}{X (s)} = \frac {K}{s}$$
