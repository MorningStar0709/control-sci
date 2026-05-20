# Dyadic Decomposition

Given vectors

$$
a = \left( \begin{array}{l l l l} 1 & a _ {2} & \dots & a _ {n} \end{array} \right) ^ {T}

b = \left( \begin{array}{c c c c} b _ {1} & b _ {2} & \dots & b _ {n} \end{array} \right) ^ {T}
$$

and scalars $\alpha$ and $\beta$ , find new vectors

$$
\bar {a} = \left( \begin{array}{c c c c} 1 & \tilde {a} _ {2} & \dots & \ddot {a} _ {n} \end{array} \right) ^ {T}

\tilde {b} = \left( \begin{array}{c c c c} 0 & \tilde {b} _ {2} & \dots & \tilde {b} _ {n} \end{array} \right) ^ {T}
$$

such that

$$\alpha a a ^ {T} + \beta b b ^ {T} = \tilde {\alpha} \tilde {a} \tilde {a} ^ {T} + \tilde {\beta} \tilde {b} \tilde {b} ^ {T} \tag {11.34}$$

If this problem can be solved, we can perform the composition of Eq. (11.33) by repeated application of the method.

Equation (11.34) can be written as

$$
\begin{array}{l} \alpha \left( \begin{array}{c} 1 \\ a _ {2} \\ \vdots \\ a _ {n} \end{array} \right) \left( \begin{array}{l l l l} 1 & a _ {2} & \dots & a _ {n} \end{array} \right) + \beta \left( \begin{array}{c} b _ {1} \\ b _ {2} \\ \vdots \\ b _ {n} \end{array} \right) \left( \begin{array}{l l l l} b _ {1} & b _ {2} & \dots & b _ {n} \end{array} \right) \\ = \tilde {\alpha} \left( \begin{array}{c} 1 \\ \tilde {a} _ {2} \\ \vdots \\ \bar {a} _ {n} \end{array} \right) \left( \begin{array}{l l l l} 1 & \tilde {a} _ {2} & \dots & \tilde {a} _ {n} \end{array} \right) + \tilde {\beta} \left( \begin{array}{c} 0 \\ \tilde {b} _ {2} \\ \vdots \\ \tilde {b} _ {n} \end{array} \right) \left( \begin{array}{l l l l} 0 & \tilde {b} _ {2} & \dots & \tilde {b} _ {n} \end{array} \right) \tag {11.35} \\ \end{array}
$$

Equating the $(1,1)$ elements gives

$$\alpha + \beta b _ {1} ^ {2} = \tilde {\alpha} \tag {11.36}$$

Equating the $(1,k)$ elements for $k > 1$ gives

$$\alpha a _ {k} + \beta b _ {1} b _ {k} = \tilde {\alpha} \bar {a} _ {k} \tag {11.37}$$

Adding and subtracting $\beta b_1^2 a_k$ give

$$(\alpha + \beta b _ {1} ^ {2}) a _ {k} + \beta b _ {1} b _ {k} - \beta b _ {1} ^ {2} a _ {k} = \tilde {\alpha} \tilde {a} _ {k}$$

Hence

$$\tilde {a} _ {k} = a _ {k} + \frac {\beta b _ {1}}{\tilde {\alpha}} (b _ {k} - b _ {1} a _ {k}) \tag {11.38}$$

The numbers $\tilde{\alpha}$ and $\tilde{a}_k$ can thus be determined. It now remains to compute $\tilde{\beta}$ and $\tilde{b}_k$ . Equating the $(k,l)$ elements of Eq. (11.35) for $k,l > 1$ gives
