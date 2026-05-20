# 8.10 $H^2$ SOLUTION

For the realization of Equation 8.57, the problem is to minimize $\| T_{\mathbf{wz}}(s)\| _2$ . The following assumptions are required:

1. $(A, B_{1})$ and $(A, B_{2})$ are stabilizable.   
2. $(C_1, A)$ and $(C_2, A)$ are detectable.   
3. $D_{12}^{T}D_{12}$ and $D_{21}D_{21}^{T}$ are nonsingular.   
4. $D_{11}=0.$

We write $T_{wz}$ by columns, as

$$T _ {\mathbf {w z}} = \left[ \left(T _ {\mathbf {w z}}\right) _ {1} \left(T _ {\mathbf {w z}}\right) _ {2} \dots \left(T _ {\mathbf {w z}}\right) _ {m} \right].$$

To calculate the $H^{2}$ -norm, we need to form

$$\operatorname{tr} T _ {\mathbf {w z}} ^ {T} (- s) T _ {\mathbf {w z}} (s) = \sum_ {i = 1} ^ {m} (T _ {\mathbf {w z}}) i ^ {T} (- s) (T _ {\mathbf {w z}}) _ {i} (s). \tag {8.58}$$

The square of the $H^2$ -norm is obtained by integrating the RHS of Equation 8.58 over the $j$ -axis. We may use Parseval's theorem to translate this into the time-domain integral

$$\| T _ {\mathbf {w z}} \| _ {2} ^ {2} = \sum_ {i = 1} ^ {m} \int_ {0} ^ {\infty} \| (T _ {\mathbf {w z}}) _ {i} (t) \| ^ {2} d t \tag {8.59}$$

where $(T_{\mathbf{wz}})_{i}(t)=\mathcal{L}^{-1}[(T_{\mathbf{wz}})_{i}(s)]$ is the response $\mathbf{z}(t)$ to a unit impulse in $w_{i}(t)$ . Now, “hitting” the system of Equation 8.57 with such an impulse is the same as giving it an initial state $b_{i}$ , the ith column of the matrix $B_{1}$ . Let $\mathbf{z}(\mathbf{x}_{0},t)$ be the response to an initial state $x_{0}$ . We may then write Equation 8.59 as

$$
\begin{array}{l} \| T _ {\mathbf {w z}} \| _ {2} ^ {2} = \sum_ {i = 1} ^ {m} \int_ {0} ^ {\infty} \| \mathbf {z} (\mathbf {b} _ {i}, t) \| ^ {2} d t \\ = \sum_ {i = 1} ^ {m} \int_ {0} ^ {\infty} \| C _ {1} \mathbf {x} (\mathbf {b} _ {i}, t) + D _ {1 2} \mathbf {u} (\mathbf {b} _ {i}, t) \| ^ {2} d t. \tag {8.60} \\ \end{array}
$$

where the notation for $\mathbf{x}$ and $\mathbf{u}$ parallels that for $\mathbf{z}$ . The problem, then, is to minimize the RHS of Equation 8.60, with

$$\dot {\mathbf {x}} = A \mathbf {x} + B _ {2} \mathbf {u} \tag {8.61}\mathbf {y} = C _ {2} \mathbf {x} + D _ {2 1} \mathbf {w} + D _ {2 2} \mathbf {u}. \tag {8.62}$$

Let us examine the case y = x, i.e., full state feedback, and expand the term corresponding to i = 1 in the RHS of Equation 8.60. We write
