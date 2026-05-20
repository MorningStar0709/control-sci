where, $U = u^{*}(t) = \pm1$ . For phase plane plots, we need to eliminate t from solutions (7.2.14) for the states. Thus, (for simplicity, we omit \* since we are now dealing with all optimal functions only and write $x_{1}(0) = x_{10}, x_{2}(0) = x_{20}$ )

$$t = (x _ {2} (t) - x _ {2 0}) / U,x _ {1} (t) = x _ {1 0} - \frac {1}{2} U x _ {2 0} ^ {2} + \frac {1}{2} U x _ {2} ^ {2} (t), \tag {7.2.15}$$

where, we used $U = \pm 1 = 1 / U$ . If

$$
u = U = + 1, \left\{ \begin{array}{l} t = x _ {2} (t) - x _ {2 0} \\ x _ {1} (t) = x _ {1 0} - \frac {1}{2} x _ {2 0} ^ {2} + \frac {1}{2} x _ {2} ^ {2} (t) = C _ {1} + \frac {1}{2} x _ {2} ^ {2} (t) \end{array} \right. \tag {7.2.16}
$$

and if

$$
u = U = - 1, \left\{ \begin{array}{l} t = x _ {2 0} - x _ {2} (t), \\ x _ {1} (t) = x _ {1 0} + \frac {1}{2} x _ {2 0} ^ {2} - \frac {1}{2} x _ {2} ^ {2} (t) = C _ {2} - \frac {1}{2} x _ {2} ^ {2} (t) \end{array} \right. \tag {7.2.17}
$$

where, $C_{1} = x_{10} - \frac{1}{2}x_{20}^{2}$ and $C_{2} = x_{10} + \frac{1}{2}x_{20}^{2}$ are constants. Now, we can easily see that the relations (7.2.16) and (7.2.17) represent a family of parabolas in $(x_{1}, x_{2})$ plane (or phase plane) as shown in Figure 7.8. The arrow indicates the direction of motion for increasing (positive) time. Our aim is to drive the system from

![](image/019f5433bd5942ba3d3b62c485eea1746df7bd63606d0c6dae344134fcd9a9e1.jpg)

<details>
<summary>text_image</summary>

u = +1
C₁<0 C₁=0 C₁>0
x₂
γ₋
x₁
C₂<0 C₂=0 C₂>0
u = -1
γ₊
</details>

Figure 7.8 Phase Plane Trajectories for $\mathbf{u} = +1$ (dashed lines) and $\mathbf{u} = -1$ (dotted lines)

any initial state $(x_{1}(0), x_{2}(0))$ to origin $(0, 0)$ in minimum time.

Then, from (7.2.15), we find that at $t = t_f$

$$x _ {1} (t = t _ {f}) = 0; \quad x _ {2} (t = t _ {f}) = 0. \tag {7.2.18}$$

With this, (7.2.15) becomes

$$0 = x _ {1 0} - \frac {1}{2} U x _ {2 0} ^ {2} + 0 \longrightarrow x _ {1 0} = \frac {1}{2} U x _ {2 0} ^ {2}. \tag {7.2.19}$$

Now, rewriting this for any initial state $x_{1} = x_{10}, x_{2} = x_{20}$ , we have

$$x _ {1} = \frac {1}{2} U x _ {2} ^ {2}. \tag {7.2.20}$$

Note that $x_{1}$ and $x_{2}$ in (7.2.19) are any initial states and not to be confused with $x_{1}(t)$ and $x_{2}(t)$ in (7.2.15) which are the states at any time t.

Now we can restate our problem as to find the time-optimal control sequence to drive the system from any initial state $(x_{1}, x_{2})$ to the origin $(0, 0)$ in minimum time.
