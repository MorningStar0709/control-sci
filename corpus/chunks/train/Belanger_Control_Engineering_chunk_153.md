# 3.7.6 Realization of Transfer Functions

This section addresses the problem of deriving a realization for a given transfer function. There are several situations where this is useful. In filter or controller design, the outcome is sometimes a specification in terms of a transfer function to be implemented by analog elements. An implementation in terms of “op-amp” integrators is essentially the same as a realization. There are also cases in control where the plant is described by its transfer function, which must be converted to state form to permit the use of a state-based design method.

The starting point is a strictly proper SISO transfer function,

$$\frac {y (s)}{u (s)} = H (s) = \frac {b _ {n - 1} s ^ {n - 1} + b _ {n - 2} s ^ {n - 2} + \cdots + b _ {0}}{s ^ {n} + a _ {n - 1} s ^ {n - 1} + \cdots + a _ {0}}. \tag {3.77}$$

Define an intermediate quantity $z(s)$ :

$$z (s) = \frac {1}{s ^ {n} + a _ {n - 1} s ^ {n - 1} + \cdots + a _ {0}} u (s). \tag {3.78}$$

The differential equation corresponding to Equation 3.78 is

$$z ^ {(n)} = - a _ {n - 1} z ^ {(n - 1)} - a _ {n - 1} z ^ {(n - 2)} - \dots - a _ {0} z + u. \tag {3.79}$$

Figure 3.16 is a simulation diagram representing Equation 3.79. The variable z and its derivatives up to the $(n-1)$ st are the outputs of integrators, and the nth derivative is constructed as prescribed by Equation 3.79.

![](image/7b7921db82cc9a0799a20d3ccb6730a69e4343dce1a44739a726bf2b916cb50b.jpg)

<details>
<summary>flowchart</summary>

```mermaid
graph TD
    u --> |+| sum((+))
    sum --> z_n1["z^(n)"]
    z_n1 --> |1/s| z_n_minus_1["1/(s)"]
    z_n_minus_1 --> |a_{n-1}| sum
    sum --> z_n_minus_2["1/s"]
    z_n_minus_2 --> |a_{n-2}| sum
    sum --> ... --> z_n_minus_3["..."]
    z_n_minus_3 --> |a_1| sum
    sum --> z_n_minus_4["1/s"]
    z_n_minus_4 --> |a_0| sum
    sum --> z
    z --> |ż| sum
    z_n_minus_4 --> |ż| sum
    sum --> z
```
</details>

Figure 3.16 Block diagram used in the construction of the controllable canonical form

From Equations 3.77 and 3.78, it follows that

$$y (s) = \left(b _ {n - 1} s ^ {n - 1} + b _ {n - 2} s ^ {n - 2} + \dots + b _ {0}\right) z (s)$$

so that

$$y = b _ {n - 1} z ^ {(n - 1)} + b _ {n - 2} z ^ {(n - 2)} + \dots + b _ {0} z. \tag {3.80}$$

Figure 3.17 generates y from z and its first $(n-1)$ derivatives, according to Equation 3.80; this completes the simulation.
