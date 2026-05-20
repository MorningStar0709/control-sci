$$[ \mathbf {u} ^ {*} (t) + \mathbf {q} ^ {*} (t) ] ^ {\prime} \mathbf {R} (t) [ \mathbf {u} ^ {*} (t) + \mathbf {q} ^ {*} (t) ]\leq \left[ \mathbf {u} (t) + \mathbf {q} ^ {*} (t) \right] ^ {\prime} \mathbf {R} (t) \left[ \mathbf {u} (t) + \mathbf {q} ^ {*} (t) \right]. \tag {7.5.16}$$

That is

$$
\begin{array}{l} \mathbf {w} ^ {* \prime} (t) \mathbf {R} (t) \mathbf {w} ^ {*} (t) \leq \mathbf {w} ^ {\prime} (t) \mathbf {R} (t) \mathbf {w} (t) \\ = \min _ {| \mathbf {u} (t) | \leq 1 |} \left\{\mathbf {w} ^ {\prime} (t) \mathbf {R} (t) \mathbf {w} (t) \right\}, \tag {7.5.17} \\ \end{array}
$$

where,

$$\mathbf {w} (t) = \mathbf {u} (t) + \mathbf {q} ^ {*} (t) = \mathbf {u} (t) + \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \boldsymbol {\lambda} ^ {*} (t)\mathbf {w} ^ {*} (t) = \mathbf {u} ^ {*} (t) + \mathbf {q} ^ {*} (t) = \mathbf {u} ^ {*} (t) + \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \boldsymbol {\lambda} ^ {*} (t). \tag {7.5.18}$$

The relation (7.5.17) implies that $\mathbf{w}'(t)$ attains its minimum value at $\mathbf{w}^{*}(t)$ .

Now we know that

1. if $\mathbf{R}(t)$ is positive definite for all $t$ , its eigenvalues $d_{1}(t), d_{2}(t), \ldots, d_{r}(t)$ are positive,

2. if $\mathbf{D}(t)$ is the diagonal matrix of the eigenvalues $d_{1}(t), d_{2}(t), \ldots, d_{r}(t)$ of $\mathbf{R}(t)$ , then

3. there is an orthogonal matrix $\mathbf{M}$ such that

$$\mathbf {M} ^ {\prime} \mathbf {M} = \mathbf {I} \rightarrow \mathbf {M} ^ {\prime} = \mathbf {M} ^ {- 1} \tag {7.5.19}$$

and

$$\mathbf {D} = \mathbf {M} ^ {\prime} \mathbf {R M} \rightarrow \mathbf {M D M} ^ {\prime} = \mathbf {R}. \tag {7.5.20}$$

Now, using (7.5.20) along with (7.5.17), we have

$$
\begin{array}{l} \mathbf {w} ^ {\prime} (t) \mathbf {R} \mathbf {w} (t) = \mathbf {w} ^ {\prime} (t) \mathbf {M D M} ^ {\prime} \mathbf {w} (t) \\ = \mathbf {v} ^ {\prime} (t) \mathbf {D} \mathbf {v} (t) = \sum_ {j = 1} ^ {r} d _ {j} (t) v _ {j} ^ {2} (t) \tag {7.5.21} \\ \end{array}
$$

where, $\mathbf{v}(t)=\mathbf{M}^{\prime}\mathbf{w}(t)$ and note that $d_{j}>0$ . Since both $M^{\prime}$ and M are orthogonal, we know that

$$\mathbf {v} ^ {\prime} (t) \mathbf {v} (t) = \mathbf {w} ^ {\prime} (t) \mathbf {M M} ^ {\prime} \mathbf {w} (t) = \mathbf {w} ^ {\prime} (t) \mathbf {w} (t) \tag {7.5.22}$$

where, we used $M^{\prime}M = I$ . We can equivalently write (7.5.22) component wise as

$$\sum_ {j = 1} ^ {r} v _ {j} ^ {2} (t) = \sum_ {j = 1} ^ {r} w _ {j} ^ {2} (t). \tag {7.5.23}$$
