$$
\tilde {\delta} _ {r} ^ {- 1} := \inf _ {K _ {2}} \left\| \left[ \begin{array}{c} K _ {2} \\ I \end{array} \right] (I + G _ {r} K _ {2}) ^ {- 1} \tilde {M} _ {r} ^ {- 1} \right\| _ {\infty} \leq (\delta - \epsilon) ^ {- 1}.
$$

(f) With the controller $K _ { 2 }$ given in (e), show that

$$
\begin{array}{l} \left\| \left[ \begin{array}{c} K _ {2} \\ I \end{array} \right] (I + G K _ {2}) ^ {- 1} \tilde {M} ^ {- 1} \right\| _ {\infty} = \left\| \left[ \begin{array}{c} K _ {2} \\ I \end{array} \right] (I + G K _ {2}) ^ {- 1} \left[ \begin{array}{c c} I & G \end{array} \right] \right\| _ {\infty} \\ \leq \left(\tilde {\delta} _ {r} - \epsilon\right) ^ {- 1} \leq (\delta - 2 \epsilon) ^ {- 1}. \\ \end{array}
$$

Again note that if $\tilde { N } _ { r }$ r and $\tilde { M _ { \eta } }$ r are the kth-order balanced truncation of $\tilde { N }$ and $\tilde { M }$ , then $\tilde { \delta } _ { r } = \delta$ .

(Note that $K _ { 1 }$ and $K _ { 2 }$ are reduced-order controllers.)

Problem 16.13 Let $G ( s ) = \left[ \frac { A \ : \left| \ : B \right. } { C \ : \left| \ : 0 \right. } \right] = \tilde { M } ^ { - 1 } \tilde { N }$ be a normalized left coprime factorization and let $K ( s )$ be a suboptimal controller given in Corollary 18.2 (with performance γ):

$$
K (s) = \left[ \begin{array}{c c} A - B B ^ {*} X _ {\infty} - Y C ^ {*} C & - Y C ^ {*} \\ \hline - B ^ {*} X _ {\infty} & 0 \end{array} \right]
$$

where

$$X _ {\infty} = \frac {\gamma^ {2}}{\gamma^ {2} - 1} Q \left(I - \frac {\gamma^ {2}}{\gamma^ {2} - 1} Y Q\right) ^ {- 1}$$

and

$$A Y + Y A ^ {*} - Y C ^ {*} C Y + B B ^ {*} = 0Q (A - Y C ^ {*} C) + (A - Y C ^ {*} C) ^ {*} Q + C ^ {*} C = 0.$$

Suppose Y and $Q$ are balanced; that is,

$$Y = Q = \operatorname{diag} (\sigma_ {1}, \dots , \sigma_ {r}, \sigma_ {r + 1}, \dots , \sigma_ {n}) = \operatorname{diag} (\Sigma_ {1}, \Sigma_ {2})$$

and let G(s) be partitioned accordingly as

$$
G (s) = \left[ \begin{array}{c c c} A _ {1 1} & A _ {1 2} & B _ {1} \\ A _ {2 1} & A _ {2 2} & B _ {2} \\ \hline C _ {1} & C _ {2} & 0 \end{array} \right].
$$

Denote $Y _ { 1 } = \Sigma _ { 1 }$ and $\begin{array} { r } { X _ { 1 } = \frac { \gamma ^ { 2 } } { \gamma ^ { 2 } - 1 } \Sigma _ { 1 } \left( I - \frac { \gamma ^ { 2 } } { \gamma ^ { 2 } - 1 } \Sigma _ { 1 } ^ { 2 } \right) ^ { - 1 } } \end{array}$ . Show that

$$
K _ {r} (s) = \left[ \begin{array}{c c} A _ {1 1} - B _ {1} B _ {1} ^ {*} X _ {1} - Y _ {1} C _ {1} ^ {*} C _ {1} & - Y _ {1} C _ {1} ^ {*} \\ \hline - B _ {1} ^ {*} X _ {1} & 0 \end{array} \right]
$$

is exactly the reduced-order controller obtained from the last problem with balanced model reduction procedure. (It is also interesting to note that
