Assumption (A1) is necessary for the existence of stabilizing controllers. The assumptions in (A2) mean that the penalty on $z = C _ { 1 } x + D _ { 1 2 } u$ includes a nonsingular, normalized penalty on the control u, that the exogenous signal w includes both plant disturbance and sensor noise, and that the sensor noise weighting is normalized and nonsingular. Relaxation of (A2) leads to singular control problems; see Stroorvogel [1992]. For those problems that have $D _ { 1 2 }$ full column rank and $D _ { 2 1 }$ full row rank but do not satisfy assumption (A2), a normalizing procedure is given in the next section so that an equivalent new system will satisfy this assumption.

Assumptions (A3) and (A4) are made for a technical reason: Together with (A1) they guarantee that the two Hamiltonian matrices in the corresponding $\mathcal { H } _ { 2 }$ problem belong to dom(Ric), as we have seen in Chapter 13. Dropping (A3) and (A4) would make the solution very complicated. A further discussion of the assumptions and their possible relaxation will be provided in Section 14.7.

The main result is now stated in terms of the solutions of the $X _ { \infty }$ and $Y _ { \infty }$ Riccati equations together with the “state feedback” and “output injection” matrices F and L.

$$
R := D _ {1 \bullet} ^ {*} D _ {1 \bullet} - \left[ \begin{array}{c c} \gamma^ {2} I _ {m _ {1}} & 0 \\ 0 & 0 \end{array} \right], \quad \text { where } \quad D _ {1 \bullet} := [ D _ {1 1} D _ {1 2} ]

\tilde {R} := D _ {\bullet 1} D _ {\bullet 1} ^ {*} - \left[ \begin{array}{c c} \gamma^ {2} I _ {p _ {1}} & 0 \\ 0 & 0 \end{array} \right], \quad \text {where} \quad D _ {\bullet 1} := \left[ \begin{array}{c} D _ {1 1} \\ D _ {2 1} \end{array} \right]

H _ {\infty} := \left[ \begin{array}{c c} A & 0 \\ - C _ {1} ^ {*} C _ {1} & - A ^ {*} \end{array} \right] - \left[ \begin{array}{c} B \\ - C _ {1} ^ {*} D _ {1 \bullet} \end{array} \right] R ^ {- 1} \left[ \begin{array}{c c} D _ {1 \bullet} ^ {*} C _ {1} & B ^ {*} \end{array} \right]
