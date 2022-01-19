s0 = [-3, 0]
s1 = [-1, 0]
s2 = [+1, 0]
s3 = [3, 0]
s4 = [-2 , sqrt(3)]
s5 = [0, sqrt(3)]
s6 =[2, sqrt(3)]
s7 = [4, sqrt(3)]
s8 = [-1, 2*sqrt(3)]
s9 = [+1, 2*sqrt(3)]
s10 = [-4, -sqrt(3)]
s11 = [-2, -sqrt(3)]
s12 = [0, -sqrt(3)]
s13 = [2, -sqrt(3)]
s14 =[-1, -2*sqrt(3)]
s15 = [1, -2*sqrt(3)]

 S = [s0, s1, s2, s3, s4, s5,s6,s7,s8,s9,s10,s11,s12,s13,s14,s15]
#S = [s0, s1, s2, s3, s4, s5,s6,s7]

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


# x=[S[i][1] for i in 1:length(S)]
# y=[S[i][2] for i in 1:length(S)]
# scatter(x,y, xlabel= "x", ylabel= "y",  label="")