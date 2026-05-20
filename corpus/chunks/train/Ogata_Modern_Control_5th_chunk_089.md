$$\left[ m _ {1} s ^ {2} + b s + \left(k _ {1} + k _ {2}\right) \right] X _ {1} (s) = \left(b s + k _ {2}\right) X _ {2} (s) + U (s) \tag {3-5}\left[ m _ {2} s ^ {2} + b s + \left(k _ {2} + k _ {3}\right) \right] X _ {2} (s) = \left(b s + k _ {2}\right) X _ {1} (s) \tag {3-6}$$

Solving Equation (3–6) for $X _ { 2 } ( s )$ and substituting it into Equation (3–5) and simplifying, we get

$$\left[ \left(m _ {1} s ^ {2} + b s + k _ {1} + k _ {2}\right) \left(m _ {2} s ^ {2} + b s + k _ {2} + k _ {3}\right) - \left(b s + k _ {2}\right) ^ {2} \right] X _ {1} (s)= \left(m _ {2} s ^ {2} + b s + k _ {2} + k _ {3}\right) U (s)$$

from which we obtain

$$\frac {X _ {1} (s)}{U (s)} = \frac {m _ {2} s ^ {2} + b s + k _ {2} + k _ {3}}{\left(m _ {1} s ^ {2} + b s + k _ {1} + k _ {2}\right) \left(m _ {2} s ^ {2} + b s + k _ {2} + k _ {3}\right) - \left(b s + k _ {2}\right) ^ {2}} \tag {3-7}$$

From Equations (3–6) and (3–7) we have

$$\frac {X _ {2} (s)}{U (s)} = \frac {b s + k _ {2}}{\left(m _ {1} s ^ {2} + b s + k _ {1} + k _ {2}\right) \left(m _ {2} s ^ {2} + b s + k _ {2} + k _ {3}\right) - \left(b s + k _ {2}\right) ^ {2}} \tag {3-8}$$

Equations (3–7) and (3–8) are the transfer functions $X _ { 1 } ( s ) / U ( s )$ and $X _ { 2 } ( s ) / U ( s )$ respectively.,

EXAMPLE 3–5 An inverted pendulum mounted on a motor-driven cart is shown in Figure 3–5(a).This is a model of the attitude control of a space booster on takeoff. (The objective of the attitude control problem is to keep the space booster in a vertical position.) The inverted pendulum is unstable in that it may fall over any time in any direction unless a suitable control force is applied. Here we consider only a two-dimensional problem in which the pendulum moves only in the plane of the page.The control force u is applied to the cart. Assume that the center of gravity of the pendulum rod is at its geometric center. Obtain a mathematical model for the system.

![](image/6653446d5ef945e611c850bd31e181a575bd2d5cab0b1c691e98735dc83db5da.jpg)

<details>
<summary>text_image</summary>

y
x
θ
ℓ
ℓ cos θ
mg
ℓ
O
P
x
u
M
</details>

(a)

![](image/44bcf7d017b9cc8bbec1e797c029b377b83d852889d79451d0f2199f6360c8b5.jpg)

<details>
<summary>text_image</summary>

y
ℓ
θ
x
ℓ
V
mg
H
H
x
u
V
M
</details>

(b)   
Figure 3–5 (a) Inverted pendulum system; (b) free-body diagram.

Define the angle of the rod from the vertical line as u. Define also the $( x , y )$ coordinates of the center of gravity of the pendulum rod as $\left( x _ { G } , y _ { G } \right)$ . Then

$$x _ {G} = x + l \sin \thetay _ {G} = l \cos \theta$$
