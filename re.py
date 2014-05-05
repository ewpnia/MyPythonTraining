# -*- coding: utf-8 -*-

import re

# ---------------------------------------------------------------------------------------

string = '(page 1 of 2000)'                 # 2000会变，能是600、90...

>>> re.search(r'\d+\)', str).group()        # 匹配结果
'2000)'
>>> re.search(r'\d+\)', str).span()         # 显示匹配出来的字符串在源字符串中的位置
(11, 16)
>>> re.findall(r'\d+', str)                 # 返回一个数组
['1', '2000']

# group(): 返回匹配的完整字符串。
# start(): 匹配的开始位置。
# end(): 匹配的结束位置。
# span(): 包含起始、结束位置的元组。
# groups(): 返回分组信息。
# groupdict(): 返回命名分组信息。

>>> re.search(r'(?:\w+\d+\w+)(\d+)', str).group()
'2000'


# ---------------------------------------------------------------------------------------


# 编译标志
# 可以用 re.I、re.M 等参数，也可以直接在表达式中添加 "(?iLmsux)" 标志。
# • s: 单行。"." 匹配包括换行符在内的所有字符。
# • i: 忽略大小写。
# • L: 让 "\w" 能匹配当地字符，貌似对中文支持不好。
# • m: 多行。
# • x: 忽略多余的空白字符，让表达式更易阅读。
# • u: Unicode。

>>> re.findall(r"[a-z]+", "%123Abc%45xyz&")
['bc', 'xyz']
>>> re.findall(r"[a-z]+", "%123Abc%45xyz&", re.I)
['Abc', 'xyz']
>>> re.findall(r"(?i)[a-z]+", "%123Abc%45xyz&")
['Abc', 'xyz']

# 下面这么写好看多了吧？
>>> pattern = r"""
... (\d+) # number
... ([a-z]+) # letter
... """
>>> re.findall(pattern, "%123Abc\n%45xyz&", re.I | re.S | re.X)
[('123', 'Abc'), ('45', 'xyz')]


# ---------------------------------------------------------------------------------------

# 组操作

# 命名组：(?P<name>...)

>>> for m in re.finditer(r"(?P<number>\d+)(?P<letter>[a-z]+)", "%123Abc%45xyz&", re.I):
... print m.groupdict()
...
{'number': '123', 'letter': 'Abc'}
{'number': '45', 'letter': 'xyz'}


# 无捕获组：(?:...)，作为匹配条件，但不返回。

>>> for m in re.finditer(r"(?:\d+)([a-z]+)", "%123Abc%45xyz&", re.I):
... print m.groups()
...
('Abc',)
('xyz',)


# 反向引用：\<number> 或 (?P=name)，引用前面的组。

>>> for m in re.finditer(r"<a>\w+</a>", "%<a>123Abc</a>%<b>45xyz</b>&"):
... print m.group()
...
<a>123Abc</a>
>>> for m in re.finditer(r"<(\w)>\w+</(\1)>", "%<a>123Abc</a>%<b>45xyz</b>&"):
... print m.group()
...
<a>123Abc</a>
<b>45xyz</b>
>>> for m in re.finditer(r"<(?P<tag>\w)>\w+</(?P=tag)>", "%<a>123Abc</a>%<b>45xyz</b>&"):
... print m.group()
...
<a>123Abc</a>
<b>45xyz</b>


# 正声明 (?=...)：组内容必须出现在右侧，不返回。
# 负声明 (?!...)：组内容不能出现在右侧，不返回。
# 反向正声明 (?<=)：组内容必须出现在左侧，不返回。
# 反向负声明 (?<!)：组内容不能出现在左侧，不返回。

>>> for m in re.finditer(r"\d+(?=[ab])", "%123Abc%45xyz%780b&", re.I):
... print m.group()
...
123
780
>>> for m in re.finditer(r"(?<!\d)[a-z]{3,}", "%123Abc%45xyz%byse&", re.I):
... print m.group()
...
byse


# ---------------------------------------------------------------------------------------

# 函数原型re.search(pattern,string,flag=0)
pattern = 'this'
text = 'Does this text match the pattern?'
match = re.search(pattern, text)    # 返回一个Match对象  
print match.re.pattern              # 要匹配的正则表达式"this"
print match.string                  # 匹配的文本"Does this match the pattern?"  
print match.start()                 # 匹配的开始位置 5
print match.end()                   # 匹配的结束位置 9

# ---------------------------------------------------------------------------------------

# 函数原型re.compile(pattern,flag=0)
# 如果程序中频繁的使用到同一个正则表达式，
# 每次使用的时候都写一遍正则表达式不仅不高效而且会大大增加出错的几率,
# re提供了compile函数将一个表达式字符串编译为一个RegexObject。
# 模块级函数会维护已编译表达式的一个缓存，
# 而这个缓存的大小是有限制的。直接使用已经编译的表达式可以避免缓存查找的开销，
# 并且在加载模块时就会预编译所有的表达式。

regex = re.compile("this")  
text = "Does this text match the pattern?"  
match = regex.search(text)  
if match:  
    print "match"  
    match.group(0)    #返回匹配的字符串   
else:
    print "not match"  

# -----------------------------------------------------------------------------------------


# 函数原型re.findall(pattern, string, flag=0)
# 使用search会返回匹配的单个实例，
# 使用findall会返回所有匹配的不重叠的子串。

pattern = 'ab'  
text = 'abbaaabbbbaaaaaa'  
re.findall(pattern, text)   # 返回['ab', 'ab']  

# ------------------------------------------------------------------

# 函数原型re.finditer(pattern, string, flag=0)
# finditer会返回一个迭代器，会生成Match实例，
# 不像findall()返回字符串.

pattern = 'ab'  
text = 'abbaaabbbbaaaaaa'  
match = re.finditer(pattern, text)   
for m in match:
    print m.start()  
    print m.end()

# ----------------------------------------------------------------------------

# 正则匹配默认采用的是贪婪算法，
# 也就是说会re在匹配的时候会利用尽可能多的输入，
# 而使用？可以关闭这种贪心行为，
# 只匹配最少的输入。

# 量词是为了简化正则表达式的读写而定义的，
# 通用的形式是{m,n},
# 这表示匹配的个数至少是m，最多是n，
# 在','之后不能有空格，否则会出错，
# 并且均为闭区间。

# {n} 之前的元素必须出现n次
# {m,n} 之前元素最少出现m次，最多n次
# {m,} 之前的元素最少出现m次，无上限
# {0,n} 之前的元素可以不出现，也可以出现，出现的话最多出现n次
# 除了之上，还有三个常用的量词*,?和+

# * 等价于{0,}
# + 等价于{1,}
# \? 等价于{0,1}
# 还有^和$，分别表示段或者字符串的开始与结束。

# ---------------------------------------------------------------------------------

# 对于一些预定义的字符集可以使用转义码可以更加紧凑的表示，
# re可以识别的转义码有3对，6个，分别为三个字母的大小写，
# 他们的意义是相反的。

# \d : 一个数字
# \D : 一个非数字
# \w : 字母或者数字
# \W : 非字母，非数字
# \s : 空白符（制表符，空格，换行符等）
# \S : 非空白符

the_str = "This is some text -- with punctuation"  
re.search(r'^\w+', the_str).group(0)       # This
re.search(r'\A\w+', the_str).group(0)      # This  
re.search(r'\w+\S*$', the_str).group(0)    # punctuation  
re.search(r'\w+\S*\Z', the_str).group(0)   # punctuation  
re.search(r'\w*t\W*', the_str).group(0)    # text --  
re.search(r'\bt\w+', the_str).group(0)     # text  
re.search(r'\Bt*\B', the_str).group(0)     # 没有匹配  

# --------------------------------------------------------------------------------------

# 用组来解析匹配，简单的说就是在一个正则表达式中有几个小括号
# ()将匹配的表达式分成不同的组，
# 使用group()函数来获取某个组的匹配，
# 其中0为整个正则表达式所匹配的内容，
# 后面从1开始从左往右依次获取每个组的匹配，
# 即每个小括号中的匹配。
# 使用groups()可以获取所有的匹配内容。


the_str = "--aabb123bbaa"  
pattern = r'(\W+)([a-z]+)(\d+)(\D+)'  
match = re.search(pattern, the_str)    
match.groups()    # ('--', 'aabb', '123', 'bbaa') 
match.group(0)    # '--aabb123bbaa'  
match.group(1)    # '--'  
match.group(2)    # 'aabb'  
match.group(3)    # '123'  
match.group(4)    # 'bbaa'

# ---------------------------------------------------------------------------------------

# python对分组的语法做了扩展，我们可以对每个分组进行命名，
# 这样便可以使用名称来调用。语法:(?P<name>pattern),
# 使用groupdict()可以返回一个包含了组名的字典。

the_str = "--aabb123bbaa"  
pattern = r'(?P<not_al_and_num>\W+)(?P<al>[a-z]+)(?P<num>\d+)(?P<not_num>\D+)'  
match = re.search(pattern, the_str)    
match.group()    # ('--', 'aabb', '123', 'bbaa')  
match.groupdict() # {'not_al_and_num': '--', 'not_num': 'bbaa', 'num': '123', 'al': 'aabb'}  
match.group(0)                    # '--aabb123bbaa'  
match.group(1)                    # '--'  
match.group(2)                    # 'aabb'  
match.group(3)                    # '123'  
match.group(4)                    # 'bbaa'   
match.group('not_al_and_num')    # '--'
match.group('al')                 # 'aabb'  
match.group('num')               # '123' '
match.group('not_num')            # 'bbaa'

# 以上的group()方法在使用的时候需要注意，
# 只有在有匹配的时候才会正常运行，否则会抛错，
# 所以在不能保证有匹配而又要输出匹配结果的时候，
# 必须做校验。

# 在re中可以设置不通的标志，
# 也就是search()和compile()等中都包含的缺省变量flag。
# 使用标志可以进行完成一些特殊的要求，如忽略大小写，多行搜索等。

the_str = "this Text"  
re.findall(r'\bt\w+', the_str)   # ['this']  
re.findall(r'\bt\w+', the_str, re.IGNORECASE) # ['this', 'Text']  


# ---------------------------------------------------------------------------------------


# 匹配符：
#         ^       匹配字符串开始位置。在多行字符串模式匹配每一行的开头。
#         $       匹配字符串结束位置。在多行字符串模式匹配每一行的结尾。
#         .       匹配除了换行符外的任何字符，在 alternate 模式(re.DOTALL)下它甚至可以匹配换行。
#         \A      匹配字符串开头
#         \Z      匹配字符串结尾
#         \b      匹配一个单词边界。即 \w 与 \W 之间。
#         \B      匹配一个非单词边界；相当于类 [^\b]。
#         \d      匹配一个数字。
#         \D      匹配一个任意的非数字字符。
#         \s      匹配任何空白字符；它相当于类  [ \t\n\r\f\v]。
#         \S      匹配任何非空白字符；它相当于类 [^ \t\n\r\f\v]。
#         \w      匹配任何字母数字字符；它相当于类 [a-zA-Z0-9_]。
#         \W      匹配任何非字母数字字符；它相当于类 [^a-zA-Z0-9_]。
#         x?      匹配可选的x字符。即是0个或者1个x字符。
#         x*      匹配0个或更多的x。
#         x+      匹配1个或者更多x。
#         x{n,m}  匹配n到m个x，至少n个，不能超过m个。
#         (a|b|c) 匹配单独的任意一个a或者b或者c。
#         (x)     捕获组，小括号括起来即可，它会记忆它匹配到的字符串。
#                 可以用 re.search() 返回的匹配对象的 groups()函数来获取到匹配的值。
#         \1      记忆组，它表示记住的第一个分组；如果有超过一个的记忆分组，可以使用 \2 和 \3 等等。
#                 记忆组的内容也要小括号括起来。
#         (?iLmsux)          iLmsux的每个字符代表一种匹配模式
#         re.I(re.IGNORECASE): 忽略大小写(括号内是完整写法，下同)
#         re.L(re.LOCALE): 使预定字符类 \w \W \b \B \s \S 取决于当前区域设定
#         re.M(re.MULTILINE): 多行模式，改变'^'和'$'的行为(参见上图)
#         re.S(re.DOTALL): 点任意匹配模式，改变'.'的行为
#         re.U(re.UNICODE): 使预定字符类 \w \W \b \B \s \S \d \D 取决于unicode定义的字符属性
#         re.X(re.VERBOSE): 松散正则表达式模式。这个模式下正则表达式可以是多行，忽略空白字符，并可以加入注释。
#         (?:表达式)         无捕获组。与捕获组表现一样，只是没有内容。
#         (?P<name>表达式)   命名组。与记忆组一样，只是多了个名称。
#         (?P=name)          命名组的逆向引用。
#         (?#...)            “#”后面的将会作为注释而忽略掉。例如：“ab(?#comment)cd”匹配“abcd”
#         (?=...)            之后的字符串需要匹配表达式才能成功匹配。不消耗字符串内容。 例：“a(?=\d)”匹配“a12”中的“a”
#         (?!...)            之后的字符串需要不匹配表达式才能成功匹配。不消耗字符串内容。 例：“a(?!\d)”匹配“abc”中的“a”
#         (?<=...)           之前的字符串需要匹配表达式才能成功匹配。不消耗字符串内容。 例：“(?<=\d)a”匹配“2a”中的“a”
#         (?<!...)           之前的字符串需要不匹配表达式才能成功匹配。不消耗字符串内容。 例：“(?<!\d)a”匹配“sa”中的“a”
#                        注：上面4个表达式的里面匹配的内容只能是一个字符，多个则报错。
#         (?(id/name)yes-pattern|no-pattern)  如果编号为 id 或者别名为 name 的组匹配到字符串，则需要匹配yes-pattern，否则需要匹配no-pattern。 “|no-pattern”可以省略。如：“(\d)ab(?(1)\d|c)”匹配到“1ab2”和“abc”

    # 元字符:
    #     "[" 和 "]"
    #         它们常用来匹配一个字符集。字符可以单个列出，也可以用“-”号分隔的两个给定字符来表示一个字符区间。
    #             例如，[abc] 将匹配"a", "b", 或 "c"中的任意一个字符；也可以用区间[a-c]来表示同一字符集，和前者效果一致。
    #         元字符在类别里并不起作用。例如，[a$]将匹配字符"a" 或 "$" 中的任意一个；"$" 在这里恢复成普通字符。
    #         也可以用补集来匹配不在区间范围内的字符。其做法是把"^"作为类别的首个字符；其它地方的"^"只会简单匹配 "^"字符本身。
    #             例如，[^5] 将匹配除 "5" 之外的任意字符。
    #         特殊字符都可以包含在一个字符类中。如，[\s,.]字符类将匹配任何空白字符或","或"."。
    #     反斜杠 "\"。
    #         做为 Python 中的字符串字母，反斜杠后面可以加不同的字符以表示不同特殊意义。
    #         它也可以用于取消所有的元字符，这样你就可以在模式中匹配它们了。
    #             例如，需要匹配字符 "[" 或 "\"，可以在它们之前用反斜杠来取消它们的特殊意义： \[ 或 \\。

    # 建议使用原始字符串:
    #     建议在处理正则表达式的时候总是使用原始字符串。如： r'\bROAD$', 而不要写成 '\\bROAD$'
    #     否则，会因为理解正则表达式而消耗大量时间(正则表达式本身就已经够让人困惑的了)。

    # 无捕获组:
    #     有时你想用一个组去收集正则表达式的一部分，但又对组的内容不感兴趣。你可以用一个无捕获组“(?:...)”来实现这项功能。
    #     除了捕获匹配组的内容之外，无捕获组与捕获组表现完全一样；可以在其中放置任何字符、匹配符，可以在其他组(无捕获组与捕获组)中嵌套它。
    #     无捕获组对于修改已有组尤其有用，因为可以不用改变所有其他组号的情况下添加一个新组。
    #     捕获组和无捕获组在搜索效率方面也一样。

    # 命名组:
    #     与用数字指定组不同的是，它可以用名字来指定。除了该组有个名字之外，命名组也同捕获组是相同的。
    #     (?P<name>...) 定义一个命名组，(?P=name) 则是对命名组的逆向引用。
    #     MatchObject 的方法处理捕获组时接受的要么是表示组号的整数，要么是包含组名的字符串。所以命名组可以通过数字或者名称两种方式来得到一个组的信息。

    # 松散正则表达式:
    #     为了方便阅读和维护，可以使用松散正则表达式，它与普通紧凑的正则表达式有两点不同：
    #     1, 空白符被忽略。空格、制表符(tab)和回车会被忽略。如果需要匹配他们，可以在前面加一个“\”来转义。
    #     2, 注释被忽略。注释以“#”开头直到行尾，与python代码中的一样。
    #     使用松散正则表达式，需要传递一个叫 re.VERBOSE的 参数。详细见下面例子。

    # 例如:

        # 必须引入 re 标准库
        import re

        # 字符串替换:  sub() 与 subn()
        s = '100 NORTH MAIN ROAD'
        # 将字符串结尾的单词“ROAD”替换成“RD.”；该 re.sub() 函数执行基于正则表达式的字符串替换。
        print(re.sub(r'\bROAD$', 'RD.', s)) # 打印： 100 NORTH MAIN RD.
        ## subn() 与 sub() 作用一样，但返回的是包含新字符串和替换执行次数的两元组。
        print(re.subn(r'\bROAD$', 'RD.', s)) # 打印： ('100 NORTH MAIN RD.', 1)

        # 字符串分割, split()
        # 在正则表达式匹配的地方将字符串分片，将返回列表。只支持空白符和固定字符串。可指定最大分割次数，不指定将全部分割。
        print(re.split(r'\s+', 'this is a test')) # 打印： ['this', 'is', 'a', 'test']
        print(re.split(r'\W+', 'This is a test.', 2)) # 指定分割次数,打印：['this', 'is', 'a test']
        # 如果你不仅对定界符之间的文本感兴趣，也需要知道定界符是什么。在 RE 中使用捕获括号，就会同时传回他们的值。
        print(re.split(r'(\W+)', 'This is a test.', 2)) # 捕获定界符,打印：['this', ' ', 'is', ' ', 'a test']

        ## `MatchObject` 实例的几个方法
        r = re.search(r'\bR(OA)(D)\b', s)
        print(r.groups()) # 返回一个包含字符串的元组,可用下标取元组的内容，打印： ('OA', 'D')
        print(r.group())  # 返回正则表达式匹配的字符串，打印： ROAD
        print(r.group(2)) # 返回捕获组对应的内容(用数字指明第几个捕获组)，打印： D
        print(r.start())  # 返回匹配字符串开始的索引, 打印： 15
        print(r.end())    # 返回匹配字符串结束的索引，打印： 19
        print(r.span())   # 返回一个元组包含匹配字符串 (开始,结束) 的索引，打印： (15, 19)

        # 匹配多个内容, findall() 返回一个匹配字符串行表
        p = re.compile('\d+')
        s0 = '12 drummers drumming, 11 pipers piping, 10 lords a-leaping'
        print(p.findall(s0)) # 打印： [12, 11, 10]
        print(re.findall(r'\d+', s0)) # 也可这样写，打印： [12, 11, 10]

        # 匹配多个内容, finditer() 以迭代器返回
        iterator = p.finditer(s0)
        # iterator = re.finditer(r'\d+', s0) # 上句也可以这样写
        for match in iterator:
            print(match.group()) # 三次分别打印：12、 11、 10

        # 记忆组
        print(re.sub('([^aeiou])y$', 'ies', 'vacancy'))    # 将匹配的最后两个字母替换掉，打印： vacanies
        print(re.sub('([^aeiou])y$', r'\1ies', 'vacancy')) # 将匹配的最后一个字母替换掉，记忆住前一个(小括号那部分)，打印： vacancies
        print(re.search('([^aeiou])y$', 'vacancy').group(1)) # 使用 group() 函数获取对应的记忆组内容，打印： c

        # 记忆组(匹配重复字符串)
        p = re.compile(r'(?P<word>\b\w+)\s+\1') # 注意, re.match() 函数不能这样用，会返回 None
        p = p.search('Paris in the the spring')
        # p = re.search(r'(?P<word>\b\w+)\s+\1', 'Paris in the the spring') # 这一句可以替换上面两句
        print(p.group())  # 返回正则表达式匹配的所有内容，打印： the the
        print(p.groups()) # 返回一个包含字符串的元组，打印： ('the',)

        # 捕获组
        r = re.search(r'\bR(OA)(D)\b', s) # 如过能匹配到，返回一个 SRE_Match 类(正则表达式匹配对象)；匹配不到则返回“None”
        # `MatchObject` 实例的几个方法
        if r: # 如果匹配不到，则 r 为 None,直接执行下面语句则会报错；这里先判断一下，避免这错误
            print(r.groups()) # 返回一个包含字符串的元组,可用下标取元组的内容，打印： ('OA', 'D')
            print(r.group())  # 返回正则表达式匹配的字符串，打印： ROAD
            print(r.group(2)) # 返回捕获组对应的内容(用数字指明第几个捕获组)，打印： D

        # 无捕获组
        print(re.match("([abc])+", "abcdefab").groups())   # 正常捕获的结果： ('c',)
        print(re.match("(?:[abc])+", "abcdefab").groups()) # 无捕获组的结果： ()

        # 命名组
        m = re.match(r'(?P<word>\b\w+\b) *(?P<word2>\b\w+\b)', 'Lots of punctuation')
        print(m.groups())       # 返回正则表达式匹配的所有内容，打印：('Lots', 'of')
        print(m.group(1))       # 通过数字得到对应组的信息，打印： Lots
        print(m.group('word2')) # 通过名称得到对应组的信息，打印： of

        # 命名组 逆向引用
        p = re.compile(r'(?P<word>\b\w+)\s+(?P=word)') # 与记忆组一样用法, re.match() 函数同样不能这样用，会返回 None
        p = p.search('Paris in the the spring') #  r'(?P<word>\b\w+)\s+(?P=word)' 与 r'(?P<word>\b\w+)\s+\1' 效果一样
        print(p.group())  # 返回正则表达式匹配的所有内容，打印： the the
        print(p.groups()) # 返回一个包含字符串的元组，打印： ('the',)

        # 使用松散正则表达式,以判断罗马数字为例
        pattern = '''
            ^                   # beginning of string
            (M{0,3})            # thousands - 0 to 3 Ms
            (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 Cs),
                                #            or 500-800 (D, followed by 0 to 3 Cs)
            (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 Xs),
                                #        or 50-80 (L, followed by 0 to 3 Xs)
            (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 Is),
                                #        or 5-8 (V, followed by 0 to 3 Is)
            $                   # end of string
            '''
        print(re.search(pattern, 'M')) # 这个没有申明为松散正则表达式，按普通的来处理了，打印： None
        print(re.search(pattern, 'M', re.VERBOSE).groups()) # 打印： ('M', '', '', '')

        # (?iLmsux) 用法
        # 以下这三句的写法都是一样的效果，表示忽略大小写，打印： ['aa', 'AA']
        print(re.findall(r'(?i)(aa)', 'aa kkAAK s'))
        print(re.findall(r'(aa)', 'aa kkAAK s', re.I))
        print(re.findall(r'(aa)', 'aa kkAAK s', re.IGNORECASE))
        # 可以多种模式同时生效
        print(re.findall(r'(?im)(aa)', 'aa kkAAK s'))  # 直接在正则表达式里面写
        print(re.findall(r'(aa)', 'aa kkAAK s', re.I | re.M)) # 在参数里面写
        print(re.findall(r'(aa)', 'aa kkAAK s', re.I or re.M))

        # 预编译正则表达式解析的写法
        # romPattern = re.compile(pattern)  # 如果不是松散正则表达式,则这样写,即少写 re.VERBOSE 参数
        romPattern = re.compile(pattern, re.VERBOSE)
        print(romPattern.search('MCMLXXXIX').groups()) # 打印： ('M', 'CM', 'LXXX', 'IX')
        print(romPattern.search('MMMDCCCLXXXVIII').groups()) # 打印： ('MMM', 'DCCC', 'LXXX', 'VIII')
        # match()、search()、sub()、findall() 等等都可以这样用

    # match() vs search()
    #     match() 函数只检查 RE 是否在字符串开始处匹配，而 search() 则是扫描整个字符串。记住这一区别是重要的。
    #     match() 只报告一次成功的匹配，它将从 0 处开始；如果匹配不是从 0 开始的， match() 将不会报告它。
    #     search() 将扫描整个字符串，并报告它找到的第一个匹配。
    # 例：
        print(re.match('super', 'superstition').span())  # 打印： (0, 5)
        print(re.match('super', 'insuperable'))          # 打印： None
        print(re.search('super', 'superstition').span()) # 打印： (0, 5)
        print(re.search('super', 'insuperable').span())  # 打印： (2, 7)

