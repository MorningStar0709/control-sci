# Example 2.7

Find the minimum length between any two points.

Solution: It is well known that the solution to this problem is a straight line. However, we like to illustrate the application of Euler-Lagrange equation for this simple case. Consider the arc between two points A and B as shown in Figure 2.6. Let ds be the small arc length, and dx and dt are the small rectangular coordinate values. Note that t is the independent variable representing distance and not time. Then,

$$(d s) ^ {2} = (d x) ^ {2} + (d t) ^ {2}. \tag {2.3.28}$$

Rewriting

$$d s = \sqrt {1 + \dot {x} ^ {2} (t)} d t, \quad \text { where } \quad \dot {x} (t) = \frac {d x}{d t}. \tag {2.3.29}$$

Now the total arc length $S$ between two points $x(t = t_0)$ and $x(t = t_f)$ is the performance index $J$ to be minimized. Thus,

$$S = J = \int d s = \int_ {t _ {0}} ^ {t _ {f}} \sqrt {1 + \dot {x} ^ {2} (t)} d t = \int_ {t _ {0}} ^ {t _ {f}} V (\dot {x} (t)) d t \tag {2.3.30}$$

![](image/7be199c4b7e211bfcf142f0485f1c6293cba6910e009fdd5e8d5b99e23632863.jpg)

<details>
<summary>line</summary>

| Point | Time (t) | x(t) |
| --- | --- | --- |
| A | t₀ | x₀ |
| ds | t₀ | (estimated from curve) |
| dx | t_f | (estimated from curve) |
| B | t_f | (estimated from curve) |
</details>

Figure 2.6 Arc Length

where, $V(\dot{x}(t)) = \sqrt{1 + \dot{x}^2(t)}$ . Note that $V$ is a function of $\dot{x}(t)$ only. Applying the Euler-Lagrange equation (2.3.22) to the performance index (2.3.30), we get

$$\frac {\dot {x} ^ {*} (t)}{\sqrt {1 + \dot {x} ^ {* 2} (t)}} = C. \tag {2.3.31}$$

Solving this equation, we get the optimal solution as

$$x ^ {*} (t) = C _ {1} t + C _ {2}. \tag {2.3.32}$$

This is evidently an equation for a straight line and the constants $C_{1}$ and $C_{2}$ are evaluated from the given boundary conditions. For example, if $x(0)=1$ and $x(2)=5$ , $C_{1}=2$ and $C_{2}=1$ the straight line is $x^{*}(t)=2t+1$ .

Although the previous example is a simple one,

1. it illustrates the formulation of a performance index from a given simple specification or a statement, and   
2. the solution is well known a priori so that we can easily verify the application of the Euler-Lagrange equation.

In the previous example, we notice that the integrand V in the functional (2.3.30), is a function of $\dot{x}(t)$ only. Next, we take an example, where, V is a function of $x(t)$ , $\dot{x}(t)$ and t.
