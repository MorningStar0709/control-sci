$$\dot {\boldsymbol {V}} _ {M x} = \boldsymbol {a} _ {M x}, \quad \dot {\boldsymbol {V}} _ {M y} = \boldsymbol {a} _ {M y} \tag {12-39}\dot {\boldsymbol {R}} _ {M x} = \boldsymbol {V} _ {M x}, \quad \dot {\boldsymbol {R}} _ {M y} = \boldsymbol {V} _ {M y} \tag {12-40}$$

上面几式中的下标 x, y 分别表示在 x 和 y 轴上的分量。 $a_{Mx}, a_{My}$ 是导弹在地球坐标系的加速度分量。为了得到导弹的加速度分量，必须得到弹目的相对位移：

$$\boldsymbol {R} _ {T M x} = \boldsymbol {R} _ {T x} - \boldsymbol {R} _ {M x} \tag {12-41}\boldsymbol {R} _ {T M \gamma} = \boldsymbol {R} _ {T \gamma} - \boldsymbol {R} _ {M \gamma} \tag {12-42}$$

从图 12-8 中, 根据三角关系可以得到视线角

$$\boldsymbol {q} = \arctan \frac {\boldsymbol {R} _ {T M x}}{\boldsymbol {R} _ {T M y}} \tag {12-43}$$

如果定义地球坐标系的速度分量为

$$\boldsymbol {V} _ {T M x} = \boldsymbol {V} _ {T x} - \boldsymbol {V} _ {M x} \tag {12-44}\boldsymbol {V} _ {T M y} = \boldsymbol {V} _ {T y} - \boldsymbol {V} _ {M y} \tag {12-45}$$

可以根据视线角的公式求导后得到视线角速率

$$\dot {\boldsymbol {q}} = \frac {\boldsymbol {R} _ {T M y} \boldsymbol {V} _ {T M x} - \boldsymbol {R} _ {T M x} \boldsymbol {V} _ {T M y}}{\boldsymbol {R} _ {T M} ^ {2}} \tag {12-46}\boldsymbol {R} _ {T M} = \left(\boldsymbol {R} _ {T M x} ^ {2} + \boldsymbol {R} _ {T M y} ^ {2}\right) ^ {\frac {1}{2}} \tag {12-47}$$

所以不难得出弹目的接近速度为

$$\boldsymbol {V} _ {c} = - \dot {\boldsymbol {R}} _ {T M} = \frac {- \left(\boldsymbol {R} _ {T M x} \boldsymbol {V} _ {T M x} + \boldsymbol {R} _ {T M y} \boldsymbol {V} _ {T M y}\right)}{\boldsymbol {R} _ {T M}} \tag {12-48}$$

根据最优导引制导律

$$\boldsymbol {\theta} = 3 \frac {\boldsymbol {V} _ {c}}{\boldsymbol {V} _ {M}} \dot {\boldsymbol {q}} \tag {12-49}$$

可得到导弹的加速的分量为

$$\boldsymbol {\theta} = \arctan \left(\frac {\boldsymbol {V} _ {M x}}{\boldsymbol {V} _ {M y}}\right) \tag {12-50}\boldsymbol {a} _ {M x} = \boldsymbol {V} _ {M} \dot {\boldsymbol {\theta}} \cos \boldsymbol {q} \tag {12-51}\boldsymbol {a} _ {M y} = - \boldsymbol {V} _ {M} \dot {\boldsymbol {\theta}} \sin \boldsymbol {q} \tag {12-52}$$

以上列出了两维的最优导引制导的必要方程,但是使用最优导引制导的导弹并不是直接向着目标发射的,而是向着一个能够导引导弹命中目标的方向发射,考虑了视线角之后可以得到导弹的指向角 L。从图 12-8 中可以看出,如果导弹进入了碰撞三角区(如果目标和导弹同时保持匀速直线运动,导弹必定会命中目标),这时利用正弦公式可以得到指向角的表达式:

$$\boldsymbol {L} = \arcsin \frac {\boldsymbol {V} _ {T} \sin (\boldsymbol {q} - \boldsymbol {\theta} _ {T})}{\boldsymbol {V} _ {M}} \tag {12-53}$$
