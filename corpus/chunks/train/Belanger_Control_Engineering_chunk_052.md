# Example 2.8 (Level Control)

For the level control system of Example 2.4, find the dc steady state with $\ell^{*} = \ell_{d}$ and $F_{\mathrm{in}}^{*} = F_{d}$ . Derive the incremental model.

Solution From Equation 2.30,

$$- \frac {c}{A} u ^ {*} \sqrt {\ell_ {d}} + \frac {F _ {d}}{A} = 0$$

or

$$u ^ {*} = \frac {F _ {d}}{c \sqrt {\ell_ {d}}}$$

As for the incremental model, with $f$ being the RHS of Equation (2.30),

$$\frac {\partial f}{\partial \ell} = - \frac {c}{2 A} \frac {u}{\sqrt {\ell}}; \quad \frac {\partial f}{\partial u} = - \frac {c}{A} \sqrt {\ell}; \quad \frac {\partial f}{\partial F _ {\mathrm{in}}} = \frac {1}{A}$$

so that

$$\dot {\Delta} \ell = - \frac {c u ^ {*}}{2 A \sqrt {\ell_ {d}}} \Delta \ell - \frac {c}{A} \sqrt {\ell_ {d}} \Delta u + \frac {1}{A} \Delta F _ {\mathrm{in}}.$$
