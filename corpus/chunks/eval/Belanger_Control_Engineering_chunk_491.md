Proof: Let $\alpha j$ be an unobservable eigenvalue of $H$ , with $\mathbf{v}$ the corresponding eigenvector. Let $\mathbf{v}$ be partitioned into two $n$ -vectors, $\mathbf{v}_1$ and $\mathbf{v}_2$ .

From Equation 8.43, and because this mode is unobservable,

$$
[ 0 \quad B ^ {T} ] \left[ \begin{array}{l} \mathbf {v} _ {1} \\ \mathbf {v} _ {2} \end{array} \right] = B ^ {T} \mathbf {v} _ {2} = 0. \tag {8.45}
$$

Since $\mathbf{v}$ is an eigenvector,

$$
H \mathbf {v} = \left[ \begin{array}{c c} A & B B ^ {T} \\ - C ^ {T} C & - A ^ {T} \end{array} \right] \left[ \begin{array}{l} \mathbf {v} _ {1} \\ \mathbf {v} _ {2} \end{array} \right] = \alpha j \left[ \begin{array}{l} \mathbf {v} _ {1} \\ \mathbf {v} _ {2} \end{array} \right]. \tag {8.46}
$$

Combining 8.45 and 8.46,

$$A \mathbf {v} _ {1} = \alpha j \mathbf {v} _ {1} \tag {8.47}- C ^ {T} C \mathbf {v} _ {1} - A ^ {T} \mathbf {v} _ {2} = \alpha j \mathbf {v} _ {2}. \tag {8.48}$$

We conclude from Equation 8.47 that either (i) $\mathbf{v}_1 = 0$ or (ii) $A$ has an eigenvalue $\alpha j$ , with $\mathbf{v}_1$ as the corresponding eigenvector.

If $\mathbf{v}_1 = 0$ , then, from Equation 8.48,

$$A ^ {T} \mathbf {v} _ {2} = - \alpha j \mathbf {v} _ {2}$$

which, combined with Equation 8.45, shows that $A^T$ (hence $A$ ) has an eigenvalue $-\alpha j$ , and that mode is uncontrollable. That is contrary to our assumption of stabilizability, so $\mathbf{v}_1 \neq 0$ .

If $\mathbf{v}_1 \neq 0$ , then Equation 8.45 shows that $A$ has an eigenvalue $\alpha j$ with $\mathbf{v}_1$ as the corresponding eigenvector. Premultiplying Equation 8.48 by $\mathbf{v}_1^{*T}$ ,

$$
\begin{array}{l} - \mathbf {v} _ {1} ^ {* T} C ^ {T} C \mathbf {v} _ {1} = \mathbf {v} _ {1} ^ {* T} (A ^ {T} + \alpha j I) \mathbf {v} _ {2} \\ = \mathbf {v} _ {2} ^ {T} (A + \alpha j I) \mathbf {v} _ {1} ^ {*} \\ \end{array}
$$

where the last step uses the fact that a scalar is its own transpose. Now, if $\alpha j$ is an eigenvalue of $A$ , so is $-\alpha j$ , and its associated eigenvector is $\mathbf{v}_1^*$ . Hence, $A\mathbf{v}_1^* = -\alpha j\mathbf{v}_1^*$ and

$$\mathbf {v} _ {1} ^ {* T} C ^ {T} C \mathbf {v} _ {1} = \mathbf {v} _ {2} ^ {T} (- \alpha j \mathbf {v} _ {1} ^ {*} + \alpha j \mathbf {v} _ {1} ^ {*}) = 0$$

and

$$\mathbf {v} _ {1} ^ {* T} C ^ {T} C \mathbf {v} _ {1} = \| C \mathbf {v} _ {1} \| ^ {2} = 0$$

or

$$C \mathbf {v} _ {1} = 0$$

which shows that the mode $\alpha j$ is not observable, contrary to our detectability assumption. We see that the assumed existence of an unobservable $j$ -axis mode for the realization of Equation 8.43 leads to a contradiction and hence must be rejected. A similar proof goes through if we assume a $j$ -axis uncontrollable mode.

We now come to our central result.
