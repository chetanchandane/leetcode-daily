
# def generate(n):
#     # i = 0
#     output = []
#     for i in range(n):
        # single = [1]*(i+1)
        # if output:
        #     if len(output) < 2: output.append(single)
        #     elif len(output) == 2: 
        #         single[1] += 1
        #         output.append(single)
        #     else:
        #         for j in range(1, len(single)-1, 1):
        #             single[j] = output[-1][j] + output[-1][j-1]                 
        # else:
        #     output.append(single)    
    #     print(output)    
    
    # return output    

def generate(n):
    # i = 0
    output = []
    for i in range(n):
        single = [1]*(i+1)
        if output is None:
            output.append(single)
        elif len(output) > 1: 
            for j in range(1, len(single)-1):
                single[j] = output[-1][j-1] + output[-1][j]
            output.append(single)    
        else:
            output.append(single)    
    print(output)        
generate(5)