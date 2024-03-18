import numpy as np
import matplotlib.pyplot as plt
def solve_ivp(func, t_span, y0, method, t_eval, args):
    t=np.linspace(t_span[0],t_span[1],int((t_span[1]-t_span[0])/t_eval))
    def RK2(func, y0, t_eval,args):
        dt=t_eval
        lenth=len(y0)
        y=[np.zeros(len(t)) for i in range(lenth)]
        for k in range(len(y0)):
            y[k][0]=y0[k]
        for i in range(len(t)-1):
            k1=func(y[0][i],y[1][i],args)
            k2=func(y[0][i]+dt*k1[0],y[1][i]+dt*k1[1],args)
            y[0][i+1]=y[0][i]+dt*(k2[0]+k1[0])/2    
            y[1][i+1]=y[1][i]+dt*(k2[1]+k1[1])/2
        return y[0],y[1],t
    def euler(func, y0, t_eval,args):
        dt=t_eval
        lenth=len(y0)
        y=[np.zeros(len(t)) for i in range(lenth)]
        for k in range(len(y0)):
            y[k][0]=y0[k]
        for i in range(len(t)-1):
            k1=func(y[0][i],y[1][i],args)
            y[0][i+1]=y[0][i]+dt*k1[0]
            y[1][i+1]=y[1][i]+dt*k1[1]
        return y[0],y[1],t
    def RK4(func, y0, t_eval,args):
        dt=t_eval
        lenth=len(y0)
        y=[np.zeros(len(t)) for i in range(lenth)]
        for k in range(len(y0)):
            y[k][0]=y0[k]
        for i in range(len(t)-1):
            k1=func(y[0][i],y[1][i],args)
            k2=func(y[0][i]+dt*k1[0]*0.5,y[1][i]+dt*k1[1]*0.5,args)
            k3=func(y[0][i]+dt*k2[0]*0.5,y[1][i]+dt*k2[1]*0.5,args)
            k4=func(y[0][i]+dt*k3[0],y[1][i]+dt*k3[1],args)
            y[0][i+1]=y[0][i]+dt*(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6
            y[1][i+1]=y[1][i]+dt*(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6
        return y[0],y[1],t
    if method == "RK2":
        return RK2(func, y0,t_eval, args)
    elif method == "euler":
        return euler(func, y0,t_eval, args)
    elif method == "RK4":
        return RK4(func, y0,t_eval, args)
    else:
        print("Method not implemented")
        return 0,0,0