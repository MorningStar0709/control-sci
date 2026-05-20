$$
\left[ \begin{array}{c c} A & B C _ {i} \\ 0 & A _ {i} \end{array} \right] \left[ \begin{array}{c c} P & P _ {1 2} \\ P _ {1 2} ^ {*} & P _ {2 2} \end{array} \right] + \left[ \begin{array}{c c} P & P _ {1 2} \\ P _ {1 2} ^ {*} & P _ {2 2} \end{array} \right] \left[ \begin{array}{c c} A & B C _ {i} \\ 0 & A _ {i} \end{array} \right] ^ {*} + \left[ \begin{array}{c} B D _ {i} \\ B _ {i} \end{array} \right] \left[ \begin{array}{c} B D _ {i} \\ B _ {i} \end{array} \right] ^ {*} = 0 \tag {7.19}

\left[ \begin{array}{c c} Q & Q _ {1 2} \\ Q _ {1 2} ^ {*} & Q _ {2 2} \end{array} \right] \left[ \begin{array}{c c} A & 0 \\ B _ {o} C & A _ {o} \end{array} \right] + \left[ \begin{array}{c c} A & 0 \\ B _ {o} C & A _ {o} \end{array} \right] ^ {*} \left[ \begin{array}{c c} Q & Q _ {1 2} \\ Q _ {1 2} ^ {*} & Q _ {2 2} \end{array} \right] + \left[ \begin{array}{c} C ^ {*} D _ {o} ^ {*} \\ C _ {o} ^ {*} \end{array} \right] \left[ \begin{array}{c} C ^ {*} D _ {o} ^ {*} \\ C _ {o} ^ {*} \end{array} \right] ^ {*} = 0 \tag {7.20}
$$

The computation can be further reduced if $W _ { i } = I \mathrm { o r } W _ { o } = I$ . In the case of $W _ { i } = I ,$ $P$ can be obtained from

$$P A ^ {*} + A P + B B ^ {*} = 0 \tag {7.21}$$

while in the case of $W _ { o } = I , Q$ can be obtained from

$$Q A + A ^ {*} Q + C ^ {*} C = 0 \tag {7.22}$$

Now let T be a nonsingular matrix such that

$$
T P T ^ {*} = (T ^ {- 1}) ^ {*} Q T ^ {- 1} = \left[ \begin{array}{c c} \Sigma_ {1} & \\ & \Sigma_ {2} \end{array} \right]
$$

(i.e., balanced) with $\Sigma _ { 1 } = \mathrm { d i a g } ( \sigma _ { 1 } I _ { s _ { 1 } } , . . . , \sigma _ { r } I _ { s _ { r } } )$ and $\Sigma _ { 2 } = \mathrm { d i a g } ( \sigma _ { r + 1 } I _ { s _ { r + 1 } } , \dots , \sigma _ { N } I _ { s _ { N } } )$ and partition the system accordingly as

$$
\left[ \begin{array}{c c} T A T ^ {- 1} & T B \\ \hline C T ^ {- 1} & 0 \end{array} \right] = \left[ \begin{array}{c c c} A _ {1 1} & A _ {1 2} & B _ {1} \\ A _ {2 1} & A _ {2 2} & B _ {2} \\ \hline C _ {1} & C _ {2} & 0 \end{array} \right]
$$

Then a reduced-order model $G _ { r }$ is obtained as

$$
G _ {r} = \left[ \begin{array}{c c} A _ {1 1} & B _ {1} \\ \hline C _ {1} & 0 \end{array} \right]
$$

Unfortunately, there is generally no known a priori error bound for the approximation error and the reduced-order model $G _ { r }$ is not guaranteed to be stable either.

A very special frequency-weighted model reduction problem is the relative error model reduction problem where the objective is to find a reduced-order model $G _ { r }$ so that

$$G _ {r} = G (I + \Delta_ {\mathrm{rel}})$$
