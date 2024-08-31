import torch

A = torch.arange(20).reshape(5, 4)
A = A.T
print(A)
B = A.sum(dim=0)
C = A.sum(dim=0, keepdim=True)
print(B)
print(C)
