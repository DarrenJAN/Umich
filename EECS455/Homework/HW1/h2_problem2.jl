s0 = [1.2028, -3.4096]
s1 = [2.8312, -2.2484]
s2 = [3.5934, -0.3994]
s3 = [3.2558, 1.5720]
s4 = [1.9220 , 3.0622]
s5 = [0, 3.6154]
s6 = [-1.9220, 3.0622]
s7 = [-3.2558, 1.5720]
s8 = [-3.5934, -0.3994]
s9 = [-2.8312, -2.2484]
s10 = [-1.2028, -3.4096]
s11 = [0, -1.8116]
s12 = [1.0000, 1.2874]
s13 = [1.6054, -0.6188]
s14 = [-1, 1.2874]
s15 = [-1.6054, -0.6188]

S = [s0, s1, s2, s3, s4, s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15]


function print_euc(S)   
    len = length(S)
    for i in 1:len
        for j in i+1:len
            dist =euclidean(S[i],S[j])
            str = string("s", i-1, " s", j-1, ": ", dist)
            display(str)
        end 
    end
end 

function print_E(S)
    sum = 0
    len = length(S)
    for i in 1:len
        e = S[i]' * S[i]
        str = string("E", i-1, ": ", e)
        display(str)
        sum += e
    end 

    display(sum)
    avg_e = sum / len
    return sum, avg_e
end