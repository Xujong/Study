# 命令行

## 1.1 Shell概览

### Shell

Shell是一种由终端运行的编程语言。

特点：

    1.多个操作组合成实体。
    2.获取输入，生成输出。
    3.有变量和状态。
    4.语法繁琐，使用特殊字符。

可以直接访问整个文件系统，完成所有任务。

### 路径和pwd

路径指定目录和文件的位置，可以是绝对或相对路径。

当前目录：“. ”；父目录：“..”

pwd命令：print working directory，打印当前工作目录完整的绝对路径。

### 主目录

主目录（~），提示符（$）。

提示符形式：<code>~ $</code> 或 <code>&lt;user&gt;@&lt;machine&gt;</code>

波浪线替换主目录路径。

### 目录命令

<code>ls</code>：打印目录下所有文件和子目录。

<code>ls 目录名</code>：在目录外执行该目录的ls操作。

<code>cd</code>：转到主目录。

<code>cd [path]</code>：转到指定路径下的目录。path可绝对可相对。

<code>cd ~/file</code>：转到主目录下的file目录。

<code>cd [direct]</code>：转到名为direct的目录，目录必须在当前目录下。

<code>cd ./[direct]</code>：转到当前目录下的direct目录。

<code>cd ../[direct]</code>：转到上一级目录中的direct目录。

<code>head [filename]</code>：显示文件前十行（用于检验文件生成）。

<code>tail [filename]</code>：显示文件后十行。

## 1.2 操作文件和目录

### 创建文件

<code>touch [filename]</code>：创建空的文本文件。

### 文本编辑

<code>cat [filename]</code>：打印文件完整内容。

<code>cat [file1] > [file2]</code>：将file1的内容复制到file2中。

<code>cat > [filename]</code>：将命令行中的文本插入到文件中。

<code>nano [filename]</code>：使用nano打开文件。

vim（vim, vi）或emacs（emacs）使用同上。

### 复制 重命名

<code>cp [source] [destination]</code>：从前者复制到后者。

<code>mv [origin] [target]</code>：前者重命名为后者。

<code>mv [origin] [direct]</code>：前者移动到后者。

### 创建目录

<code>mkdir [direct]</code>：创建新目录。

<code>mkdir [path]/[direct]</code>：路径末尾创建新目录。

不能在不存在的目录中创建新文件。

### 删除

<code>rm [filename]</code>：删除文件

<code>rm -r [direct]</code>：删除目录。-r表示递归。

### 标志和通配符

作为一种标志存在。

## 1.3 帮助文档

### 程序手册

<code>man [command]</code>：阅读指定命令的程序手册。

一个命令的结构：

<code>command [parament] -[option] --[variention]=[value]</code>

**参数**为操作对象。

**选项**告知程序以某种预定义方式运行，前面加“-”。

**变量**传递特定类型的信息，使用双减号“--”表示。赋值使用“=”

### less命令

less是man的内部程序，用于打开帮助文档。less也可用于查看其它文本文件，调用方法：

<code>less [filename]</code>

### 工具查询

<code>apropos [toolname]</code>：寻找相关工具。

如：<code>apropos "text editor"</code>表示寻找文本编辑器类工具。

### 重定向和管道组合程序

shell能将一个命令的输出发送到文件或直接传递给另一个程序。

重定向包括：<code>&gt;</code>创建新文件或覆盖已有文件；<code>&gt;&gt;</code>将内容添加到文件末尾。

管道将程序连接在一起，将一个程序的输出作为另一个程序的输入。如：<code>head -1 example.txt | tail -1</code>

## 1.4 权限与共享

有权限才能访问对应权限下的文件。有最高权限时可用功能不受限制。

### 类型

用户类型：user（拥有者），group（拥有特殊访问权限），other（其他）

访问类型：读取（r），写入（w）、执行（x）

### 权限管理

<code>ls -l [file]</code>：显示文件的权限内容。

<code>chown [-R] [[user]][:group] target1 [[target2 ..]]</code>：更改target的user和group的权限。如果使用-r且有多个目标时递归执行。

ls的-l表示长格式列出目录内容。显示时第一个字符表示类型，目录为d，链接为l，其余为-。

### 设置所有权

将文件file.txt归属于组grp：<code>chown :grp file.txt</code>

### 设置权限

<code>chown -r :grp [path]</code>使grp组的成员可以访问path下所有文件。

<code>chmod [options] &lt;mode&gt; &lt;path&gt;</code>更改path的权限为mode。

### 创建链接

创建到文件或程序的硬链接或符号链接，为一个文件创建多个引用，指向文件的同一个存储位置。

<code>ln -s prog [program]</code>：为程序创建一个符号链接。

### 连接到另一台计算机的命令

<code>ssh [user @ host]</code>：连接到另一个计算机。

<code>scp &lt;source_file&gt; [user @ host]:&lt;destination&gt;</code>：将文件从一台计算机复制到另一台计算机。

## 1.5 环境

使用echo命令打印字符串：<code>echo &lt;string&gt;</code>

<code>echo $USERAME</code>显示USERNAME环境变量的值

<code>export Varient="String"</code>给变量赋值，这样<code>echo $Varient</code>会打印变量的值。

| 环境变量    | 含义         | 环境变量            | 含义         | 环境变量   | 含义     |
|---------|------------|-----------------|------------|--------|--------|
| USER    | 用户名        | PATH            | 可执行程序的搜索目录 | PWD    | 当前目录   |
| EDITOR  | 默认文本编辑器    | GROUP           | 用户所属的组     | HOME/~ | Home目录 |
| DISPLAY | 通过网络连接显示图形 | LD_LIBRARY_PATH | 预编译库路径     |        |        |

环境变量存储相关环境的信息，提供字符串的缩写。

<code>env</code>：查看所有环境变量

### 保存环境变量

配置和添加环境变量：<code>~/.bashrc</code>文件，它是用户级的bash主配置文件。其余包括<code>.bah_profile,.profile</code>等。

<code>source .bashrc</code>：使改动在当前会话中立即生效。

### 运行程序时的PATH

环境为命令行提供找到程序位置的信息，如果在非标准位置运行，则必须指定路径。

直接使用程序的引用如<code>prog</code>并不能找到程序，即使在程序所在的位置，也需要使用<code>,/prog</code>来指示程序完整路径。若要不需要输入路径也能运行，则环境变量PATH中必须含有其目录。

添加到PATH：<code>export PATH=$PATH:&lt;path&gt;</code>。使用export设置PATH变量，PATH为变量，$PATH为旧PATH值，冒号后为添加到PATH已有列表的新目录。

### 设置别名

alias使用第二个参数替换第一个参数。如：

<code>ls 'ls --color'</code>，将ls替换为命令ls --color。

保存别名：<code>source ~/.bash_aliases</code>

## 1.6 使用bash编写脚本

含有shell命令的文件称为脚本，类似一个程序，可以多次执行。

扩展名为.sh，创建脚本文件：<code>vim explore.sh</code>

任何有效命令都可以存在bash脚本中。注释采用#。

创建后，需要设为可执行文件：<code>chmod a+x explore.sh</code>

使用：<code>./explore.sh</code>

