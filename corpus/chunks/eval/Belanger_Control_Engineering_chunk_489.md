# 8.6 THE CALCULATION OF SYSTEM NORMS

We shall calculate system norms from state-space data, because good algorithms have been devised for this purpose. First let us compute the $H^2$ norm. Let $g(t)$ be the matrix impulse response corresponding to $G(s)$ , i.e.,

$$g (t) = C e ^ {A t} B.$$

Since $A$ is assumed stable ( $G \in H_2$ ), we may use Parseval's theorem and write Equation 8.27 as

$$
\begin{array}{l} \| G \| _ {2} ^ {2} = \operatorname{tr} \int_ {0} ^ {\infty} g ^ {T} (t) g (t) d t \\ = \operatorname{tr} \int_ {0} ^ {\infty} B ^ {T} C ^ {A ^ {T} t} C ^ {T} C e ^ {A t} B d t \\ \end{array}
$$

or

$$\| G \| _ {2} ^ {2} = \operatorname{tr} B ^ {T} L _ {c} B \tag {8.37}$$

where

$$L _ {c} = \int_ {0} ^ {\infty} e ^ {A ^ {T} t} C ^ {T} C e ^ {A t} d t. \tag {8.38}$$

From Chapter 7, $L_{c}$ satisfies the Lyapunov equation,

$$A ^ {T} L _ {c} + L _ {c} A = - C ^ {T} C. \tag {8.39}$$

Since trxy = tryx, we may also use

$$\| G \| _ {2} ^ {2} = \operatorname{tr} \int_ {0} ^ {\infty} g (t) g ^ {T} (t) d t$$

which leads to

$$\| G \| _ {2} ^ {2} = \operatorname{tr} C L _ {o} C ^ {T} \tag {8.40}$$

where

$$A L _ {o} + L _ {o} A ^ {T} = - B B ^ {T}. \tag {8.41}$$

Example 8.5 A minimal realization for the transfer function of Example 8.3 is

$$
\begin{array}{l} \dot {\mathbf {x}} = \left[ \begin{array}{c c} 0 & 1 \\ - 2 & - 3 \end{array} \right] \mathbf {x} + \left[ \begin{array}{c c} 1 & - 1 \\ 0 & 1 \end{array} \right] \mathbf {u} \\ \mathbf {y} = \mathbf {x}. \\ \end{array}
$$

Compute the $H^{2}$ norm of G.

Solution The Lyapunov equation, Equation 8.39, is simple enough to be solved by hand. The result is

$$
L _ {c} = \left[ \begin{array}{l l} \frac {5}{4} & \frac {1}{4} \\ \frac {1}{4} & \frac {1}{4} \end{array} \right].
$$

From Equation 8.37,

$$
\begin{array}{l} \| G \| _ {2} ^ {2} = \operatorname{tr} \left[ \begin{array}{l l} 1 & 0 \\ - 1 & 1 \end{array} \right] \left[ \begin{array}{l l} \frac {5}{4} & \frac {1}{4} \\ \frac {1}{4} & \frac {1}{4} \end{array} \right] \left[ \begin{array}{l l} 1 & - 1 \\ 0 & 1 \end{array} \right] \\ = \frac {9}{4} \\ \end{array}
$$

as expected.

As a check, we may use Equations 8.40 and 8.41. We calculate

$$
L _ {o} = \left[ \begin{array}{c c} \frac {1 7}{1 2} & - 1 \\ - 1 & \frac {5}{6} \end{array} \right]
\| G \| _ {2} = \operatorname{tr} I L _ {o} I = \frac {9}{4}.
$$

To derive an algorithm for the calculation of the $H^{\infty}$ norm, we need the following results.

Lemma 8.1 Let

$$
H = \left[ \begin{array}{c c} A & B B ^ {T} \\ - C ^ {T} C & - A ^ {T} \end{array} \right]
$$
