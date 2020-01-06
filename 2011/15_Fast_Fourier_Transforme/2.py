
# Example 2
# Multiple subplots in one figure
from pylab import *
from scipy import *
from scipy.fftpack import fftshift
x=r_[0:101]
y01=sin(2*pi*x/100)
y02=cos(2*pi*x/100)
y03 = randn(100);
y04 = sinc(2*pi*x/100);
Y04 = abs(fftshift(fft(y04)))
y05 = sinc(1.5*pi*x/100);
y06 = sinc(2.5*pi*x/100);
Y06 = abs(fftshift(fft(y06)))
subplot(2,2,1);plot(x,y01,linewidth=3);hold(True);
plot(x,y02,'r',linewidth=3)
grid(True);title('sin(x) & cos(x)');
subplot(2,2,2);plot(y03,linewidth=2);grid(True);title('Random Numbers');
subplot(2,2,3);plot(x,y04,'k',linewidth=3);grid(True);title('sinc(x)');
hold(True);
subplot(2,2,3);plot(x,y05,'--',linewidth=3);
subplot(2,2,3);plot(x,y06,'r',linewidth=2);
subplot(2,2,4);plot(Y04,linewidth=2.5);grid(True);title('FFT of sinc(x)');
show()