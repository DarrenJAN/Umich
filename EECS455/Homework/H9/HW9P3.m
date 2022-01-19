clear all;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                       %
%                Simulation Parameters                  %
%                                                       %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
ncount=input('Number of errors = ');
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%                                                       %
%                Setup the Simulation                   %
%                                                       %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
E=1
Eb=E;                 % Relation between energy per code symbol and bit
s(1,:)  =  sqrt(E)*[ exp(j*2*pi*0/8), exp(j*2*pi*0/8), exp(j*2*pi*0/8), exp(j*2*pi*0/8) ];
s(2,:)  =  sqrt(E)*[ exp(j*2*pi*0/8), exp(j*2*pi*4/8), exp(j*2*pi*0/8), exp(j*2*pi*0/8) ];
s(3,:)  =  sqrt(E)*[ exp(j*2*pi*0/8), exp(j*2*pi*2/8), exp(j*2*pi*5/8), exp(j*2*pi*2/8) ];
s(4,:)  =  sqrt(E)*[ exp(j*2*pi*0/8), exp(j*2*pi*6/8), exp(j*2*pi*5/8), exp(j*2*pi*2/8) ];
s(5,:)  =  sqrt(E)*[ exp(j*2*pi*4/8), exp(j*2*pi*0/8), exp(j*2*pi*0/8), exp(j*2*pi*0/8) ];
s(6,:)  =  sqrt(E)*[ exp(j*2*pi*4/8), exp(j*2*pi*4/8), exp(j*2*pi*0/8), exp(j*2*pi*0/8) ];
s(7,:)  =  sqrt(E)*[ exp(j*2*pi*4/8), exp(j*2*pi*2/8), exp(j*2*pi*5/8), exp(j*2*pi*2/8) ];
s(8,:)  =  sqrt(E)*[ exp(j*2*pi*4/8), exp(j*2*pi*6/8), exp(j*2*pi*5/8), exp(j*2*pi*2/8) ];
s(9,:)  =  sqrt(E)*[ exp(j*2*pi*2/8), exp(j*2*pi*5/8), exp(j*2*pi*2/8), exp(j*2*pi*0/8) ];
s(10,:)  =  sqrt(E)*[ exp(j*2*pi*2/8), exp(j*2*pi*1/8), exp(j*2*pi*2/8), exp(j*2*pi*0/8) ];
s(11,:)  =  sqrt(E)*[ exp(j*2*pi*2/8), exp(j*2*pi*3/8), exp(j*2*pi*7/8), exp(j*2*pi*2/8) ];
s(12,:)  =  sqrt(E)*[ exp(j*2*pi*2/8), exp(j*2*pi*7/8), exp(j*2*pi*7/8), exp(j*2*pi*2/8) ];
s(13,:)  =  sqrt(E)*[ exp(j*2*pi*6/8), exp(j*2*pi*5/8), exp(j*2*pi*2/8), exp(j*2*pi*0/8) ];
s(14,:)  =  sqrt(E)*[ exp(j*2*pi*6/8), exp(j*2*pi*1/8), exp(j*2*pi*2/8), exp(j*2*pi*0/8) ];
s(15,:)  =  sqrt(E)*[ exp(j*2*pi*6/8), exp(j*2*pi*3/8), exp(j*2*pi*7/8), exp(j*2*pi*2/8) ];
s(16,:)  =  sqrt(E)*[ exp(j*2*pi*6/8), exp(j*2*pi*7/8), exp(j*2*pi*7/8), exp(j*2*pi*2/8) ];

%=========================================================================================%
%                                                                                         %
%                           Compute the Union Bound First                                 %
%                                                                                         %
%=========================================================================================%

for m=1:35
	EbN0dB(m)=-4+(m-1)/2
	EbN0(m)=10^(EbN0dB(m)/10);
	N0=Eb/EbN0(m);            % Noise power
	sigma=sqrt(N0/2);

%=========================================================================================%
%                                                                                         %
%   YOUR CODE FOR UNION BOUND GOES HERE                                                   %
%                                                                                         %
%=========================================================================================%
    pes_ub(m)=0
    for i=1:16
        pe(i)=0;
        for l=1:16
            d(i,l)=sqrt(sum((abs(s(i,:)-s(l,:))).^2));
            if (l ~= i) 
                pe(i)=pe(i)+qfunc(d(i,l)/(2*sigma)); 
            end
        end
        pes_ub(m)=pes_ub(m)+pe(i)/16;
    end
% 	pes_ub(m)= .... this is your result for the union bound

end
semilogy(EbN0dB,pes_ub,'r','LineWidth',2)    % PLOT THE RESULTS
hold on

clear EbN0dB
%=========================================================================================%
%                                                                                         %
%                           Now do the simulation                                         %
%                                                                                         %
%=========================================================================================%

for m=1:25
    EbN0dB(m)=-4+(m-1)/2
    EbN0(m)=10^(EbN0dB(m)/10);
    N0=Eb/EbN0(m);            % Noise power
    sigma=sqrt(N0/2);


%=========================================================================================%

    allsignals=s;
    nberrors=0;
    nserrors=0;
    nbsim=0;
    nsim=0;
    while(or((nserrors < ncount),(nbsim < 100000)))  % THIS CONDITION DETERMINES HOW MANY SIMULATIONS YOU RUN
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        %                                                       %
        %              Generate data and signals                %
        %                                                       %
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        b=round(rand(1,4));
        index=(b(4)+2*b(3)+4*b(2)+8*b(1))+1;
        strans=allsignals(index,:);
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        %                                                       %
        %                  Add Noise                            %
        %                                                       %
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

        noise=sigma*randn(1,4)+j*sigma*randn(1,4);
        rcvd=strans+noise; 

        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        %                                                       %
        %           Decode the received signal              %
        %                                                       %
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        r = [ rcvd;rcvd;rcvd;rcvd;rcvd;rcvd;rcvd;rcvd;rcvd;rcvd;rcvd;rcvd;rcvd;rcvd;rcvd;rcvd];
        vec_distance = vecnorm(r - s, 2, 2);
        [min_distance, dec_index] = min(vec_distance);
        % 
        % min_distance = 999;
        % dec_index = 0;
        % for i = 1:16
        %      
        %      distance = norm(s(i,:) - rcvd )
        %      distance_vec(i) = distance
        %     if(distance < min_distance)
        %         min_distance = distance
        %         dec_index = i
        %     end
        % end
        
        if(dec_index ~= index)
            nserrors = nserrors +1;
        end
        nbsim = nbsim + 4;
        nsim = nsim + 1;
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        %                                                       %
        %        PUT YOUR CODE HERE FOR DECODING THE SIGNAL     % 
        %        AND COUNTING THE NUMBER OF ERRORS              %
        %        nberrors is number of bit errors               %
        %        nserrors is number of symbol errors            %
        %                                                       %
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    end
	peb(m)=nberrors/nbsim;
	pes(m)=nserrors/nsim;
    semilogy(EbN0dB,pes,'LineWidth',2)
    axis([-4 12 0.00000001 1])
    grid on
    hold on
    xlabel('E_b/N_0 (dB)','FontSize',16)
    ylabel('P_{e,b}','FontSize',16)
    legend('Union bound', 'Simulation')
end



function Total_Q = pij(si, S,Sigma)
    Total_Q = 0;
    for i =  1:16
        if i == si
            continue;
        else
            distance = norm(S(i,:) - S(si,:));
            disp("distance in " + si +" "+ i +"  : "+ distance)
            y = qfunc(distance / (2* Sigma));
            Total_Q =  Total_Q + y;
            disp("P2 for "+ si + " " + i +" is: "  + y)
        end 
    end 
    disp("Pei for " + i + " is :" + Total_Q)
end


