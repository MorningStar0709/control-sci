By simple matrix multiplication and equating the coefficients of like powers of s on either side, we get a set of algebraic equations in general, and in particular in this example we have a single scalar equation as

$$1 + \left(2 k _ {1 1} - k _ {1 2} ^ {2}\right) \frac {1}{s ^ {2}} + k _ {1 1} ^ {2} \frac {1}{s ^ {4}} = 1 - \frac {1}{s ^ {2}} + \frac {1}{s ^ {4}} \tag {4.5.28}$$

giving us

$$k _ {1 1} = 1, \quad k _ {1 2} = \sqrt {3} \tag {4.5.29}$$

and the optimal feedback control as

$$u ^ {*} (t) = - \bar {\mathbf {K}} \mathbf {x} ^ {*} (t) = - \left[ 1 \sqrt {3} \right] \mathbf {x} ^ {*} (t). \tag {4.5.30}$$

Note: This example can be easily verified by using the algebraic Riccati equation (3.5.15) (of Chapter 3)

$$\bar {\mathbf {P}} \mathbf {A} + \mathbf {A} ^ {\prime} \bar {\mathbf {P}} - \bar {\mathbf {P}} \mathbf {B} \mathbf {R} ^ {- 1} \mathbf {B} ^ {\prime} \bar {\mathbf {P}} + \mathbf {Q} = 0 \tag {4.5.31}$$

discussed in Chapter 3. Using the previous relation, we get

$$
\bar {\mathbf {P}} = \left[ \begin{array}{c c} \sqrt {3} & 1 \\ 1 & \sqrt {3} \end{array} \right] \tag {4.5.32}
$$

and the optimal control (3.5.14) as

$$\mathbf {u} ^ {*} (t) = - \mathbf {R} ^ {- 1} \mathbf {B} ^ {\prime} \bar {\mathbf {P}} \mathbf {x} ^ {*} (t) = - [ 1 \sqrt {3} ] \mathbf {x} ^ {*} (t) \tag {4.5.33}$$

which is the same as (4.5.30).

Let us redraw the closed-loop optimal control system in Figure 4.10 as unity feedback system shown in Figure 4.11.

![](image/8344b4c57b3640cf6be1a899b14257b8343eba865cbc40fa057738503850b927.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    A["R(s)"] --> B((+))
    B --> C["U(s)"]
    C --> D["\overline{K}[sI - A"]^{-1}B]
    D --> E["X(s)"]
    E --> F["Feedback"]
    F --> B
```
</details>

Figure 4.11 Closed-Loop Optimal Control System with Unity Feedback

Here, we can easily recognize that for a single-input, single-output case, the optimal feedback control system is exactly like a classical feedback control system with unity negative feedback and transfer function as $G_{o}(s) = \bar{\mathbf{k}}[s\mathbf{I} - \mathbf{A}]^{-1}\mathbf{b}$ . Thus, the frequency domain interpretation in terms of gain margin, phase margin can be easily done using Nyquist, Bode, or some other plot of the transfer function $G_{o}(s)$ .
