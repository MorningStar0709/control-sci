$$x _ {t} = \Phi_ {t, 0} \left(x _ {0} + \int_ {0} ^ {t} \Phi_ {0, s} D _ {s} \mathrm{d} w _ {s}\right).$$

记

$$H _ {t} = \Phi_ {t, 0} - \int_ {0} ^ {t} G _ {1} (t) G _ {2} (\lambda) C _ {\lambda} \Phi_ {\lambda , 0} \mathrm{d} \lambda ,$$

那么

$$
\begin{array}{l} \hat {x} _ {t} ^ {G} = c _ {t} + G _ {0} (t) y _ {0} + G _ {1} (t) \int_ {0} ^ {t} G _ {2} (s) F _ {s} d w _ {s} \\ + G _ {1} (t) \int_ {0} ^ {t} G _ {2} (s) C _ {s} \Phi_ {s, 0} \left(x _ {0} + \int_ {0} ^ {s} \Phi_ {0, \lambda} D _ {\lambda} d w _ {\lambda}\right) d s \\ = c _ {t} + G _ {0} (t) y _ {0} + G _ {1} (t) \int_ {0} ^ {t} G _ {2} (s) F _ {s} d w _ {s} + G _ {1} (t) \int_ {0} ^ {t} G _ {2} (s) C _ {s} \Phi_ {s, 0} d s x _ {0} \\ + G _ {1} (s) \int_ {0} ^ {t} \int_ {\lambda} ^ {t} G _ {2} (s) C _ {s} \Phi_ {s, 0} d s \Phi_ {0, \lambda} D _ {\lambda} d w _ {\lambda}, \\ \end{array}
$$

所以

$$
\begin{array}{l} x _ {t} - \hat {x} _ {t} ^ {G} = H _ {t} \left(x _ {0} + \int_ {0} ^ {t} \Phi_ {0, t} D _ {s} \mathrm{d} w _ {s}\right) + G _ {1} (t) \int_ {0} ^ {t} \int_ {0} ^ {\lambda} G _ {2} (s) C _ {s} \Phi_ {s, 0} \mathrm{d} s \Phi_ {0, \lambda} D _ {\lambda} \mathrm{d} w _ {\lambda} \\ - c _ {t} - G _ {0} (t) y _ {0} - G _ {1} (t) \int_ {0} ^ {t} G _ {2} (s) F _ {s} \mathrm{d} w _ {s}. \tag {4.4.60} \\ \end{array}
$$

记

$$L _ {s} ^ {\mathbf {T}} = \left(G _ {1} (t) \int_ {0} ^ {s} G _ {2} (s) C _ {\lambda} \Phi_ {\lambda , 0} \mathrm{d} \lambda + H _ {t}\right) \Phi_ {0, s}, \tag {4.4.61}$$

取微分后得

$$\frac {\mathrm{d}}{\mathrm{d} s} L _ {s} ^ {\mathrm{T}} = - L _ {s} ^ {\mathrm{T}} A _ {s} + G _ {1} (t) G _ {2} (s) C _ {s}, \quad L _ {t} ^ {\mathrm{T}} = I, \quad L _ {0} ^ {\mathrm{T}} = H _ {t}.$$

从式 (4.4.60) 及式 (4.4.61) 知

$$x _ {t} - \hat {x} _ {t} ^ {G} = H _ {t} x _ {0} - c _ {t} - G _ {0} (t) y _ {0} + \int_ {0} ^ {t} L _ {s} ^ {\mathrm{T}} D _ {s} \mathrm{d} w _ {s} - \int_ {0} ^ {t} G _ {1} (t) G _ {2} (s) F _ {s} \mathrm{d} w _ {s}.$$

注意到 $Ew_{t}x_{0}^{\mathrm{T}} = 0, Ew_{t}y_{0}^{\mathrm{T}} = 0,$ 由式(4.3.17)知

$$
\begin{array}{l} E (x _ {t} - \hat {x} _ {t} ^ {G}) (x _ {t} - \hat {x} _ {t} ^ {G}) ^ {\mathbf {T}} \\ = E \left(H _ {t} x _ {0} - c _ {t} - G _ {0} (t) y _ {0}\right) \left(H _ {t} x _ {0} - x _ {t} - G _ {0} (t) y _ {0}\right) ^ {\mathrm{T}} \\ + \int_ {0} ^ {t} [ L _ {s} ^ {\mathrm{T}} D _ {s} - G _ {1} (t) G _ {2} (s) F _ {s} ] [ L _ {s} ^ {\mathrm{T}} D _ {s} - G _ {1} (t) G _ {2} (s) F _ {s} ] ^ {\mathrm{T}} \mathrm{d} s. \tag {4.4.62} \\ \end{array}
$$

从式 (4.4.59) 及式 (4.4.61) 知
