# Lyapunov's Second Method

Lyapunov's second method is a useful tool for determining the stability of nonlinear dynamic systems. Lyapunov developed the theory for differential equations, but a corresponding theory also can be derived for difference equations. The main idea is to introduce a generalized energy function called the Lyapunov function, which is zero at the equilibrium and positive elsewhere. The equilibrium will be stable if we can show that the Lyapunov function decreases along the trajectories of the system.

![](image/d42a1a4ac0efedf3619bd1823a10e1fb3ace7ade5cb9fbb71183d7a139b32116.jpg)

<details>
<summary>text_image</summary>

V(x(k+1))
x(k+1)
x(k)
x₁
V(x(k))
</details>

Figure 3.8 Geometric illustration of Lyapunov's theorem.

The first step to show stability is to find the Lyapunov function, which is defined as follows:

DEFINITION 3.6 LYAPUNOV FUNCTION V(x) is a Lyapunov function for the system

$$x (k + 1) = f (x (k)) \quad f (0) = 0 \tag {3.8}$$

if:

1. $V(x)$ is continuous in $x$ and $V(0) = 0$ .   
2. $V(x)$ is positive definite.   
3. $\Delta V(x) = V(f(x)) - V(x)$ is negative definite.

A simple geometric illustration of the definition is given in Fig. 3.8. The level curves of a positive definite continuous function V are closed curves in the neighborhood of the origin. Let each curve be labeled by the value of the function. Condition 3 implies that the dynamics of the system is such that the solution always moves toward curves with lower values. All level curves encircle the origin and do not intersect any other level curve.

From the geometric interpretation it thus seems reasonable that the existence of a Lyapunov function ensures asymptotic stability. The following theorem is a precise statement of this fact.

THEOREM 3.4 STABILITY THEOREM OF LYAPUNOV The solution $x(k) = 0$ is asymptotically stable if there exists a Lyapunov function to the system (3.8). Further, if

$$0 < \varphi (\| x \|) < V (x)$$

where $\varphi (\| x\|)\to \infty$ as $(\| x\|)\rightarrow \infty$ , then the solution is asymptotically stable for all initial conditions.

The main obstacle to using the Lyapunov theory is finding a suitable Lyapunov function. This is in general a difficult problem; however, for the linear system of (3.2), it is straightforward to determine quadratic Lyapunov functions. Take $V(x) = x^{T}Px$ as a candidate for a Lyapunov function. The increment of V is then given by
