# Perturbation Equations

For purposes of propagating the covariance matrix in the intervals between measurements (see the discussion in Section 4.8) it is necessary to linearize (4.93) by perturbing around the present best estimate. In the perturbation equation, the scalars a, v, and $F _ { v }$ are treated by using the relations

$$\delta v = \mathbf {e} _ {v} \delta \mathbf {v} = (1 / v) \mathbf {v} ^ {T} \delta \mathbf {v}, \tag {4.97a}\delta a = (1 / a) \mathbf {a} ^ {T} \delta \mathbf {a}, \tag {4.97b}$$

and from (4.96a),

$$
\begin{array}{l} \delta F _ {v} = (- 1 / v ^ {2}) \mathbf {v} ^ {T} \mathbf {a} \delta v + (1 / v) [ \mathbf {a} ^ {T} \delta \mathbf {v} + \mathbf {v} ^ {T} \delta \mathbf {a} ] \\ = (- 1 / v ^ {2}) (v \mathbf {a} - F _ {v} \mathbf {v}) ^ {T} \delta v + (1 / v) \mathbf {v} ^ {T} \delta \mathbf {a}. \tag {4.98} \\ \end{array}
$$

Note that the terms containing the $w ' s$ in (4.93) are not differentiated, since the $w ' s$ themselves are assumed to be small. Equations (4.97) and (4.98) can be cast in the usual form (see Section 4.8, (4.100)):

$$\frac {d \mathbf {x} (t)}{d t} = F \mathbf {x} (t) + G \mathbf {w} (t).$$

The matrices F and G are used in the propagation of the covariance matrix from one measurement time to the next, as is the $3 \times 3$ spectral-density matrix Q of the white noise vector w. Also, the white noise vector w(t) consists of the three noises in (4.90), that is, $\mathbf { w } ^ { T } ( t ) = [ w _ { n } w _ { v } w _ { \omega } ]$ .
