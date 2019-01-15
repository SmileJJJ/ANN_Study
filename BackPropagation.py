import math
import numpy
import random

'''
三层神经网络类(输入层，隐藏层，输出层)
输入层：输入层神经元个数,输入层神经元，输入层截距(共享)
隐藏层：隐藏层神经元个数，隐藏层权重(输入*隐藏)，隐藏层截距(共享)
输出层：输出层个数,输出层权重(隐藏*输出)

'''


class Ann(object):
    LEARNING_RATE = 0.5

    '''
    神经元结构
    输入神经元
    隐藏层权重
    输出层权重
    输入层截距
    隐藏层截距

    '''
    def __init__(self,neurons__structure,
                 hidden_layer_weight=None,
                 output_layer_weight=None,
                 hidden_layer_bias=None,
                 output_layer_bias=None,
                 active_method='sigmoid'):

        self.input_layer_neurons_num = neurons__structure[0]
        self.active_method = active_method

        self.hidden_layer_neurons = []
        self.hidden_layer_neurons_num = neurons__structure[1]
        self.hidden_layer_weight = hidden_layer_weight
        self.hidden_layer_bias = hidden_layer_bias

        self.output_layer_neurons = []
        self.output_layer_neurons_num = neurons__structure[2]
        self.output_layer_weight = output_layer_weight
        self.output_layer_bias = output_layer_bias

        self.weight_init()

    def weight_init(self):
        # 隐藏层权重配置
        if not self.hidden_layer_weight:
            self.hidden_layer_weight = []
            for i in range(self.input_layer_neurons_num * self.hidden_layer_neurons_num):
                self.hidden_layer_weight.append(random.random())
        else:
            self.hidden_layer_weight = list(self.hidden_layer_weight)
            for i in range(len(self.hidden_layer_weight)):
                if not self.hidden_layer_weight[i]:
                    self.hidden_layer_weight[i] = random.random()

        # 输出层权重配置
        if not self.output_layer_weight:
            self.output_layer_weight = []
            for i in range(self.hidden_layer_neurons_num * self.output_layer_neurons_num):
                self.output_layer_weight.append(random.random())
        else:
            self.output_layer_weight = list(self.output_layer_weight)
            for i in range(len(self.output_layer_weight)):
                if not self.output_layer_weight[i]:
                    self.output_layer_weight[i] = random.random()

    def train(self,input_layer_neurons,target):
        self.forward_propagation(input_layer_neurons)

        self.back_propagation(target)

    # 前向传播
    def forward_propagation(self,input_layer_neurons):
        for i in range(self.hidden_layer_neurons_num):
            self.hidden_layer_neurons.append(input_layer_neurons[0] * self.hidden_layer_weight[i*2]
                                             + input_layer_neurons[1] * self.hidden_layer_weight[i*2+1]
                                             + 1 * self.hidden_layer_bias)

        for i in range(len(self.hidden_layer_neurons)):
            self.hidden_layer_neurons[i] = self.active_function(self.hidden_layer_neurons[i])

        for i in range(self.output_layer_neurons_num):
            self.output_layer_neurons.append(self.hidden_layer_neurons[0] * self.output_layer_weight[i*2]
                                             + self.hidden_layer_neurons[1] * self.output_layer_weight[i*2+1]
                                             + 1 * self.output_layer_bias)

        for i in range(len(self.output_layer_neurons)):
            self.output_layer_neurons[i] = self.active_function(self.output_layer_neurons[i])

    def back_propagation(self,target):
        total_errors = self.output_error(target)
        print(total_errors)
        pd_total_2_output_weights = []
        pd_total_2_hidden_weights = []

        # 求总体误差对输出层权重系数的偏导(总体误差之和)
        for i in range(self.output_layer_neurons_num):
            pd_1 = self.pd_total_error_2_out_out(target[i],self.output_layer_neurons[i])
            pd_2 = self.pd_out_out_2_out_net(self.output_layer_neurons[i])
            for j in range(self.hidden_layer_neurons_num):
                pd_3 = self.pd_out_net_2_weight(j)
                pd_total_2_output_weights.append(pd_1 * pd_2 * pd_3)

        # 求总体误差对输出层神经元的偏导(总体误差分开)
        for i in range(self.output_layer_neurons_num):
            pd_total_2_hidden = []
            for   ？？？？？？？？？？

        print(pd_total_2_output_weights)

    def active_function(self,input_number):
        if self.active_method == 'sigmoid':
            return 1 / (1 + math.exp(-input_number))
        else:
            return None

    def output_error(self,target_output):
        total_errors = 0
        for i in range(self.output_layer_neurons_num):
            total_errors += 1 / 2 * (target_output[i] - self.output_layer_neurons[i]) ** 2
        return total_errors

    # 用误差对权重系数求偏导，得到权重系数对整体误差的影响程度，(链式法则)
    # 一：求整体误差(target)对输出(out_out)的偏导
    # 二：求输出(out_out)对未经过激活函数激活的加权和输出(out_net)的偏导
    # 三：求加权和输出(out_net)对权重系数(weight)的偏导
    def pd_total_error_2_out_out(self,target,out_out):
        return - (target - out_out)

    def pd_out_out_2_out_net(self,out_out):
        if self.active_method == 'sigmoid':
            return out_out * (1 - out_out)

    def pd_out_net_2_weight(self,index):
        return self.hidden_layer_neurons[index]

if __name__ == '__main__':
    Ann_test = Ann((2,2,2),(0.15,0.20,0.25,0.30),(0.40,0.45,0.50,0.55),0.35,0.60)
    Ann_test.train((0.05,0.10),(0.01,0.99))