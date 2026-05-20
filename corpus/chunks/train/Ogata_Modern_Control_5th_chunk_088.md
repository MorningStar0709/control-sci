and identify $a _ { 1 } , a _ { 2 } , b _ { 0 } , b _ { 1 }$ , and $b _ { 2 }$ as follows:

$$a _ {1} = \frac {b}{m}, \quad a _ {2} = \frac {k}{m}, \quad b _ {0} = 0, \quad b _ {1} = \frac {b}{m}, \quad b _ {2} = \frac {k}{m}$$

Referring to Equation (3–35), we have

$$\beta_ {0} = b _ {0} = 0\beta_ {1} = b _ {1} - a _ {1} \beta_ {0} = \frac {b}{m}\beta_ {2} = b _ {2} - a _ {1} \beta_ {1} - a _ {2} \beta_ {0} = \frac {k}{m} - \left(\frac {b}{m}\right) ^ {2}$$

Then, referring to Equation (2–34), define

$$x _ {1} = y - \beta_ {0} u = yx _ {2} = \dot {x} _ {1} - \beta_ {1} u = \dot {x} _ {1} - \frac {b}{m} u$$

From Equation (2–36) we have

$$\dot {x} _ {1} = x _ {2} + \beta_ {1} u = x _ {2} + \frac {b}{m} u\dot {x} _ {2} = - a _ {2} x _ {1} - a _ {1} x _ {2} + \beta_ {2} u = - \frac {k}{m} x _ {1} - \frac {b}{m} x _ {2} + \left[ \frac {k}{m} - \left(\frac {b}{m}\right) ^ {2} \right] u$$

and the output equation becomes

$$y = x _ {1}$$

or

$$
\left[ \begin{array}{l} \dot {x} _ {1} \\ \dot {x} _ {2} \end{array} \right] = \left[ \begin{array}{c c} 0 & 1 \\ - \frac {k}{m} & - \frac {b}{m} \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] + \left[ \begin{array}{c} \frac {b}{m} \\ \frac {k}{m} - \left(\frac {b}{m}\right) ^ {2} \end{array} \right] u \tag {3-3}
$$

and

$$
y = \left[ \begin{array}{l l} 1 & 0 \end{array} \right] \left[ \begin{array}{l} x _ {1} \\ x _ {2} \end{array} \right] \tag {3-4}
$$

Equations (3–3) and (3–4) give a state-space representation of the system. (Note that this is not the only state-space representation.There are infinitely many state-space representations for the system.)

Figure 3–4 Mechanical system.   
![](image/33d426ab12cf66fe49117aa9de5f13a6dc54eb908852bdfa643342d77edbb0ec.jpg)

<details>
<summary>text_image</summary>

u
x₁
k₂
m₁
b
m₂
x₂
k₁
m₂
k₃
</details>

EXAMPLE 3–4 Obtain the transfer functions $X _ { 1 } ( s ) / U ( s )$ and $X _ { 2 } ( s ) / U ( s )$ of the mechanical system shown in Figure 3–4.

The equations of motion for the system shown in Figure 3–4 are

$$m _ {1} \ddot {x} _ {1} = - k _ {1} x _ {1} - k _ {2} (x _ {1} - x _ {2}) - b (\dot {x} _ {1} - \dot {x} _ {2}) + um _ {2} \ddot {x} _ {2} = - k _ {3} x _ {2} - k _ {2} (x _ {2} - x _ {1}) - b (\dot {x} _ {2} - \dot {x} _ {1})$$

Simplifying, we obtain

$$m _ {1} \ddot {x} _ {1} + b \dot {x} _ {1} + (k _ {1} + k _ {2}) x _ {1} = b \dot {x} _ {2} + k _ {2} x _ {2} + um _ {2} \ddot {x} _ {2} + b \dot {x} _ {2} + (k _ {2} + k _ {3}) x _ {2} = b \dot {x} _ {1} + k _ {2} x _ {1}$$

Taking the Laplace transforms of these two equations, assuming zero initial conditions, we obtain
