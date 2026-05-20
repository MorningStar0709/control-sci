Example 3. Assume for simplicity that the missile’s motion is constrained in the vertical plane. Furthermore, we will assume that the missile can be modeled as a point mass. Therefore, from the missile’s balanced forces shown in the diagram below, we can write the equations of motion as follows (see also Example 1 in Chapter 2):

![](image/e8cf424e818b3213242e975fdcf5dad37b4142fb16c32678fdcff387edc03a6c.jpg)

<details>
<summary>text_image</summary>

L
u
p
T
α
V
γ
x
cg
v
mg
w
r
q
y
z
</details>

Fig. 3.21.

Equations of Motion

$$
\begin{array}{l} \frac {d V}{d t} = (1 / m) [ T \cos \alpha - D ] - g \sin \gamma , \\ \frac {d \gamma}{d t} = (1 / m V) [ L + T \sin \alpha ] - (g / V) \cos \gamma , \\ \frac {d x}{d t} = V \cos \gamma , \\ \frac {d h}{d t} = V \sin \gamma . \\ \end{array}
$$

Aerodynamic Derivative Coefficients

$$
\begin{array}{l} {\cal L} = \frac {1}{2} \rho V ^ {2} S C _ {L}, \\ D = \frac {1}{2} \rho V ^ {2} S C _ {D}, \\ C _ {L} = C _ {L \alpha} (\alpha - \alpha_ {0}), \\ C _ {D} = C _ {D 0} + k C _ {L} ^ {2}, \\ \end{array}
$$

where

$$
\begin{array}{l} g = \text { acceleration   of   gravity }, \\ h = \text { altitude }, \\ k = \text { induced   drag   coefficient }, \\ \end{array}
m = \mathrm{mass},D = \text { drag },L = \text { lift },M = \text { Mach number },S = \text { reference area },T = \text { thrust },V = \text { velocity },
\begin{array}{l} C _ {D}, C _ {L} = \text { drag   and   lift   coefficients }, \\ \text { respectively }, \\ \end{array}
C _ {D 0} = \text { zero - lift drag coefficient },C _ {L _ {\alpha}} = \partial C _ {L} / \partial \alpha .
$$

The aerodynamic derivative coefficients $C _ { L _ { \alpha } } , C _ { D 0 }$ , and k are functions of the Mach number as follows:

$$C _ {L \alpha} = C _ {L \alpha} (M),C _ {D 0} = C _ {D 0} (M),M = M (V, h),k = k (M),\rho = \rho (h).$$

Moreover, the missile mass and the thrust are functions of time; that is,

$$m = m (t) \quad \text { and } \quad T = T (t).$$

Note that the AOA can be treated as a control variable (if used in connection with an optimization case) that satisfies the inequality constraint

$$\alpha_ {m i n} \leq \alpha \leq \alpha_ {m a x}.$$
