# Test Cases: 组织架构管理功能

## Overview
- **Feature**: 组织架构管理
- **Requirements Source**: `data/问我架构需求.md`
- **Test Coverage**: 覆盖所有P0/P1需求，包括架构配置、账号关联、架构列表报表、账号管理
- **Last Updated**: 2026-04-03

## Requirements List

| ID | Requirement | Priority |
|----|-------------|----------|
| REQ-001 | 架构配置：允许用户定义和管理组织层级，逐级创建，每个项目每个层级只能存在一个 | P0 |
| REQ-002 | 组织架构创建：必须逐级创建，有一级才能选二级，选择最小层级后无法再添加其他层级 | P0 |
| REQ-003 | 组织架构删除：删除架构会级联删除其下子项和下级架构，删除前需要二次确认 | P0 |
| REQ-004 | 架构子项创建：一级子项无需上级，非一级必须关联一个上级子项，同层级下子项名称不能重复 | P0 |
| REQ-005 | 架构子项展示：显示完整层级路径，如 一级-二级-当前子项 | P0 |
| REQ-006 | 社媒监控：组织架构下拉框仅允许选择最小层级的架构子项 | P0 |
| REQ-007 | 社媒监控：支持批量关联架构 | P0 |
| REQ-008 | 架构列表：按架构层级维度tab切换展示，展示各维度下数据统计 | P0 |
| REQ-009 | 架构列表：导出功能，按筛选条件全量导出，字段与页面一致 | P0 |
| REQ-010 | 架构账号管理：展示最小层级架构子项，显示状态（正常/有失效/待录入） | P0 |
| REQ-011 | 架构账号管理：重置功能-清空账号组织架构，需要二次确认 | P0 |
| REQ-012 | 架构账号管理：导出功能，包含各平台账号数量和授权链接 | P0 |
| REQ-013 | 短链生成：每次生成独立短链，通过哈希缓存避免重复，不影响已有短链 | P0 |
| REQ-014 | 社媒监控详情：显示完整架构路径，支持编辑 | P0 |
| REQ-015 | 架构名称在同一项目中不能重复 | P0 |
| REQ-016 | 删除架构子项需要二次确认 | P0 |

---

## Test Case Categories

### 1. Functional Tests

#### TC-F-001: 创建一级组织架构
- **Requirement**: REQ-001, REQ-002, REQ-015
- **Priority**: High
- **Preconditions**:
  - 用户已登录系统
  - 进入【设置】->【组织架构】->【架构配置】tab
  - 当前项目无任何架构层级
- **Test Steps**:
  1. 点击"创建组织架构"按钮
  2. 架构层级选择"一级层级"
  3. 输入架构名称"国家"
  4. 点击保存
- **Expected Results**:
  - 组织架构创建成功
  - 列表中显示新建的"国家"一级架构
  - 可以开始创建二级层级
- **Postconditions**: 项目中存在一个一级架构"国家"

#### TC-F-002: 创建二级组织架构
- **Requirement**: REQ-001, REQ-002
- **Priority**: High
- **Preconditions**:
  - 已存在一级架构"国家"
  - 在架构配置页面
- **Test Steps**:
  1. 点击"创建组织架构"按钮
  2. 检查架构层级下拉选项
  3. 选择"二级层级"
  4. 输入架构名称"省份"
  5. 点击保存
- **Expected Results**:
  - 二级架构"省份"创建成功
  - 架构层级下拉中二级可选，一级仍存在
  - 现在可以创建三级/最小层级
- **Postconditions**: 项目中有一级"国家"，二级"省份"

#### TC-F-003: 创建到最小层级组织架构
- **Requirement**: REQ-002
- **Priority**: High
- **Preconditions**:
  - 已存在一级"国家"，二级"省份"
  - 在架构配置页面
- **Test Steps**:
  1. 点击"创建组织架构"按钮
  2. 选择"最小层级"
  3. 输入架构名称"城市"
  4. 点击保存
  5. 再次点击"创建组织架构"，查看下拉选项
- **Expected Results**:
  - 最小层级"城市"创建成功
  - 再次创建时，架构层级下拉框中没有其他可选项（已到最小层级）
- **Postconditions**: 架构层级完整：国家 -> 省份 -> 城市（最小）

#### TC-F-004: 创建一级架构子项
- **Requirement**: REQ-004, REQ-005
- **Priority**: High
- **Preconditions**:
  - 已存在一级架构"国家"
  - 在架构配置页面
- **Test Steps**:
  1. 在"国家"架构下点击"创建子项"
  2. 检查是否显示"关联上级"字段
  3. 输入子项名称"中国"
  4. 点击保存
- **Expected Results**:
  - 不显示"关联上级"字段（因为是一级子项）
  - 子项"中国"创建成功
  - 子项显示名称为"中国"
- **Postconditions**: 一级架构"国家"下有子项"中国"

#### TC-F-005: 创建二级架构子项并关联上级
- **Requirement**: REQ-004, REQ-005
- **Priority**: High
- **Preconditions**:
  - 一级架构"国家"存在子项"中国"
  - 二级架构"省份"已创建
- **Test Steps**:
  1. 在"省份"架构下点击"创建子项"
  2. 检查"关联上级"下拉框
  3. 选择上级子项"中国"
  4. 输入子项名称"广东"
  5. 点击保存
- **Expected Results**:
  - "关联上级"下拉框显示所有一级子项（中国）
  - 子项"广东"创建成功
  - 子项显示完整路径："中国-广东"
- **Postconditions**: 二级子项"广东"关联到一级子项"中国"

#### TC-F-006: 创建最小层级子项并关联上级
- **Requirement**: REQ-004, REQ-005, REQ-006
- **Priority**: High
- **Preconditions**:
  - 存在一级国家->中国，二级省份->广东，最小层级城市
- **Test Steps**:
  1. 在"城市"架构下点击"创建子项"
  2. 关联上级选择"中国-广东"
  3. 输入子项名称"广州"
  4. 点击保存
- **Expected Results**:
  - 创建成功
  - 子项显示完整路径："中国-广东-广州"
- **Postconditions**: 完整层级创建完成

#### TC-F-007: 删除组织架构（级联删除）
- **Requirement**: REQ-003
- **Priority**: High
- **Preconditions**:
  - 存在完整层级：国家(一级) -> 省份(二级) -> 城市(最小)
  - 各层级下都有子项
- **Test Steps**:
  1. 点击删除一级架构"国家"
  2. 确认弹出二次确认窗口
  3. 点击确认删除
- **Expected Results**:
  - 弹出二次确认窗口提示删除会级联删除下级
  - 删除成功后
    - 一级架构"国家"被删除
    - 二级架构"省份"被级联删除
    - 最小层级"城市"被级联删除
    - 所有子项都被删除
- **Postconditions**: 项目回到无架构状态

#### TC-F-008: 删除架构子项
- **Requirement**: REQ-016
- **Priority**: High
- **Preconditions**:
  - 存在一级架构子项"中国"
- **Test Steps**:
  1. 点击删除子项"中国"
  2. 弹出二次确认
  3. 确认删除
- **Expected Results**:
  - 弹出二次确认窗口
  - 确认后子项删除成功
  - 不影响架构层级本身
- **Postconditions**: 架构层级"国家"仍存在，子项"中国"被删除

#### TC-F-009: 社媒监控组织架构下拉仅显示最小层级
- **Requirement**: REQ-006
- **Priority**: High
- **Preconditions**:
  - 完整层级已创建：国家->省份->城市（最小）
  - 已有子项：中国->广东->广州
  - 进入社媒监控页面
- **Test Steps**:
  1. 点击组织架构下拉框
  2. 查看可选项
- **Expected Results**:
  - 下拉框中只显示最小层级的子项（广州）
  - 不显示一级、二级子项
  - 支持模糊搜索
- **Postconditions**: 页面状态不变

#### TC-F-010: 批量关联架构到社媒账号
- **Requirement**: REQ-007
- **Priority**: High
- **Preconditions**:
  - 存在最小层级子项"中国-广东-广州"
  - 社媒监控页面有多个未关联架构的账号
  - 进入社媒监控页面
- **Test Steps**:
  1. 勾选多个账号
  2. 点击"批量关联架构"按钮
  3. 弹窗中选择目标架构子项
  4. 确认关联
- **Expected Results**:
  - 弹窗打开，可选择架构
  - 确认后所有勾选账号关联到选定架构
  - 刷新后账号的组织架构字段显示正确
- **Postconditions**: 选中账号已关联到目标架构

#### TC-F-011: 架构列表按维度tab切换展示
- **Requirement**: REQ-008
- **Priority**: High
- **Preconditions**:
  - 已创建三级架构：国家、省份、城市（最小）
  - 已创建各级子项
  - 进入【数据监控】->【架构列表】
- **Test Steps**:
  1. 查看tab标签
  2. 点击"国家"tab
  3. 查看列表内容
  4. 点击"省份"tab
  5. 查看列表内容
- **Expected Results**:
  - tab按层级从高到低排序：国家、省份、城市
  - "国家"tab展示所有一级子项，每行一个国家子项
  - "省份"tab展示所有二级子项，每行一个省份子项
  - 表头第一个字段名称随tab维度变化
- **Postconditions**: 页面状态正常

#### TC-F-012: 架构列表统计数据正确展示
- **Requirement**: REQ-008
- **Priority**: High
- **Preconditions**:
  - 架构列表页面，已选择维度tab
  - 已有账号关联到各个架构子项
- **Test Steps**:
  1. 查看各列数据
  2. 检查账号数量、播放量、粉丝数量、内容数、点赞数等字段
- **Expected Results**:
  - 所属架构列显示完整上级路径（如：中国/广东）
  - 账号数量显示该架构下绑定的账号数
  - 播放量是该架构下所有账号播放量总和
  - 粉丝数量是所选日期范围最后一天的粉丝数
  - 粉丝增长量 = 最后一天粉丝数 - 第一天粉丝数
  - 各项统计数据正确累加
- **Postconditions**: 页面状态不变

#### TC-F-013: 架构列表导出
- **Requirement**: REQ-009
- **Priority**: High
- **Preconditions**:
  - 架构列表页面有数据
  - 已设置筛选条件
- **Test Steps**:
  1. 点击导出按钮
  2. 下载文件
  3. 查看导出内容
- **Expected Results**:
  - 导出成功开始下载
  - Excel中包含当前筛选条件下的所有数据
  - 导出字段与页面展示一致（除操作列）
  - 数据量正确
- **Postconditions**: 数据已导出

#### TC-F-014: 架构账号管理列表展示正确状态
- **Requirement**: REQ-010
- **Priority**: High
- **Preconditions**:
  - 进入【组织架构】->【架构账号管理】tab
- **Test Steps**:
  1. 查看列表
  2. 检查三种状态
- **Expected Results**:
  - 所有最小层级子项都展示
  - 状态"正常"：该架构下所有账号授权都正常
  - 状态"有失效"：该架构下存在至少一个授权失效账号
  - 状态"待录入"：该架构下没有任何账号
  - 所属架构列显示完整路径（如：广东省-广州市-天河区）
  - 各平台账号数量格式：正常授权数量/授权失效数量
  - 红色标记显示失效账号数量
- **Postconditions**: 页面状态不变

#### TC-F-015: 架构账号管理重置单个账号
- **Requirement**: REQ-011
- **Priority**: High
- **Preconditions**:
  - 架构账号管理页面
  - 存在一个已关联架构的账号
- **Test Steps**:
  1. 点击查看账号，打开弹窗
  2. 找到目标账号，点击重置
  3. 查看二次确认弹窗文案
  4. 确认重置
- **Expected Results**:
  - 弹窗展示该架构下所有账号，失效账号排在最前面并标红
  - 点击重置弹出二次确认
  - 确认文案："重置后该账号将无任何组织架构，确定清空吗"
  - 确认后该账号组织架构被清空，变为无组织架构状态
  - 架构账号管理列表中账号数量更新
- **Postconditions**: 目标账号组织架构已清空

#### TC-F-016: 架构账号管理导出
- **Requirement**: REQ-012
- **Priority**: High
- **Preconditions**:
  - 架构账号管理页面有数据
- **Test Steps**:
  1. 点击导出
  2. 下载并查看文件
- **Expected Results**:
  - 导出成功
  - 包含字段：架构名称、所属架构、状态、各平台账号数量、各平台授权链接
  - 数据完整正确
- **Postconditions**: 数据已导出

#### TC-F-017: 短链生成不同参数生成不同短链
- **Requirement**: REQ-013
- **Priority**: High
- **Preconditions**:
  - 进入授权页面
  - 用户已登录
- **Test Steps**:
  1. 选择Facebook平台，账号标签"内容"，生成短链A
  2. 保持客户未授权状态，再次选择相同平台，账号标签"视频"，生成短链B
  3. 检查短链A和短链B是否互相影响
- **Expected Results**:
  - 生成两个不同的短链
  - 短链A参数保持不变，不受短链B影响
  - 两个短链都能正常使用
- **Postconditions**: 两个短链都存在

#### TC-F-018: 相同参数生成短链返回已有缓存
- **Requirement**: REQ-013
- **Priority**: Medium
- **Preconditions**:
  - 已生成过一次参数（用户ID+平台+账号标签+...）的短链
- **Test Steps**:
  1. 使用完全相同的参数再次请求生成短链
  2. 检查返回结果
- **Expected Results**:
  - 返回已存在的短链，不生成新的
  - 从缓存读取，响应快速
- **Postconditions**: 数据库中只有一条记录

#### TC-F-019: 社媒监控详情显示完整架构路径
- **Requirement**: REQ-014
- **Priority**: Medium
- **Preconditions**:
  - 账号已关联完整层级架构：中国-湖北-武汉
  - 进入该账号的社媒监控详情页
- **Test Steps**:
  1. 查找"所属架构"字段
  2. 查看展示内容
- **Expected Results**:
  - 显示完整路径直到最小层级："中国-湖北-武汉"
- **Postconditions**: 页面状态不变

#### TC-F-020: 社媒监控详情编辑所属架构
- **Requirement**: REQ-014
- **Priority**: Medium
- **Preconditions**:
  - 账号已有关联架构
  - 在社媒监控详情页
- **Test Steps**:
  1. 点击编辑所属架构
  2. 选择新的最小层级架构子项
  3. 保存
- **Expected Results**:
  - 可以重新选择
  - 保存成功后所属架构更新为新选择
- **Postconditions**: 账号所属架构已更新

---

### 2. Edge Case Tests

#### TC-E-001: 同一项目中创建重复架构名称
- **Requirement**: REQ-015
- **Priority**: High
- **Preconditions**:
  - 已存在一级架构"国家"
  - 在创建组织架构页面
- **Test Steps**:
  1. 再次创建架构，名称仍输入"国家"
  2. 点击保存
- **Expected Results**:
  - 保存失败
  - 提示"同一个项目中架构名称不能重复"
- **Postconditions**: 数据库无新增，原数据不变

#### TC-E-002: 同一层级同一项目中创建重复子项名称
- **Requirement**: REQ-004
- **Priority**: High
- **Preconditions**:
  - 一级架构"国家"下已有子项"中国"
- **Test Steps**:
  1. 再次创建一级子项，名称"中国"
  2. 点击保存
- **Expected Results**:
  - 保存失败
  - 提示"同一层级中子项名称不能重复"
- **Postconditions**: 无新增数据

#### TC-E-003: 空架构名称提交
- **Requirement**: REQ-001
- **Priority**: Medium
- **Preconditions**:
  - 在创建组织架构页面
- **Test Steps**:
  1. 选择架构层级
  2. 架构名称留空
  3. 点击保存
- **Expected Results**:
  - 保存失败
  - 提示"架构名称不能为空"
- **Postconditions**: 无数据创建

#### TC-E-004: 空子项名称提交
- **Requirement**: REQ-004
- **Priority**: Medium
- **Preconditions**:
  - 在创建架构子项页面
- **Test Steps**:
  1. 选择上级（如需要）
  2. 子项名称留空
  3. 点击保存
- **Expected Results**:
  - 保存失败
  - 提示"子项名称不能为空"
- **Postconditions**: 无数据创建

#### TC-E-005: 删除最后一个层级后可再次创建层级
- **Requirement**: REQ-002, REQ-003
- **Priority**: Medium
- **Preconditions**:
  - 已创建到最小层级
  - 现在删除最小层级
- **Test Steps**:
  1. 删除最小层级架构
  2. 尝试创建新的层级
- **Expected Results**:
  - 删除成功后，可以继续创建新的层级
  - 原来的倒数第二级变为可添加下一级
- **Postconditions**: 可以重新创建新的层级结构

#### TC-E-006: 架构子项层级路径很深展示
- **Requirement**: REQ-005
- **Priority**: Low
- **Preconditions**:
  - 创建了5级架构：洲->国家->省份->城市->区县
  - 每一级都创建了子项并正确关联
- **Test Steps**:
  1. 查看最深层级子项的显示名称
- **Expected Results**:
  - 完整展示路径："亚洲-中国-广东-广州-天河区"
  - 显示不溢出，布局正常
- **Postconditions**: 展示正常

#### TC-E-007: 架构下没有子项删除架构
- **Requirement**: REQ-003
- **Priority**: Low
- **Preconditions**:
  - 创建了架构但没有创建任何子项
- **Test Steps**:
  1. 删除该架构
- **Expected Results**:
  - 删除成功
  - 不影响其他层级
- **Postconditions**: 架构删除成功

#### TC-E-008: 筛选条件下导出零数据
- **Requirement**: REQ-009
- **Priority**: Low
- **Preconditions**:
  - 在架构列表页面
  - 设置筛选条件后没有匹配数据
- **Test Steps**:
  1. 点击导出
- **Expected Results**:
  - 导出空文件或提示"无数据可导出"
  - 不报错
- **Postconditions**: 操作完成

#### TC-E-009: 所有账号都失效状态展示
- **Requirement**: REQ-010
- **Priority**: Medium
- **Preconditions**:
  - 某个架构子项下所有账号都失效
- **Test Steps**:
  1. 查看架构账号管理列表中该条目的状态
- **Expected Results**:
  - 状态显示为"有失效"
  - 账号数量显示为 (0/全部)
- **Postconditions**: 展示正常

#### TC-E-010: 空项目创建完整层级
- **Requirement**: REQ-001, REQ-002
- **Priority**: Medium
- **Preconditions**:
  - 新项目，没有任何架构
- **Test Steps**:
  1. 直接创建最小层级架构
- **Expected Results**:
  - 允许创建（规则说最小层级一直可选）
  - 创建成功，这是唯一层级
  - 无法再创建其他层级
- **Postconditions**: 项目只有一个最小层级架构

---

### 3. Error Handling Tests

#### TC-ERR-001: 未选择架构层级点击保存
- **Requirement**: REQ-001
- **Priority**: Medium
- **Preconditions**:
  - 在创建组织架构弹窗
- **Test Steps**:
  1. 输入架构名称
  2. 不选择架构层级
  3. 点击保存
- **Expected Results**:
  - 保存失败
  - 提示"请选择架构层级"
- **Postconditions**: 弹窗保持打开，可重新输入

#### TC-ERR-002: 二级架构子项不选择上级保存
- **Requirement**: REQ-004
- **Priority**: High
- **Preconditions**:
  - 在创建二级架构子项弹窗
- **Test Steps**:
  1. 输入子项名称
  2. 不选择上级子项
  3. 点击保存
- **Expected Results**:
  - 保存失败
  - 提示"请选择上级子项"
- **Postconditions**: 弹窗保持打开

#### TC-ERR-003: 删除架构取消二次确认
- **Requirement**: REQ-003
- **Priority**: Medium
- **Preconditions**:
  - 有一个可删除的架构
- **Test Steps**:
  1. 点击删除架构
  2. 弹出二次确认后点击取消
- **Expected Results**:
  - 弹窗关闭
  - 架构未被删除
- **Postconditions**: 架构仍然存在

#### TC-ERR-004: 删除子项取消二次确认
- **Requirement**: REQ-016
- **Priority**: Medium
- **Preconditions**:
  - 有一个可删除的子项
- **Test Steps**:
  1. 点击删除子项
  2. 二次确认点击取消
- **Expected Results**:
  - 弹窗关闭
  - 子项未被删除
- **Postconditions**: 子项仍然存在

#### TC-ERR-005: 重置账号取消二次确认
- **Requirement**: REQ-011
- **Priority**: Medium
- **Preconditions**:
  - 打开账号列表弹窗
  - 有一个已关联架构的账号
- **Test Steps**:
  1. 点击重置
  2. 二次确认点击取消
- **Expected Results**:
  - 弹窗关闭
  - 账号组织架构未改变
- **Postconditions**: 账号架构保持不变

#### TC-ERR-006: 没有权限访问架构页面
- **Requirement**: All
- **Priority**: Low
- **Preconditions**:
  - 用户无此项目权限
- **Test Steps**:
  1. 直接URL访问组织架构页面
- **Expected Results**:
  - 提示无权限
  - 禁止访问
- **Postconditions**: 无数据泄露

#### TC-ERR-007: 关联已删除架构子项
- **Requirement**: REQ-006
- **Priority**: Medium
- **Preconditions**:
  - 架构子项被删除，但账号页面缓存还在
- **Test Steps**:
  1. 尝试选择已删除的架构子项关联
- **Expected Results**:
  - 下拉框不显示已删除子项
  - 无法选择
  - 保存失败提示架构不存在
- **Postconditions**: 账号不关联已删除架构

#### TC-ERR-008: 编辑架构修改名称为已有名称
- **Requirement**: REQ-015
- **Priority**: Medium
- **Preconditions**:
  - 已有架构A名称"国家"，架构B名称"省份"
  - 正在编辑架构B
- **Test Steps**:
  1. 将架构B名称改为"国家"
  2. 保存
- **Expected Results**:
  - 保存失败
  - 提示名称重复
- **Postconditions**: 架构B名称不变

---

### 4. State Transition Tests

#### TC-ST-001: 层级创建状态转换
- **Requirement**: REQ-002
- **Priority**: High
- **Preconditions**:
  - 空项目
- **Test Steps**:
  1. 初始状态：无层级 -> 可选项：一级、最小层级
  2. 创建一级 -> 检查可选项
  3. 创建二级 -> 检查可选项
  4. 创建最小 -> 检查可选项
- **Expected Results**:
  - 步骤1：只显示一级和最小层级可选
  - 步骤2：一级创建后，二级、最小可选
  - 步骤3：二级创建后，最小可选
  - 步骤4：最小创建后，没有可选项
  - 同一级架构只能存在一个，创建后该级从下拉移除
- **Postconditions**: 层级创建完成，状态正确

#### TC-ST-002: 删除中间层级对上下层级的影响
- **Requirement**: REQ-003
- **Priority**: High
- **Preconditions**:
  - 完整层级：一级(A) -> 二级(B) -> 最小(C)
  - 各级都有子项，子项正确关联上级
- **Test Steps**:
  1. 删除二级架构B
  2. 检查结果
- **Expected Results**:
  - 二级B及其所有子项被删除
  - 最小C及其所有子项被级联删除
  - 一级A保留
  - 删除后可以继续创建新的二级层级
- **Postconditions**: 只有一级A保留

#### TC-ST-003: 子项删除对子后代的影响
- **Requirement**: REQ-003
- **Priority**: High
- **Preconditions**:
  - 子项：A(一级) -> B(二级子项关联A) -> C(最小子项关联B)
- **Test Steps**:
  1. 删除一级子项A
  2. 检查B和C
- **Expected Results**:
  - A删除成功
  - B因为关联A，是否删除取决于实现（需要确认需求，但子项本身不持有下级，所以B可能保留只是上级为空）
  - 此处期望：B仍然存在，上级变为空，后续编辑需要重新选择上级
- **Postconditions**: A删除，B保留但无上级

#### TC-ST-004: 账号架构重置后可以重新关联
- **Requirement**: REQ-011
- **Priority**: High
- **Preconditions**:
  - 账号已关联架构A
- **Test Steps**:
  1. 重置账号，清空架构
  2. 尝试重新关联到架构B
- **Expected Results**:
  - 重置成功后架构为空
  - 可以成功关联到新架构B
  - 关联后架构显示为B
- **Postconditions**: 账号关联到新架构

#### TC-ST-005: 切换架构列表不同维度tab
- **Requirement**: REQ-008
- **Priority**: Medium
- **Preconditions**:
  - 多个架构维度存在
  - 在架构列表页面
- **Test Steps**:
  1. 默认第一个维度（最高层级）
  2. 点击第二个维度tab
  3. 点击第三个维度tab
  4. 检查数据和表头
- **Expected Results**:
  - 每次切换都正确加载对应维度数据
  - 表头第一个字段随维度变化正确更新
  - 分页、筛选状态保持
- **Postconditions**: 停留在最后选中的维度

---

## Test Coverage Matrix

| Requirement ID | Test Cases | Coverage Status |
|---------------|------------|-----------------|
| REQ-001 | TC-F-001, TC-F-002, TC-F-003 | ✓ Complete |
| REQ-002 | TC-F-001, TC-F-002, TC-F-003, TC-E-010, TC-ST-001 | ✓ Complete |
| REQ-003 | TC-F-007, TC-ERR-003, TC-E-005, TC-ST-002, TC-ST-003 | ✓ Complete |
| REQ-004 | TC-F-004, TC-F-005, TC-F-006, TC-E-003, TC-E-004, TC-ERR-002 | ✓ Complete |
| REQ-005 | TC-F-004, TC-F-005, TC-F-006, TC-E-006 | ✓ Complete |
| REQ-006 | TC-F-009, TC-ERR-007 | ✓ Complete |
| REQ-007 | TC-F-010 | ✓ Complete |
| REQ-008 | TC-F-011, TC-F-012, TC-ST-005 | ✓ Complete |
| REQ-009 | TC-F-013, TC-E-008 | ✓ Complete |
| REQ-010 | TC-F-014, TC-E-009 | ✓ Complete |
| REQ-011 | TC-F-015, TC-ERR-005 | ✓ Complete |
| REQ-012 | TC-F-016 | ✓ Complete |
| REQ-013 | TC-F-017, TC-F-018 | ✓ Complete |
| REQ-014 | TC-F-019, TC-F-020 | ✓ Complete |
| REQ-015 | TC-F-001, TC-E-001, TC-ERR-008 | ✓ Complete |
| REQ-016 | TC-F-008, TC-ERR-004 | ✓ Complete |

---

## Notes
- 所有P0需求都已覆盖完整
- 短链生成的哈希缓存方案已覆盖功能测试
- 级联删除的行为基于需求描述，实际级联范围需要确认是否子项也要删除下级子项
- 架构列表中筛选器需要在社媒监控、直播监控、帖文监控都增加，本测试用例主要覆盖架构列表本身，其他页面的筛选器增加需要额外补充测试
- 授权页面短链管理的数据表维护部分需求描述较少，如果需要完整测试需要更多细节
