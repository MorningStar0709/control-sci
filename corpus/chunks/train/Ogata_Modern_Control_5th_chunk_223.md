MATLAB Program 5–10   
% ---- Unit-ramp response ----
% ***** The unit-ramp response is obtained as the unit-step
% response of G(s)/s *****
% ***** Enter the numerator and denominator of G(s)/s *****
num = [2 1];
den = [1 1 1 0];
% ***** Specify the computing time points (such as t = 0:0.1:10)
% and then enter step-response command: c = step(num,den,t) *****
t = 0:0.1:10;
c = step(num,den,t);
% ***** In plotting the ramp-response curve, add the reference
% input to the plot. The reference input is t. Add to the
% argument of the plot command with the following: t,t,'-'. Thus
% the plot command becomes as follows: plot(t,c,'o',t,t,'-') *****
plot(t,c,'o',t,t,'-')
% ***** Add grid, title, xlabel, and ylabel *****
grid
title('Unit-Ramp Response Curve for System G(s) = (2s + 1)/(s^2 + s + 1)')
xlabel('t Sec')
ylabel('Input and Output')

![](image/61e92291d6ec49b7d1f890b5eddcaa21259ecf273206ae33817c08f6483dff8d.jpg)

<details>
<summary>line</summary>

| t Sec | Input and Output |
| --- | --- |
| 0 | 0 |
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 4 |
| 5 | 5 |
| 6 | 6 |
| 7 | 7 |
| 8 | 8 |
| 9 | 9 |
| 10 | 10 |
</details>

Figure 5–26 Unit-ramp response curve.

Unit-Ramp Response of a System Defined in State Space. Next, we shall treat the unit-ramp response of the system in state-space form. Consider the system described by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {B} uy = \mathbf {C x} + D u$$

where u is the unit-ramp function. In what follows, we shall consider a simple example to explain the method. Consider the case where

$$
\begin{array}{l} \mathbf {A} = \left[ \begin{array}{c c} 0 & 1 \\ - 1 & - 1 \end{array} \right], \quad \mathbf {B} = \left[ \begin{array}{c} 0 \\ 1 \end{array} \right], \quad \mathbf {x} (0) = \mathbf {0} \\ \mathbf {C} = \left[ \begin{array}{c c} 1 & 0 \end{array} \right], \qquad \qquad D = [ 0 ] \\ \end{array}
$$

When the initial conditions are zeros, the unit-ramp response is the integral of the unitstep response. Hence the unit-ramp response can be given by

$$z = \int_ {0} ^ {t} y d t \tag {5-44}$$

From Equation (5–44), we obtain

$$\dot {z} = y = x _ {1} \tag {5-45}$$

Let us define

$$z = x _ {3}$$

Then Equation (5–45) becomes

$$\dot {x} _ {3} = x _ {1} \tag {5-46}$$

Combining Equation (5–46) with the original state-space equation, we obtain
