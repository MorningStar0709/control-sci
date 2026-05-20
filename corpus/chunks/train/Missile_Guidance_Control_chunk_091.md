q = free-stream dynamic pressure at a point far from the airfoil, S = reference area, usually the area of one of the airfoils, lref = reference length, usually the mean missile diameter from a body cross-section.

Figure 3.6 illustrates the angles under discussion.

![](image/f1ab453fd1121b476c0edece92e519d929d81cf6981f539f5f433da0147cab7a.jpg)

<details>
<summary>text_image</summary>

ui
+ αp
Xb
tan αp = w ||k ||
u ||i ||
= w(1)
u(1)
= w/u
wk
Zb
VM projected
Pitch plane
</details>

![](image/45b9dd1cf58a2dcae25f5a38d969b1a189e442da38fca7c79f144fcb165bf2f0.jpg)

<details>
<summary>text_image</summary>

ui
+ αy
Xb
tan αy = v||j||
u||i||
= v(1)
u(1)
= v/u
vj
Yb
VM projected
Yaw plane
</details>

Fig. 3.6. Missile angle representation.

The rolling moment L can now be rewritten using the above-introduced coefficients and definitions:

$$
\begin{array}{l} L = [ (\partial L / \partial \alpha_ {p}) | _ {\alpha_ {p} = 0} ] \alpha_ {p} + [ (\partial L / \partial \alpha_ {y}) | _ {\alpha_ {y} = 0} ] \alpha_ {y} + [ (\partial L / \partial \delta_ {a}) | _ {\delta_ {\alpha} = 0} ] \delta_ {a} \\ = (L _ {\alpha_ {p}}) \alpha_ {p} + (L _ {\alpha_ {y}}) \alpha_ {y} + (L _ {\delta_ {\alpha}}) \delta_ {a} \\ = q S l _ {r e f} (C _ {l _ {\alpha_ {p}}}) \alpha_ {p} + q S l _ {r e f} (C _ {l _ {\alpha_ {y}}}) \alpha_ {y} + q S l _ {r e f} (C _ {l _ {\delta_ {\alpha}}}) \alpha_ {p} \\ = q S l _ {r e f} [ (C _ {l _ {\alpha_ {p}}}) \alpha_ {p} + (C _ {l _ {\alpha_ {y}}}) \alpha_ {y} + (C _ {l _ {\delta_ {\alpha}}}) \delta_ {a} ]. \tag {3.26} \\ \end{array}
$$

Solving (2.29a) for d $P / d t$ , we can now write the rotational acceleration equation for roll in the form

$$\frac {d P}{d t} = Q R \left[ \left(I _ {y} - I _ {z}\right) / I _ {x} \right] + \left(q S l _ {r e f} / I _ {x}\right) \left[ \left(C _ {l _ {\alpha_ {p}}}\right) \alpha_ {p} + \left(C _ {l _ {\alpha_ {y}}}\right) \alpha_ {y} + \left(C _ {l _ {\delta_ {\alpha}}}\right) \delta_ {\alpha} \right]. \tag {3.27}$$
