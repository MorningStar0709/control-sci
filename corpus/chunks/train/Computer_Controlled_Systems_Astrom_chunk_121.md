# The Pulse Response

Consider a discrete-time system with one input and one output. The input and output signals over a finite interval can be represented as finite-dimensional vectors

$$
U = \left( \begin{array}{l l l} u (0) & \dots & u (N - 1) \end{array} \right) ^ {T}

Y = \left( \begin{array}{l l l} y (0) & \dots & y (N - 1) \end{array} \right) ^ {T}
$$

The general linear model that relates Y to U can then be expressed as

$$\boldsymbol {Y} = \overline {{\boldsymbol {H}}} \boldsymbol {U} + \boldsymbol {Y} _ {p}$$

where $\overline{H}$ is an $N \times N$ matrix. $Y_{p}$ accounts for the initial conditions. If the relation between U and Y is causal, the matrix $\overline{H}$ must be lower triangular. The element $h(k,m)$ of $\overline{H}$ is thus zero if m > k. The input-output relationship for a general linear system can be written as

$$y (k) = \sum_ {m = 0} ^ {k} \overline {{{h}}} (k, m) u (m) + y _ {p} (k)$$

where the term $y_{p}$ is introduced to account for initial conditions in the system. The function $\overline{h}(k,m)$ is called the pulse-response function, or the weighting function, of the system. The pulse-response function is a convenient representation, because it can easily be measured directly by injecting a pulse of unit magnitude and the width of the sampling interval and recording the output. For zero initial conditions, the value $\overline{h}(k,m)$ of the pulse response gives the output at time k for a unit pulse at time m. For systems with many inputs and outputs, the pulse response is simply a matrix-valued function. For time-invariant systems, the pulse response is a function of k - m only, that is,

$$\overline {{{h}}} (k, m) = h (k - m)$$

It is easy to compute the pulse response of the system defined by the state-space model in (2.16). It follows from (2.17) that

$$y (k) = C \Phi^ {k - k _ {0}} x (k _ {0}) + \sum_ {j = k _ {0}} ^ {k - 1} C \Phi^ {k - j - 1} \Gamma u (j) + D u (k)$$

The pulse-response function for the discrete-time system is thus

$$
h (k) = \left\{ \begin{array}{l l} 0 & k <   0 \\ D & k = 0 \\ C \Phi^ {k - 1} \Gamma & k \geq 1 \end{array} \right. \tag {2.20}
$$

The pulse response is a sum of functions of the form

$$\operatorname{Re} \left\{\boldsymbol {P} (k) \lambda_ {i} ^ {k} \right\}$$

where $P$ is a polynomial in $k$ , and $\lambda_{i}$ are the eigenvalues of the matrix $\Phi$ .

The pulse response has the following property.
