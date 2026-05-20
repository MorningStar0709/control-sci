# ■ Theorem 3.6

An LTI system is internally stable if, and only if, all eigenvalues of A lie in the open left-half plane.

Proof: The words "open left-half plane" exclude the imaginary axis, i.e., refer to $Re(s) < 0$ .

The terms of the zero-input solution $\mathbf{x}_{zi}(t)$ are of the form $t^{k}e^{s_{i}t}$ , where the $s_{i}$ are the eigenvalues of A. If all eigenvalues have negative real parts, then all terms of $x_{zi}$ tend to zero; this shows sufficiency.

If one eigenvalue of $A$ , say $s_1$ , is such that $Res_1 \geq 0$ , we show that the system is not internally stable with the following argument. Let $\mathbf{v}_1$ be an eigenvector corresponding to $s_1$ . If the initial state is $\mathbf{v}_1$ , then $\mathbf{x}_{zi}(t) = \mathbf{v}_1 e^{s_1 t}$ . Since $Res_1 \geq 0$ , $\mathbf{x}_{zi}$ does not tend to zero; this establishes necessity.

We call eigenvalues of A with negative real parts stable modes, and those with real parts that are positive or zero, unstable modes. The test of internal stability is simply to check that all modes are stable.

The concept of input-output stability is concerned with the boundedness of the zero-state output in response to bounded inputs.
