THEOREM 2.3 INVARIANCE OF PULSE RESPONSE The pulse response (2.20) is invariant with respect to coordinate transformations of the state-space model.

Proof. Introduce new coordinates $z = Tx$ . The pulse response of the transformed system is then, for $k \geq 1$ ,

$$
\begin{array}{l} \tilde {h} (k) = \tilde {C} \tilde {\Phi} ^ {k - 1} \tilde {\Gamma} = C T ^ {- 1} \left(T \Phi T ^ {- 1}\right) ^ {k - 1} T \Gamma \\ = C T ^ {- 1} T \Phi^ {k - 1} T ^ {- 1} T \Gamma = C \Phi^ {k - 1} \Gamma = h (k) \\ \end{array}
$$

$\tilde{D} = D$ has to be added for $k = 0$ .

If $h(k) \neq 0$ for only a finite number of k, then the system is called a finite impulse-response (FIR) system. This implies that the output only will be influenced by a finite number of inputs.
