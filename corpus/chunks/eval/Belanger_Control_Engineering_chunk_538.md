If $\widehat{u}(k) = u_0(k)$ , the discrete impulse, then the response $\widehat{y}(k)$ is the discrete-time impulse response. Its $z$ -transform is $G(z)$ , because $\mathcal{Z}[u_0(k)] = 1$ . As in the case of continuous-time systems, the discrete-time impulse response of a physically realizable system cannot be anticipatory. This fact forces the transfer function to be proper. To see this, consider that the long division of the ratio of polynomials of Equation 9.20 would begin with a positive power of $z^*$ equal to $i$ if the numerator leading term were $z^{n + i}$ , $i > 0$ , thus implying an impulse response sequence with a nonzero value at $k = -i$ .

Example 9.6 Calculate the discrete-time impulse response of the system described by the difference equation

$$\widehat {y} (k) = 1. 5 \widehat {y} (k - 1) - 0. 5 \widehat {y} (k - 2) + \widehat {u} (k - 1) + \widehat {u} (k - 2).$$

Solution By inspection,

$$
\begin{array}{l} \frac {\widehat {y} (z)}{\widehat {u} (z)} = \frac {z ^ {- 1} + z ^ {- 2}}{1 - 1 . 5 z ^ {- 1} + 0 . 5 z ^ {- 2}} \\ = \frac {(z + 1)}{z ^ {2} - 1 . 5 z + 0 . 5} = \frac {(z + 1)}{(z - 1) (z - 0 . 5)} \\ = \frac {4}{z - 1} - \frac {3}{z - 0 . 5} \\ = z ^ {- 1} \left[ \frac {4 z}{z - 1} - \frac {3 z}{z - 0 . 5} \right]. \\ \end{array}
$$

The impulse response is

$$g (k) = [ 4 - 3 (. 5) ^ {k - 1} ] u _ {- 1} (k - 1).$$

As in the case of continuous time, an LTI discrete-time system can also be represented by a set of first-order equations; this time, of course, they are difference equations, written in matrix form as

$$
\begin{array}{l} \widehat {\mathbf {x}} (k + 1) = A \widehat {\mathbf {x}} (k) + B \widehat {\mathbf {u}} (k) \\ \widehat {\mathbf {y}} (k) = C \widehat {\mathbf {x}} (k) + D \widehat {\mathbf {u}} (k). \tag {9.21} \\ \end{array}
$$

This is a state representation, and $\widehat{\mathbf{x}}$ is the state vector.

It is easy to write the zero-input response of the system of Equation 9.21: with $\widehat{\mathbf{u}}(k) = \mathbf{0}$ , the state equations are a simple recursion. We have

$$
\begin{array}{l} \widehat {\mathbf {x}} _ {z _ {i}} (1) = A \widehat {\mathbf {x}} (0) \\ \widehat {\mathbf {x}} _ {z i} (2) = A \widehat {\mathbf {x}} _ {z i} (1) = A ^ {2} \widehat {\mathbf {x}} (0) \\ \widehat {\mathbf {x}} _ {z _ {i}} (k) = A ^ {k} \widehat {\mathbf {x}} (0). \tag {9.22} \\ \end{array}
$$

•
•
•

If $\mathbf{v}_i$ is an eigenvector of $A$ corresponding to the eigenvalue $z_i$ , then, with $\widehat{\mathbf{x}}(0) = \mathbf{v}_i$ ,
