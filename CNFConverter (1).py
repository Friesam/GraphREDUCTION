
# coding: utf-8

# In[25]:


def Convert2CNF(n,p):
     outputfilename = "CNF-200-90.cnf"
     adjacency=Generator(n,p)
     m=0
     NumberVertec=len(adjacency)
     output_file = open(outputfilename, "w")
     
     for i in range (1,NumberVertec):
        for j in range ((i+1),NumberVertec):
            for k in range ((j+1),NumberVertec):
                if ((adjacency[i,j]) & (adjacency[i,k]) & (adjacency[j,k])):
                    m+=1
                    #output_file.write( "\n"+str(i)+"\t"+str(j)+"\t"+str(k)+"\t"+str(0)+"\n"+str(-i)+"\t"+str(-j)+"\t"+str(-k)+"\t"+str(0))
                    #output_file.write( "\n"+str(adjacency[i,j])+"\t"+str(adjacency[i,k])+"\t"+str(adjacency[j,k])+"\n"+str(-adjacency[i,j])+"\t"+str(-adjacency[i,k])+"\t"+str(-adjacency[j,k]))
     output_file.write( str("p cnf " + str(n)+"\t"+str(2*m)))           
     for i in range (1,NumberVertec):
        for j in range ((i+1),NumberVertec):
            for k in range ((j+1),NumberVertec):
                if ((adjacency[i,j]) & (adjacency[i,k]) & (adjacency[j,k])):
                    output_file.write( "\n"+str(i)+"\t"+str(j)+"\t"+str(k)+"\t"+str(0)+"\n"+str(-i)+"\t"+str(-j)+"\t"+str(-k)+"\t"+str(0))
def Generator(n,p):
    import numpy as np
#n is the number of vertices in the graph. \
# p is probability of edge by random integers from the “discrete uniform” distribution 
    adjacency = np.random.randint(0,100,(n,n))
    l=0
    for i in range(0,n):
        for j in range(l,n):
            if (adjacency[i,j] > p):
                adjacency[i,j]=0
                adjacency[j,i]=0
            else:
                adjacency[i,j]=1
                adjacency[j,i]=1
            
        adjacency[i,i]=0  
        l+=1
    return adjacency


# In[26]:


Convert2CNF(200,90)

