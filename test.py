# Dict1 = {}
# Dict1['example'] = {'position': 1, 'type': ' ', 'category': 'f', 'address': 0}
# Dict1['a'] = {'position': 2, 'type': 'char', 'category': 'v', 'address': 8}
# Dict1['b'] = {'position': 3, 'type': 'char', 'category': 'v', 'address': 16}
# Dict1['c'] = {}
# print type(Dict1['c'])
# Dict1['c']['position'] = 4
# Dict1['c']['type'] = 'char'
# Dict1['c']['category'] = 'v'
# Dict1['c']['address'] = 24
# print Dict1['c']
import generate_table
import tmp



tmp_sentence=[]#temporary
tmp_exp=[]
simpleDict={}
exp_table=[]
rawSentences={}

ErrorCode={}
ErrorCode['Undefined Identifier']=66
ErrorCode['expect BEGIN']=9
ErrorCode['expect :']=12
ErrorCode['expect .']=19
ErrorCode['expect END']=10
ErrorCode['Expression Error']=77
def getRawSentence(rawStr):

    #pop and judge 'begin'
    tmpword=rawStr.pop()
    if tmpword!='begin':
        print "Fatal Error:expect a \"begin\"\n"
        exit(9)

    # pop and judge ':'
    tmpword = rawStr.pop()
    if tmpword!=':':
        print "Error:expect a \":\" after  \"begin\"\n"
        exit(12)

    if rawStr[0]!='.':
        print "Error:expect a \".\" after  \"end\"\n"
        exit(19)
    else:
        del rawStr[0]
    if rawStr[0]!='end':
        print "Fatal Error:expect a \"end\"\n"
        exit(10)
    else:
        del rawStr[0]
        return rawStr
    return None
def getSingleSentence(rawSs):
    tmplist=[]
    tmpS=[]
    while rawSs:
        tmpword=rawSs.pop()
        if tmpword ==';':
            tmplist.append(tmpS)
            tmpS=[]
            continue
        if (tmpword not in t.Dict.keys())&(t.Scan.Dict[tmpword]=='00'):
            print "Error:Undefined Identifier \"",tmpword,"\"\n"
            exit(ErrorCode['Undefined Identifier'])
        tmpS.append(tmpword)
    # print "tmplist is",tmplist[0],"\nEND"
    return tmplist
def getExpression(tmpS):
    if len(tmpS)>2:
        del tmpS[0]
        del tmpS[0]
        tmpS.append('#')
        return tmpS
    else:
        print "Error:Expression Error\n"
        exit(ErrorCode['Expression Error'])
def getSimpleDict(tmp1):
    simple_dict={}
    for i in tmp1:
        if not t.Scan.Dict.has_key(i):
            continue
        if t.Scan.Dict[i]=='00':
            simple_dict[i]=1
        elif t.Scan.Dict[i]=='03':
            simple_dict[i] = 2
        else:
            simple_dict[i] = 3
    return simple_dict
def test(exp):
    quat=tmp.syntax()
    quat.SyntaxAnalysis(getExpression(exp[0]),getSimpleDict(exp[0]))
    quat.SyntaxAnalysis(getExpression(exp[1]), getSimpleDict(exp[1]))
    quat.SyntaxAnalysis(getExpression(exp[2]), getSimpleDict(exp[2]))
def getQuaternions():

    pass
if __name__ == '__main__':
    t=generate_table.Table()
    # simple_dict=dict()
    t.Program()
    t.Strings.pop()
    rawSentences = getRawSentence(t.Strings)
    SentenceList=getSingleSentence(rawSentences)
    # print SentenceList[0]
    # print len(SentenceList[0])
    # # getExpression(SentenceList[0])
    test(SentenceList)
    # simpleDict=getSingleSentence(SentenceList[0])
    # quad=tmp.syntax(SentenceList[0],simpleDict)
    #tmps=getComSentence(t.Strings)
    #print tmps
    # find 'begin' if not throw an error
    #
    # while True:
    #     word=t.Strings.pop()
    #     if(t.Scan.Dict[word]=='09'):
    #         break;
    #     elif (t.Strings is None):
    #         print "Fatal Error:expect a \"Begin\"\n"
    #         exit(9)
    # #Find the ':' following 'begin'.If not throw an error
    # word=t.Strings.pop()
    # if (t.Scan.Dict[word] == '12'):
    #     pass
    # else:
    #     print "Fatal Error:expect a \":\" after  \"Begin\"\n"
    #     exit(12)
    # if (t.Strings[0]=='.'):
    #     print "find it"
    #     del t.Strings[0]
    #     print t.Strings
    #
    # while True:
    #     #Push a whole sentence into tmp_sentence
    #     while True:
    #         if t.Strings:
    #             word = t.Strings.pop()
    #         else:
    #             break
    #         if (t.Scan.Dict[word] != '13'):
    #             tmp_sentence.append(word)
    #         else:
    #             t.Strings.pop()
    #             break;
    #     tmp_sentence=tmp_sentence[::-1]#
    #     tmp_sentence.pop()#pop the first identifier before ':='
    #     tmp_sentence.pop()
    #     while tmp_sentence:
    #         word=tmp_sentence.pop()
    #         if t.Scan.Dict[word]!='10':
    #             tmp_exp.append(word)
    #         else:
    #             word=tmp_sentence.pop()
    #             break
    #     if word=='.':
    #         break
    #         # pop ':=' from tmp_sentence
    #     if tmp_exp:
    #         exp_table = tmp_exp
    #         exp_table.append('#')
    #         toSimpleDict(tmp_exp)
    #         tmp_exp = []
    #         syntax = tmp.syntax(exp_table, simple_dict)
    #     else:
    #         break
