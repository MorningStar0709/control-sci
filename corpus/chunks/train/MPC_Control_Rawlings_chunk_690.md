$$
\begin{array}{l} \left[ \begin{array}{c} u _ {1 s} \\ u _ {2 s} \end{array} \right] ^ {p + 1} = \underbrace {\left[ \begin{array}{c c} w _ {1} G _ {1 1} ^ {- 1} & \\ & w _ {2} G _ {2 2} ^ {- 1} \end{array} \right]} _ {\overline {{K}} _ {s}} \left[ \begin{array}{c} y _ {1 s p} \\ y _ {2 s p} \end{array} \right] + \\ \underbrace {\left[ \begin{array}{c c} w _ {2} I & - w _ {1} G _ {1 1} ^ {- 1} G _ {1 2} \\ - w _ {2} G _ {2 2} ^ {- 1} G _ {2 1} & w _ {1} I \end{array} \right]} _ {L _ {s}} \left[ \begin{array}{c} u _ {1 s} \\ u _ {2 s} \end{array} \right] ^ {p} \\ \end{array}
$$

This iteration can be summarized by

$$u _ {s} ^ {p + 1} = \overline {{K}} _ {s} y _ {\mathrm{sp}} + L _ {s} u _ {s} ^ {p}$$

If $L _ { s }$ is stable, this iteration converges to

$$u _ {s} ^ {\infty} = (I - L _ {s}) ^ {- 1} \overline {{K}} _ {s} y _ {\mathrm{sp}}u _ {s} ^ {\infty} = G ^ {- 1} y _ {\mathrm{sp}}$$

and we have no offset. We already have seen that we cannot expect the dynamic noncooperative iteration to converge. The next several examples explore the issue of whether we can expect at least the steadystate iteration to be stable.

Cooperative case. In the cooperative case, both players work on minimizing the offset in both outputs. Player one solves

$$
\min _ {u _ {1}} (1 / 2) \left[ \begin{array}{c} y _ {1} - y _ {1 s p} \\ y _ {2} - y _ {2 s p} \end{array} \right] ^ {\prime} \left[ \begin{array}{c c} \rho_ {1} \overline {{Q}} _ {1} & \\ & \rho_ {2} \overline {{Q}} _ {2} \end{array} \right] \left[ \begin{array}{c} y _ {1} - y _ {1 s p} \\ y _ {2} - y _ {2 s p} \end{array} \right]

\text {s.t.} \left[ \begin{array}{c} y _ {1} \\ y _ {2} \end{array} \right] = \left[ \begin{array}{c} G _ {1 1} \\ G _ {2 1} \end{array} \right] u _ {1} + \left[ \begin{array}{c} G _ {1 2} \\ G _ {2 2} \end{array} \right] u _ {2}
$$

We can write this in the general form

$$\min _ {r _ {s}} (1 / 2) r _ {s} ^ {\prime} H r _ {s} + h ^ {\prime} r _ {s}\mathrm{s.t.} D r _ {s} = d$$

in which

$$
\begin{array}{l} r _ {s} = \left[ \begin{array}{c} y _ {1 s} \\ y _ {2 s} \\ u _ {1 s} \end{array} \right] \quad H = \left[ \begin{array}{c c c} \rho_ {1} \overline {{Q}} _ {1} & & \\ & \rho_ {2} \overline {{Q}} _ {2} & \\ & & 0 \end{array} \right] \quad h = \left[ \begin{array}{c} - Q y _ {\mathrm{sp}} \\ 0 \end{array} \right] \\ D = \left[ \begin{array}{c c} I & - G _ {1} \end{array} \right] \qquad d = G _ {2} u _ {2} \qquad G _ {1} = \left[ \begin{array}{c} G _ {1 1} \\ G _ {1 2} \end{array} \right] \qquad G _ {2} = \left[ \begin{array}{c} G _ {1 2} \\ G _ {2 2} \end{array} \right] \\ \end{array}
$$
