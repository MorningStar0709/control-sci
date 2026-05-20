$$
T = \left[ \begin{array}{c c c} I / 2 & I / 2 & 0 \\ I / 2 & - I / 2 & 0 \\ 0 & 0 & I \end{array} \right], \quad T ^ {- 1} = \left[ \begin{array}{c c c} I & I & 0 \\ I & - I & 0 \\ 0 & 0 & I \end{array} \right]
$$

to get

$$
E _ {1 1} = \left[ \begin{array}{c c c c} A _ {1 1} & 0 & A _ {1 2} / 2 & B _ {1} \\ 0 & A _ {1 1} & - A _ {1 2} / 2 & 0 \\ A _ {2 1} & - A _ {2 1} & A _ {2 2} & B _ {2} \\ \hline 0 & - 2 C _ {1} & C _ {2} & 0 \end{array} \right]
$$

Consider a dilation of $E _ { 1 1 } ( s )$ :

$$
\begin{array}{l} \begin{array}{r l r} {E (s)} & = & {\left[ \begin{array}{l l} E _ {1 1} (s) & E _ {1 2} (s) \\ E _ {2 1} (s) & E _ {2 2} (s) \end{array} \right]} \end{array} \\ = \left[ \begin{array}{c c c c c} A _ {1 1} & 0 & A _ {1 2} / 2 & B _ {1} & 0 \\ 0 & A _ {1 1} & - A _ {1 2} / 2 & 0 & \sigma_ {N} \Sigma_ {1} ^ {- 1} C _ {1} ^ {*} \\ A _ {2 1} & - A _ {2 1} & A _ {2 2} & B _ {2} & - C _ {2} ^ {*} \\ \hline 0 & - 2 C _ {1} & C _ {2} & 0 & 2 \sigma_ {N} I \\ - 2 \sigma_ {N} B _ {1} ^ {*} \Sigma_ {1} ^ {- 1} & 0 & - B _ {2} ^ {*} & 2 \sigma_ {N} I & 0 \end{array} \right] \\ =: \quad \left[ \begin{array}{c c} \tilde {A} & \tilde {B} \\ \hline \tilde {C} & \tilde {D} \end{array} \right] \\ \end{array}
$$

Then it is easy to verify that

$$
\tilde {P} = \left[ \begin{array}{c c c} {\Sigma_ {1}} & 0 & \\ {0} & {\sigma_ {N} ^ {2} \Sigma_ {1} ^ {- 1}} & 0 \\ {0} & 0 & {2 \sigma_ {N} I _ {s _ {N}}} \end{array} \right]
$$

satisfies

$$
\begin{array}{l} \tilde {A} \tilde {P} + \tilde {P} \tilde {A} ^ {*} + \tilde {B} \tilde {B} ^ {*} = 0 \\ \tilde {P} \tilde {C} ^ {*} + \tilde {B} \tilde {D} ^ {*} = 0 \\ \end{array}
$$

Using these two equations, we have

$$
\begin{array}{l} \begin{array}{r l r} {E (s) E ^ {\sim} (s)} & = & {\left[ \begin{array}{c c c} \tilde {A} & - \tilde {B} \tilde {B} ^ {*} & \tilde {B} \tilde {D} ^ {*} \\ 0 & - \tilde {A} ^ {*} & \tilde {C} ^ {*} \\ \hline \tilde {C} & - \tilde {D} \tilde {B} ^ {*} & \tilde {D} \tilde {D} ^ {*} \end{array} \right]} \end{array} \\ = \left[ \begin{array}{c c c} \tilde {A} & - \tilde {A} \tilde {P} - \tilde {P} \tilde {A} ^ {*} - \tilde {B} \tilde {B} ^ {*} & \tilde {P} \tilde {C} ^ {*} + \tilde {B} \tilde {D} ^ {*} \\ 0 & - \tilde {A} ^ {*} & \tilde {C} ^ {*} \\ \hline \tilde {C} & - \tilde {C} \tilde {P} - \tilde {D} \tilde {B} ^ {*} & \tilde {D} \tilde {D} ^ {*} \end{array} \right] \\ = \left[ \begin{array}{c c c} \tilde {A} & 0 & 0 \\ 0 & - \tilde {A} ^ {*} & \tilde {C} ^ {*} \\ \hline \tilde {C} & 0 & \tilde {D} \tilde {D} ^ {*} \end{array} \right] \\ { = } { \tilde { D } \tilde { D } ^ { * } = 4 \sigma _ { N } ^ { 2 } I } \\ \end{array}
$$

where the second equality is obtained by applying a similarity transformation
