$$
\begin{array}{l} \frac {1}{2} \mathbf {u} ^ {* \prime} (t) \mathbf {R} (t) \mathbf {u} ^ {*} (t) + \boldsymbol {\lambda} ^ {* \prime} (t) \mathbf {A} (t) \mathbf {x} ^ {*} (t) + \boldsymbol {\lambda} ^ {* \prime} (t) \mathbf {B} (t) \mathbf {u} ^ {*} (t) \\ \leq \frac {1}{2} \mathbf {u} ^ {\prime} (t) \mathbf {R} (t) \mathbf {u} (t) + \boldsymbol {\lambda} ^ {* \prime} (t) \mathbf {A} (t) \mathbf {x} ^ {*} (t) + \boldsymbol {\lambda} ^ {* \prime} (t) \mathbf {B} (t) \mathbf {u} (t) \tag {7.5.10} \\ \end{array}
$$

which becomes

$$
\begin{array}{l} \frac {1}{2} \mathbf {u} ^ {* \prime} (t) \mathbf {R} (t) \mathbf {u} ^ {*} (t) + \boldsymbol {\lambda} ^ {* \prime} (t) \mathbf {B} (t) \mathbf {u} ^ {*} (t) \\ \leq \frac {1}{2} \mathbf {u} ^ {\prime} (t) \mathbf {R} (t) \mathbf {u} (t) + \boldsymbol {\lambda} ^ {* \prime} (t) \mathbf {B} (t) \mathbf {u} (t) \\ = \min _ {| \mathbf {u} ^ {\prime} (t) | \leq 1} \left\{\frac {1}{2} \mathbf {u} ^ {\prime} (t) \mathbf {R} (t) \mathbf {u} (t) + \boldsymbol {\lambda} ^ {* \prime} (t) \mathbf {B} (t) \mathbf {u} (t) \right\}. \tag {7.5.11} \\ \end{array}
$$

\- Step 4: Optimal Control: Let us denote

$$\mathbf {q} ^ {*} (t) = \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \boldsymbol {\lambda} ^ {*} (t) \tag {7.5.12}$$

and write

$$\boldsymbol {\lambda} ^ {* \prime} (t) \mathbf {B} (t) \mathbf {u} ^ {*} (t) = \mathbf {u} ^ {* \prime} (t) \mathbf {B} ^ {\prime} (t) \boldsymbol {\lambda} ^ {*} (t) = \mathbf {u} ^ {* \prime} (t) \mathbf {R} (t) \mathbf {q} ^ {*} (t). \tag {7.5.13}$$

Using (7.5.12) and (7.5.13) in (7.5.11), we get

$$
\begin{array}{l} \frac {1}{2} \mathbf {u} ^ {* \prime} (t) \mathbf {R} (t) \mathbf {u} ^ {*} (t) + \mathbf {u} ^ {* \prime} (t) \mathbf {R} (t) \mathbf {q} ^ {*} (t) \\ \leq \frac {1}{2} \mathbf {u} ^ {\prime} (t) \mathbf {R} (t) \mathbf {u} (t) + \mathbf {u} ^ {\prime} (t) \mathbf {R} (t) \mathbf {q} ^ {*} (t). \tag {7.5.14} \\ \end{array}
$$

Now, adding

$$\frac {1}{2} \mathbf {q} ^ {* \prime} (t) \mathbf {R} (t) \mathbf {q} ^ {*} (t) = \frac {1}{2} \boldsymbol {\lambda} ^ {* \prime} (t) \mathbf {B} (t) \mathbf {R} ^ {- 1} (t) \mathbf {B} ^ {\prime} (t) \boldsymbol {\lambda} ^ {*} (t) \tag {7.5.15}$$

to both sides of (7.5.14), we get
