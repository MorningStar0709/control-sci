$$
\begin{array}{l} P _ {t} = L _ {t} ^ {\mathrm{T}} P _ {t} L _ {t} = L _ {0} ^ {\mathrm{T}} R _ {0} L _ {0} + \int_ {0} ^ {t} \mathrm{d} \left(L _ {s} ^ {\mathrm{T}} P _ {s} L _ {s}\right) \\ = H _ {t} R _ {0} H _ {t} ^ {\mathrm{T}} + \int_ {0} ^ {t} \left[ \left(G _ {1} (t) G _ {2} (s) C _ {s} - L _ {s} ^ {\mathrm{T}} A _ {s}\right) P _ {s} L _ {s} \right. \\ + L _ {s} ^ {\mathrm{T}} P _ {s} \left(C _ {s} ^ {\mathrm{T}} G _ {2} ^ {\mathrm{T}} (s) G _ {1} ^ {\mathrm{T}} (t) - A _ {s} ^ {\mathrm{T}} L _ {s}\right) + L _ {s} ^ {\mathrm{T}} \left(P _ {s} A _ {s} ^ {\mathrm{T}} + A _ {s} P _ {s} + D _ {s} D _ {s} ^ {\mathrm{T}} \right. \\ - \left(D _ {s} F _ {s} ^ {\mathrm{T}} + P _ {s} C _ {s} ^ {\mathrm{T}}\right) \left(F _ {s} F _ {s} ^ {\mathrm{T}}\right) ^ {- 1} \left(D _ {s} F _ {s} ^ {\mathrm{T}} + P _ {s} C _ {s} ^ {\mathrm{T}}\right) ^ {\mathrm{T}} L _ {s} ] \mathrm{d} s \\ = L _ {0} ^ {\mathrm{T}} R _ {0} L _ {0} - \int_ {0} ^ {t} \left[ G _ {1} (t) G _ {2} (s) - L _ {s} ^ {\mathrm{T}} \left(D _ {s} F _ {s} ^ {\mathrm{T}} + P _ {s} C _ {s} ^ {\mathrm{T}}\right) \left(F _ {s} F _ {s} ^ {\mathrm{T}}\right) ^ {- 1} \right] \\ \cdot F _ {s} F _ {s} ^ {\mathrm{T}} \left[ G _ {1} (t) G _ {2} (s) - L _ {s} ^ {\mathrm{T}} \left(D _ {s} F _ {s} ^ {\mathrm{T}} + P _ {s} C _ {s} ^ {\mathrm{T}}\right) \left(F _ {s} F _ {s} ^ {\mathrm{T}}\right) ^ {- 1} \right] ^ {\mathrm{T}} \mathrm{d} s \\ + \int_ {0} ^ {t} \left[ L _ {s} ^ {\mathrm{T}} D _ {s} - G _ {1} (t) G _ {2} (s) F _ {s} \right] \left[ L _ {s} ^ {\mathrm{T}} D _ {s} - G _ {1} (t) G _ {2} (s) F _ {s} \right] ^ {\mathrm{T}} \mathrm{d} s. \tag {4.4.63} \\ \end{array}
$$

由于 $E(x_0 - \hat{x}_0)y_0^{\mathrm{T}} = 0$ ， $E(x_0 - \hat{x}_0)\hat{x}_0^{\mathrm{T}} = 0$ ，所以

$$
\begin{array}{l} E \left(H _ {t} x _ {0} - c _ {t} - G _ {0} (t) y _ {0}\right) \left(H _ {t} x _ {0} - c _ {t} - G _ {0} (t) y _ {0}\right) ^ {\mathrm{T}} \\ = H _ {t} R _ {0} H _ {t} ^ {\mathrm{T}} + E \left(H _ {t} \hat {x} _ {0} - c _ {t} - G _ {0} (t) y _ {0}\right) \left(H _ {t} \hat {x} _ {0} - c _ {t} - G _ {0} (t) y _ {0}\right) ^ {\mathrm{T}}. \tag {4.4.64} \\ \end{array}
$$

归并式 (4.4.62)\~(4.4.64) 便知
