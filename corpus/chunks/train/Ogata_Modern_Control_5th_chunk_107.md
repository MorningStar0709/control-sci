Solution. Assume that displacements x and y are measured from respective steady-state positions in the absence of the input u. Applying the Newton’s second law to this system, we obtain

$$m _ {1} \ddot {x} = k _ {2} (y - x) + b (\dot {y} - \dot {x}) + k _ {1} (u - x)m _ {2} \ddot {y} = - k _ {2} (y - x) - b (\dot {y} - \dot {x})$$

Hence, we have

$$m _ {1} \ddot {x} + b \dot {x} + (k _ {1} + k _ {2}) x = b \dot {y} + k _ {2} y + k _ {1} um _ {2} \ddot {y} + b \dot {y} + k _ {2} y = b \dot {x} + k _ {2} x$$

Taking Laplace transforms of these two equations, assuming zero initial conditions, we obtain

$$\left[ m _ {1} s ^ {2} + b s + \left(k _ {1} + k _ {2}\right) \right] X (s) = \left(b s + k _ {2}\right) Y (s) + k _ {1} U (s)\left[ m _ {2} s ^ {2} + b s + k _ {2} \right] Y (s) = \left(b s + k _ {2}\right) X (s)$$

Eliminating X(s) from the last two equations, we have

$$\left(m _ {1} s ^ {2} + b s + k _ {1} + k _ {2}\right) \frac {m _ {2} s ^ {2} + b s + k _ {2}}{b s + k _ {2}} Y (s) = \left(b s + k _ {2}\right) Y (s) + k _ {1} U (s)$$

which yields

$$\frac {Y (s)}{U (s)} = \frac {k _ {1} \left(b s + k _ {2}\right)}{m _ {1} m _ {2} s ^ {4} + \left(m _ {1} + m _ {2}\right) b s ^ {3} + \left[ k _ {1} m _ {2} + \left(m _ {1} + m _ {2}\right) k _ {2} \right] s ^ {2} + k _ {1} b s + k _ {1} k _ {2}}$$

![](image/cb0d6a078957f924c12be157d119a00a9329db0edaaaa69bb7878f32fd7df6b1.jpg)

<details>
<summary>text_image</summary>

m₂
k₂
b
m₁
k₁
u
x
y
</details>

Figure 3–21 Suspension system.

Figure 3–22 Mechanical system.   
![](image/321f62f21c663189f4de8d23a4c5129d5a38045f0cf55a10d276ffb3e5e090b2.jpg)

<details>
<summary>text_image</summary>

b
m₁
k
m₂
y₁
y₂
u
</details>

A–3–3. Obtain a state-space representation of the system shown in Figure 3–22.

Solution. The system equations are

$$
\begin{array}{l} m _ {1} \ddot {y} _ {1} + b \dot {y} _ {1} + k (y _ {1} - y _ {2}) = 0 \\ m _ {2} \ddot {y} _ {2} + k (y _ {2} - y _ {1}) = u \\ \end{array}
$$

The output variables for this system are $y _ { 1 }$ and $y _ { 2 }$ . Define state variables as

$$x _ {1} = y _ {1}x _ {2} = \dot {y} _ {1}x _ {3} = y _ {2}x _ {4} = \dot {y} _ {2}$$

Then we obtain the following equations:

$$
\begin{array}{l} \dot {x} _ {1} = x _ {2} \\ \dot {x} _ {2} = \frac {1}{m _ {1}} \left[ - b \dot {y} _ {1} - k (y _ {1} - y _ {2}) \right] = - \frac {k}{m _ {1}} x _ {1} - \frac {b}{m _ {1}} x _ {2} + \frac {k}{m _ {1}} x _ {3} \\ \dot {x} _ {3} = x _ {4} \\ \dot {x} _ {4} = \frac {1}{m _ {2}} \left[ - k \left(y _ {2} - y _ {1}\right) + u \right] = \frac {k}{m _ {2}} x _ {1} - \frac {k}{m _ {2}} x _ {3} + \frac {1}{m _ {2}} u \\ \end{array}
$$

Hence, the state equation is
