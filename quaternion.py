# coding=utf-8
# import sys
# sys.setdefaultencoding('utf-8')

tmp_sentence = []
tmp_exp = []
simpleDict = {}
exp_table = []
rawSentences = {}

ErrorCode = {}
ErrorCode['Undefined Identifier'] = 66
ErrorCode['expect BEGIN'] = 9
ErrorCode['expect :'] = 12
ErrorCode['expect .'] = 19
ErrorCode['expect END'] = 10
ErrorCode['Expression Error'] = 77

class quaternion:
    def __init__(self,tableDict,scanDict,str):
        self.dic={}
        self.tab=[]
        self.quad = []
        self.cnt=0
        self.i=0
        self.flag=0
        self.tableDict=tableDict
        print "*************************************************************************"
        self.scanDict=scanDict
        self.str=str
        print self.str
    def SyntaxAnalysis(self,tab,head,dic):
        self.quad = []
        self.i=0# 栈指针
        self.flag=self.cnt# 记录临时变量T数目
        self.dic=dic
        self.tab=tab
        self.head=head
        self.m(head)
        self.cnt+=self.flag
        # j=self.quad[0]
        # s="asd"
        # print j[:len(j)-4]+head+")"
        # print self.quad
        return self.quad
        # for j in self.quad:  # 输出四元式结果
        #     print j
    def m(self,head=''):  # PM程序
        if len(self.tab)>self.i:
            if (self.tab[self.i] == '+'):
                ret1 = self.e()
                self.quad.append('(+,0,' + ret1 + ","+head+")")
                self.flag += 1
                # self.cnt+=1
            elif (self.tab[self.i] == '-'):
                self.i += 1
                ret2 = self.e()
                self.quad.append('(-,0,' + ret2 +","+ head+")")
                self.flag += 1
                # self.cnt += 1
            else:
                ret3 = self.e()
                if  ret3:
                    self.quad.append('(:=,' + ret3 +", ,"+head+")")

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
    def getRawSentence(self,rawStr):

        # pop and judge 'begin'
        tmpword = rawStr.pop()
        if tmpword != 'begin':
            print "Fatal Error:expect a \"begin\"\n"
            exit(ErrorCode['expect BEGIN'])

        # pop and judge ':'
        tmpword = rawStr.pop()
        if tmpword != ':':
            print "Error:expect a \":\" after  \"begin\"\n"
            exit(ErrorCode['expect :'])

        if rawStr[0] != '.':
            print "Error:expect a \".\" after  \"end\"\n"
            exit(ErrorCode['expect .'])
        else:
            del rawStr[0]
        if rawStr[0] != 'end':
            print "Fatal Error:expect a \"end\"\n"
            exit(ErrorCode['expect END'])
        else:
            del rawStr[0]
            return rawStr
        return None

    def getSingleSentence(self,rawSs):
        tmplist = []
        tmpS = []
        while rawSs:
            tmpword = rawSs.pop()
            if tmpword == ';':
                tmplist.append(tmpS)
                tmpS = []
                continue
            if (tmpword not in self.tableDict.keys()) & (self.scanDict[tmpword] == '00'):
                print "Error:Undefined Identifier \"", tmpword, "\"\n"
                exit(ErrorCode['Undefined Identifier'])
            tmpS.append(tmpword)
        # print "tmplist is",tmplist[0],"\nEND"
        return tmplist

    def getExpression(self,tmpS):
        if len(tmpS) > 2:
            tmphead = tmpS[0]
            del tmpS[0]
            del tmpS[0]
            tmpS.append('#')
            return tmpS, tmphead
        else:
            print "Error:Expression Error\n"
            exit(ErrorCode['Expression Error'])

    def getSimpleDict(self,tmp1):
        simple_dict = {}
        for i in tmp1:
            if not self.scanDict.has_key(i):
                continue
            if self.scanDict[i] == '00':
                simple_dict[i] = 1
            elif self.scanDict[i] == '03':
                simple_dict[i] = 2
            else:
                simple_dict[i] = 3
        return simple_dict

    def getQuaternion(self,exp):
        # quat = quaternion.syntax()
        result = []
        for cnter in range(len(exp)):
            exptmp, exphead = self.getExpression(exp[cnter])
            result += self.SyntaxAnalysis(exptmp, exphead, self.getSimpleDict(exp[cnter]))
        # print result
        return result
    def getQuaternions(self):
        # self.table.Dict=TableDict
        # self.Table.Scan.Dict=Table.Scan.Dict
        # self.TableStrings=TableStrings
        rawSentences = self.getRawSentence(self.str)
        print rawSentences
        SentenceList = self.getSingleSentence(rawSentences)
        quaternions=self.getQuaternion(SentenceList)
        print quaternions
        # print self.getQuaternion(SentenceList)
        # return self.getQuaternion(SentenceList)
        pass
