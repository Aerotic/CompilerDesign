# coding=utf-8
# import sys
# sys.setdefaultencoding('utf-8')
letter = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'
operater = '+-*/()'
class syntax:
    def __init__(self):
        # print '\n语义分析结果(四元式):'

        # self.getStack(stack)#获取单词栈
        # self.getDict(dict)#获取字典
        self.dic={}
        self.tab=[]
        self.quad = []
        # self.i = 0  # 栈指针
        # self.flag = 0  # 记录临时变量T数目
        # self.m()
        self.cnt=0
        self.i=0
        self.flag=0
        # for i in self.quad:  # 输出四元式结果
        #     print i
    def SyntaxAnalysis(self,tab,dic):
        self.quad = []
        self.i=0
        self.flag=self.cnt
        self.cnt+=1
        self.dic=dic
        self.tab=tab
        self.m()
        print "cnt is",self.cnt,"\n"
        for j in self.quad:  # 输出四元式结果
            print j
    def m(self):  # PM程序
        if len(self.tab)>self.i:
            if (self.tab[self.i] == '+'):
                self.i += 1
                ret1 = self.e()
                self.quad.append('(+,0,' + ret1 + ',out)')
                self.flag += 1
            elif (self.tab[self.i] == '-'):
                self.i += 1
                ret2 = self.e()
                self.quad.append('(-,0,' + ret2 + ',out)')
                self.flag += 1
            else:
                ret3 = self.e()
                self.quad.append('(=,' + ret3 + ',0,out)')

    def e(self):  # PE程序
        ret1 = self.t()
        ret2, ret3 = self.e1()
        if (ret2 != '&'):  # 若ret2不为&，则可以产生四元式，否则将变量传递给父项
            self.flag += 1
            self.quad.append('(' + ret2 + ',' + ret1 + ',' + ret3 + ',T' + str(self.flag) + ')')
            return 'T' + str(self.flag)
        else:
            return ret1

    def e1(self):  # PE1程序
        if (self.tab[self.i] == '+'):
            self.i += 1
            ret1 = self.t()
            ret2, ret3 = self.e1()
            if (ret2 == '&'):
                return '+', ret1
            else:
                self.flag += 1
                self.quad.append('(' + ret2 + ',' + ret1 + ',' + ret3 + ',T' + str(self.flag) + ')')
                return '+', 'T' + str(self.flag)
        elif (self.tab[self.i] == '-'):
            self.i += 1
            ret1 = self.t()
            ret2, ret3 = self.e1()
            if (ret2 == '&'):
                return '-', ret1
            else:
                self.flag += 1
                self.quad.append('(' + ret2 + ',' + ret1 + ',' + ret3 + ',T' + str(self.flag) + ')')
                return '-', 'T' + str(self.flag)
        else:
            return '&', '&'

    def t(self):  # PT程序
        ret1 = self.f()
        ret2, ret3 = self.t1()
        if (ret2 != '&'):
            self.flag += 1
            self.quad.append('(' + ret2 + ',' + ret1 + ',' + ret3 + ',T' + str(self.flag) + ')')
            return 'T' + str(self.flag)
        else:
            return ret1

    def t1(self):  # PT1程序
        if (self.tab[self.i] == '*'):
            self.i += 1
            ret1 = self.f()
            ret2, ret3 = self.t1()
            if (ret2 == '&'):
                return '*', ret1
            else:
                self.flag += 1
                self.quad.append('(' + ret2 + ',' + ret1 + ',' + ret3 + ',T' + str(self.flag) + ')')
                return '*', 'T' + str(self.flag)
        elif (self.tab[self.i] == '/'):
            self.i += 1
            ret1 = self.f()
            ret2, ret3 = self.t1()
            if (ret2 == '&'):  # 若ret2不为&，则可以产生四元式，否则将变量传递给父项
                return '/', ret1
            else:
                self.flag += 1
                self.quad.append('(' + ret2 + ',' + ret1 + ',' + ret3 + ',T' + str(self.flag) + ')')
                return '/', 'T' + str(self.flag)
        else:
            return '&', '&'

    def f(self):  # PF程序
        if (self.tab[self.i] == '('):
            self.i += 1
            ret1 = self.e()
            self.i += 1
            return str(ret1)
        elif (self.dic[self.tab[self.i]] == 1):  # 当为标识符时，传递给父项
            temp = self.i
            self.i += 1
            return self.tab[temp]
        elif (self.dic[self.tab[self.i]] == 2):  # 当为整数时，传递给父项
            temp = self.i
            self.i += 1
            return self.tab[temp]