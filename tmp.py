# coding=utf-8
# import sys
# sys.setdefaultencoding('utf-8')

class syntax:
    def __init__(self):
        self.dic={}
        self.tab=[]
        self.quad = []
        self.cnt=0
        self.i=0
        self.flag=0
    def SyntaxAnalysis(self,tab,head,dic):
        self.quad = []
        self.i=0
        self.flag=self.cnt
        self.dic=dic
        self.tab=tab
        self.head=head
        self.m()
        self.cnt+=self.flag
        print "cnt is",self.cnt,"\n"
        return self.quad
    def m(self):  # PM程序
        if len(self.tab)>self.i:
            if (self.tab[self.i] == '+'):
                ret1 = self.e()
                self.quad.append('(+,0,' + ret1 + ","+self.head+")")
                self.flag += 1
                # self.cnt+=1
            elif (self.tab[self.i] == '-'):
                self.i += 1
                ret2 = self.e()
                self.quad.append('(-,0,' + ret2 +","+ self.head+")")
                self.flag += 1
                # self.cnt += 1
            else:
                ret3 = self.e()
                self.quad.append('(:=,' + ret3 +", ,"+self.head+")")

    def e(self):  # PE程序
        ret1 = self.t()
        ret2, ret3 = self.e1()
        if (ret2 != '&'):  # 若ret2不为&，则可以产生四元式，否则将变量传递给父项
            self.flag += 1
            self.quad.append('(' + ret2 + ',' + ret1 + ',' + ret3 + ',t' + str(self.flag) + ')')
            return 't' + str(self.flag)
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
                self.quad.append('(' + ret2 + ',' + ret1 + ',' + ret3 + ',t' + str(self.flag) + ')')
                return '+', 't' + str(self.flag)
        elif (self.tab[self.i] == '-'):
            self.i += 1
            ret1 = self.t()
            ret2, ret3 = self.e1()
            if (ret2 == '&'):
                return '-', ret1
            else:
                self.flag += 1
                self.quad.append('(' + ret2 + ',' + ret1 + ',' + ret3 + ',t' + str(self.flag) + ')')
                return '-', 'T' + str(self.flag)
        else:
            return '&', '&'

    def t(self):  # PT程序
        ret1 = self.f()
        ret2, ret3 = self.t1()
        if (ret2 != '&'):
            self.flag += 1
            self.quad.append('(' + ret2 + ',' + ret1 + ',' + ret3 + ',t' + str(self.flag) + ')')
            return 't' + str(self.flag)
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