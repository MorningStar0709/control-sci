# pH Control

Control of pH (the concentration of hydrogen ions) is a well-known control problem that presents difficulties due to large variations in process dynamics. The problem is similar to the simple concentration control problem in Example 9.3. The main difficulty arises from a static nonlinearity between pH and concentration. This nonlinearity depends on the substances in the solution and on their concentrations.

The pH number is a measure of the concentration or, more precisely, the activity of hydrogen ions in a solution. It is defined by

$$\mathrm{pH} = - \log \left[ \mathrm{H} ^ {+} \right] \tag {9.15}$$

where $[H^{+}]$ denotes the concentration of hydrogen ions. The formula (9.15) is, strictly speaking, not correct, since $[H^{+}]$ has the dimension of concentration, which is measured in the unit M = mol/l. The correct version of Eq. (9.15) is thus $pH = -\log([H^{+}]f_{H})$ , where $f_{H}$ is a constant with the dimension liters per mole. The formula of Eq. (9.15) will be used here, however, because it is universally accepted in textbooks of chemistry.

Water molecules are dissociated (split into hydrogen and hydroxyl ions) according to the formula

$$\mathrm{H} _ {2} \mathrm{O} \rightleftharpoons \mathrm{H} ^ {+} + \mathrm{OH} ^ {-}$$

In chemical equilibrium the concentration of hydrogen $H^{+}$ (or rather $H_{3}O^{\cdot}$ ) and hydroxyl OH ions are given by the formula

$$\frac {\left[ \mathrm{H} ^ {+} \right] \left[ \mathrm{OH} ^ {-} \right]}{\left[ \mathrm{H} _ {2} \mathrm{O} \right]} = \text { constant } \tag {9.16}$$

Only a small fraction of the water molecules are split into ions. The water activity is practically unity, and we get

$$\left[ \mathrm{H} ^ {+} \right] \left[ \mathrm{OH} ^ {-} \right] = K _ {w} \tag {9.17}$$

where the equilibrium constant $K_{w}$ has the value $10^{-14}\left[(\mathrm{mol}/\mathrm{l})^{2}\right]$ at $25^{\circ}C$ . The main nonlinearity of the pH control problem will now be discussed.
