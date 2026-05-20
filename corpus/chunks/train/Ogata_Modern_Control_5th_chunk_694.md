```mermaid
graph TD
    u --> Bn1["b_n - a_n b_0"]
    u --> Bn2["b_{n-1} - a_{n-1} b_0"]
    u --> Bn3["b_1 - a_1 b_0"]
    u --> Bn4["b_0"]
    Bn1 --> Sum1["+/-"]
    Bn2 --> Sum2["+/-"]
    Bn3 --> Sum3["+/-"]
    Bn4 --> Sum4["+/-"]
    Sum1 --> Int1["∫"]
    Sum2 --> Int2["∫"]
    Sum3 --> Int3["∫"]
    Sum4 --> Int4["∫"]
    Int1 --> x1["x_1"]
    Int2 --> x2["x_2"]
    Int3 --> x3["x_{n-1}"]
    Int4 --> x4["x_n"]
    x1 --> a_n["a_n"]
    x2 --> a_{n-1}[a_{n-1}]
    x3 --> a_n1["a_1"]
    x4 --> a_n2["a_1"]
    a_n --> Sum1
    a_{n-1} --> Sum2
    a_{n-1} --> Sum3
    a_{n-1} --> Sum4
    a_n1 --> Sum1
    a_{n-1} --> Sum2
    a_{n-1} --> Sum3
    a_n2 --> Sum4
    a_n3 --> Sum1
    a_n3 --> Sum2
    a_n3 --> Sum3
    a_n3 --> Sum4
    Sum1 --> y["y"]
    Sum2 --> y
    Sum3 --> y
    Sum4 --> y
```
</details>

A–9–3. Consider the transfer-function system defined by

$$
\begin{array}{l} \frac {Y (s)}{U (s)} = \frac {b _ {0} s ^ {n} + b _ {1} s ^ {n - 1} + \cdots + b _ {n - 1} s + b _ {n}}{(s + p _ {1}) (s + p _ {2}) \cdots (s + p _ {n})} \\ = b _ {0} + \frac {c _ {1}}{s + p _ {1}} + \frac {c _ {2}}{s + p _ {2}} + \dots + \frac {c _ {n}}{s + p _ {n}} \tag {9-83} \\ \end{array}
$$

where $p _ { i } \neq p _ { j }$ Derive the state-space representation of this system in the following diagonal. canonical form:

$$
\left[ \begin{array}{c} \dot {x} _ {1} \\ \dot {x} _ {2} \\ \cdot \\ \cdot \\ \cdot \\ \dot {x} _ {n} \end{array} \right] = \left[ \begin{array}{c c c c c c} - p _ {1} & & & & & 0 \\ & - p _ {2} & & & & \\ & & \cdot & & & \\ & & & \cdot & & \\ & & & & \cdot & \\ 0 & & & & & - p _ {n} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ \cdot \\ \cdot \\ \cdot \\ x _ {n} \end{array} \right] + \left[ \begin{array}{c} 1 \\ 1 \\ \cdot \\ \cdot \\ \cdot \\ 1 \end{array} \right] u \tag {9-84}

y = \left[ \begin{array}{l l l l} c _ {1} & c _ {2} & \dots & c _ {n} \end{array} \right] \left[ \begin{array}{c} x _ {1} \\ x _ {2} \\ \cdot \\ \cdot \\ \cdot \\ x _ {n} \end{array} \right] + b _ {0} u \tag {9-85}
$$

Solution. Equation (9–83) may be written as

$$Y (s) = b _ {0} U (s) + \frac {c _ {1}}{s + p _ {1}} U (s) + \frac {c _ {2}}{s + p _ {2}} U (s) + \dots + \frac {c _ {n}}{s + p _ {n}} U (s) \tag {9-86}$$

Define the state variables as follows:

$$X _ {1} (s) = \frac {1}{s + p _ {1}} U (s)X _ {2} (s) = \frac {1}{s + p _ {2}} U (s)X _ {n} (s) = \frac {1}{s + p _ {n}} U (s)$$

which may be rewritten as

$$s X _ {1} (s) = - p _ {1} X _ {1} (s) + U (s)s X _ {2} (s) = - p _ {2} X _ {2} (s) + U (s)s X _ {n} (s) = - p _ {n} X _ {n} (s) + U (s)$$

The inverse Laplace transforms of these equations give
