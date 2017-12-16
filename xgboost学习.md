## XGBoost调参指南
[参考-官网](http://xgboost.readthedocs.io/en/latest/////////how_to/param_tuning.html)
### 方法1
可按照**max_depth, min_child_weight colsamplt_bytree,eta**的顺序一个一个调，每次调的时候其他参数保持不变
### 方法2:防止过拟合
When you observe high training accuracy, but low tests accuracy, it is likely that you encounter overfitting problem.

There are in general two ways that you can control overfitting in xgboost

- The first way is to directly control model complexity
	This include **max_depth, min_child_weight and gamma**
- The second way is to add randomness to make training robust to noise
This include **subsample, colsample_bytree**
You can also reduce stepsize **eta**, but needs to remember to increase **num_round** when you do so.

## XGBoost参数
[参考1-官网](http://xgboost.readthedocs.io/en/latest/////parameter.html) [参考2-CSDN](http://m.blog.csdn.net/qimiejia5584/article/details/78622442)
<br>XGBoost参数类型分为三种：
- general parameters/一般参数：决定使用哪种booster，可选gbtree、dart、gblinear
- booster parameters/提升器参数：不同的booster选取不同的参数
- task parameters/任务参数：设置学习场景，比如回归、二类分类、多类分类等

| 参数类型 | 参数名 | 参数取值 | 默认值 | 说明 |
|-------- | --------| -------- | -------- | -------- |
| **general** | | | | |
|| booster | gbtree<br>dart<br>gblinear | gbtree | 指定使用的booster。前两种为树模型，后两种为线性模型。一般用默认的就好|
| | silent | 0、1 | 0 | 0表示输出运行信息，1表示采取静默模式 |
| | nthread | |系统允许的最大线程数 | 并发线程数 |
| | num_pbuffer | 不可指定 | | 缓冲池大小 |
| | num_feature | 不可指定 |  | 特征维度 |
| **booster** |  |  |  | |
| **Tree Booster** | **eta** | [0,1] |0.3| 学习率 |
| | **gamma** | [0,∞] |0 | 最小损失分裂。越大越保守，一般0.1、0.2这样子  |
| | **max_depth** | [0,∞] | 6 | 树的最大深度。越大模型越复杂，越容易过拟合 |
| | **min_child_weight** | [0,∞] | 1 | 子节点最小的权重。非常容易影响结果，参数数值越大，就越保守，越不会过拟合 |
| | max_delta_step | [0,∞] |0  | 最大delta的步数|
| | **subsample** | (0,1] | 1 | 子样本数目。是否只使用部分的样本进行训练，这可以避免过拟合化。默认为1，即全部用作训练。 |
| | **colsample_bytree** | (0,1] | 1 | 每棵树的列数（特征数） |
| | colsample_bylevel | (0,1] | 1 | 每一层的列数（特征数）|
| | lambda |  | 1 | L2正则化的权重 |
| | alpha |  | 0 | L1正则化的权重 |
| | tree_method | {‘auto’, ‘exact’, ‘approx’, ‘hist’, ‘gpu_exact’, ‘gpu_hist’}  | 'auto' |树构造的算法 |
| | sketch_eps | (0,1) |0.03 | 当tree_mothed='approx'才有用|
| | scale_pos_weight |  | 1 | 用在不均衡的分类中 |
| | updater |  | ’grow_colmaker,prune’ | 更新器 |
| | refresh_leaf |  |1 |当updater= refresh才有用 |
| | process_type | {‘default’, ‘update’} |’default’ |程序运行方式。update表示更新已有的树|
| | grow_policy |  {‘depthwise’, ‘lossguide’}  |’depthwise’ |控制新结点加入树的方式。当tree_mothod='hist'才有用|
| | max_leaves |  |0 | 要添加的最大结点数 |
| | max_bin |  | 256|当tree_mothod='hist'才有用|
| | predictor | {‘cpu_predictor’, ‘gpu_predictor’}  |’cpu_predictor’ | 算法预测时采用的方式|
| **Dart Booster**<br>（比Tree Booster增加了5个参数）  | sample_type| {“uniform”,“weighted”}  | "uniform"|选样方式 |
|  |normalize_type  |{"tree", "forest"} | "tree"|正则化方式 |
| | rate_drop   | [0.0, 1.0] |0.0| 舍弃上一轮树的比例|
|| one_drop |  | 0| 当值不为0的时候，至少有一棵树被舍弃|
| |skip	_drop  | [0.0, 1.0] |0.0 | 跳过舍弃树的程序的概率|
| **Linear Booster** | lambda |  |0 |L2正则化的权重 |
|  | alpha |  |0 | L1正则化的权重|
|  | lambda_bias |  |0 |L2正则化的偏爱 |
| **Tweedie Regression**<br>（三种booster共有的参数） | tweedie_variance_power | (1,2) |1.5 | 接近2代表接近gamma分布，接近1代表接近泊松分布|
| **task** |  |  | | |
|  | **objective** | “reg:linear” – 线性回归<br> “reg:logistic” – 逻辑回归<br>"binary:logistic" – 逻辑回归处理二分类（输出概率）<br>"binary:logitraw" – 逻辑回归处理二分类（输出分数）<br>"count:poisson" – 泊松回归处理计算数据（输出均值、max_delta_step参数默认为0.7）<br>"multi:softmax" – 采用softmax目标函数处理多分类问题（需要设定类别数"num_class"）<br>"multi:softprob" – 多分类（与上一搁一样，只是它的输出是ndata*nclass<br>"rank:pairwise" – 处理排位问题<br>"reg:gamma" – 用γ回归（返回均值）<br>"reg:tweedie" – 用特威迪回归| 'reg:linear' |定义学习任务及相应的学习目标 |
|  | base_score |  | 0.5 | 所有实例的初始预测得分 |
|  | eval_metric |  | 回归问题:rmse<br>分类问题:error<br>排位问题:map| 评价指标/性能度量。Python可通过list传递多个评价指标 |
|  | seed |  | 0  | 随机数种子。每次取一样的seed可得到相同的随机划分 |
| **Command Line** |  |  | | |
||**num_round**||| boosting的轮数/迭代次数|

xgb使用sklearn接口会改变的函数名是：[官网](http://xgboost.readthedocs.io/en/latest/////python/python_api.html#module-xgboost.sklearn)
- eta -> learning_rate
- lambda -> reg_lambda
- alpha -> reg_alpha