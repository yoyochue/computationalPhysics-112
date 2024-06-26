import numpy as np
import matplotlib.pyplot as plt
def solve_ivp(func, t_span, y0, method, t_eval, args):
    """
    func: function
        The right-hand side of the differential equation.t
    t_span: array_like, [t0, t1], t0 < t1, from t0 to t1
        The time span for the integration.
    y0: array_like, shape (n,)
        The initial condition on the state vector.
    method: string
        The method to use for the integration. One of 'RK2', 'euler', 'RK4'.
    t_eval: float
        The time step to use.
    args: tuple
        Extra arguments to pass to the function. need to have correct order.

    Example for func with args:
        def f(x,v,arg,t):
            m=arg[0]
            k=arg[1]
            beta=arg[2]
        return [v,-k*x/m-beta*v] 
    """
    t=np.linspace(t_span[0],t_span[1],int((t_span[1]-t_span[0])/t_eval))
    def RK2(func, y0, t_eval,args,t):
        t=t
        dt=t_eval
        lenth=len(y0)
        y=[np.zeros(len(t)) for i in range(lenth)]
        for k in range(len(y0)):
            y[k][0]=y0[k]
        for i in range(len(t)-1):
            k1=func(y[0][i],y[1][i],args,t[i])
            k2=func(y[0][i]+dt*k1[0],y[1][i]+dt*k1[1],args,t[i]+dt)
            y[0][i+1]=y[0][i]+dt*(k2[0]+k1[0])/2    
            y[1][i+1]=y[1][i]+dt*(k2[1]+k1[1])/2
        return y[0],y[1],t
    def euler(func, y0, t_eval,args,t):
        t=t
        dt=t_eval
        lenth=len(y0)
        y=[np.zeros(len(t)) for i in range(lenth)]
        for k in range(len(y0)):
            y[k][0]=y0[k]
        for i in range(len(t)-1):
            k1=func(y[0][i],y[1][i],args,t[i])
            y[0][i+1]=y[0][i]+dt*k1[0]
            y[1][i+1]=y[1][i]+dt*k1[1]
        return y[0],y[1],t
    def RK4(func, y0, t_eval,args,t):
        t=t
        dt=t_eval
        lenth=len(y0)
        y=[np.zeros(len(t)) for i in range(lenth)]
        for k in range(len(y0)):
            y[k][0]=y0[k]
        for i in range(len(t)-1):
            k1=func(y[0][i],y[1][i],args,t[i])
            k2=func(y[0][i]+dt*k1[0]*0.5,y[1][i]+dt*k1[1]*0.5,args,t[i]+dt*0.5)
            k3=func(y[0][i]+dt*k2[0]*0.5,y[1][i]+dt*k2[1]*0.5,args,t[i]+dt*0.5)
            k4=func(y[0][i]+dt*k3[0],y[1][i]+dt*k3[1],args,t[i]+dt)
            y[0][i+1]=y[0][i]+dt*(k1[0]+2*k2[0]+2*k3[0]+k4[0])/6
            y[1][i+1]=y[1][i]+dt*(k1[1]+2*k2[1]+2*k3[1]+k4[1])/6
        return y[0],y[1],t
    if method == "RK2":
        return RK2(func, y0,t_eval, args,t)
    elif method == "euler":
        return euler(func, y0,t_eval, args,t)
    elif method == "RK4":
        return RK4(func, y0,t_eval, args,t)
    else:
        print("Method not implemented")
        return 0,0,0