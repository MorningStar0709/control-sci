# Realization

The equations needed to implement the general MRAS can now be summarized:

$$y _ {m} = \frac {B _ {m}}{A _ {m}} u _ {c}e _ {f} = \frac {Q}{P} e = \frac {Q}{P} (y - y _ {m})\eta = - \left(\frac {1}{P _ {1}} u + \varphi^ {T} \theta\right)\varepsilon = e _ {f} + \frac {b _ {0} Q}{A _ {o} A _ {m}} \eta\frac {d \theta}{d t} = \gamma \varphi \varepsilonu = - \theta^ {T} (P _ {1} \varphi)$$

A block diagram of the model-reference adaptive system is shown in Fig. 5.21. The block labeled "Filter" in Fig. 5.21 is a linear system that generates $P_{1}\varphi$ and $\varphi$ from the signals $u_{c}, u,$ and $y$ . The vector $\varphi$ is composed of three parts having the same structure. It therefore suffices to discuss one part. Consider, for example, how to generate $\varphi_{u}$ and $P_{1}\varphi_{u}$ where

$$P _ {1} \varphi_ {u} = \left(\frac {p ^ {k - 1}}{P _ {2}} u \dots \frac {1}{P _ {2}} u\right) ^ {T} = (x _ {1} \dots x _ {k}) ^ {T} = x ^ {T}$$

and

$$\varphi_ {u} = \left(\frac {p ^ {k - 1}}{P} u \dots \frac {1}{P} u\right) ^ {T}$$

where $P = P_{1}P_{2}$ and $k = \deg R = \deg P_{2}$ .

Let the polynomials $P_{1}$ and $P_{2}$ be

$$
\begin{array}{l} P _ {1} = p ^ {n} + \alpha_ {1} p ^ {n - 1} + \dots + \alpha_ {n} \\ P _ {2} = p ^ {k} + \beta_ {1} p ^ {k - 1} + \dots + \beta_ {k} \\ \end{array}
$$

We also assume that $\deg P_{1} > \deg P_{2}$ . The vectors x and $\varphi_{u}$ can then be realized as follows:

$$
\frac {d x}{d t} = \left( \begin{array}{c c c c c} - \beta_ {1} & - \beta_ {2} & \dots & - \beta_ {k - 1} & - \beta_ {k} \\ 1 & 0 & & 0 & 0 \\ \vdots & \ddots & & & \\ 0 & 0 & & 1 & 0 \end{array} \right) x + \left( \begin{array}{c} 1 \\ 0 \\ \vdots \\ 0 \end{array} \right) u

\frac {d z}{d t} = \left( \begin{array}{c c c c c} - \alpha_ {1} & - \alpha_ {2} & \dots & - \alpha_ {n - 1} & - \alpha_ {n} \\ 1 & 0 & & 0 & 0 \\ \vdots & \ddots & & & \\ 0 & 0 & & 1 & 0 \end{array} \right) z + \left( \begin{array}{c} 1 \\ 0 \\ \vdots \\ 0 \end{array} \right) x _ {k}
$$

where $x_{k} = 1/P_{2} \cdot u$ is the last element of the x vector. The elements of $\varphi_{u}$ are the k last elements of the state vector z. Furthermore, $1/P_{1} \cdot u$ can also be obtained from the generation of $\varphi_{u}$ and $P_{1}\varphi_{u}$ . To generate the full vectors $\varphi$ and $P_{1}\varphi$ , we thus need three realizations of the transfer functions $P_{1}$ and $P_{2}$ . The block labeled “Filter” in Fig. 5.21 represents these systems.
