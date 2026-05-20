The state model, using the extended Kalman filter algorithm, can be formulated in the usual way as follows:

$$\delta \mathbf {x} _ {k + 1} = \Phi \delta \mathbf {x} _ {k} + w _ {k},E \{w _ {k} \} = 0,E \{w _ {k} w _ {k} ^ {T} \} = Q _ {k} \delta_ {k j},$$

and the measurement

$$c _ {k} = c \left(\mathbf {x} _ {k}\right) + v _ {k} = z _ {k} - h (.,.) + v _ {k},E \left\{v _ {k} \right\} = 0,E \{v _ {k} v _ {k} ^ {T} \} = R _ {k} \delta_ {k j},$$

where

$$
\begin{array}{l} \delta \mathbf {x} _ {k} = I N S \text {   error   states   to   be   estimated }, \\ \Phi = \text { state - transition   matrix   for   INS   errors }, \\ \mathbf {x} _ {k} = \text { states   of   INS   and   aircraft }, \\ c _ {k} = \text { ground   clearance   measurement }, \\ z _ {k} = \text { altitude   of   aircraft }, \\ h = \text { height   of   terrain   at   position } (.,.), \\ w _ {k} = \text { system   driving   noise }, \\ v _ {k} = \text { measurement   noise   error }, \\ k = \text { subscript   denoting   time }, \\ \begin{array}{l} Q _ {k} = \text { an } r \times r \text { matrix   known   as   the   covariance   matrix   of   the   state   model } \\ \text { uncertainties   (or   system   noise   strength) }, \end{array} \\ \begin{array}{l} R _ {k} = \text { an } m \times m \text { matrix   known   as   the   covariance   matrix   of   the   observation } \\ \text { noise   (also   called   measurement   noise   strength) }. \end{array} \\ \end{array}
$$

At any time k,

$$\mathbf {x} = \mathbf {x} _ {I N S} + \delta \mathbf {x},\delta \mathbf {x} = [ \delta x \delta y \delta z \delta v _ {x} \delta v _ {y} ] ^ {T},$$

where $\delta x , \delta y , \delta z , \delta v _ { x }$ , and $\delta v _ { y }$ are the errors in the x-position, y-position, altitude, x velocity, and y velocity, respectively. (Note that other INS error states can also be included in δx.)

We close this section by noting that TERCOM is also finding use in commercial aviation. More specifically, the Boeing Company recently outfitted a 737–900 with new cockpit technology that includes a situation display showing the aircraft’s vertical profile compared with stored terrain data. Boeing plans to demonstrate this new technology to the airlines.
