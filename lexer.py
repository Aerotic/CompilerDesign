# -*-coding:utf-8-*-
import sys
import string

keywords = {}
#123
# 关键字部分
keywords['False'] = 101
keywords['class'] = 102
keywords['finally'] = 103
keywords['is'] = 104
keywords['return'] = 105
keywords['None'] = 106
keywords['continue'] = 107
keywords['for'] = 108
keywords['lambda'] = 109
keywords['try'] = 110
keywords['True'] = 111
keywords['def'] = 112
keywords['from'] = 113
keywords['nonlocal'] = 114
keywords['while'] = 115
keywords['and'] = 116
keywords['del'] = 117
keywords['global'] = 118
keywords['not'] = 119
keywords['with'] = 120
keywords['as'] = 121
keywords['elif'] = 122
keywords['if'] = 123
keywords['or'] = 124
keywords['yield'] = 125
keywords['assert'] = 126
keywords['else'] = 127
keywords['import'] = 128
keywords['pass'] = 129
keywords['break'] = 130
keywords['except'] = 131
keywords['in'] = 132
keywords['raise'] = 133
keywords['main']=134
keywords['void']=135
#数据类型
keywords['int'] = 135
keywords['char'] = 136

# 符号
keywords['+'] = 201
keywords['-'] = 202
keywords['*'] = 203
keywords['/'] = 204
keywords['='] = 205
keywords[':'] = 206
keywords['<'] = 207
keywords['>'] = 208
keywords['%'] = 209
keywords['&'] = 210
keywords['!'] = 211
keywords['('] = 212
keywords[')'] = 213
keywords['['] = 214
keywords[']'] = 215
keywords['{'] = 216
keywords['}'] = 217
keywords['#'] = 218
keywords['|'] = 219
keywords[','] = 220
keywords[';'] = 221

# 变量
# keywords['var'] = 301

# 常量
# keywords['const'] = 401

# Error
# keywords['const'] = 501

signlist = {}


# 预处理函数，将文件中的空格，换行等无关字符处理掉
def pre_treatment():
    try:
        fp_read = open("source.txt", 'r')
        fp_write = open('file.tmp', 'w')
        sign = 0
        while True:
            read = fp_read.readline()
            if not read:
                break
            length = len(read)
            i = -1
            while i < length - 1:
                i += 1
                if sign == 0:
                    if read[i] == ' ':
                        continue
                if read[i] == '#':
                    break
                elif read[i] == ' ':
                    if sign == 1:
                        continue
                    else:
                        sign = 1
                        fp_write.write(' ')
                elif read[i] == '\t':
                    if sign == 1:
                        continue
                    else:
                        sign = 1
                        fp_write.write(' ')
                elif read[i] == '\n':
                    if sign == 1:
                        continue
                    else:
                        fp_write.write(' ')
                        sign = 1
                elif read[i] == '"':
                    fp_write.write(read[i])
                    i += 1
                    while i < length and read[i] != '"':
                        fp_write.write(read[i])
                        i += 1
                    if i >= length:
                        break
                    fp_write.write(read[i])
                elif read[i] == "'":
                    fp_write.write(read[i])
                    i += 1
                    while i < length and read[i] != "'":
                        fp_write.write(read[i])
                        i += 1
                    if i >= length:
                        break
                    fp_write.write(read[i])
                else:
                    sign = 3
                    fp_write.write(read[i])
    except Exception:
        print("Negative", ': This FileName Not Found!')


def save(string):
    if string in keywords.keys():
        if string not in signlist.keys():
            signlist[string] = keywords[string]
    else:
        try:
            float(string)
            save_const(string)
        except ValueError:
            save_var(string)


def save_var(string):
    if string not in signlist.keys():
        if len(string.strip()) < 1:
            pass
        else:
            if is_signal(string) == 1:
                signlist[string] = 301
            else:
                signlist[string] = 501


def save_const(string):
    if string not in signlist.keys():
        signlist[string] = 401


def save_error(string):
    if string not in signlist.keys():
        #if string.strip(';') in signlist.keys():
        signlist[string] = 501


def is_signal(s):
    if s[0] == '_' or s[0] in string.ascii_letters:
        for i in s:
            if i in string.ascii_letters or i == '_' or i in string.digits:
                pass
            else:
                return 0
        return 1
    else:
        return 0


def recognition():
    try:
        fp_read = open("file.tmp", 'r')
        string = ""
        sign = 0
        while True:
            read = fp_read.read(1)
            if not read:
                break

            if read == ' ':
                if len(string.strip()) < 1:
                    sign = 0
                    pass
                else:
                    if sign == 1 or sign == 2:
                        string += read
                    else:
                        save(string)
                        string = ""
                        sign = 0
            elif read == '(':
                if sign == 1 or sign == 2:
                    string += read
                else:
                    save(string)
                    string = ""
                    save('(')
            elif read == ')':
                if sign == 1 or sign == 2:
                    string += read
                else:
                    save(string)
                    string = ""
                    save(')')
            elif read == '[':
                if sign == 1 or sign == 2:
                    string += read
                else:
                    save(string)
                    string = ""
                    save('[')
            elif read == ']':
                if sign == 1 or sign == 2:
                    string += read
                else:
                    save(string)
                    string = ""
                    save(']')
            elif read == '{':
                if sign == 1 or sign == 2:
                    string += read
                else:
                    save(string)
                    string = ""
                    save('{')
            elif read == '}':
                if sign == 1 or sign == 2:
                    string += read
                else:
                    save(string)
                    string = ""
                    save('}')
            elif read == '<':
                save(string)
                string = ""
                save('<')
            elif read == '>':
                save(string)
                string = ""
                save('>')
            elif read == ',':
                save(string)
                string = ""
                save(',')
            elif read == "'":
                string += read
                if sign == 1:
                    sign = 0
                    save_const(string)
                    string = ""
                else:
                    if sign != 2:
                        sign = 1
            elif read == '"':
                string += read
                if sign == 2:
                    sign = 0
                    save_const(string)
                    string = ""
                else:
                    if sign != 1:
                        sign = 2
            elif read == ':':
                if sign == 1 or sign == 2:
                    string += read
                else:
                    save(string)
                    string = ""
                    save(':')
            elif read == '+':
                save(string)
                string = ""
                save('+')
            elif read == '=':
                save(string)
                string = ""
                save('=')
            elif read == ';':
                save(string)
                string=""
                save(';')
            else:
                string += read


    except Exception as e:
        print(e)


def main():
    # if len(sys.argv) < 2:
    #     print("Please Input FileName")
    # else:
    #     pre_treatment(sys.argv[1])
    pre_treatment()
    recognition()
    global result


        #print("++", signlist[i],  i, "++")


if __name__ == '__main__':
    main()
    result=open("result.txt",'w')
    for i in signlist.keys():
            if signlist[i] > 100 and signlist[i] < 136:#"%d"%signlist[i]
                result.write("关键字 " + i+'\n')
            elif signlist[i] > 200 and signlist[i] < 230:
                result.write("符号 " + i+'\n')
            elif signlist[i] < 137and signlist[i] > 134:
                result.write("数据类型 " + i + '\n')
            elif signlist[i]==401:
                if i[0]=='\"':
                    #i.strip('\"')
                    result.write("字符串 " + i.strip('\"') + '\n')
                if i[0]=='\'':
                    result.write("字符 " + i.strip('\'') + '\n')

            else:
                result.writelines("变量 " + i+'\n')
    result.close()