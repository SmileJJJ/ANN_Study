import math
import numpy

'''
三层神经网络类(输入层，隐藏层，输出层)
输入层：输入层神经元个数,输入层神经元，输入层截距(共享)
隐藏层：隐藏层神经元个数，隐藏层权重(输入*隐藏)，隐藏层截距(共享)
输出层：输出层个数,输出层权重(隐藏*输出)

'''
class Ann(object):

    '''
    神经元结构
    输入神经元
    隐藏层权重
    输出层权重
    截距
    '''
    def __init__(self,neurons__structure,
                 input_layer_neurons,
                 hidden_layer_weight,
                 output_layer_weight,
                 nn_bias,):

        self.input_layer_neurons_num = neurons__structure[0]
        self.input_layer_neurons = input_layer_neurons
        self.input_layer_bias = nn_bias[0]

        self.hidden_layer_neurons_num = neurons__structure[1]
        self.hidden_layer_weight = hidden_layer_weight
        self.hidden_layer_bias = nn_bias[1]

        self.output_layer_num = neurons__structure[2]
        self.output_layer_weight = output_layer_weight


    def weight_init(self):

if __name__ == '__main__':
    Ann_test = Ann((2,2,2),(0.05,0.10),(0.15,0.20,0.25,0.30),(0.40,0.45,0.50,0.55),(0.35,0.60))


# #输入层
# layer_1_i1 = 0.05
# layer_1_i2 = 0.10
# layer_1_b1 = 0.35
# w1 = 0.15
# w2 = 0.20
# w3 = 0.25
# w4 = 0.30
#
# #隐藏层1
# layer_2_h1 = 0
# layer_2_h2 = 0
# w5 = 0.40
# w6 = 0.45
# w7 = 0.50
# w8 = 0.55
#
# #隐藏层2
# layer_3_o1_predict = 0.01
# layer_3_o2_predict = 0.99
#
# #激活函数
# def active_function(input,fun_name='sigmoid'):
#     if fun_name == 'sigmoid':
#         result = 1 / (1 + math.exp(-input))
#     return result
#
# #前向传播
# layer_2_h1 = layer_1_i1 * w1 + layer_1_i2 * w2 + 1 * layer_1_b1
# layer_2_h2 = layer_1_i1 * w3 + layer_1_i2 * w4 + 1 * layer_1_b1

