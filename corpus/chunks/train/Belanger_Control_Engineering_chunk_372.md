# 7.2 PROPERTIES OF STATE FEEDBACK

An LTI system, with the state description

$$\dot {\mathbf {x}} = A \mathbf {x} + B \mathbf {u}\mathbf {y} = C \mathbf {x} \tag {7.1}$$

is given, where the state vector $\mathbf{x}$ is of dimension $n$ , the input $\mathbf{u}$ is of dimension $r$ , and the output $\mathbf{y}$ is of dimension $m$ . A state feedback law is an expression for the input $\mathbf{u}$ in terms of the state $\mathbf{x}$ . A linear state feedback law has the form

$$\mathbf {u} = - K \mathbf {x} \tag {7.2}$$

where $K$ , the state gain matrix, is of dimensions $r \times n$ . With $\mathbf{u}$ given by Equation 7.2, the closed-loop state description becomes

$$\dot {\mathbf {x}} = (A - B K) \mathbf {x}\mathbf {y} = C \mathbf {x}. \tag {7.3}$$

Equation 7.3 describes an autonomous linear, time-invariant (LTI) system. If $K$ can be chosen such that $A - BK$ has all its eigenvalues in the open LHP, then $\lim_{t \to \infty} \mathbf{x}(t) = 0$ , and $\lim_{t \to 0} \mathbf{y}(t) = 0$ . As it stands, this control law performs a regulation function and drives the state and the output to zero from any initial state.

If we wish to regulate to some constant output set point $y_{d} \neq 0$ , we must first calculate the dc steady state for which $y_{d}$ is the output. From Chapter 2, the steady-state input $u^{*}$ and state $x^{*}$ satisfy

$$0 = A \mathbf {x} ^ {*} + B \mathbf {u} ^ {*}\mathbf {y} _ {d} = C \mathbf {x} ^ {*}. \tag {7.4}$$

A unique solution to Equation 7.4 exists if, and only if, the matrix $[A_{C}^{B}]$ is nonsingular. From Chapter 3, that means that there is no transmission zero at $s = 0$ . We shall assume this to be true, in which case $\mathbf{x}^*$ and $\mathbf{u}^*$ are linear in $\mathbf{y}_d$ and given by expressions of the form

$$\mathbf {x} ^ {*} = M _ {x} \mathbf {y} _ {d}\mathbf {u} ^ {*} = M _ {u} \mathbf {y} _ {d}. \tag {7.5}$$

![](image/092d00a28343d0090498e17812942bb5de0b671a6fa2c1247045d34b09997d76.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    yd --> Mx
    Mx --> x* --> sum1["+"]
    sum1 --> -Δx --> K
    K --> Δu --> sum2["+"]
    Δu --> u --> (sI-A)^{-1}B --> x --> C
    C --> y
    x* -->|-| sum2
    sum2 --> u
    u --> C
    Mx --> u*
    Mx --> u*
```
</details>

Figure 7.1 Steady-state and incremental signals, state feedback

![](image/cd5e6392e423b805ff04dcca1827c28aadf3acf07388bda7fcb70324e65a78fc.jpg)

<details>
<summary>flowchart</summary>
