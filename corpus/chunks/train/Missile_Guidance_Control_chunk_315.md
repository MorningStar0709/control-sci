Assuming a point-mass model for the missile, the three-dimensional equations can be stated as follows [13]:

$$\frac {d x}{d t} = V \cos \gamma \cos \psi , \tag {4.82a}\frac {d y}{d t} = V \cos \gamma \sin \psi , \tag {4.82b}\frac {d h}{d t} = V _ {m} \sin \gamma , \tag {4.82c}\frac {d E}{d t} = [ T - D (h, M, n ] (V / W), \tag {4.82d}\frac {d \gamma}{d t} = (n _ {v} - \cos \gamma) (g / V), \tag {4.82e}\frac {d \psi}{d t} = (n _ {h} / \cos \gamma) (g / V), \tag {4.82f}$$

where

x = downrange displacement of the missile,

y = cross-range displacement of the missile,

h = altitude of the missile,

g = gravitational acceleration,

γ = flight path angle,

Vm = velocity of the missile = (2g (E – h))1/2,

E = specific energy,

M = Mach number,

T = thrust,

D = aerodynamic drag,

W = weight of the missile,

nh, nv = horizontal and vertical load factors, respectively,

n = 
(n2 + n2v) = resultant load factor.

![](image/e2767a5aaf5a118639797cf1cb65585dd3727c0ff8945c38e8e5e85920ce3b1e.jpg)

<details>
<summary>text_image</summary>

Z
Target
Vt
R LOS
Vm
ε
Interceptor
ψ
Y
X
</details>

Fig. 4.31. Three-dimensional pursuit–evasion geometry.

In the above set of equations, the variation of drag with altitude, Mach number, and load factor is given by the expression [13]

$$D / W (h, M, n) = D _ {o} + D _ {i} n ^ {k}, \tag {4.83a}D _ {o} = (q A / W) C _ {D o} (h, M), \tag {4.83b}D _ {i} = (q A / W) ^ {i - k} C _ {D i} (M), \tag {4.83c}Q = \frac {1}{2} \rho (h) V ^ {2}, \tag {4.83d}$$

where

$$A = \text { reference area },C _ {D o} = \text { zero - lift drag coefficient },C _ {D i} = \text { induced drag coefficient },\rho (h) = \text { air density },q = \text { dynamic pressure }.$$

The assumptions on these equations are (1) pursuer and evader are considered as constant-speed mass points, (2) the pursuer is a homing missile launched against an initially nonmaneuvering evader (i.e., target), (3) pursuer and evader have perfect information on their relative state with respect to the other, and (4) gravity can be neglected.

Referring to Figure 4.31, one can write the three second-order differential equations as follows [34]:
