# 4.5 Proportional Navigation

Perhaps the most widely known and used guidance law for short- to medium-range homing missiles is proportional navigation (PN), because of its inherent simplicity and ease of implementation. Simply stated, classical proportional navigation guidance is based on recognition of the fact that if two bodies are closing on each other, they will eventually intercept if the line of sight (LOS) between the two does not rotate relative to the inertial space. More specifically, the PN guidance law seeks to null the LOS rate against nonmaneuvering targets by making the interceptor missile heading proportional to the LOS rate. For instance, in flying a proportional navigation course, the missile attempts to null out any line-of-sight rate that may be developing. The missile does this by commanding wing deflections to the control surfaces. Consequently, these deflections cause the missile to execute accelerations normal to its instantaneous velocity vector. Thus, the missile commands g’s to null out measured LOS rate. As will be developed in the discussion that follows, this relation can be expressed as follows:

$$a _ {n} = N V _ {c} \left(\frac {d \lambda}{d t}\right), \tag {4.24}$$

where

$$
a _ {n} = \text { the commanded normal (or lateral) acceleration [ft / sec } ^ {2} ] \text { or [m / sec } ^ {2} ],
\begin{array}{l} N = \text { the   navigation   constant   (also   known   as   navigation   ratio, } \\ \quad \text { effective   navigation   ratio,   and   navigation   gain), a positive } \\ \quad \text { real   number   [dimensionless], } \end{array}
V _ {c} = \text { the closing velocity [ft / sec] or [m / sec]},\frac {d \lambda}{d t} = \text { the LOS rate measured by the missile seeker [rad / sec] }.
$$

The proportionality factor consists of the navigation constant, closing velocity multiplier, and a geometric gain factor that accounts for the fact that the orientation of the missile velocity is not necessarily along the instantaneous LOS. The navigation constant (N ) is based on the missile’s acceleration requirements and will vary depending on target maneuvers and other system-induced tracking-error sources. In order to minimize the missile acceleration requirement, values of N between 3 and

5 are usually used to obtain an acceptable miss distance intercept. Note that for most applications, the effective navigation ratio is restricted to integer values.
