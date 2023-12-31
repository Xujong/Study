# Python计算机二级（七）文件和数据格式化

## 文件

文件是存储在辅助存储器上的一组数据序列。

**概念：数据的集合和抽象。**

包括文本文件和二进制文件。

### 文件的类型

#### 文本文件

一般由单一特定编码的字符组成，如UTF-8等。

内容统一展示和阅读，通过文本编辑软件打开。

可以看作是存储在磁盘上的长字符串。

#### 二进制文件

由比特0和比特1组成，没有统一编码，文件组织格式与用途有关。

按照非字符但有特定格式形式的文件，属于字节流。

**二者的区别：有没有统一编码**

### 文件的打开和关闭

不管是文本文件还是二进制文件，操作步骤都是“打开—操作—关闭”

#### 文件的打开

文件的打开使用open()方法实现：

```python
变量 = open(文件路径与文件名, 打开模式)
```

具体操作如下：

首先，在项目目录下创建一个文本文档，这里命名为a.txt，然后使用以下代码：

```python
file = open('a.txt', 'rt')  # 以文本文件方式打开文件
print(file.readline())  # 输出文件内容
file.close()  # 关闭文件
# 这里在Python3.9环境下会报错，解决方案：
file = open('a.txt', 'rt', 'encoding = utf-8')
```

| 打开模式 | 含义                                                    |
| -------- | ------------------------------------------------------- |
| r        | 只读模式，文件不存在时报错FileNotFoundError（默认值）   |
| w        | 覆盖写入模式，文件不存在则创建                          |
| x        | 创建写入模式，文件不存在则创建，存在报错FileExistsError |
| a        | 追加写模式，文件不存在则创建                            |
| b        | 二进制文件模式                                          |
| t        | 文本文件模式（默认值）                                  |
| +        | 在原功能基础上加入同时读写功能                          |

常用的组合：

| 模式代码 | 含义                                         |
| -------- | -------------------------------------------- |
| r        | 以文本方式只读打开文件，不能修改             |
| r+       | 以文本方式可读写打开文件                     |
| w        | 以文本方式打开空文件，写入内容并保存为新文件 |
| a+       | 以文本方式打开文件，追加写入内容并更新原文件 |
| rb       | 以二进制方式只读打开文件                     |
| close()  | 文件使用后，用close()方法关闭                |

在指定路径上创建一个文本文件a.txt，内容为“全国计算机等级考试”，打开并关闭该文件使用的代码为：

```python
PATH = 'D:\\test'
f = open(PATH+'a.txt', 'rt')
print(f.readline())
f.close()
```

**注意：**表示路径时，使用/或\\\，因为\表示转义字符

### 文件的读写

根据打开方式不同，文件的读写方式也不同

#### 读取文件

| 读写方法             | 含义                                                         |
| -------------------- | ------------------------------------------------------------ |
| f.read(size=-1)      | 读入整个文件内容，参数可选，表示读入前size长度的字符串或字节流 |
| f.readline(size=-1)  | 从文件中读入一行内容。参数可选，表示读入一行前size长度的字符串或字节流 |
| f.readlines(hint=-1) | 读入所有行，以每行为元素生成列表。参数可选，表示读入hint行   |
| f.seek(offset)       | 改变文件操作指针位置，0为开头，2为结尾                       |

**读取指针：**指向读取位置的指针。从文件中读取内容之后，读取指针向前进，再次读取的内容从新位置开始。当上次读取完全部内容的时候，指针指向文件结尾，因此不能继续读取。此时使用f.seek(0)将指针移到文件开始处即可继续操作。

##### 遍历文件

逐行遍历文件：

```python
f = open(文件路径及名称, 'r')
for line in f:
    print(line)
f.close()
```

#### 写入文件

| 方法                | 含义                                 |
| ------------------- | ------------------------------------ |
| f.write(s)          | 向文件写入字符串或字节流s            |
| f.writelines(lines) | 将一个元素为字符串的列表整体写入文件 |

f.write(s)需要显式地对输入内容加入换行符\n，否则不能自动换行

## 数据组织的维度

计算机处理的数据需要提前组织，表明数据之间的关系和逻辑，从而形成维度

### 一维数据

由对等关系的有序或无序数据构成，采用线性组织，对应数学中的序列

Python中列表、元组、集合均为一维数据

### 二维数据

由关联关系数据组成，采用二维表格方式组织，对应数学中的矩阵

常见的表格为二维数据

二维数据分行和列

### 高维数据

由键值对形式的数据组成，采用对象方式组织，可以进行嵌套

高位数据衍生出HTML、MySQL、JSON等具体数据组织的语法结构

## 一维数据处理

### 表示

最简单的数据组织类型，由于是线性结构，在Python中主要采用列表形式表示

采用列表时需要注意数据类型

### 存储

 思路：采用特殊字符分隔数据，包括：

1.空格分隔

2.逗号分隔

3.换行分隔

4.其他特殊符号（; :等）

#### 逗号分隔数据（CSV）

逗号分隔的存储格式为CSV格式，是一种通用的、相对简单的文件格式，在商业和科学上广泛应用

大部分编辑器支持直接读取或另存为为CSV格式，扩展名.csv

保存为CSV格式后，元素采用半角逗号分隔，形成一行

Python存储数据采用CSV格式，读入时读入成列表对象

列表对象输出为CSV：

```python
# 一列表lst
f=open('D:/city.csv', 'w')
f.write(','.join(lst)+'\n')  # 使用join()方法添加列表内容，使用逗号分隔
f.close()
```

### 处理

CSV文件$\to$读取一维数据$\to$表示为列表对象$\to$去除换行符（strip()方法）$\to$逗号分隔（split()方法）

从CSV获取的内容，其末尾有换行符，需要去掉换行符之后进行逗号分隔

## 二维数据的处理

### 表示

二维数据由多个一维数据构成，可认为是多层的一维数据。可采用二维列表表示，即列表的元素也是列表。

如：

```python
lst=[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

二维数据采用相同的数据类型和格式，便于操作。包括：第一维列表内的所有元素类型相同，第二维列表的元素均为列表。

### 存储

二维数据由一维数据组成，CSV格式存储

CSV格式的行为一维，文件为二维

写入内容：

```python
f = open('data.csv', 'w')
for row in lst:
    f.write(','.join(row)+'\n')
f.close()
```

### 处理

需要从CSV格式读取数据，表示为二维列表对象：

```python
f = open('data.csv', 'r')
lst=[]
for line in f:
    lst.append(line.strip('\n').split(','))
f.close()
print(lst)
```

对于二维列表的操作也与一维列表不同：

```python
for row in lst:  # 第row行
    for item in row:  # 第item列
        处理内容
```



