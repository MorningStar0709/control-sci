$$k _ {2} (y - w) = A \left(P _ {1} - P _ {1} ^ {\prime}\right) + A \left(P _ {2} - P _ {2} ^ {\prime}\right) \tag {4-42}$$

Since

$$k _ {1} z = A \left(P _ {1} - P _ {1} ^ {\prime}\right) \tag {4-43}$$

and

$$q _ {1} = \frac {P _ {1} - P _ {1} ^ {\prime}}{R}$$

we have

$$k _ {1} z = A R q _ {1}$$

Also, since

$$q _ {1} d t = A (d w - d z) \rho$$

we have

$$q _ {1} = A (\dot {w} - \dot {z}) \rho$$

or

$$\dot {w} - \dot {z} = \frac {k _ {1} z}{A ^ {2} R \rho}$$

Define $A ^ { 2 } R \rho = B$ . (B is the viscous-friction coefficient.) Then

$$\dot {w} - \dot {z} = \frac {k _ {1}}{B} z \tag {4-44}$$

Also, for the right-hand-side dashpot we have

$$q _ {2} d t = A \rho d w$$

Since $q _ { 2 } = \left( P _ { 2 } - P _ { 2 } ^ { \prime } \right) / R$ , we obtain

$$\dot {w} = \frac {q _ {2}}{A \rho} = \frac {A \left(P _ {2} - P _ {2} ^ {\prime}\right)}{A ^ {2} R \rho}$$

or

$$A \left(P _ {2} - P _ {2} ^ {\prime}\right) = B \dot {w} \tag {4-45}$$

Substituting Equations (4–43) and (4–45) into Equation (4–42), we have

$$k _ {2} y - k _ {2} w = k _ {1} z + B \dot {w}$$

Taking the Laplace transform of this last equation, assuming zero initial condition, we obtain

$$k _ {2} Y (s) = \left(k _ {2} + B s\right) W (s) + k _ {1} Z (s) \tag {4-46}$$

Figure 4–37 Hydraulic system.   
![](image/1232dc31cc79d9a298d800bf5c1e9222cb5d7d650986a1aa563f5675d1820080.jpg)

<details>
<summary>text_image</summary>

k₁
R
q₁
P₁
P₁'
w
R
q₂
P₂
P₂'
w
k₂
F
y
z
</details>

Area = A

Taking the Laplace transform of Equation (4–44), assuming zero initial condition, we obtain

$$W (s) = \frac {k _ {1} + B s}{B s} Z (s) \tag {4-47}$$

By using Equation (4–47) to eliminate W(s) from Equation (4–46), we obtain

$$k _ {2} Y (s) = \left(k _ {2} + B s\right) \frac {k _ {1} + B s}{B s} Z (s) + k _ {1} Z (s)$$

from which we obtain the transfer function $Z ( s ) / Y ( s )$ to be

$$\frac {Z (s)}{Y (s)} = \frac {k _ {2} s}{B s ^ {2} + \left(2 k _ {1} + k _ {2}\right) s + \frac {k _ {1} k _ {2}}{B}}$$

Multiplying $B / { \left( k _ { 1 } k _ { 2 } \right) }$ to both the numerator and denominator of this last equation, we get

$$\frac {Z (s)}{Y (s)} = \frac {\frac {B}{k _ {1}} s}{\frac {B ^ {2}}{k _ {1} k _ {2}} s ^ {2} + \left(\frac {2 B}{k _ {2}} + \frac {B}{k _ {1}}\right) s + 1}$$

Define $B / k _ { 1 } = T _ { 1 } , B / k _ { 2 } = T _ { 2 }$ Then the transfer function. $Z ( s ) / Y ( s )$ becomes as follows:

$$\frac {Z (s)}{Y (s)} = \frac {T _ {1} s}{T _ {1} T _ {2} s ^ {2} + (T _ {1} + 2 T _ {2}) s + 1}$$
