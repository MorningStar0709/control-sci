where $c$ is a scalar. In the absence of $\mathbf { a } _ { T }$ , the term $( \mathbf { b } \times \mathbf { V } _ { g } )$ represents the rotational effect on $\mathbf { V } _ { g }$ . Hence, the factor c specifies the degree of rotational effect on $\mathbf { V } _ { g }$ during powered flight. If $c = 1$ , the total rotational effect is nil, and from the above equations it is evident that $\mathbf { V } _ { g } / \left| \mathbf { V } _ { g } \right|$ remains constant. Rearrangement of the equation

$$\mathbf {a} _ {T} \times \mathbf {V} _ {g} = c \mathbf {b} \times \mathbf {V} _ {g}$$

gives

$$\left((c - 1) \mathbf {b} + \left(\frac {d \mathbf {V} _ {g}}{d t}\right)\right) \times \mathbf {V} _ {g} = 0.$$

If $c = 1$ , the above equation reduces to

$$\left(\frac {d \mathbf {V} _ {g}}{d t}\right) \times \mathbf {V} _ {g} = 0,$$

and if $c = 0$

$$\mathbf {a} _ {T} \times \mathbf {V} _ {g} = 0.$$

It can be readily shown that this equation represents a faster rate of decrease of $| \mathbf { V } _ { g } |$ . However, in most practical applications, nonzero values (unity in particular) for $c$ result in better fuel economy than when the thrust is aligned with $\mathbf { V } _ { g }$ .

Example. In [3], page 79, equation (3.26), a possible equation for the correlated velocity is given as

$$\mathbf {V} _ {c} = (\sqrt {\mu p} / R _ {1} R _ {2} \sin \theta) \{\mathbf {R} _ {2} - [ 1 - (R _ {2} / p) (1 - \cos \theta) ] \mathbf {R} _ {1} \},$$

where $p$ is the semilatus rectum or conic parameter, $\mathbf { R } _ { 1 }$ is the missile’s present position vector, ${ \bf R } _ { 2 }$ is the target vector, $\theta$ is the central angle between $\mathbf { R } _ { 1 }$ and ${ \bf R } _ { 2 }$ , and $\mu$ is the gravitational constant as illustrated in the sketch below.

![](image/dc99f1dab778381425c75cdba3597d22fd99c1787e5c61ff0a7210c411a760dc.jpg)

<details>
<summary>text_image</summary>

V_{cR} \n V_c \n V_{c\theta} \n R_1 \n 1_R \n \theta \n 1_\theta \n Target \n R_2
</details>

Geometry of the problem.

Since this equation is given in terms of the coordinate frame consisting of $\mathbf { R } _ { 1 }$ and ${ \bf R } _ { 2 }$ , it may be convenient to work in a local vertical frame. This equation, then, can be transformed as follows:

$$
\begin{array}{l} V _ {c \theta} = \mathbf {V} _ {c} \cdot \mathbf {1} _ {\theta} = (\sqrt {\mu p} / R _ {1} R _ {2} \sin \theta) [ R _ {2} \cos ((\pi / 2) - \theta) ] \\ = (\sqrt {\mu p} / R _ {1} R _ {2} \sin \theta) (R _ {2} \sin \theta) = \sqrt {\mu} \sqrt {p} / R _ {1} \\ \end{array}
