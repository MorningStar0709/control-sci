# Example A.1 Double integrator

The double integrator is used throughout the book as a main example to illustrate the theories presented. The process is described by the differential equation

$$\frac {d ^ {2} y}{d t ^ {2}} = u \tag {A.1}$$

The transfer function is $G(s) = 1/s^{2}$ . We introduce y and $\dot{y}$ as the states $x_{1}$ and $x_{2}$ , respectively, of the system. The state-space representation is then

$$
\frac {d x}{d t} = \left( \begin{array}{l l} 0 & 1 \\ 0 & 0 \end{array} \right) x + \binom {0} {1} u \tag {A.2}

y = \left( \begin{array}{l l} 1 & 0 \end{array} \right) x
$$

Sampling (A.2) using a zero-order hold with the sampling period h gives the discrete-time system (see Example 2.2)

$$
x (k h + h) = \left( \begin{array}{c c} 1 & h \\ 0 & 1 \end{array} \right) x (k h) + \binom {h ^ {2} / 2} {h} u (k h) \tag {A.3}

y (k h) = \left( \begin{array}{l l} 1 & 0 \end{array} \right) x (k h)
$$

The pulse-transfer operator of (A.3) is given by

$$H (q) = \frac {h ^ {2} (q + 1)}{2 (q - 1) ^ {2}} \tag {A.4}$$

There are several physical processes that can be described as double integrators. One such is the attitude of a satellite, which can be described by the equation

$$J \frac {d ^ {2} \theta}{d t ^ {2}} = M _ {c} + M _ {d}$$

![](image/2b5a7adb3ddcd8b13568adc4850fb34b83ca13f3242f03a4f247db5039d93b7c.jpg)

<details>
<summary>text_image</summary>

Torque motor
Ball
x
φ
Beam
u
</details>

Figure A.1 Schematic illustration of the ball and beam.

where $\theta$ is the attitude angle, $M_{c}$ is the control torque, $M_{d}$ is the disturbing torque, and J is the moment of inertia.

Another example that can be described by the double integrator is a rolling ball on a tilting beam (see Fig. A.1). The equation of the ball and beam can be described by

$$J \frac {d ^ {2} \theta}{d t ^ {2}} = m g r \sin \varphi \approx m g r \varphix = r \theta$$

or

$$\frac {d ^ {2} x}{d t ^ {2}} = m g r ^ {2} \varphi / J$$

where $\theta$ is the angle of the ball, g is the normal acceleration, x is the position of the ball, and $\varphi$ is the tilting angle of the beam.
