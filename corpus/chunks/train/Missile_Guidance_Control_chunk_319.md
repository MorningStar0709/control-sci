# Target Equations

Referring to Figure 4.32, the total acceleration a is the sum of two vectors, namely, ${ \bf F } _ { n }$ and $\mathbf { F } _ { v }$ , where

$$\mathbf {F} _ {v} = F _ {v} \mathbf {e} _ {v} = (F _ {v} / v) \mathbf {v}, \tag {4.91}$$

where

$$
\mathbf {a} = \text { acceleration vector },
\begin{array}{c} \mathbf {F} _ {v} = \text { force   vector   along   the   velocity } \\ \text { vector }, \end{array}
\mathbf {F} _ {n} = \text { force vector along the normal },\mathbf {v} = \text { velocity vector },
\begin{array}{c} \mathbf {e} _ {v} = \text { unit   vector   along   the   velocity } \\ \text { vector   v }, \end{array}
\mathbf {e} _ {n} = \text { unit vector along } \mathbf {F} _ {n}.
$$

The coordinate system defined by the vectors v and ${ \bf F } _ { n }$ rotates at a rate

$$\omega_ {c} = \omega \mathbf {e} _ {v} + (F _ {n} / v) \mathbf {e} (\mathbf {v} \times \mathbf {a}) = (\omega / v) \mathbf {v} + (1 / v ^ {2}) (\mathbf {v} \times \mathbf {a}). \tag {4.92}$$

Hence, we can write the rate of change of a as follows:

$$
\begin{array}{l} d \mathbf {a} / d t = \left(\frac {d \mathbf {F} _ {n}}{d t}\right) \mathbf {e} _ {n} + \left(\frac {d \mathbf {F} _ {v}}{d t}\right) \mathbf {e} _ {v} + \boldsymbol {\omega} _ {c} \times \mathbf {a} \\ = (1 / F _ {n}) \left(\frac {d F _ {n}}{d t}\right) [ \mathbf {a} - (F _ {v} / v) \mathbf {v} ] + (1 / v) \left(\frac {d F _ {v}}{d t}\right) + (\omega / v) (\mathbf {v} \times \mathbf {a}) \\ + (1 / v ^ {2}) (\mathbf {v} \times \mathbf {a}) \times \mathbf {a} \\ = [ (- 1 / \tau) + (w _ {n} / F _ {n}) ] [ \mathbf {a} - (F _ {v} / v) \mathbf {v} ] + \{(- F _ {v} / v \tau_ {f}) + (w _ {f} / v) \} \mathbf {v} \\ + (\omega / v) (\mathbf {v} \times \mathbf {a}) + (1 / v ^ {2}) [ v F _ {v} \mathbf {a} - a ^ {2} \mathbf {v} ] \\ = (\omega / v) (\mathbf {v} \times \mathbf {a}) + [ (F _ {v} / v) - (1 / \tau_ {n}) ] \mathbf {a} - k \mathbf {v} + w _ {n} \mathbf {e} _ {n} + w _ {f} \mathbf {e} _ {v}, \tag {4.93} \\ \end{array}
$$

where

$$k = (a / v) ^ {2} + (F _ {v} / v) [ (1 / \tau_ {f}) - (1 / \tau_ {n}) ]. \tag {4.94}$$

![](image/f5e7a1c1df06ac4345bd283aefb583ef7061e301dd780f2d6dff7041d1433881.jpg)

<details>
<summary>text_image</summary>

Y
a
Fv
V
ym
Fn
cg
xm
X
</details>

Fig. 4.32. Coordinate system for target equations.

Equations (4.90) and (4.93), together with equations

$$\frac {d \mathbf {x}}{d t} = \mathbf {v}, \tag {4.95a}\frac {d \mathbf {v}}{d t} = \mathbf {a}, \tag {4.95b}$$
