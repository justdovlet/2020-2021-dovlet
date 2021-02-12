import numpy as np
import math
#import matplotlib.pyplot as plt

# 90 градусов = 1.5708 в радианах
q = 1.5708*0
w = 1.5708*0
p = 2
d = 1

A = np.matrix('1 1 1 1;'
             +'1 1 -1 1;'
             +'1 -1 -1 1;'
             +'1 -1 1 1;'
             +'-1 1 1 1;'
             +'-1 -1 -1 1;'
             +'-1 -1 1 1;'
             +'-1 1 -1 1')


"""
A = np.matrix('-1 -1 -1 1;'
             +'1 -1 -1 1;'
             +'1 1 -1 1;'
             +'-1 1 -1 1;'
             +'-1 -1 1 1;'
             +'1 -1 1 1;'
             +'1 1 1 1;'
             +'-1 1 1 1')
"""


B = np.matrix( [[-math.sin(q)  ,  -math.cos(w)*math.cos(q)    ,  -math.sin(w)*math.cos(q) , 0], 
               [ math.cos(q)   ,  -math.cos(w)*math.sin(q)    ,  -math.sin(w)*math.sin(q) , 0],
               [ 0             ,  math.sin(w)                 ,  -math.cos(w)             , 0],
               [ 0             ,  0                           ,  p                        , 1]])

C = A.dot(B)

#print("Матрица после перемножения матриц")
#print(C)
x = []
y = []
for iter in range (8):
  x.append (d * C[iter,0] / C[iter,2])
  y.append (d * C[iter,1] / C[iter,2])


#x = A[:,0]
#y = A[:,1]

print (x)
print (y)


#print(C)
'''
print ("\nx:")
print(x)



print ("\ny:")
print(y)


print ("\n x и y округлённые")
print (x.round(5))
print (y.round(5))


for i in range(8):
  for k in range(8):
    if (i!=k):
      plt.plot([ x[i,0],y[i,0] ],[ x[k,0],y[k,0] ])




for i in range(8):
  for k in range(8):
    if (i!=k):
      plt.plot([ x[i,0],y[i,0] ],[ x[k,0],y[k,0] ], color ="black", marker = "o")

'''
#plt.plot(x1, y1, x2, y2, marker = 'o')


#x1, y1 = [-1, 12], [1, 4]
#x2, y2 = [1, 10], [3, 2]
#plt.plot(x1, y1, x2, y2, marker = 'o')

#plt.show()
'''

plt.plot([x[0,0],y[0,0]], [x[1,0],y[1,0]])
plt.plot([x[1,0],y[1,0]], [x[2,0],y[2,0]])
plt.plot([x[2,0],y[2,0]], [x[3,0],y[3,0]])
plt.plot([x[3,0],y[3,0]], [x[0,0],y[0,0]], color = "none")
plt.plot([x[0,0],y[0,0]], [x[3,0],y[3,0]])



plt.plot([ x[0,0],y[0,0] ])
plt.plot([ x[1,0],y[1,0] ])



plt.plot(x[0,0],y[0,0], x[1,0],y[1,0], linestyle = "-", marker = 'o' )
plt.plot(x[1,0],y[1,0], x[2,0],y[2,0], linestyle = "-", marker = 'o' )
plt.plot(x[2,0],y[2,0], x[3,0],y[3,0], linestyle = "-", marker = 'o' )
plt.plot(x[3,0],y[3,0], x[0,0],y[0,0], linestyle = "-", marker = 'o' )



x1,x2,y1,y2 = [],[],[],[]

i = [0,1,2,0,3,4,5,6,7,4,0,1,5,2,6,3]
k = [1,2,3,3,4,5,6,7,4,0,1,5,2,6,3,7]

for h in range(len(i)):
  x1.append(x[i[h],0])
  y1.append(y[i[h],0])
  x2.append(x[k[h],0])
  y2.append(y[k[h],0])

plt.plot([x1,y1],[x2,y2])
'''
#line = [0, 4 ,7, 1, 2, 3, 6, 4, 3, 0, 1, 6, 5, 7, 5, 2]
#m_line = 3,6,5
import tkinter as Tkinter

window = Tkinter.Tk()
canva = Tkinter.Canvas(window)

for iterator in range (8):
  x[iterator] = (x[iterator] + 2)*75
  y[iterator] = (y[iterator] + 2)*75


canva.create_line((x[0]),(y[0]), (x[4]),(y[4]))
canva.create_line((x[4]),(y[4]), (x[7]),(y[7]))
canva.create_line((x[7]),(y[7]), (x[1]),(y[1]))
canva.create_line((x[1]),(y[1]), (x[2]),(y[2]))
canva.create_line((x[3]),(y[3]), (x[6]),(y[6]))
canva.create_line((x[6]),(y[6]), (x[4]),(y[4]))
canva.create_line((x[2]),(y[2]), (x[3]),(y[3]))
canva.create_line((x[3]),(y[3]), (x[0]),(y[0]))
canva.create_line((x[0]),(y[0]), (x[1]),(y[1]))
canva.create_line((x[6]),(y[6]), (x[5]),(y[5]))
canva.create_line((x[5]),(y[5]), (x[2]),(y[2]))
canva.create_line((x[5]),(y[5]), (x[7]),(y[7]))

canva.pack()
Tkinter.Tk().mainloop()
'''
canva.create_line((x[0]+2)*50,(y[0]+2)*50, (x[4]+2)*50,(y[4]+2)*50)
canva.create_line((x[4]+2)*50,(y[4]+2)*50, (x[7]+2)*50,(y[7]+2)*50)
canva.create_line((x[7]+2)*50,(y[7]+2)*50, (x[1]+2)*50,(y[1]+2)*50)
canva.create_line((x[1]+2)*50,(y[1]+2)*50, (x[2]+2)*50,(y[2]+2)*50)
canva.create_line((x[3]+2)*50,(y[3]+2)*50, (x[6]+2)*50,(y[6]+2)*50)
canva.create_line((x[6]+2)*50,(y[6]+2)*50, (x[4]+2)*50,(y[4]+2)*50)
canva.create_line((x[2]+2)*50,(y[2]+2)*50, (x[3]+2)*50,(y[3]+2)*50)
canva.create_line((x[3]+2)*50,(y[3]+2)*50, (x[0]+2)*50,(y[0]+2)*50)
canva.create_line((x[0]+2)*50,(y[0]+2)*50, (x[1]+2)*50,(y[1]+2)*50)
canva.create_line((x[6]+2)*50,(y[6]+2)*50, (x[5]+2)*50,(y[5]+2)*50)
canva.create_line((x[5]+2)*50,(y[5]+2)*50, (x[2]+2)*50,(y[2]+2)*50)
canva.create_line((x[5]+2)*50,(y[5]+2)*50, (x[7]+2)*50,(y[7]+2)*50)





for g in range(len(line)-1):
  if line[g+1] != 3 and line[g+1] != 6 and line[g+1] != 5:
    canva.create_line(x[line[g]],y[line[g]], x[line[g+1]],y[line[g+1]])
  else:
    print(0)
    #plt.plot ([ x[line[g]],y[line[g]] ],[ x[line[g+1]],y[line[g+1]] ], color = "black", marker = 'o')



plt.plot([ x[0],y[0] ],[ x[1],y[1] ], color = "black")
plt.plot([ x[1],y[1] ],[ x[2],y[2] ], color = "black")
plt.plot([ x[2],y[2] ],[ x[3],y[3] ], color = "black")
plt.plot([ x[3],y[3] ],[ x[0],y[0] ], color = "black")

plt.plot([ x[0],y[0] ],[ x[4],y[4] ], color = "none")

plt.plot([ x[4],y[4] ],[ x[5],y[5] ], color = "black")
plt.plot([ x[5],y[5] ],[ x[6],y[6] ], color = "black")
plt.plot([ x[6],y[6] ],[ x[7],y[7] ], color = "black")
plt.plot([ x[7],y[7] ],[ x[4],y[4] ], color = "black")

plt.plot([ x[4],y[4] ],[ x[0],y[0] ], color = "black")

plt.plot([ x[0],y[0] ],[ x[1],y[1] ], color = "none")

plt.plot([ x[1],y[1] ],[ x[5],y[5] ], color = "black")

plt.plot([ x[5],y[5] ],[ x[2],y[2] ], color = "none")

plt.plot([ x[2],y[2] ],[ x[6],y[6] ], color = "black")

plt.plot([ x[6],y[6] ],[ x[3],y[3] ], color = "none")

plt.plot([ x[3],y[3] ],[ x[7],y[7] ], color = "black")
'''
"""

plt.plot([ x[0,0],y[0,0] ],[ x[1,0],y[1,0] ], color = "black")
plt.plot([ x[1,0],y[1,0] ],[ x[2,0],y[2,0] ], color = "black")
plt.plot([ x[2,0],y[2,0] ],[ x[3,0],y[3,0] ], color = "black")
plt.plot([ x[0,0],y[0,0] ],[ x[3,0],y[3,0] ], color = "black")

plt.plot([ x[3,0],y[3,0] ],[ x[4,0],y[4,0] ], color = "none")

plt.plot([ x[4,0],y[4,0] ],[ x[5,0],y[5,0] ], color = "black")
plt.plot([ x[5,0],y[5,0] ],[ x[6,0],y[6,0] ], color = "black")
plt.plot([ x[6,0],y[6,0] ],[ x[7,0],y[7,0] ], color = "black")
plt.plot([ x[7,0],y[7,0] ],[ x[4,0],y[4,0] ], color = "black")

plt.plot([ x[4,0],y[4,0] ],[ x[0,0],y[0,0] ], color = "black")

plt.plot([ x[0,0],y[0,0] ],[ x[1,0],y[1,0] ], color = "none")

plt.plot([ x[1,0],y[1,0] ],[ x[5,0],y[5,0] ], color = "black")

plt.plot([ x[5,0],y[5,0] ],[ x[2,0],y[2,0] ], color = "none")

plt.plot([ x[2,0],y[2,0] ],[ x[6,0],y[6,0] ], color = "black")

plt.plot([ x[6,0],y[6,0] ],[ x[3,0],y[3,0] ], color = "none")

plt.plot([ x[3,0],y[3,0] ],[ x[7,0],y[7,0] ], color = "black")

"""
"""


plt.plot([ x[1,0],y[1,0] ],[ x[2,0],y[2,0] ], color = "none")

plt.plot([ x[2,0],y[2,0] ],[ x[3,0],y[3,0] ])
plt.plot([ x[3,0],y[3,0] ],[ x[7,0],y[7,0] ], color = "white")


plt.plot([ x[7,0],y[7,0] ],[ x[3,0],y[3,0] ])
plt.plot([ x[3,0],y[3,0] ],[ x[7,0],y[7,0] ], color = "none")


plt.plot([ x[7,0],y[7,0] ],[ x[4,0],y[4,0] ])
plt.plot([ x[4,0],y[4,0] ],[ x[5,0],y[5,0] ])
"""
#plt.plot(x,y)

#plt.show()