# EXAMPLE PROBLEMS AND SOLUTIONS

A–5–1. In the system of Figure $5 \mathrm { - } 4 9 , x ( t )$ is the input displacement and $\theta ( t )$ is the output angular displacement. Assume that the masses involved are negligibly small and that all motions are restricted to be small; therefore, the system can be considered linear. The initial conditions for x and u are zeros, or $x ( 0 - ) = 0$ and $\theta ( 0 - ) = 0$ . Show that this system is a differentiating element. Then obtain the response $\theta ( t )$ when $x ( t )$ is a unit-step input.

Solution. The equation for the system is

$$b (\dot {x} - L \dot {\theta}) = k L \theta$$

or

$$L \dot {\theta} + \frac {k}{b} L \theta = \dot {x}$$

The Laplace transform of this last equation, using zero initial conditions, gives

$$\left(L s + \frac {k}{b} L\right) \Theta (s) = s X (s)$$

And so

$$\frac {\Theta (s)}{X (s)} = \frac {1}{L} \frac {s}{s + (k / b)}$$

Thus the system is a differentiating system.

For the unit-step input $X ( s ) = 1 / s$ , the output $\Theta ( s )$ becomes

$$\Theta (s) = \frac {1}{L} \frac {1}{s + (k / b)}$$

The inverse Laplace transform of $\Theta ( s )$ gives

$$\theta (t) = \frac {1}{L} e ^ {- (k / b) t}$$

![](image/7439c6eaee9b8bcc57473c9672f3f8344ff1c429dc39ea218ba15356289c534f.jpg)

<details>
<summary>text_image</summary>

x
b
L
θ
k
No friction
</details>

Figure 5–49 Mechanical system.

![](image/158ee79869632b542ff713b3fc01c6f027f749d20232c77f5768d7cf143adff4.jpg)

<details>
<summary>line</summary>

| t | x(t) |
| --- | --- |
| 0 | 1 |
| 1 | 1 |
</details>

Figure 5–50 Unit-step input and the response of the mechanical system shown in Figure 5–49.   
![](image/d573aac42bb257bfd54deab1482b10135da6f1398ee43aafc5c5e81dec7ae13f.jpg)

<details>
<summary>line</summary>

| t | θ(t) |
| --- | --- |
| 0 | 1/L |
</details>

Note that if the value of $k / b$ is large, the response $\theta ( t )$ approaches a pulse signal, as shown in Figure 5–50.

A–5–2. Gear trains are often used in servo systems to reduce speed, to magnify torque, or to obtain the most efficient power transfer by matching the driving member to the given load.
