Given a simulation diagram, it is easy to write state equations. The integrator outputs are taken to be the state variables; the derivative of any state variable is simply the input to the corresponding integrator. With

$$x _ {1} = z, \quad x _ {2} = \dot {z}, \quad \dots , \quad x _ {n} = z ^ {(n - 1)}$$

![](image/c3f818c8eefe4453c0117477da1a4ed4dccd3b21c59455f6a5a8a19ae2369f81.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph LR
    u --> |+| sum
    sum --> |-| A1["1/s"]
    A1 --> z(n-1) --> |+| B1["1/s"]
    B1 --> ẑ --> |+| sum
    sum --> y
    sum --> a0["a0"]
    a0 --> |+| sum
    sum --> a1a["a1"]
    a1a --> |+| sum
    sum --> a1n-1["a_{n-1}"]
    a1n-1 --> |+| sum
    sum --> b0["b0"]
    b0 --> |+| sum
    sum --> b1b["b_1"]
    b1b --> |+| sum
    sum --> b0b["b_{0-1}"]
    b0b --> |+| sum
    sum --> b1n-1["n_{n-1}"]
    b1n-1 --> |+| sum
```
</details>

Figure 3.17 Block diagram for the controllable canonical form

we have

$$\dot {x} _ {1} = x _ {2}\dot {x} _ {2} = x _ {3}$$

:

$$\dot {x} _ {n - 1} = x _ {n}\dot {x} _ {n} = - a _ {0} x _ {1} - a _ {1} x _ {2} - \dots - a _ {n - 1} x _ {n} + u$$

and

$$y = b _ {0} x _ {1} + b _ {1} x _ {2} + \dots + b _ {n - 1} x _ {n}.$$

In matrix form,

$$
\dot {\mathbf {x}} = \left[ \begin{array}{c c c c c c} 0 & 1 & 0 & 0 & \dots & 0 \\ 0 & 0 & 1 & 0 & \dots & 0 \\ \vdots & \vdots & \vdots & \vdots & \vdots & \vdots \\ 0 & 0 & \dots & \dots & 0 & 1 \\ - a _ {0} & - a _ {1} & \dots & \dots & \dots & - a _ {n - 1} \end{array} \right] \mathbf {x} + \left[ \begin{array}{c} 0 \\ 0 \\ \vdots \\ \vdots \\ 1 \end{array} \right] u

y = \left[ \begin{array}{l l l l} b _ {0} & b _ {1} & \dots & b _ {n - 1} \end{array} \right] \mathbf {x}. \tag {3.81}
$$

Equation 3.81 is the controllable canonical form. It is easily written by inspection, if the transfer function is expressed as a ratio of polynomials.
