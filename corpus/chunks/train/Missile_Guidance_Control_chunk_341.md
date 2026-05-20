A general representative mathematical expression for the performance measure of a control system objective covering all the above cases is

$$J (u) = h [ x (t _ {f}), t _ {f} ] + \int_ {t _ {0}} ^ {t _ {f}} g [ x (t), u (t), t ] d t, \tag {4.143}$$

where $t _ { 0 }$ is the initial time, $t _ { f }$ is the final time, h is a scalar-valued function of terminal time and the states, and g is a scalar-valued function of the states, controls, and time defined in the entire interval $[ t _ { 0 } , t _ { f } ]$ . The performance measure for a missile control problem is (4.137), or it may take the form

$$J (u) = [ x (t _ {f}) - d (t _ {f}) ] ^ {T} H [ x (t _ {f}) - d (t _ {f}) ] + \int_ {t _ {0}} ^ {t _ {f}} d t, \tag {4.144}$$

with $d ( t _ { f } )$ representing the specified target point. Then in the above objective function (4.144), the first quadratic term indicates the weighted deviations of the final states of the missile from the target (i.e., miss distance), and the second integral indicates the time of flight. The elements of the positive semidefinite weighting matrix H can be selected so as to reflect the relative importance between the two terms $( H = 0$ gives a strict minimal-time optimal control problem).
