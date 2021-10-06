import numpy as np
w_1 = float(input("Enter initial weight 1 = "))
w_2 = float(input("Enter initial weight 2 = "))
x = [ [0,0], [0,1], [1,0], [1,1]]
x_array = np.asarray(x)
out = x_array[:, 1] * x_array[:, 0]
def step (net):
    if net >= 1:
        return 1
    else:
        return 0
error = np.array([0,0,0,0])
for i in range(len(x)):
    f_net = step(np.dot(np.asarray([w_1, w_2]) , x[i]))
    error[i] = out[i] - f_net
E = np.sum(error)
max_it = 1000
t = 1
vals = [[w_1, w_2]]
while t < max_it & E != 0:
    for i in range(len(x)):
        f_net = step(np.dot(np.asarray([w_1, w_2]) , x[i]))
        error[i] = out[i] - f_net
        if(error[i]!=0):
            w_1 = w_1 + error[i] * x[i][0]
            w_2 = w_2 + error[i] * x[i][1]
    vals.append([w_1, w_2])
    E = np.sum(error)
    t = t+1
    print("After iteration ",t-1,":")
    print("[{0}\t{1}]".format(w_1,w_2))
print("Final vectors = [{0}\t{1}]".format(w_1,w_2))
