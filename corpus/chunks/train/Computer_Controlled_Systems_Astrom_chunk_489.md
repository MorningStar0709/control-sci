# Differentiation and Tustin Approximations

A transfer function represents a differential equation. It is natural to obtain a difference equation by approximating the derivatives with a forward difference (Euler's method)

$$p x (t) = \frac {d x (t)}{d t} \approx \frac {x (t + h) - x (t)}{h} = \frac {q - 1}{h} x (t)$$

or a backward difference

$$p x (t) = \frac {d x (t)}{d t} \approx \frac {x (t) - x (t - h)}{h} = \frac {q - 1}{q h} x (t)$$

In the transform variables, this corresponds to replacing s by $(z-1)/h$ or $(z-1)/zh$ . Section 2.8 shows that the variables z and s are related in some respects as $z = \exp(sh)$ . The difference approximations correspond to the series expansions

$$z = e ^ {s h} \approx 1 + s h \quad (\text { Euler's method }) \tag {8.1}z = e ^ {s h} \approx \frac {1}{1 - s h} \quad (\text { Backward difference }) \tag {8.2}$$

Another approximation, which corresponds to the trapezoidal method for numerical integration, is

$$z = e ^ {s h} \approx \frac {1 + s h / 2}{1 - s h / 2} \quad (\text { Trapezoidal method }) \tag {8.3}$$

In digital-control context, the approximation in (8.3) is often called Tustin's approximation, or the bilinear transformation. Using the approximation methods above, the pulse-transfer function $H(z)$ is obtained by simply replacing the

![](image/f5c96a946aea5531cc2097f5ebeef70ae6d76945324f44ada5bcfc05303fdd0f.jpg)  
Figure 8.2 Mapping of the stability region in the s-plane on the z-plane for the transformations (8.4), (8.5), and (8.6).

argument $s$ in $G(s)$ by $s'$ , where

$$s ^ {\prime} = \frac {z - 1}{h} \quad (\text { Forward difference or Euler's method }) \tag {8.4}s ^ {\prime} = \frac {z - 1}{z h} \quad (\text { Backward difference }) \tag {8.5}s ^ {\prime} = \frac {2}{h} \cdot \frac {z - 1}{z + 1} \quad (\text { Tustin's approximation }) \tag {8.6}$$

Hence

$$H (z) = G \left(s ^ {\prime}\right)$$

The methods are very easy to apply even for hand calculations. Figure 8.2 shows how the stability region $\operatorname{Re}s < 0$ in the $s$ -plane is mapped on the $z$ -plane for the mappings (8.4), (8.5), and (8.6).
