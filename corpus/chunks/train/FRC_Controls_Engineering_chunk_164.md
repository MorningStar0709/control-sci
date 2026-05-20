# 6.10.7 Do flywheels need PD control?

PID controllers typically control voltage to a motor in FRC independent of the equations of motion of that motor. For position PID control, large values of $K _ { p }$ can lead to overshoot and $K _ { d }$ is commonly used to reduce overshoots. Let’s consider a flywheel controlled with a standard PID controller. Why wouldn’t $K _ { d }$ provide damping for velocity overshoots in this case?

PID control is designed to control second-order and first-order systems well. It can be used to control a lot of things, but struggles when given higher order systems. It has three degrees of freedom. Two are used to place the two poles of the system, and the third is used to remove steady-state error. With higher order systems like a one input, seven state system, there aren’t enough degrees of freedom to place the system’s poles in desired locations. This will result in poor control.

The math for PID doesn’t assume voltage, a motor, etc. It defines an output based on derivatives and integrals of its input. We happen to use it for motors because it actually works pretty well for it because motors are second-order systems.

The following math will be in continuous time, but the same ideas apply to discrete time. This is all assuming a velocity controller.

Our simple motor model hooked up to a mass is

$$V = I R + \frac {\omega}{K _ {v}} \tag {6.25}\tau = I K _ {t} \tag {6.26}\tau = J \frac {d \omega}{d t} \tag {6.27}$$

For an explanation of where these equations come from, read section 12.1.

First, we’ll solve for $\textstyle { \frac { d \omega } { d t } }$ in terms of V .

Substitute equation (6.26) into equation (6.25).

$$V = I R + \frac {\omega}{K _ {v}}V = \left(\frac {\tau}{K _ {t}}\right) R + \frac {\omega}{K _ {v}}$$

Substitute in equation (6.27).

$$V = \frac {(J \frac {d \omega}{d t})}{K _ {t}} R + \frac {\omega}{K _ {v}}$$

Solve for $\textstyle { \frac { d \omega } { d t } }$

$$V = \frac {J \frac {d \omega}{d t}}{K _ {t}} R + \frac {\omega}{K _ {v}}V - \frac {\omega}{K _ {v}} = \frac {J \frac {d \omega}{d t}}{K _ {t}} R\frac {d \omega}{d t} = \frac {K _ {t}}{J R} \left(V - \frac {\omega}{K _ {v}}\right)\underbrace {\frac {d \omega}{d t}} _ {\dot {\mathbf {x}}} = \underbrace {- \frac {K _ {t}}{J R K _ {v}}} _ {\mathbf {A}} \underbrace {\omega} _ {\mathbf {x}} + \underbrace {\frac {K _ {t}}{J R}} _ {\mathbf {B}} \underbrace {V} _ {\mathbf {u}} \tag {6.28}$$
