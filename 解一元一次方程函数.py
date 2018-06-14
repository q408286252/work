#只能解一元一次方程  它把变量换算成虚数然后
def solve(eq,variable='x'): #variable 变量
  eq1 = eq.replace("=","-(") + ")" #吧'=' 换成'-(' 字符尾部加')'
  c = eval(eq1,{variable:1j})  #变量变为1单位虚数
  return -c.real/c.imag  #-实数值/虚数值 = x值
