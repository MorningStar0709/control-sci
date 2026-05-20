$$\frac {\delta R}{\delta V _ {R}} = \left(\frac {2 r _ {t}}{V _ {R}}\right) \left[ \frac {1 - \cos \phi}{\sin \phi - \lambda \sin \gamma \cos (\gamma - \phi)} \right], \tag {6.148}$$

and using (6.76), we obtain

$$\frac {\delta R}{\delta V _ {R}} = \left(\frac {2 r _ {t}}{V _ {R}}\right) \left\{\frac {(1 - \cos \phi) [ ((\frac {r _ {i}}{r _ {t}}) - \cos \phi) \tan \gamma + \sin \phi ]}{(1 - \cos \phi) + ((\frac {r _ {i}}{r _ {t}}) - 1) \tan \gamma \sin \phi} \right\}. \tag {6.149}$$

We may obtain a first-order approximation for (6.149) by letting

$$r _ {i} / r _ {t} \cong 1, \tag {6.150}$$

resulting in

$$\frac {\delta R}{\delta V _ {R}} = \left(\frac {2 r _ {t}}{V _ {R}}\right) [ \tan \gamma (1 - \cos \phi) + \sin \phi ]. \tag {6.151a}$$

The range error due to an error in controlling and/or measuring the flight-path angle in the trajectory plane may be computed from (6.145) and (6.146), and after making use of (6.15), we obtain, to a first-order approximation, the equation

$$\frac {\delta R}{\delta \gamma} = 2 r _ {t} \left[ 1 + \frac {\sin (\phi - 2 \gamma)}{\sin 2 \gamma} \right]. \tag {6.151b}$$

Note that at a burnout flight-path angle of $\gamma ^ { * }$ (a minimum-energy trajectory; for more details on minimum energy see Section 6.4.2.1), one may readily show by substituting (6.90) into (6.151b) that $\partial R / \partial \gamma = 0$ . Thus, if the mission does not otherwise require, the flight-path angle should be near $\gamma ^ { * }$ at burnout, so as to minimize the range error that results from $\delta \gamma$ .

Next, we consider the variation of impact range with errors in burnout altitude about the nominal design point. The variation about the nominal point can also be inferred from (6.145) and (6.146) as follows:

$$\frac {\delta R}{\delta h} = \frac {1 + (\frac {r _ {t}}{r _ {i}}) (\frac {1 - \cos \phi}{\lambda \sin^ {2} \gamma})}{\frac {\sin \phi}{\lambda \sin^ {2} \gamma} - \frac {\cos (\gamma - \phi)}{\sin \gamma}}, \tag {6.152a}$$

and using (6.76) for λ,

$$\frac {\delta R}{\delta h} = \frac {1 + (\frac {r _ {t}}{r _ {i}}) [ (\frac {r _ {i}}{r _ {t}}) - \frac {\sin (\gamma - \phi)}{\sin \gamma} ]}{\{(\frac {\sin \phi}{1 - \cos \phi}) [ (\frac {r _ {i}}{r _ {t}}) - \frac {\sin (\gamma - \phi)}{\sin \gamma} ] - \frac {\cos (\gamma - \phi)}{\sin \gamma} \}}. \tag {6.152b}$$

To first order, use (6.150) in (6.152b) to obtain the simplified expression [16]

$$\frac {\delta R}{\delta h} = 2 \tan \gamma - \frac {\sin (\gamma - \phi)}{\sin \gamma}. \tag {6.152c}$$

Consequently, since the primary effect of burnout altitude errors is to change the potential energy of the trajectory, the general form of (6.152c) should be, and is, similar to that of Eq. (6.151a), which also represents an energy change of the freeflight ellipse.
