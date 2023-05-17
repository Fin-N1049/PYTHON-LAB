import numpy as np
import pandas as pd
def PCA(X , num_components):
     
    # mean Centering the data  
    X_meaned = X - np.mean(X , axis = 0) 
   
    # calculating the covariance matrix of the mean-centered data.
    cov_mat = np.cov(X_meaned, rowvar = False)
    print("\nCovarience Matrix :\n",cov_mat)
     
    #Calculating Eigenvalues and Eigenvectors of the covariance matrix
    eigen_values , eigen_vectors = np.linalg.eigh(cov_mat)
    print("\nEigen Value :\n",eigen_values)
    print("\nEigen Vector:\n",eigen_vectors)
    
    #sort the eigenvalues and eigenvectors in descending order
    sorted_index = np.argsort(eigen_values)[::-1]
    sorted_eigenvalue = eigen_values[sorted_index]
    sorted_eigenvectors = eigen_vectors[:,sorted_index]
     
    # select the first n eigenvectors, n is desired dimension
    eigenvector_subset = sorted_eigenvectors[:,0:num_components]
     #Transform the data 
    X_reduced = np.dot(eigenvector_subset.transpose() ,#
               X_meaned.transpose() ).transpose()
     
    return X_reduced
   
r=int(input("Enter the number of row    : "))
c=int(input("Enter the number of colums : "))
print("\nEnter the values in the form of",r,"*",c,"matrix form :");
a=[(input().split()) for j in range(r)]
matrix=np.array(a,float)
print("\nMatrix : \n",matrix)
 
mat_reduced = PCA(matrix , 2)

#Creating a Pandas DataFrame of reduced Dataset
principal_df = pd.DataFrame(mat_reduced , columns = ['PC1','PC2'])
print("\nPrincipal Component Analysis : \n")
print(principal_df)