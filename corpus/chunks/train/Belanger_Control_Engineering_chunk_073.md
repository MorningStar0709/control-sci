# 3.2 LINEARITY PROPERTIES

A linear, time-invariant system is one described by the equations

$$\dot {\mathbf {x}} = A \mathbf {x} + B \mathbf {u}\mathbf {y} = C \mathbf {x} + D \mathbf {u}. \tag {3.1}$$

The dimension of the state vector x is n, the input u is an r-dimensional vector, and the output y is of dimension m. The matrices A, B, C, and D are constant matrices of appropriate dimensions. The initial state, $\mathbf{x}(0)$ , is $x_{0}$ .

It can be shown that there exists a unique solution $\mathbf{x}(t)$ to Equation 3.1 such that $\mathbf{x}(0) = \mathbf{x}_0$ .

The solution of LTI systems is broken down into two components, whose properties we will now explore. The zero-input response satisfies

$$\dot {\mathbf {x}} _ {z i} = A \mathbf {x} _ {z i}\mathbf {y} _ {z i} = C \mathbf {x} _ {z i} \tag {3.2}\text { with } \quad \mathbf {x} _ {z i} (0) = \mathbf {x} _ {0}.$$

The zero-state response satisfies

$$\dot {\mathbf {x}} _ {z s} = A \mathbf {x} _ {z s} + B \mathbf {u}\mathbf {y} _ {z s} = C \mathbf {x} _ {z s} + D \mathbf {u} \tag {3.3}\text { with } \quad \mathbf {x} _ {z s} (0) = \mathbf {0}.$$

LTI systems possess several important linearity properties.

a. Zero-input linearity: Let $\mathbf{x}_{1}(t)$ and $\mathbf{x}_{2}(t)$ be the zero-input responses with $\mathbf{x}_{1}(0)=\mathbf{x}_{10}$ and $\mathbf{x}_{2}(0)=\mathbf{x}_{20}$ . Then the zero-input response for the initial state $\alpha x_{10}+\beta x_{20}$ , with $\alpha$ and $\beta$ constants, is $\mathbf{x}(t)=\alpha\mathbf{x}_{1}(t)+\beta\mathbf{x}_{2}(t)$ . To show this, insert $\mathbf{x}(t)$ in Equation 3.2:

$$\dot {\mathbf {x}} = \alpha \dot {\mathbf {x}} _ {1} + \beta \dot {\mathbf {x}} _ {2} = \alpha A \mathbf {x} _ {1} + \beta A \mathbf {x} _ {2} = A (\alpha \mathbf {x} _ {1} + \beta \mathbf {x} _ {2}) = A \mathbf {x}$$

so that $\mathbf{x}(t)$ is a zero-input solution. Since

$$\mathbf {x} (0) = \alpha \mathbf {x} _ {1} (0) + \beta \mathbf {x} _ {2} (0) = \alpha \mathbf {x} _ {1 0} + \beta \mathbf {x} _ {2 0}$$

it follows that $\mathbf{x}$ also has the required initial value and therefore, by uniqueness, is the desired solution.
