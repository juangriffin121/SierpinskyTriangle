import matplotlib.pyplot as plt
import numpy as np
fig,ax=plt.subplots()
u=np.array([0,1])
r=np.array([np.cos(np.pi*(-2/3+1/2)),np.sin(np.pi*(-2/3+1/2))])
l=np.array([np.cos(np.pi*(2/3+1/2)),np.sin(np.pi*(2/3+1/2))])
ori=np.array([0,0])
tr=np.array([ori+u,ori+r,ori+l])
up_array=np.array([u,u,u])
left_array=np.array([l,l,l])
right_array=np.array([r,r,r])
ITS=7
its=0
while its<ITS:
  trr=tr
  tru=tr+up_array+(-1)*right_array
  trl=tr+left_array+(-1)*right_array
  tr=np.array([tru,trr,trl])
  up_array=np.array([2*up_array,2*up_array,2*up_array])
  left_array=np.array([2*left_array,2*left_array,2*left_array])
  right_array=np.array([2*right_array,2*right_array,2*right_array])
  its=its+1
def decompose(triangle):
  '''

  Parameters
  ----------
  triangle : np.ndarray
  An array of the other 3 triangles that are contained within the input one, or an array of three 2Dpoints in space

  Returns
  -------
  None.
  -------
  Recursibly graphs in a matplotlib plot all the lines that conect the three points in the inner most triangles

  '''
  if len(triangle[0])==3:
    decompose(triangle[0])
    decompose(triangle[1])
    decompose(triangle[2])
  elif len(triangle[0])==2:
    ax.plot([triangle[0][0],triangle[1][0]],[triangle[0][1],triangle[1][1]],'b',linewidth=0.1)
    ax.plot([triangle[2][0],triangle[1][0]],[triangle[2][1],triangle[1][1]],'b',linewidth=0.1)
    ax.plot([triangle[0][0],triangle[2][0]],[triangle[0][1],triangle[2][1]],'b',linewidth=0.1)
  else:
    print("todo mal")
decompose(tr)