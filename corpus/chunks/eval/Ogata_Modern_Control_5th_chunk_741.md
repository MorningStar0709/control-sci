Equation (10–18) is known as Ackermann’s formula for the determination of the state feedback gain matrix K.

Regulator Systems and Control Systems. Systems that include controllers can be divided into two categories: regulator systems (where the reference input is constant, including zero) and control systems (where the reference input is time varying). In what follows we shall consider regulator systems. Control systems will be treated in Section 10–7.

Choosing the Locations of Desired Closed-Loop Poles. The first step in the pole-placement design approach is to choose the locations of the desired closed-loop poles. The most frequently used approach is to choose such poles based on experience in the root-locus design, placing a dominant pair of closed-loop poles and choosing other poles so that they are far to the left of the dominant closed-loop poles.

Note that if we place the dominant closed-loop poles far from the jv axis, so that the system response becomes very fast, the signals in the system become very large, with the result that the system may become nonlinear. This should be avoided.

Another approach is based on the quadratic optimal control approach.This approach will determine the desired closed-loop poles such that it balances between the acceptable response and the amount of control energy required. (See Section 10–8.) Note that requiring a high-speed response implies requiring large amounts of control energy.Also, in general, increasing the speed of response requires a larger, heavier actuator, which will cost more.

EXAMPLE 10–1 Consider the regulator system shown in Figure 10–2. The plant is given by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} u$$

where

$$
\mathbf {A} = \left[ \begin{array}{c c c} 0 & 1 & 0 \\ 0 & 0 & 1 \\ - 1 & - 5 & - 6 \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{c} 0 \\ 0 \\ 1 \end{array} \right]
$$

The system uses the state feedback control u=–Kx. Let us choose the desired closed-loop poles at

$$s = - 2 + j 4, \quad s = - 2 - j 4, \quad s = - 1 0$$

(We make such a choice because we know from experience that such a set of closed-loop poles will result in a reasonable or acceptable transient response.) Determine the state feedback gain matrix K.

![](image/2662ca8141576a52f106dfc8fb11e510e8e3a8ba883b876eef7df49964308a7b.jpg)

<details>
<summary>flowchart</summary>
