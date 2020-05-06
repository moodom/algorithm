# import torch
# from torch.autograd import gradcheck,Function,Varisable
# from torch.nn import Conv2d
# class LinearFunction(Function):
#     @staticmethod
#     def forward(ctx,input,weight,bias=None):
#         ctx.save_for_backward(input,weight,bias)
#         output=input.mm(weight.t())
#         if bias is not None:
#             output+=bias.unqueeze(0).expand_as(output)
#         return output 
#     @staticmethod
#     def backward(ctx,grad_output):
#         input,weight,bias=ctx.saved_variables
#         grad_input=grad_weight=grad_bias=None 
#         if ctx.needs_input_grad[0]:
#             grad_input=grad_output.mm(weight)
#         if ctx.needs_input_grad[1]:
#             grad_weight=grad_output.t().mm(input)
#         if bias is not None and ctx.needs_input_grad[2]:
#             grad_bias=grad_output.sum(0).squeeze(0)
#         return grad_input,grad_weight,grad_bias
# input = (Variable(torch.randn(20,20).double(), requires_grad=True),)
# test = gradcheck(LinearFunction(), input, eps=1e-6, atol=1e-4)
# print(test)  #　没问题的话输出True
# import torch
# import torch.nn as nn
# class LinearModel(nn.Module):
#     def __init__(self,ndim):
#         super(LinearModel,self).__init__()
#         self.ndim=ndim
#         self.weight=nn.Parameter(torch.randn(ndim,1))
#         self.bias=nn.Parameter(torch.randn(1))
#     def forward(self,x):
#         return x.mm(self.weight)+self.bias
# from sklearn.datasets import load_boston
# boston=load_boston()
# lm=LinearModel(13)
# criterion=nn.MSELoss()
# optim=torch.optim.SGD(lm.parameters(),lr=1e-11)
# data=torch.tensor(boston["data"],requires_grad=True, dtype=torch.float32)
# target=torch.tensor(boston["target"],requires_grad=True,dtype=torch.float32)
# for step in range(10000):
#     predict=lm(data)
#     loss=criterion(predict,target)
#     if step and step%100==0:
#         print("Loss :{:.3f}".format(loss.item()))
#     optim.zero_grad()
#     loss.backward()
#     optim.step()

# import torch
# import torch.nn as nn 
# torch.nn.Linear()
# torch.nn.Conv2d()
# nn.BatchNorm2d()
# nn.MaxPool2d()
# nn.MaxPool2d()
# nn.Dropout()
# nn.MSELoss()
# torch.optim.SGD()

class Func(torch.autograd.Function):
    @staticmethod
    def forward(ctx,input):
        ctx.input=input
        return input*torch.sigmoid(1.702*input)

    @staticmethod
    def backward(ctx,grad_output):
        input=ctx.input 
        tmp=torch.sigmoid(1.702*input)
        return grad_output*(tmp+1.702*input*tmp*(1-tmp))