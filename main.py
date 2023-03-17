# python3

def parallel_processing(n, m, data):
    output = []
    time=0
    # TODO: write the function for simulating parallel tasks,
    darba_nummurs=0
    threads=[]
    job={}
    for i in range(n):
        threads.append(i)
    
    while darba_nummurs<m:

        if time in job.values():
        
            for i in range(len(threads)):
                if time==job.get(i):
                    if darba_nummurs<len(data):
                        output.append([threads[i],time])
                        job[threads[i]]=data[darba_nummurs]+time
                        darba_nummurs+=1
                    else:
                        break
            time+=1

        elif len(job)==0:
            for i in range(len(threads)):
                job[threads[i]]=data[darba_nummurs]
                output.append([threads[i],time])
                darba_nummurs+=1
            time+=1
        else:
            time+=1
        

    # create the output pairs

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    text=list(map(int, input().split()))
    n=text[0]
    m=text[1]
    


    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []
    data=list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    #print(result)
    for i in range(len(result)):
        print(result[i][0],result[i][1])
        #print()


if __name__ == "__main__":
    main()
