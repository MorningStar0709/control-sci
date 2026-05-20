$$
\begin{array}{l} u (k) = - L \hat {x} (k \mid k) - L _ {v} \hat {v} (k \mid k) \\ = - L \hat {x} (k \mid k) - L _ {v} K (y (k) - C \hat {x} (k \mid k - 1)) \tag {12.42} \\ = - L _ {v} (\Phi - K C) \hat {x} (k | k - 1) - L _ {v} K y (k) \\ \end{array}
$$

where $\hat{x}(k \mid k - 1)$ is given by (12.39). The controller is still of order $n$ . Eliminating $\hat{x}$ between (12.39) and (12.42), we find that the controller can be described by the relation

$$
\begin{array}{l} u (k) = - L _ {v} (\Phi - K C) (q I - \Phi + K C) ^ {- 1} (\Gamma u (k) + K y (k)) - L _ {v} K y (k) \\ = - L _ {v} (\Phi - K C) (q I - \Phi + K C) ^ {- 1} \Gamma u (k) \\ - L _ {v} (\Phi - K C + q I - \Phi + K C) (q I - \Phi + K C) ^ {- 1} K y (k) \tag {12.43} \\ = - L _ {u} (\Phi - K C) (q I - \Phi + K C) ^ {- 1} \Gamma u (k) \\ - L _ {v} q (q I - \Phi + K C) ^ {- 1} K y (k) \\ \end{array}
$$

Introducing $R_{2}(q) = \det (qI - \Phi + KC)$ we get

$$u (k) = - \frac {R _ {1} (q)}{R _ {2} (q)} u (k) - \frac {S (q)}{R _ {2} (q)} y (k)$$

where $\deg R_1(z) = n$ , $\deg R_2(z) < n$ and $\deg S(z) = n$ with $S(0) = 0$ . Hence

$$u (k) = - \frac {S (q)}{R _ {1} (q) + R _ {2} (q)} y (k) = - \frac {S (q)}{R (q)} y (k) \tag {12.44}$$

We thus find that the controller has the property $\deg R(z) = \deg S(z) = n$ . Furthermore the condition $S(0) = 0$ implies that $\deg S^*(z) < n$ .
