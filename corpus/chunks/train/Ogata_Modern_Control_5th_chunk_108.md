$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \\ \dot {x} _ {4} \end{array} \right] = \left[ \begin{array}{c c c c} 0 & 1 & 0 & 0 \\ - \frac {k}{m _ {1}} & - \frac {b}{m _ {1}} & \frac {k}{m _ {1}} & 0 \\ 0 & 0 & 0 & 1 \\ \frac {k}{m _ {2}} & 0 & - \frac {k}{m _ {2}} & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \\ x _ {4} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 0 \\ 0 \\ \frac {1}{m _ {2}} \end{array} \right] u
$$

and the output equation is

$$
\left[ \begin{array}{l} y _ {1} \\ y _ {2} \end{array} \right] = \left[ \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 0 & 0 & 1 & 0 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \\ x _ {3} \\ x _ {4} \end{array} \right]
$$

A–3–4. Obtain the transfer function $X _ { o } ( s ) / X _ { i } ( s )$ of the mechanical system shown in Figure 3–23(a). Also obtain the transfer function $E _ { o } ( s ) / E _ { i } ( s )$ of the electrical system shown in Figure 3–23(b). Show that these transfer functions of the two systems are of identical form and thus they are analogous systems.

Figure 3–23

(a) Mechanical system; (b) analogous electrical system.

![](image/f9a275160e45e4e44025d27745f48fc718d81e0af4803025638f37de80f6899c.jpg)

<details>
<summary>text_image</summary>

k₁
b₁
xᵢ
b₂
xₒ
k₂
y
</details>

(a)

![](image/3272963d8ed131f2570d89904fd0d1a293400893da2ac9095ae63de09e6b5bc3.jpg)

<details>
<summary>chemical</summary>

Electrical circuit diagram with resistors and capacitors labeled R2, C2, R1, C1, ei, and eo
</details>

(b)

Solution. In Figure 3–23(a) we assume that displacements $x _ { i } , x _ { o } .$ , and y are measured from their respective steady-state positions.Then the equations of motion for the mechanical system shown in Figure 3–23(a) are

$$b _ {1} \left(\dot {x} _ {i} - \dot {x} _ {o}\right) + k _ {1} \left(x _ {i} - x _ {o}\right) = b _ {2} \left(\dot {x} _ {o} - \dot {y}\right)b _ {2} \left(\dot {x} _ {o} - \dot {y}\right) = k _ {2} y$$

By taking the Laplace transforms of these two equations, assuming zero initial conditions, we have

$$b _ {1} \left[ s X _ {i} (s) - s X _ {o} (s) \right] + k _ {1} \left[ X _ {i} (s) - X _ {o} (s) \right] = b _ {2} \left[ s X _ {o} (s) - s Y (s) \right]b _ {2} \left[ s X _ {o} (s) - s Y (s) \right] = k _ {2} Y (s)$$

If we eliminate Y(s) from the last two equations, then we obtain

$$b _ {1} \left[ s X _ {i} (s) - s X _ {o} (s) \right] + k _ {1} \left[ X _ {i} (s) - X _ {o} (s) \right] = b _ {2} s X _ {o} (s) - b _ {2} s \frac {b _ {2} s X _ {o} (s)}{b _ {2} s + k _ {2}}$$

or
