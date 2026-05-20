# 3–2 MATHEMATICAL MODELING OF MECHANICAL SYSTEMS

This section first discusses simple spring systems and simple damper systems. Then we derive transfer-function models and state-space models of various mechanical systems.

Figure 3–1 (a) System consisting of two springs in parallel; (b) system consisting of two springs in series.   
![](image/531855554638121781a116827b01a1b5282c1ec559ce5b0c209b2258fef79902.jpg)

<details>
<summary>text_image</summary>

k₁
k₂
x
F
</details>

(a)

![](image/e303e4186fbb721bb2c275bce354b0ff4d79c0e044054a7e0c50493c62e3d700.jpg)

<details>
<summary>text_image</summary>

k₁
y
x
k₂
F
</details>

(b)

EXAMPLE 3–1 Let us obtain the equivalent spring constants for the systems shown in Figures 3–1(a) and (b), respectively.

For the springs in parallel [Figure 3–1(a)] the equivalent spring constant $k _ { \mathrm { e q } }$ is obtained from

$$k _ {1} x + k _ {2} x = F = k _ {\mathrm{eq}} x$$

or

$$k _ {\mathrm{eq}} = k _ {1} + k _ {2}$$

For the springs in series [Figure–3–1(b)], the force in each spring is the same. Thus

$$k _ {1} y = F, \quad k _ {2} (x - y) = F$$

Elimination of y from these two equations results in

$$k _ {2} \left(x - \frac {F}{k _ {1}}\right) = F$$

or

$$k _ {2} x = F + \frac {k _ {2}}{k _ {1}} F = \frac {k _ {1} + k _ {2}}{k _ {1}} F$$

The equivalent spring constant $k _ { \mathrm { e q } }$ for this case is then found as

$$k _ {\mathrm{eq}} = \frac {F}{x} = \frac {k _ {1} k _ {2}}{k _ {1} + k _ {2}} = \frac {1}{\frac {1}{k _ {1}} + \frac {1}{k _ {2}}}$$

EXAMPLE 3–2 Let us obtain the equivalent viscous-friction coefficient $b _ { \mathrm { e q } }$ for each of the damper systems shown in Figures 3–2(a) and (b).An oil-filled damper is often called a dashpot.A dashpot is a device that provides viscous friction, or damping. It consists of a piston and oil-filled cylinder.Any relative motion between the piston rod and the cylinder is resisted by the oil because the oil must flow around the piston (or through orifices provided in the piston) from one side of the piston to the other.The dashpot essentially absorbs energy.This absorbed energy is dissipated as heat, and the dashpot does not store any kinetic or potential energy.

Figure 3–2 (a) Two dampers connected in parallel; (b) two dampers connected in series.   
![](image/5d848cc08fa154619d521248454a022d73eecf361f801f0af6acc15f6378fd17.jpg)

<details>
<summary>flowchart</summary>
