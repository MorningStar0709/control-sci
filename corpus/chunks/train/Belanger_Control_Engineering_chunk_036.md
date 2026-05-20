# Example 2.3 (Train)

Description: A train, consisting of one or two locomotives and many identical cars, is being driven over a horizontal track. One locomotive heads the train, and there may be a second at the rear. The cars and locomotives are joined by identical couplings modeled by a spring-and-damper parallel combination. (See Figure 2.8 for details). The control objectives are to maintain a desired speed and to avoid overstressing the couplings.

Inputs and Outputs: The control inputs are the forces $F_{1}$ and $F_{2}$ supplied by the locomotives or, more precisely, the forces exerted by the tracks on the locomotives. Velocities are with respect to the ground. The outputs are the velocity of the head locomotive and the spacing between the units of the train.

Basic Principles: The couplers joining the ith and $(i+1)$ st units deliver a force $K(x_{i+1}-x_{0})+D(v_{i}-v_{i+1})$ where $v_{i}$ is the velocity of the ith car with respect to the inertial reference frame.

Objective: Derive a model, and simulate under given conditions.

![](image/c25f96fee9db363e81333640707976133f0dcff359202b657a5c760a74f839a8.jpg)

<details>
<summary>text_image</summary>

x₃
x₂
m
l
m
M
F
x₁
</details>

Figure 2.8 Model of a train

Solution For the head locomotive,

$$M \dot {v} _ {1} = F _ {1} - K (x _ {2} - x _ {0}) - D (v _ {1} - v _ {2}). \tag {2.23}$$

For the $i$ th car,

$$m \dot {v} _ {i} = K (x _ {i} - x _ {0}) + D (v _ {i - 1} - v _ {i}) - K (x _ {i + 1} - x _ {0}) - D (v _ {i} - v _ {i + 1}),i = 2, 3, \dots , N - 1 \tag {2.24}$$

For the Nth car,

$$m \dot {v} _ {N} = K (x _ {N} - x _ {0}) + D (v _ {N - 1} - v _ {N}). \tag {2.25}$$

If the Nth car is replaced by a second locomotive, m is changed to M and a force $F_{2}$ is added to the right-hand side (RHS) of Equation 2.25.

The other state equations are

$$\dot {x} _ {1} = v _ {1}\dot {x} _ {2} = v _ {1} - v _ {2}\dot {x} _ {3} = v _ {2} - v _ {3}$$

•
•
•

$$\dot {x} _ {N} = v _ {N - 1} - v _ {N}. \tag {2.26}$$

The outputs are $v_{1}$ , and the state variables $x_{2}, x_{3}, \ldots, x_{N}$ .

For the specific values $M = 2 \times 10^{5} \mathrm{~kg}$ , $m = 40,000 \mathrm{~kg}$ , $K = 2.5 \times 10^{6} \mathrm{~N/m}$ , $D = 1.5 \times 10^{5} \mathrm{~N/m/s}$ , and $x_{0} = 20 \mathrm{~m}$ , the state equations are Equation 2.26 and
