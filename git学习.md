*git是分布式版本控制系统，跟踪管理的是修改，而非文件*

## 基本操作
1.安装git: `sudo apt-get install git`    
安装后设置： `git config --global user.name "Your Name"`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`git config --global user.email "email@example.com"`  
2.初始化目录为git仓库： **`git init`**  
&nbsp;&nbsp;&nbsp;把文件添加到仓库：**`git add <file>`**  
&nbsp;&nbsp;&nbsp;把文件提交到仓库：**`git commit -m <说明>`**  
3.查看仓库当前的状态：**`git status`**  
&nbsp;&nbsp;&nbsp;查看修改了哪些内容：`git diff`  
4.查看提交历史：**`git log (--pretty=oneline)`**  
&nbsp;&nbsp;&nbsp;查看命令历史：`git reflog`  
&nbsp;&nbsp;&nbsp;回到上一版本：`git reset --hard HEAD^ `  
5.工作区和版本库间的关系  
&nbsp;&nbsp;&nbsp;&nbsp;![工作区和版本库](https://static.liaoxuefeng.com/files/attachments/919020037470528/0)  
6.撤销修改  
&nbsp;&nbsp;&nbsp;修改了但是未git add: `git checkout -- <file>`  
&nbsp;&nbsp;&nbsp;git add了但未git commit: `git reset HEAD <file>`  
7.删除文件：在目录中用rm命令删除文件后  
&nbsp;&nbsp;&nbsp;&nbsp;若确实要删除文件:`git rm <file>`  
&nbsp;&nbsp;&nbsp;&nbsp;若删错了，可恢复：`git checkout -- <file>`

## 远程仓库  
1.关联远程库:**`git remote add origin <远程库地址>`** (关联后远程库的名字就是origin)  
2.推送：**`git push (-u) origin BRANCH`** (-u第一次推送时加，将本地当前的分支推送到远程的BRANCH分支）  
         `git push origin 本地分支名:远程分支名` (将本地某分支推送到远程某分支)
         
3.将远程BRANCH分支与本地整合：**`git pull origin BRANCH`** (等同于git fetch和git merge)  
         `git pull origin 远程分支名:本地分支名`

4.克隆：**`git clone <远程库地址>`** (无需先进行关联)  
5.查看远程仓库地址：`git remote -v`

## 分支管理  
1.查看当前所有分支：`git branch`   (`git branch -a`查看本地和远程的分支)  
2.创建分支：`git branch <name>`  
3.切换分支：`git checkout <name>`  
4.创建+切换分支：`git checkout -b <name>`  
5.合并某分支到当前分支：`git merge <name>`  
6.删除分支：`git branch -d <name>`  
7.分支冲突 （1）手动解决 （2）解决冲突后查看分支合并图：`git log --graph (--pretty=oneline)`  
8.分支管理策略、Bug分支、Feature分支、多人协作（实际开发中用)参照[Git教程-廖雪峰的官方网站](https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/)

9.比较两个分支的差异：

`git diff branch1 branch2 --stat`   //显示出所有有差异的文件列表

`git diff branch1 branch2 文件名(带路径)`   //显示指定文件的详细差异

`git diff branch1 branch2`      //显示出所有有差异的文件的详细差异

10. 查看本地分支与远程分支的关联关系：`git branch -vv`

11. 更新远程分支列表： `git remote update origin --prune`

12. 拉取远程分支并创建本地分支 `git checkout -b 本地分支名x origin/远程分支名x` （采用此种方法建立的本地分支会和远程分支建立映射关系）
