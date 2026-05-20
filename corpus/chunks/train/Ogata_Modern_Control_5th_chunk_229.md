# MATLAB Program 5–14

```matlab
% ---- Response to initial condition ----
% ***** System response to initial condition is converted to
% a unit-step response by modifying the numerator polynomial *****
% ***** Enter the numerator and denominator of the transfer
% function G(s) *****
num = [0.1 0.35 0];
den = [1 3 2];
% ***** Enter the following step-response command *****
step(num,den)
% ***** Enter grid and title of the plot *****
grid
title('Response of Spring-Mass-Damper System to Initial Condition') 
```

Figure 5–31 Response of the mechanical system considered in Example 5–8.   
![](image/8708704bd6ea669dcfb34c9084721c8364bd275f3f666258261d06879121369d.jpg)

<details>
<summary>line</summary>

| Time (sec) | Amplitude |
| --- | --- |
| 0.0 | 0.10 |
| 0.5 | 0.095 |
| 1.0 | 0.08 |
| 1.5 | 0.06 |
| 2.0 | 0.04 |
| 2.5 | 0.025 |
| 3.0 | 0.015 |
| 3.5 | 0.01 |
| 4.0 | 0.005 |
| 4.5 | 0.002 |
| 5.0 | 0.001 |
</details>

Response to Initial Condition (State-Space Approach, Case 1). Consider the system defined by

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x}, \quad \mathbf {x} (0) = \mathbf {x} _ {0} \tag {5-49}$$

Let us obtain the response x(t) when the initial condition x(0) is specified.Assume that there is no external input function acting on this system. Assume also that x is an n-vector.

First, take Laplace transforms of both sides of Equation (5–49).

$$s \mathbf {X} (s) - \mathbf {x} (0) = \mathbf {A X} (s)$$

This equation can be rewritten as

$$s \mathbf {X} (s) = \mathbf {A X} (\mathrm{s}) + \mathbf {x} (0) \tag {5-50}$$

Taking the inverse Laplace transform of Equation (5–50), we obtain

$$\dot {\mathbf {x}} = \mathbf {A} \mathbf {x} + \mathbf {x} (0) \delta (t) \tag {5-51}$$

(Notice that by taking the Laplace transform of a differential equation and then by taking the inverse Laplace transform of the Laplace-transformed equation we generate a differential equation that involves the initial condition.)

Now define

$$\dot {\mathbf {z}} = \mathbf {x} \tag {5-52}$$

Then Equation (5–51) can be written as

$$\ddot {\mathbf {z}} = \mathbf {A} \dot {\mathbf {z}} + \mathbf {x} (0) \delta (t) \tag {5-53}$$

By integrating Equation (5–53) with respect to t, we obtain

$$\dot {\mathbf {z}} = \mathbf {A} \mathbf {z} + \mathbf {x} (0) 1 (t) = \mathbf {A} \mathbf {z} + \mathbf {B} u \tag {5-54}$$

where

$$\mathbf {B} = \mathbf {x} (0), \quad u = 1 (t)$$

Referring to Equation (5–52), the state ${ \bf x } ( t )$ is given by Thus,z  (t).
