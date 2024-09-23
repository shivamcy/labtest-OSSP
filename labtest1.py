import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter,filtfilt
def fun(smooth):
    abv=np.where(smooth>120)[0]
    abv_arr=np.split(abv,np.where(np.diff(abv)!=1)[0])
    for pt in abv_arr:
       if len(pt)>15:
          plt.plot(pt,smooth[pt],color="green")  

time=np.arange(1440)
vc=120 + np.random.normal(0,1,1440)
plt.plot(time,vc,label="vehicles data with noise",linewidth="0.5",color="blue")
b,a=butter(3,0.05)
smooth=filtfilt(b,a,vc)
plt.plot(time,smooth,label="filtered data",linewidth="2",color="red")
avg=np.mean(smooth.reshape(24,60),axis=1)
print(avg)
plt.scatter(np.arange(0,1440,60),avg,label="hourly average",color="yellow")
fun(smooth)


plt.title("vehicle count system")
plt.legend()
plt.show()
