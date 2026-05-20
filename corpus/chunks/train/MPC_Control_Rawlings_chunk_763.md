Next we consider an unconstrained parametric quadratic program $\mathrm { m i n } _ { u } V ( x , u )$ where $V ( x , u ) : = ( 1 / 2 ) ( x - u ) ^ { 2 } + u ^ { 2 } / 2$ . The problem is illustrated in Figure 7.3. For each $x \in \mathbb { R } , \nabla _ { u } V ( x , u ) = - x + 2 u$ and $\nabla _ { u u } V ( x , u ) = 2$ so that $u ^ { 0 } ( x ) = x / 2$ and $V ^ { 0 } ( x ) = x ^ { 2 } / 4$ . Hence $u ^ { 0 } ( \cdot )$ is linear and $V ^ { 0 } ( \cdot )$ is quadratic in R.

![](image/67f81613f5b5c8493a74e8d54a1cdf4b35c6d43ea6f668d5ab5f762ef5013649.jpg)

<details>
<summary>text_image</summary>

u
x
u^0(x)
</details>

Figure 7.3: Unconstrained parametric quadratic program.   
![](image/a09ce643f26c52182c32baebeb756fbb71f9e864de5fac517e351fab80f5d980.jpg)

<details>
<summary>text_image</summary>

u
Z
u⁰(x)
constraint
x
u⁰_uc(x)
</details>

Figure 7.4: Parametric quadratic program.

We now add the constraint set $\mathbb { Z } : = \ \{ ( x , u ) \mid u \geq 1 , \ u + x / 2 \ \geq$ $2 , u + x \geq 2 \}$ ; see Figure 7.4. The solution is defined on three regions, $X _ { 1 } : = ( - \infty , 0 ] , X _ { 2 } : = [ 0 , 2 ]$ , and $X _ { 3 } : = [ 2 , \infty )$ . From the preceding example, the unconstrained minimum is achieved at $u _ { \mathrm { u c } } ^ { 0 } ( x ) = { x } / { 2 }$ shown by the solid straight line in Figure 7.4. Since $\nabla _ { u } V ( x , u ) = - x + 2 u$ , $\nabla _ { u } V ( x , u ) \ > \ 0$ for all $u > u _ { \mathrm { u c } } ^ { 0 } ( x ) = x / 2$ . Hence, in $X _ { 1 } , u ^ { 0 } ( x )$ lies on the boundary of Z and satisfies $u ^ { 0 } ( x ) \ : = \ : 2 - x$ . Similarly, in $X _ { 2 }$ , $u ^ { 0 } ( x )$ lies on the boundary of Z and satisfies $u ^ { 0 } ( x ) \ = \ 2 - x / 2$ . Finally, in $X _ { 3 } , u ^ { 0 } ( x ) = u _ { \mathrm { u c } } ^ { 0 } ( x ) = x / 2$ , the unconstrained minimizer, and lies in the interior of $\mathbb { Z }$ for $x > 1$ . The third constraint $u \geq 2 - x$ is active in $X _ { 1 }$ , the second constraint $u \ge 2 - x / 2$ is active in $X _ { 2 }$ , while no constraints are active in $X _ { 3 }$ . Hence the minimizer $u ^ { 0 } ( \cdot )$ is piecewise affine, being affine in each of the regions $X _ { 1 } , X _ { 2 }$ and $X _ { 3 }$ . Since $V ^ { 0 } ( x ) ~ = ~ ( 1 / 2 ) | x - u ^ { 0 } ( x ) | ^ { 2 } + u ^ { 0 } ( x ) ^ { 2 } / 2$ , the value function $V ^ { 0 } ( \cdot )$ is piecewise quadratic, being quadratic in each of the regions $X _ { 1 } , X _ { 2 }$ and $X _ { 3 }$ .

We require, in the sequel, the following definitions:
