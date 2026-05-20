# 3.5 Rotary to Linear Motion

Sometimes the second gear in a chain is straightened out to $r _ { 2 } = \infty$ . The case of innite radius corresponds to what is called a rack - a set of gear teeth arrayed in a straight line. The gear which meshes with a rack is called a pinion. Such systems contain a combination of rotating and translating elements and they can be analyzed by careful application of the principles developed in this and the previous chapters.

Consider the rack and pinion shown in Figure 3.6. Assume the gear can rotate about its xed axis and the rack is free to slide back and forth in the x direction. The force applied by the rack to the gear must be

$$F = \tau / r$$

because of the tangential contact constraint. The displacements are related by

$$x = r \theta$$

by the basic geometry of circles.

In a combined system we write translational EOM(s) for the sliding components and rotational EOM(s) for the rotating components, but by substituting the relationships above, we can transform one of the EOMs so that both are in terms of rotary (or translational) variables.

When a component lies after a rotary to linear transformation, the net eect is a transformation from linear to rotary by $r ^ { 2 }$ . Consider the rotary-linear system shown in Figure 3.7. Writing equations of motion:

$$\tau = F r + J \ddot {\theta}F = M \ddot {x}$$

Applying $x = r \theta ,$

$$F = M r \ddot {\theta}$$

substituting

$$\tau = r (M r \ddot {\theta}) + J \ddot {\theta}\tau = (J + r ^ {2} M) \ddot {\theta}$$

Note that the mass has been transformed to a rotational inertia by $r ^ { 2 }$ .

![](image/14bc3782d87df9f5584ded316acc9d35ddb33ea9e82a04dd3b765cef10d40117.jpg)

<details>
<summary>text_image</summary>

r
θ
F
x
M
</details>

Figure 3.7: A system containing a rack and pinion coupled to rotary and linear masses.
