$$
\begin{array}{l} \hat {\theta} (N + 1) = (\Phi^ {T} \Phi + \varphi \varphi^ {T}) ^ {- 1} (\Phi^ {T} y + \varphi y _ {N + 1}) \\ = (\Phi^ {T} \Phi) ^ {- 1} \Phi^ {T} y + \left((\Phi^ {T} \Phi + \varphi \varphi^ {T}) ^ {- 1} - (\Phi^ {T} \Phi) ^ {- 1}\right) \Phi^ {T} y \tag {13.13} \\ + \left(\Phi^ {T} \Phi + \varphi \varphi^ {T}\right) ^ {- 1} \varphi y _ {N + 1} \\ \end{array}
$$

Observe that

$$\hat {\theta} (N) = (\Phi^ {T} \Phi) ^ {- 1} \Phi^ {T} y$$

and

$$
\begin{array}{l} \left(\left(\Phi^ {T} \Phi + \varphi \varphi^ {T}\right) ^ {- 1} - \left(\Phi^ {T} \Phi\right) ^ {- 1}\right) \Phi^ {T} y \\ = \left(\Phi^ {T} \Phi + \varphi \varphi^ {T}\right) ^ {- 1} \left(\Phi^ {T} \Phi - \Phi^ {T} \Phi - \varphi \varphi^ {T}\right) \left(\Phi^ {T} \Phi\right) ^ {- 1} \Phi^ {T} y \\ = - \left(\Phi^ {T} \Phi + \varphi \varphi^ {T}\right) ^ {- 1} \varphi \varphi^ {T} \left(\Phi^ {T} \Phi\right) ^ {- 1} \Phi^ {T} y \\ = - \left(\Phi^ {T} \Phi + \varphi \varphi^ {T}\right) ^ {- 1} \varphi \varphi^ {T} \hat {\theta} \\ \end{array}
$$

Equation (13.13) can be written as

$$\hat {\theta} (N + 1) = \hat {\theta} (N) + K (N) \left(y _ {N + 1} - \varphi^ {T} (N + 1) \hat {\theta} (N)\right)$$

In order to obtain a recursive equation for the weighting factor $K(N)$ , it is convenient to introduce the quantity P defined by

$$P (N) = \left(\Phi^ {T} (N) \Phi (N)\right) ^ {- 1}$$

P is proportional to the variance of the estimates (compare with Theorem 13.2). Applying the matrix inversion lemma (Lemma B.1) to the matrix $P(N+1)$ gives

$$
\begin{array}{l} P (N + 1) = \left(\Phi^ {T} (N + 1) \Phi (N + 1)\right) ^ {- 1} = \left(\Phi^ {T} \Phi + \varphi \varphi^ {T}\right) ^ {- 1} \\ = \left(\Phi^ {T} \Phi\right) ^ {- 1} - \left(\Phi^ {T} \Phi\right) ^ {- 1} \varphi (I + \varphi^ {T} \left(\Phi^ {T} \Phi\right) ^ {- 1} \varphi) ^ {- 1} \varphi^ {T} \left(\Phi^ {T} \Phi\right) ^ {- 1} \\ \end{array}
$$

Hence

$$
\begin{array}{l} P (N + 1) = P (N) - P (N) \varphi (N + 1) \\ \times \left(I + \varphi^ {T} (N + 1) P (N) \varphi (N + 1)\right) ^ {- 1} \varphi^ {T} (N + 1) P (N) \\ \end{array}
$$

Simple calculations now give

$$
\begin{array}{l} K (N) = P (N + 1) \varphi (N + 1) \\ = P (N) \varphi (N + 1) \left(I + \varphi^ {T} (N + 1) P (N) \varphi (N + 1)\right) ^ {- 1} \\ \end{array}
$$

Notice that a matrix inversion is necessary to compute P. However, the matrix to be inverted is of the same dimension as the number of measurements; that is, for a single-output system, it is a scalar.
