Since we have q linearly independent column vectors $\mathbf { f } _ { 1 } , \mathbf { f } _ { 2 } , \ldots , \mathbf { f } _ { q }$ , we can use the Cayley–Hamilton theorem to express vectors $\mathbf { A f } _ { 1 } , \mathbf { A f } _ { 2 } , \ldots , \mathbf { A f } _ { q }$ in terms of these q vectors. That is,

$$\mathbf {A} \mathbf {f} _ {1} = a _ {1 1} \mathbf {f} _ {1} + a _ {2 1} \mathbf {f} _ {2} + \dots + a _ {q 1} \mathbf {f} _ {q}\mathbf {A} \mathbf {f} _ {2} = a _ {1 2} \mathbf {f} _ {1} + a _ {2 2} \mathbf {f} _ {2} + \dots + a _ {q 2} \mathbf {f} _ {q}\mathbf {A} \mathbf {f} _ {q} = a _ {1 q} \mathbf {f} _ {1} + a _ {2 q} \mathbf {f} _ {2} + \dots + a _ {q q} \mathbf {f} _ {q}$$

Hence, Equation (10–137) may be written as follows:

$$
\left[ \begin{array}{c c c c c c c c} \mathbf {A f} _ {1} & \mathbf {A f} _ {2} & \dots & \mathbf {A f} _ {q} & \mathbf {A v} _ {q + 1} & \dots & \mathbf {A v} _ {n} \end{array} \right]

= \left[ \begin{array}{c c c c c c c} \mathbf {f} _ {1} & \mathbf {f} _ {2} & \dots & \mathbf {f} _ {q} & \mathbf {v} _ {q + 1} & \dots & \mathbf {v} _ {n} \end{array} \right] \left[ \begin{array}{c c c c c c} a _ {1 1} & \dots & a _ {1 q} & a _ {1 q + 1} & \dots & a _ {1 n} \\ a _ {2 1} & \dots & a _ {2 q} & a _ {2 q + 1} & \dots & a _ {2 n} \\ . & & . & . & & . \\ . & & . & . & & . \\ . & & . & . & & . \\ a _ {q 1} & \dots & a _ {q q} & a _ {q q + 1} & \dots & a _ {q n} \\ \hline 0 & \dots & 0 & a _ {q + 1 q + 1} & \dots & a _ {q + 1 n} \\ . & & . & . & & . \\ . & & . & . & & . \\ . & & . & . & & . \\ 0 & \dots & 0 & a _ {n q + 1} & \dots & a _ {n n} \end{array} \right]
$$

Define

$$
\left[ \begin{array}{c c c} a _ {1 1} & \dots & a _ {1 q} \\ a _ {2 1} & \dots & a _ {2 q} \\ \cdot & & \cdot \\ \cdot & & \cdot \\ \cdot & & \cdot \\ a _ {q 1} & \dots & a _ {q q} \end{array} \right] = \mathbf {A} _ {1 1}

\left[ \begin{array}{c c c} a _ {1 q + 1} & \dots & a _ {1 n} \\ a _ {2 q + 1} & \dots & a _ {2 n} \\ \cdot & & \cdot \\ \cdot & & \cdot \\ \cdot & & \cdot \\ a _ {q q + 1} & \dots & a _ {q n} \end{array} \right] = \mathbf {A} _ {1 2}

\left[ \begin{array}{c c c} 0 & \dots & 0 \\ \cdot & & \cdot \\ \cdot & & \cdot \\ \cdot & & \cdot \\ 0 & \dots & 0 \end{array} \right] = \mathbf {A} _ {2 1} = (n - q) \times q \text { zero   matrix }

\left[ \begin{array}{c c c} a _ {q + 1 q + 1} & \dots & a _ {q + 1 n} \\ \cdot & & \cdot \\ \cdot & & \cdot \\ \cdot & & \cdot \\ a _ {n q + 1} & \dots & a _ {n n} \end{array} \right] = \mathbf {A} _ {2 2}
$$

Then Equation (10–137) can be written as
