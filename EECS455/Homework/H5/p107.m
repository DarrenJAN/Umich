clear all;
%=========================================================================%
%                                                                         %
%                Generate Signal                                          %
%                                                                         %
%=========================================================================%
%                                                                         %
%=========================================================================%

fmax=256;
N=4096;
fs=2*fmax;                % Sampling Frequency
df=2*fmax/N               % Frequency spacing
dt=1./(df.*N)             % Time spacing
t=(1:N)*dt-dt;            % Time samples
Tmax=N*dt                 % Simulation time
f=(1:N)*df-df;            % Frequency samples
f2=f-N/2*df;

npreamble=64;                      % Length of Preamble
btzo=[1 0 1 1 1 0 0 1 0 1 1 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 1 1 1 1 0 0 1 0 1 1 0 1 0 1 0 0 0 1 0 1 0 1 1 1 0 1 1 0 0 0 0 1 1 0 1 1];
bt=(-1).^btzo;

%=========================================================================%
%  Generate Pulses                                                        %
%=========================================================================%
x1t=zeros(1,N);               % Make the signal the right length
Nspp=8;                      % Nspp=Number of samples per pulse
x1t(1:Nspp*npreamble)=kron(bt,ones(1,Nspp));   % That is each pulse is N identical samples

x1f=fftshift(fft(x1t)*dt);
figure(100)
subplot(2,1,1), plot(t, x1t)
xlabel('time (s)')
ylabel('Transmitted Signal')
axis([0 4 -1.5 1.5])
grid on
subplot(2,1,2), plot(f2, 20*log10(abs(x1f)))
xlabel('frequency')
ylabel('Transmitted Spectrum')
grid on

%=========================================================================%
%  Put the signal through the channel                                     %
%=========================================================================%
sigma=2;
noise=sigma*randn(1,N);
x2t=x1t+noise;
delay=round(100*rand);
x2t=circshift(x2t',delay)';
x2f=fftshift(fft(x2t)*dt);

figure(101)
subplot(2,1,1), plot(t,real(x2t))
axis([0 4 -8 8])
grid on
xlabel('time (s)')
ylabel('Received Signal')
subplot(2,1,2), plot(f2,20*log10(abs(x2f)))
xlabel('frequency')
ylabel('Recevied Spectrum')

