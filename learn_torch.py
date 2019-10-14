import torch
from torch.autograd import Variable

tensor = torch.FloatTensor([[1,2],[2,3]])
variable = Variable(tensor,requires_grad= True)

print