# 3.3.1 The Matrix Exponential

Consider the zero-input equation

$$\dot {\mathbf {x}} = A \mathbf {x} \tag {3.4}$$

to be solved with a given initial state $\mathbf{x}(0)$ .

By differentiation of Equation 3.4, we obtain

$$\ddot {\mathbf {x}} = A \dot {\mathbf {x}} = A ^ {2} \mathbf {x}.$$

Repetition $k$ times yields

$$\mathbf {x} ^ {(3)} = A ^ {2} \dot {\mathbf {x}} = A ^ {3} \mathbf {x}\mathbf {x} ^ {(k)} = A ^ {k} \mathbf {x}. \tag {3.5}$$

The $k$ th derivative at $t = 0$ is

$$\mathbf {x} ^ {(k)} (0) = A ^ {k} \mathbf {x} (0). \tag {3.6}$$

Equation 3.6 shows that $\mathbf{x}^{(k)}(0)$ exists for all finite $k$ . This means that the components of $\mathbf{x}(t)$ are analytic functions, which admit representation by Taylor series. Thus,

$$
\begin{array}{l} \mathbf {x} (t) = \mathbf {x} (0) + \dot {\mathbf {x}} (0) t + \frac {1}{2 !} \ddot {\mathbf {x}} (0) t ^ {2} + \dots + \frac {1}{k !} \mathbf {x} ^ {(k)} (0) t ^ {k} + \dots \\ = \mathbf {x} (0) + A \mathbf {x} (0) t + \frac {1}{2 !} A ^ {2} \mathbf {x} (0) t ^ {2} + \dots + \frac {1}{k !} A ^ {k} \mathbf {x} (0) t ^ {k} + \dots \\ = \left(I + A t + \frac {1}{2 !} A ^ {2} t ^ {2} + \dots + \frac {1}{k !} A ^ {k} t ^ {k} + \dots\right) \mathbf {x} (0). \tag {3.7} \\ \end{array}
$$

The series in parentheses can be shown to converge for all finite t. It is called the matrix exponential and given the symbol $e^{At}$ , by analogy with the scalar exponential and its series. Thus,

$$e ^ {A t} = I + A t + \frac {1}{2 !} A ^ {2} t ^ {2} + \dots + \frac {1}{k !} A ^ {k} t ^ {k} + \dots . \tag {3.8}$$

Numerical algorithms to evaluate $e^{At}$ are based on this series, with a few tricks thrown in (see Problem 3.3).

The solution $\mathbf{x}(t) = e^{At}\mathbf{x}(0)$ is seen to be a linear transformation: $e^{At}$ is an $n\times n$ matrix which, by matrix-vector multiplication, transforms vector $\mathbf{x}(0)$ into vector $\mathbf{x}(t)$ . The transformation depends on $t$ , the difference between the initial and final times; the initial time, taken here to be zero, is arbitrary. This fact is used in the numerical solution of $\dot{\mathbf{x}} = A\mathbf{x}$ to generate values of $\mathbf{x}$ at $t = \Delta, 2\Delta, 3\Delta, \ldots$ , as follows:

$$\mathbf {x} (\Delta) = e ^ {A \Delta} \mathbf {x} (0)\mathbf {x} (2 \Delta) = e ^ {A \Delta} \mathbf {x} (\Delta)$$

![](image/e9f7ba8f51c52392c1c8142c61c974150333130d8ca4228022a30df10c70409d.jpg)

$$\mathbf {x} (k \Delta + \Delta) = e ^ {A \Delta} \mathbf {x} (k \Delta). \tag {3.9}$$
