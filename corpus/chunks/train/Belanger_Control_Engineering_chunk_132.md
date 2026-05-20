# 3.7.2 Similarity Transformations

Given a realization of $H(s)$ , it is possible to generate others through similarity transformations. A similarity transformation is really just a change in coordinates. Given

$$\dot {\mathbf {x}} = A \mathbf {x} + B \mathbf {u}\mathbf {y} = C \mathbf {x} + D \mathbf {u}$$

let

$$\mathbf {x} = T \mathbf {z}$$

or

$$\mathbf {z} = T ^ {- 1} \mathbf {x}$$

where T is a constant $n \times n$ nonsingular matrix. The vector z is used as the new state vector, i.e., the new set of coordinates. The state equations for z are easily derived, as

$$\dot {\mathbf {z}} = T ^ {- 1} \dot {\mathbf {x}} = T ^ {- 1} A \mathbf {x} + T ^ {- 1} B \mathbf {u}$$

or

$$\dot {\mathbf {z}} = T ^ {- 1} A T \mathbf {z} + T ^ {- 1} B \mathbf {u} \tag {3.55}$$

and

$$\mathbf {y} = C T \mathbf {z} + D \mathbf {u}. \tag {3.56}$$

Equations 3.55 and 3.56 are the state equations of the system in terms of the vector z. To show that the transfer function has not changed, note that the transfer function corresponding to Equations 3.55 and 3.56 is

$$H ^ {\prime} (s) = C T (s I - T ^ {- 1} A T) ^ {- 1} T ^ {- 1} B + D. \tag {3.57}$$

Now,

$$
\begin{array}{l} s I - T ^ {- 1} A T = s T ^ {- 1} T - T ^ {- 1} A T \\ = T ^ {- 1} (s I - A) T \\ \end{array}
$$

so that

$$
\begin{array}{l} (s I - T ^ {- 1} A T) ^ {- 1} = \left[ T ^ {- 1} (s I - A) T \right] ^ {- 1} \\ = T ^ {- 1} (s I - A) ^ {- 1} T. \\ \end{array}
$$

Insertion of this in Equation 3.57 yields

$$H ^ {\prime} (s) = C (s I - A) ^ {- 1} B + D = H (s).$$

This result is not surprising. The transfer function relates the input and output of the system, and should not be affected if we use a different coordinate system to describe the “inside of the box.”

It should also come as no surprise that controllability and observability are not affected by a similarity transformation. To see this, we show that, if $\mathbf{v}_i$ is an eigenvector of $A$ , corresponding to the eigenvalue $s_i$ , then $T^{-1}\mathbf{v}_i$ is an eigenvector of $T^{-1}AT$ . That follows from

$$(T ^ {- 1} A T) T ^ {- 1} \mathbf {v} _ {i} = T ^ {- 1} A \mathbf {v} _ {i} = s _ {i} T ^ {- 1} \mathbf {v} _ {i}.$$

(Note that the eigenvalues of $A$ and $T^{-1}AT$ are the same.)

Application of the eigenvector test for observability on the realization of Equations 3.55 and 3.56 yields

$$(C T) \left(T ^ {- 1} \mathbf {v} _ {i}\right) = C \mathbf {v} _ {i}$$

which shows that the new realization is urobserve if, and only if, the original one is. A similar argument is applicable to controllability.
