# DEFINITION 5.2 Positive definite and semidefinite functions

A continuously differentiable function $V: R^n \to R$ is called positive definite in a region $U \subset R^n$ containing the origin if

1. $V(0) = 0$   
2. $V(x) > 0, x \in U$ and $x \neq 0$

A function is called positive semidefinite if Condition 2 is replaced by $V(x) \geq 0$ .

□

A positive definite function has level curves that enclose the origin. Curves corresponding to larger values of the function enclose curves that correspond to smaller values. The situation in the two-dimensional case is illustrated in Fig. 5.10. If we can find a function so that the velocity vector, $dx/dt = f(x)$ , always points toward the interior of the level curves, then it seems intuitively clear that a solution that starts inside a given level curve can never pass to the outside of the same level curve. We have the following theorem.

![](image/a070a4694871bd36c41b826d687ad476e83d3f3d93669e4c1459c0bb3d46d22d.jpg)

<details>
<summary>text_image</summary>

x₂
dx/dt
x=0
x₁
V(x)=const
</details>

Figure 5.10 Illustration of Lyapunov's method for investigating stability.
