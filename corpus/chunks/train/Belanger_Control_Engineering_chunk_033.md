# Example 2.2 (Active Suspension)

Description: Figure 2.4 shows a simple model of a vehicle suspension. The mass M is the body of the vehicle, and the small mass m is the unsprung part, e.g., the tires, axles, and so forth. Spring $K_{1}$ and dash-pot D are passive suspension elements, with a force u, possibly provided by a hydraulic actuator, added for active suspension. Spring $K_{2}$ acts between the axle and the road and models the stiffness of the tires. The height $y_{R}$ of the roadway with respect to an inertial reference varies, and the vehicle is moving at constant speed V. The purpose of control is to ensure ride quality.

Inputs and Outputs: The active suspension force u is the control input, and the roadway height $y_{R}(t)$ is the disturbance input. The output is the height of the vehicle body, $x_{1}$ , with respect to the reference.

Basic Principles: The force exerted by a spring is $K(x - x_{0})$ , where x is the spring length and $x_{0}$ is the length when the spring is at rest; this is known as Hooke's law. A dash-pot exerts a force $D\dot{x}$ , where x is the distance between the two ends.

Objectives: Write a model for the system, and simulate for the condition is given.

Solution The force exerted by the top spring is $K_{1}(x_{1} - x_{2} - x_{10})$ , where $x_{10}$ is the rest length. The reference direction is such as to pull the two masses together; physically, if $x_{2}$ stays fixed and $x_{1}$ increases, the force must act downward on $M$ . The damping force is $D(\dot{x}_1 - \dot{x}_2)$ . If $x_2$ is fixed and $\dot{x}_1$ is positive, the damper resists motion and hence must pull $M$ downward. With $v_1 = \dot{x}_1$ and $v_2 = \dot{x}_2$ , Newton's second law yields

![](image/08d20d615c258070a983899f061dff92e07c3a930cb2d2dcb63f63b9aff3a1c1.jpg)

<details>
<summary>text_image</summary>

M
K₁
u
D
u
m
K₂
x₁
x₂
yR
t
</details>

Figure 2.4 An active suspension system

$$M \frac {d v _ {1}}{d t} = - K _ {1} (x _ {1} - x _ {2} - x _ {1 0}) - D (v _ {1} - v _ {2}) - M g + um \frac {d v _ {2}}{d t} = K _ {1} (x _ {1} - x _ {2} - x _ {1 0}) + D (v _ {1} - v _ {2}) - K _ {2} (x _ {2} - y _ {R} - x _ {2 0}) - m g - u.$$

Note that, because of Newton's third law, $u$ must act in opposite directions on $M$ and $m$ .

Including the two velocity definitions, the state equations are
