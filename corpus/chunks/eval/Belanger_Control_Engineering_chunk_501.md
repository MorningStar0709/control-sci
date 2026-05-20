so that

$$\max _ {i j} [ \mathrm{tr} T _ {i j} ^ {*} T _ {i j} ] \leq \mathrm{tr} T ^ {*} T \leq n m \max _ {i j} [ \mathrm{tr} T _ {i j} ^ {*} T _ {i j} ]. \tag {8.56}$$

If $T$ is a function of $j\omega$ , Equation 8.56 also holds for the Parseval integral over frequency, since it holds pointwise. Taking square roots everywhere yields the desired result.

For the $\infty$ -norm, we define a vector

$$\mathbf {v} ^ {T} = [ \mathbf {v} _ {1} ^ {T} \mathbf {v} _ {2} ^ {T} \dots \mathbf {v} _ {m} ^ {T} ]$$

where the dimension of $\mathbf{v}_j$ is the column dimension of $T_{ij}$ . Then

$$
\| T \mathbf {v} \| _ {2} = \left\| \left[ \begin{array}{c c c c} T _ {1 1} \mathbf {v} _ {1} + T _ {1 2} \mathbf {v} _ {2} + \dots + T _ {1 m} \mathbf {v} _ {m} \\ T _ {2 1} \mathbf {v} _ {1} + & \dots & + T _ {2 m} \mathbf {v} _ {m} \\ \vdots & \vdots & \vdots \\ T _ {m 1} \mathbf {v} _ {1} + & \dots & + T _ {m m} \mathbf {v} _ {m} \end{array} \right] \right\|.
$$

We can select the $T_{ij}$ with the largest $\infty$ -norm, choose the $\mathbf{v}_j$ of unit norm that maximizes $\| T_{ij}\mathbf{v}_j\| _2$ , and set the remainder of the vector $\mathbf{v}$ to zero. In that case, $\| T\mathbf{v}\| _2 = \| T_{ij}\|_\infty$ ; this value is therefore a lower bound, which proves the left inequality (Equation 8.55).

To obtain the upper bound, we write

$$\| T \mathbf {v} \| _ {2} ^ {2} = \sum_ {i = 1} ^ {n} \| T _ {i 1} \mathbf {v} _ {1} + T _ {i 2} \mathbf {v} _ {2} + \dots + T _ {i m} \mathbf {v} _ {m} \| _ {2} ^ {2}$$

and

$$\sup _ {\| \mathbf {v} \| = 1} \| T _ {i 1} \mathbf {v} _ {1} + \dots + T _ {i m} \mathbf {v} _ {m} \| ^ {2} \leq m \max _ {j} \overline {{\sigma}} ^ {2} (T _ {i j}).$$

Since there are $n$ such terms,

$$\| T \mathbf {v} \| _ {2} ^ {2} \leq n m \max _ {i j} \overline {{\sigma}} ^ {2} (T _ {i j}).$$

The theorem follows if we take square roots and note that the result holds at all frequencies. ■
