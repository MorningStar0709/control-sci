Thrust Pointing Vector: In Section 6.5.4 we discussed the thrust vector control aspect for controlling the missile during the atmospheric phase. Since the thrust works along the body-axis of the missile, the missile must be rotated to a pointing vector in the desired direction in order to change the direction of flight. The model assumes that the pointing vector and the missile body-axis are the same. This pointing vector is defined by the pitch angle resulting from the guidance phases at the current time in the flyout. The guidance phases are set up from data that describe how a particular missile pitches as a function of time. Now, if the thrust T is not zero, the maximum angle of attack α is not zero, and the gravity turn option of the current guidance phase is not selected, then the desired pitch in the launch point ENU coordinate frame at the start of the phase is

$$\theta = \theta + \theta_ {A}, \tag {6.264a}$$

and later in the phase,

$$\theta = \theta + \theta_ {R} t _ {p}, \tag {6.264b}$$

where

$$\theta = \text { current missile pitch angle } [ \text { rad } ],\theta_ {A} = \text { current guidance phase pitch angle [rad] },\theta_ {R} = \text { current guidance phase pitch rate } [ \mathrm{rad/sec} ],t _ {p} = \text { time within the current guidance phase [sec] }.$$

Azimuth is calculated in the launch ENU frame by rotating the current value of the pointing vector into the launch ENU frame as follows:

$$\psi = \tan^ {- 1} (R _ {N T x} / R _ {N T y}), \tag {6.265}$$

where

$$\psi = \text { the current missile azimuth } [ \text { rad } ],R _ {N T n} = \text { the current pointing vector in the ENU } n \text {-direction. }$$

The model uses pitch θ, azimuth ψ, and the launch site latitude and longitude angles to rotate a unit pointing vector in the body-axis frame into the ECI frame, resulting in the new pointing vector RNT .

Angle-of-Attack Limits and Gravity Turns The angle of attack α is found by the expression

$$\alpha = \cos^ {- 1} [ (\mathbf {R} _ {N T} \cdot \mathbf {V}) / (\mathbf {R} _ {N T m} \times | \mathbf {V} |) ], \tag {6.266}$$

where

$$\mathbf {R} _ {N T} = \text { current pointing vector in the } E C I \text { frame } [ \mathrm{m} ],\mathbf {R} _ {N T m} = \text { current pointing vector magnitude } [ \mathrm{m} ],\mathbf {V} = \text { current velocity vector in the } E C I [ \mathrm{m/sec} ].$$

If the angle of attack α is greater than the maximum α, then the pointing vector ${ \bf R } _ { N T }$ is recalculated so as not to exceed this maximum.
