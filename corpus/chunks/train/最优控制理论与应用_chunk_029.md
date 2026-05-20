$$
f _ {x _ {1}} ^ {\prime} \left(\boldsymbol {X} ^ {*}\right) = \frac {\partial f \left(x _ {1} , x _ {2}\right)}{\partial x _ {1}} \Bigg | _ { \begin{array}{l} x _ {1} = x _ {1} ^ {*} \\ x _ {2} = x _ {2} ^ {*} \end{array} }

f _ {x _ {2}} ^ {\prime} \left(\boldsymbol {X} ^ {*}\right) = \frac {\partial f \left(x _ {1} , x _ {2}\right)}{\partial x _ {2}} \Bigg | _ { \begin{array}{l} x _ {1} = x _ {1} ^ {*} \\ x _ {2} = x _ {2} ^ {*} \end{array} }
f _ {x _ {1} x _ {1}} ^ {\prime \prime} \left(\boldsymbol {X} ^ {*}\right) = \frac {\partial^ {2} f \left(x _ {1} , x _ {2}\right)}{\partial x _ {1} ^ {2}} \Bigg | _ {x _ {1} = x _ {1} ^ {*}} \quad f _ {x _ {1} x _ {2}} ^ {\prime \prime} \left(\boldsymbol {X} ^ {*}\right) = \frac {\partial^ {2} f \left(x _ {1} , x _ {2}\right)}{\partial x _ {1} \partial x _ {2}} \Bigg | _ {x _ {1} = x _ {1} ^ {*}}
f _ {x _ {2} x _ {2}} ^ {\prime \prime} \left(\boldsymbol {X} ^ {*}\right) = \frac {\partial^ {2} f \left(x _ {1} , x _ {2}\right)}{\partial x _ {2} ^ {2}} \Bigg | _ { \begin{array}{l} x _ {1} = x _ {1} ^ {*} \\ x _ {2} = x _ {2} ^ {*} \end{array} }
$$

$o\left[\left(\Delta x_{1}\right)^{2},\left(\Delta x_{2}\right)^{2}\right]$ 表示高阶无穷小。将式(2-4)用向量矩阵形式表示

$$
\begin{array}{l} f (\boldsymbol {X}) = f \left(x _ {1}, x _ {2}\right) = f \left(\boldsymbol {X} ^ {*}\right) + \left[ \Delta x _ {1} \quad \Delta x _ {2} \right] \left[ \begin{array}{l} f _ {x _ {1}} ^ {\prime} \\ f _ {x _ {2}} ^ {\prime} \end{array} \right] _ {\boldsymbol {X} = \boldsymbol {X} ^ {*}} + \\ \left[ \begin{array}{l l} \Delta x _ {1} & \Delta x _ {2} \end{array} \right] \left[ \begin{array}{l l} f _ {x _ {1} x _ {1}} ^ {\prime \prime} & f _ {x _ {1} x _ {2}} ^ {\prime \prime} \\ f _ {x _ {1} x _ {2}} ^ {\prime \prime} & f _ {x _ {2} x _ {2}} ^ {\prime \prime} \end{array} \right] _ {X = X ^ {*}} \left[ \begin{array}{l} \Delta x _ {1} \\ \Delta x _ {2} \end{array} \right] + o \left[ \begin{array}{l} (\Delta x _ {1}) ^ {2}, (\Delta x _ {2}) ^ {2} \end{array} \right] \\ = f \left(\boldsymbol {X} ^ {*}\right) + \Delta \boldsymbol {X} ^ {\mathrm{T}} f _ {\boldsymbol {X} ^ {*}} ^ {\prime} + \Delta \boldsymbol {X} ^ {\mathrm{T}} f _ {\boldsymbol {X}} ^ {\prime \prime} \cdot \Delta \boldsymbol {X} + o \left[ \left(\Delta x _ {1}\right) ^ {2}, \left(\Delta x _ {2}\right) ^ {2} \right] \tag {2-5} \\ \end{array}
$$

式中
