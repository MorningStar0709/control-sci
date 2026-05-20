# Root Locus

The root-locus method is a classical technique for the design of control systems. The method is based on the idea of attempting to place the closed-loop poles in desired positions. Thus it is closely related to pole placement. In this method, polynomials R and S are first chosen as R = 1 and S = K, which correspond to proportional control. The gain K is then changed and the roots of the characteristic equation

$$\boldsymbol {A} + \boldsymbol {K B} = 0$$

are investigated. The roots of this equation can easily be sketched for varying K. If a reasonable pole placement cannot be obtained, the orders of the polynomials R and S are increased using heuristic rules. The procedure is then repeated.

The root-locus method can clearly be regarded as a pole placement technique. By applying pole placement the complexity of the controller required to position all poles can be found directly. With pole placement all poles are positioned in one operation. The complexity of the controller is determined by the complexity of the process model used in the design.
