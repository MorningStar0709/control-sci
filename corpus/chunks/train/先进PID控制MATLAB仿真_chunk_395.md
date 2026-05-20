$$\dot {\boldsymbol {E}} = \boldsymbol {\Lambda} \boldsymbol {E} + \boldsymbol {M}$$

则

$$
\begin{array}{l} \dot {V} _ {1} = \frac {1}{2} \dot {\boldsymbol {E}} ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {E} + \frac {1}{2} \boldsymbol {E} ^ {\mathrm{T}} \boldsymbol {P} \dot {\boldsymbol {E}} = \frac {1}{2} \left(\boldsymbol {E} ^ {\mathrm{T}} \boldsymbol {\Lambda} ^ {\mathrm{T}} + \boldsymbol {M} ^ {\mathrm{T}}\right) \boldsymbol {P} \boldsymbol {E} + \frac {1}{2} \boldsymbol {E} ^ {\mathrm{T}} \boldsymbol {P} (\boldsymbol {\Lambda} \boldsymbol {E} + \boldsymbol {M}) \\ = \frac {1}{2} \boldsymbol {E} ^ {\mathrm{T}} (\boldsymbol {A} ^ {\mathrm{T}} \boldsymbol {P} + \boldsymbol {P A}) \boldsymbol {E} + \frac {1}{2} \boldsymbol {M} ^ {\mathrm{T}} \boldsymbol {P E} + \frac {1}{2} \boldsymbol {E} ^ {\mathrm{T}} \boldsymbol {P M} \\ = - \frac {1}{2} \boldsymbol {E} ^ {\mathrm{T}} \boldsymbol {Q} \boldsymbol {E} + \frac {1}{2} \left(\boldsymbol {M} ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {E} + \boldsymbol {E} ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {M}\right) = - \frac {1}{2} \boldsymbol {E} ^ {\mathrm{T}} \boldsymbol {Q} \boldsymbol {E} + \boldsymbol {E} ^ {\mathrm{T}} \boldsymbol {P} \boldsymbol {M} \\ \end{array}
$$

将 M 代入上式，并考虑 $E^{\mathrm{T}}Pb\left(\theta_{f}-\theta_{f}^{*}\right)^{\mathrm{T}}\xi(x)=\left(\theta_{f}-\theta_{f}^{*}\right)^{\mathrm{T}}\left[E^{\mathrm{T}}Pb\xi(x)\right]$ ，得

$$
\begin{array}{l} \dot {V} _ {1} = - \frac {1}{2} E ^ {T} Q E + E ^ {T} P b \left(\theta_ {f} - \theta_ {f} ^ {*}\right) ^ {T} \xi (x) + E ^ {T} P b \omega \\ = - \frac {1}{2} E ^ {\mathrm{T}} Q E + \left(\theta_ {f} - \theta_ {f} ^ {*}\right) ^ {\mathrm{T}} E ^ {\mathrm{T}} P b \xi (x) + E ^ {\mathrm{T}} P b \omega \\ \dot {V} _ {2} = \frac {1}{\gamma} \left(\theta_ {f} - \theta_ {f} ^ {*}\right) ^ {\mathrm{T}} \dot {\theta} _ {f} \\ \end{array}
$$

V 的导数为

$$\dot {V} = \dot {V} _ {1} + \dot {V} _ {2} = - \frac {1}{2} \boldsymbol {E} ^ {\mathrm{T}} \boldsymbol {Q} \boldsymbol {E} + \boldsymbol {E} ^ {\mathrm{T}} \boldsymbol {P b} \omega + \frac {1}{\gamma} \left(\theta_ {f} - \theta_ {f} ^ {*}\right) ^ {\mathrm{T}} \left[ \dot {\theta} _ {f} + \gamma \boldsymbol {E} ^ {\mathrm{T}} \boldsymbol {P b} \xi (\boldsymbol {x}) \right]$$

将自适应律式（8.14）代入上式，得
