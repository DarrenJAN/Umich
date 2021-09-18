clear all
N=500000;                   % Number of data symbols transmitted.
s(1:8)=exp(1j*(0:7)*pi/4)   % The 8 signals.
Es=sum(abs(s).^2)/8;        % Average energy per signal
Eb=Es/3;                    % Average energy per bit
tic                         % Start a clock to see how long this takes
for j1=1:31                 % Run the simulation for different values of Eb/N0 (dB).
    EbN0dB(j1)=(j1-1)/2     % Set the value of Eb/N0 in dB
    EbN0=10.^(EbN0dB(j1)/10);      % Convert to non-dB units
    N0=Eb/EbN0;             % Since Eb is known determine N0.
    sigma=sqrt(N0/2);       % Variance of noise is sqrt(N0/2).
    NSymbolErrors=0;               % Counter for number of errors
    NBitErrors=0;               % Counter for number of errors
    for n=1:N               % Simulation loop
        data=round(7*rand(1,1)+1);       % Determine index of a transmitted signal
        r=s(data)+sigma*(randn(1,1)+j*randn(1,1));   % Add noise to the signal
        dmin=10000;         % Start with a large distance
        for k=1:8           % Find the signal closest to the received signal
            d=abs(r-s(k));
            if (d<dmin) info=k; dmin=d; end
        end
        if (info ~= data) NSymbolErrors =NSymbolErrors+1;    % Determine if there is an error
            bhat=de2bi(bitmap(info),5);
            b=de2bi(bitmap(data),5);
            NBitErrors =NBitErrors+sum(abs(b-bhat));
        end
    end
    Pe(j1)=NSymbolErrors/N;         % Estimate of the probability of error
    Peb(j1)=NBitErrors/N/3;
    [EbN0dB(j1),Pe(j1), Peb(j1)]      % Display for each EbN0 to see how long it is taking.
end
figure(2)
semilogy(EbN0dB,Pe)         % Plot the result
hold on
semilogy(EbN0dB,Peb)         % Plot the result
grid on
xlabel('$E_b/N_0$ (dB)','FontSize',16,'Interpreter','Latex')
ylabel('$P_{e,s}$', 'FontSize',16,'Rotation',0,'Interpreter','Latex')
set(gca,'FontSize',16)
axis([0 15 .99999e-5 1])
toc



function f=bitmap(n)
switch n
    case 1
        f=0;  % 000
    case 2
        f=1;  %001
    case 3
        f=3;  %011
    case 4
        f=2;  %010
    case 5
        f=6;  %110
    case 6
        f=7;  %111
    case 7
        f=5;  %101
    case 8
        f=4;  %100
end
end
