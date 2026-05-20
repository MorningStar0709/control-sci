$$
\begin{array}{l} \mathbf {P} _ {k + 1} ^ {+} = \mathbf {P} _ {k + 1} ^ {-} (\mathbf {I} - \mathbf {C} _ {k + 1} ^ {\mathsf {T}} \mathbf {K} _ {k + 1} ^ {\mathsf {T}}) - \mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1} \mathbf {P} _ {k + 1} ^ {-} (\mathbf {I} - \mathbf {C} _ {k + 1} ^ {\mathsf {T}} \mathbf {K} _ {k + 1} ^ {\mathsf {T}}) \\ + \mathbf {K} _ {k + 1} \mathbf {R} _ {k + 1} \mathbf {K} _ {k + 1} ^ {\top} \\ \end{array}
$$

Expand terms.

$$
\begin{array}{l} \mathbf {P} _ {k + 1} ^ {+} = \mathbf {P} _ {k + 1} ^ {-} - \mathbf {P} _ {k + 1} ^ {-} \mathbf {C} _ {k + 1} ^ {\top} \mathbf {K} _ {k + 1} ^ {\top} - \mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1} \mathbf {P} _ {k + 1} ^ {-} \\ + \mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1} \mathbf {P} _ {k + 1} ^ {-} \mathbf {C} _ {k + 1} ^ {\top} \mathbf {K} _ {k + 1} ^ {\top} + \mathbf {K} _ {k + 1} \mathbf {R} _ {k + 1} \mathbf {K} _ {k + 1} ^ {\top} \\ \end{array}
$$

Factor out ${ \bf K } _ { k + 1 }$ and $\mathbf { K } _ { k + 1 } ^ { \mathsf { T } }$ .

$$
\begin{array}{l} \mathbf {P} _ {k + 1} ^ {+} = \mathbf {P} _ {k + 1} ^ {-} - \mathbf {P} _ {k + 1} ^ {-} \mathbf {C} _ {k + 1} ^ {\top} \mathbf {K} _ {k + 1} ^ {\top} - \mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1} \mathbf {P} _ {k + 1} ^ {-} \\ + \mathbf {K} _ {k + 1} (\mathbf {C} _ {k + 1} \mathbf {P} _ {k + 1} ^ {-} \mathbf {C} _ {k + 1} ^ {\top} + \mathbf {R} _ {k + 1}) \mathbf {K} _ {k + 1} ^ {\top} \\ \end{array}
$$

$\mathbf { C } _ { k + 1 } \mathbf { P } _ { k + 1 } ^ { - } \mathbf { C } _ { k + 1 } ^ { \top } + \mathbf { R } _ { k + 1 }$ is the innovation (measurement residual) covariance at timestep $k + 1$ . We’ll let this expression equal $\mathbf { S } _ { k + 1 }$ . We won’t need it in the final theorem, but it makes the derivations after this point more concise.

$$\mathbf {P} _ {k + 1} ^ {+} = \mathbf {P} _ {k + 1} ^ {-} - \mathbf {P} _ {k + 1} ^ {-} \mathbf {C} _ {k + 1} ^ {\top} \mathbf {K} _ {k + 1} ^ {\top} - \mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1} \mathbf {P} _ {k + 1} ^ {-} + \mathbf {K} _ {k + 1} \mathbf {S} _ {k + 1} \mathbf {K} _ {k + 1} ^ {\top} \tag {9.19}$$

Now take the trace.

$$
\begin{array}{l} \mathrm{tr} (\mathbf {P} _ {k + 1} ^ {+}) = \mathrm{tr} (\mathbf {P} _ {k + 1} ^ {-}) - \mathrm{tr} (\mathbf {P} _ {k + 1} ^ {-} \mathbf {C} _ {k + 1} ^ {\mathsf {T}} \mathbf {K} _ {k + 1} ^ {\mathsf {T}}) - \mathrm{tr} (\mathbf {K} _ {k + 1} \mathbf {C} _ {k + 1} \mathbf {P} _ {k + 1} ^ {-}) \\ + \mathrm{tr} (\mathbf {K} _ {k + 1} \mathbf {S} _ {k + 1} \mathbf {K} _ {k + 1} ^ {\mathsf {T}}) \\ \end{array}
$$

Transpose one of the terms twice.
