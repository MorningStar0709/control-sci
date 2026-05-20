# Persistent Excitation

Let us first consider estimation of parameters in a FIR model given by Eq. (2.33). The parameters of the model cannot be determined unless some conditions are imposed on the input signal. It follows from the condition for uniqueness of the least-squares estimate given by Theorem 2.1 that the minimum is unique if the matrix

$$
\Phi^ {\mathrm{T}} \Phi = \left( \begin{array}{c c c c} \sum_ {n + 1} ^ {t} u ^ {2} (k - 1) & \sum_ {n + 1} ^ {t} u (k - 1) u (k - 2) & \dots & \sum_ {n + 1} ^ {t} u (k - 1) u (k - n) \\ \sum_ {n + 1} ^ {t} u (k - 1) u (k - 2) & \sum_ {n + 1} ^ {t} u ^ {2} (k - 2) & \dots & \sum_ {n + 1} ^ {t} u (k - 2) u (k - n) \\ \vdots & & & \\ \sum_ {n + 1} ^ {t} u (k - 1) u (k - n) & & & \sum_ {n + 1} ^ {t} u ^ {2} (k - n) \end{array} \right) \tag {2.42}
$$

has full rank. This condition is called an excitation condition. For long data sets, all sums in Eq. (2.42) can be taken from 1 to t. We then get

$$
C _ {n} = \lim _ {t \rightarrow \infty} \frac {1}{t} \Phi^ {T} \Phi = \left(\begin{array}{c c c c}c (0)&c (1)&\dots&c (n - 1)\\c (1)&c (0)&\dots&c (n - 2)\\\vdots&&&\\c (n - 1)&c (n - 2)&\dots&c (0)\end{array}\right) \tag {2.43}
$$

where $c(k)$ are the empirical covariances of the input, that is,

$$c (k) = \lim _ {t \rightarrow \infty} \frac {1}{t} \sum_ {i = 1} ^ {t} u (i) u (i - k) \tag {2.44}$$

For long data sets the condition for uniqueness can thus be expressed as the matrix in Eq. (2.43) being positive definite. This leads to the following definition.
