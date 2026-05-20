By substituting the given numerical values for $m _ { 1 } , m _ { 2 } , k$ , and b and simplifying, we obtain

$$\ddot {y} _ {1} = - 3 6 y _ {1} + 3 6 y _ {2} - 0. 6 \dot {y} _ {1} + 0. 6 \dot {y} _ {2} + u\ddot {y} _ {2} = 1 8 y _ {1} - 1 8 y _ {2} + 0. 3 \dot {y} _ {1} - 0. 3 \dot {y} _ {2}$$

Let us choose the state variables as follows:

$$x _ {1} = y _ {1}x _ {2} = y _ {2}x _ {3} = \dot {y} _ {1}x _ {4} = \dot {y} _ {2}$$

![](image/ea6b597cb3450deca061a56bee95be87058324b0e3980f7d80b333308f38ef33.jpg)

<details>
<summary>text_image</summary>

Regulator u
m₁
y₁
k
b
m₂
y₂
</details>

Figure 10–49 Mechanical system.

Then, the state-space equations become

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \dot {x} _ {3} \\ \dot {x} _ {4} \end{array} \right] = \left[ \begin{array}{c c c c} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ - 3 6 & 3 6 & - 0. 6 & 0. 6 \\ 1 8 & - 1 8 & 0. 3 & - 0. 3 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \\ x _ {4} \end{array} \right] + \left[ \begin{array}{c} 0 \\ 0 \\ 1 \\ 0 \end{array} \right] u

\left[ \begin{array}{c} y _ {1} \\ y _ {2} \end{array} \right] = \left[ \begin{array}{c c c c} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ x _ {3} \\ x _ {4} \end{array} \right]
$$

Define

$$
\mathbf {A} = \left[ \begin{array}{c c c c} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ \hdashline - 3 6 & 3 6 & - 0. 6 & 0. 6 \\ 1 8 & - 1 8 & 0. 3 & - 0. 3 \end{array} \right] = \left[ \begin{array}{c c} \mathbf {A} _ {a a} & \mathbf {A} _ {a b} \\ \hdashline \mathbf {A} _ {b a} & \mathbf {A} _ {b b} \end{array} \right],

\mathbf {B} = \left[ \begin{array}{c} 0 \\ 0 \\ \dots \\ 1 \\ 0 \end{array} \right] = \left[ \begin{array}{c} \mathbf {B} _ {a} \\ \dots \\ \mathbf {B} _ {b} \end{array} \right]
$$

The state feedback gain matrix K and observer gain matrix $\mathbf { K } _ { e }$ can be obtained easily by use of MATLAB as follows:

$$
\mathbf {K} = \left[ \begin{array}{c c c c} 1 3 0. 4 4 4 4 & - 4 1. 5 5 5 6 & 2 3. 1 0 0 0 & 1 5. 4 1 8 5 \end{array} \right]

\mathbf {K} _ {e} = \left[ \begin{array}{c c} 1 4. 4 & 0. 6 \\ 0. 3 & 1 5. 7 \end{array} \right]
$$

(See MATLAB Program 10–26.)
