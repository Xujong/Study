# Python计算机二级（四）组合数据类型

## 基本概念

计算机需要对一组数据进行统一处理，这样的一组数据叫做组合数据类型。

### 集合类型

元素集合（类似数学意义上的），元素之间无序且符合唯一性。

集合类型没有索引和位置的概念。

定义语法：

```python
set = {元素1, 元素2, ...}
```

用途：元素去重

#### 元素

1.集合中的元素不可重复

2.只能是不可变数据类型。列表、字典、集合不能作为集合的元素（与数学概念的不同）

#### 特点

1.输出顺序和输入顺序可能不一致（无序性）

2.能够过滤掉多余元素，输入元素时直接去重（唯一性）

3.元素不能比较，不能排序（无序性）

#### 操作符

| 操作符 | 运算                  |
| ------ | --------------------- |
| A-B    | $A-A\cap B$（差集）   |
| A&B    | $A\cap B$（交集）     |
| A^B    | $A+B-A\cap B$（补集） |
| A\|B   | $A+B$（并集）         |

#### 函数

| 函数       | 功能                                 |
| ---------- | ------------------------------------ |
| s.add()    | 添加元素                             |
| s.remove() | 移除元素                             |
| s.clear()  | 清空集合                             |
| len(s)     | 集合的元素个数                       |
| x in s     | x是s的元素                           |
| x not in s | x不是s的元素                         |
| set()      | 将其它组合类型转化为集合或生成空集合 |

### 序列类型

一个元素向量，元素有先后，通过序号访问。元素可重复。

典型代表：字符串类型、列表类型、元组类型

#### 访问

序列元素的访问，使用索引进行。索引使用中括号表示。

索引的表示

| 元素编号 | 正向递增索引 | 反向递减索引 |
| -------- | ------------ | ------------ |
| 1        | 0            | -6           |
| 2        | 1            | -5           |
| 3        | 2            | -4           |
| 4        | 3            | -3           |
| 5        | 4            | -2           |
| 6        | 5            | -1           |

#### 操作符

| 操作符     | 功能                       |
| ---------- | -------------------------- |
| x in s     | x是s的元素                 |
| x not in s | x不是s的元素               |
| s+t        | 连接序列                   |
| s*n        | 将序列复制n次              |
| s[i]       | 序列的第i个元素            |
| s[i:j]     | 切片，序列的第i到j-1个元素 |
| s[i:j:k]   | 切片，k为步长              |
| len(s)     | 元素个数                   |
| min(s)     | 最小元素                   |
| max(s)     | 最大元素                   |
| s.index(x) | 元素x第一次出现位置        |
| s.count(x) | x出现的总次数              |

#### 元组类型tuple

使用小括号容纳元素，属于常值类型。

操作与序列相同。

### 映射类型

键值对形式。元素以键值对(key, value)形式存在。

典型类型：字典类型

## 列表

包含0个或多个元素的有序序列，属于序列类型。

没有长度限制，元素类型可以不同。

### 创建

```python
l = [元素1, 元素2, 元素3, ...]
list(x)  # x表示要被转换为列表的变量
list()  # sheng'c
```

### 索引

列表的基本操作之一，用于获得列表元素信息。

沿用序列类型的索引方式，使用中括号为索引操作符。

索引不能超过范围，否则报错IndexError。

#### 索引的使用

```python
list[3]
list[-5]
list[-len(list)] # 列表第一个元素
```

#### 遍历列表

```python
for i in 列表或列表切片:
    处理代码块
# 通过索引遍历
for i in 索引范围:
    处理代码块
```

#### 切片

用于获得列表片段的基本操作。切片得到的类型也是列表。

使用方式：

```python
list[n:m] # 元素l[n]起，l[m]结束
list[n:m:k] # 元素l[n]起，到l[m]结束，步长为i
```

**Python表示区间使用“:”，表示枚举使用“,”**

切片可以混合使用正向递增序号和反向递减序号，以正负号分辨。一般要求序号位置n在m前，若等于或反向，返回空列表。未设置步长时默认为1。

### 列表操作

| 函数      | 功能                                   |
| --------- | -------------------------------------- |
| len(list) | 获取列表长度（元素个数）               |
| min(list) | 列表最小元素                           |
| max(list) | 列表最大元素                           |
| list(x)   | 将x转变为列表类型。x为空时创建空列表。 |
| sort()    | 对列表永久性排序                       |
| sorted()  | 对列表临时性排序                       |

| 方法         | 功能                 |
| ------------ | -------------------- |
| append(x)    | 将x添加至列表结尾    |
| insert(i, x) | 在索引为i处添加x     |
| clear()      | 删除所有元素         |
| pop(i)       | 弹出第i个元素        |
| remove()     | 删除重复元素的第一个 |
| reverse()    | 永久性倒置列表顺序   |
| copy()       | 复制列表所有元素     |

del操作：删除

```python
del list[i] # 删除索引为i的元素
del list[n:m] # 删除切片
del list[n:m:k] # 删除带步长切片
```

****

## 字典

映射类型的一种。使用键值对这种一一对应的方式组织数据，方便通过键来查找值。

### 创建

```python
dic = {键1: 值1, 键2: 值2, 键3: 值3, 键4: 值4, 键5: 值5, ...}
dic = {} # 创建空字典
```

### 说明

1.键不能重复，且必须是不可修改数据类型。列表不能做键。重复的键使用后一个的值覆盖。

2.字典的各个元素没有顺序

3.直接使用大括号，只能生成字典，不能生成集合

### 索引

字典中，键是值的索引，因此直接利用键值对索引元素即可。

语法：

```python
变量 = dic[键] # 使用键作为下标进行索引
dic[键] = 值 # 此语句可用于修改键对应的值或添加键值对
```

键可用等值变量名代替。

**注意：字典不能使用值进行索引**

### 操作

#### 函数和方法

| 函数   | 功能                   |
| ------ | ---------------------- |
| len(d) | 字典长度（键值对个数） |
| min(d) | 字典键的最小值         |
| max(d) | 字典键的最大值         |
| dict() | 生成空字典             |

| 方法              | 功能                                        |
| ----------------- | ------------------------------------------- |
| keys()            | 返回键列表                                  |
| values()          | 返回值列表                                  |
| items()           | 返回键值对列表                              |
| get(key, default) | 键存在时返回相应值，否则返回default         |
| pop(key, default) | 键存在时弹出键值对，返回值，否则返回default |
| popitem()         | 从字典中随机弹出一个键值对，以元组形式返回  |
| clear()           | 删除字典中所有键值对                        |

前三个方法对应的类型是特殊的：

```python
dic = {'A': 1, 'B': 2, 'C': 3}
print(dic.keys())
print(dic.values())
print(dic.items())
# 输出
dict_keys(['A', 'B', 'C'])
dict_values([1, 2, 3])
dict_items([('A', 1), ('B', 2), ('C', 3)])
```

#### 其他操作

1.删除元素

```python
dic = {'A': 1, 'B': 2, 'C': 3}
del dic['A']
print(dic)
# 输出
{'B': 2, 'C': 3}
```

2.判断元素是否在字典中

```python
dic = {'A': 1, 'B': 2, 'C': 3}
print('B' in dic)
print('D' in dic)
print('C' not in dic)
# 输出
True
False
False
```

3.遍历字典元素

语法：

```python
for 变量 in 字典:
    语句块
```

循环中的的变量是字典的键，需要返回值时要用到get()方法：

```python
dic = {'A': 1, 'B': 2, 'C': 3}
for i in dic:
    print(i, dic.get(i))
# 输出
A 1
B 2
C 3
```

