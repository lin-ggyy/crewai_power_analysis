# 发电组合策略分析系统

基于 [CrewAI](https://crewai.com) 多智能体框架构建的发电侧电力交易决策辅助工具，适用于火电、风电、光伏混合机组的日前市场分析。

## 核心功能

- **新能源出力预测**：基于风速、日照等气象数据，逐时预测风电和光伏出力
- **火电成本分析**：根据煤价、煤耗等参数计算边际成本和最优出力区间
- **组合策略生成**：整合预测与成本，输出现货申报建议、收益测算和风险评估

## 智能体架构

三个智能体按顺序协作：

1. **新能源出力分析师**：将天气预报转化为出力预测，评估预测可信度
2. **火电经济分析师**：计算发电成本曲线，判断机组盈利区间和启停时机
3. **发电组合策略师**：综合前两者输出，制定全局最优策略和风险预案

流程：出力预测 → 成本分析 → 策略决策

## 快速开始

### 环境要求

- Python >= 3.10, < 3.14
- [uv](https://docs.astral.sh/uv/) 包管理器

### 安装

```
pip install uv
cd crewai
uv sync
```

### 配置

在项目根目录创建 .env 文件：

```
MODEL=deepseek/deepseek-chat
DEEPSEEK_API_KEY=sk-你的key
```

### 运行

```
crewai run
```

策略报告输出至 output/策略报告.md。

### 自定义参数

编辑 src/power_portfolio_analysis/main.py 中的 inputs 字典：

| 参数 | 说明 | 示例值 |
| --- | --- | --- |
| date_range | 分析日期 | 2026-05-20 |
| wind_capacity | 风电装机 (MW) | 200 |
| solar_capacity | 光伏装机 (MW) | 150 |
| thermal_capacity | 火电装机 (MW) | 600 |
| min_output | 最小技术出力 (MW) | 180 |
| coal_price | 煤价 (元/吨) | 800 |
| coal_rate | 供电煤耗 (克/度) | 310 |
| startup_cost | 启动成本 (元) | 500000 |
| ramp_rate | 爬坡速率 (MW/h) | 60 |
| weather_data | 天气数据 (逐时温度/风速/日照) | CSV 格式 |
| market_price | 日前电价 (逐时) | CSV 格式 |
| contracted_volume | 中长期合约电量 (MWh) | 500 |
| contract_price | 合约电价 (元/MWh) | 380 |

### 项目结构

```
├── src/power_portfolio_analysis/
│   ├── config/
│   │   ├── agents.yaml
│   │   └── tasks.yaml
│   ├── tools/
│   │   └── custom_tool.py
│   ├── crew.py
│   └── main.py
├── output/
│   └── 策略报告.md
├── knowledge/
├── pyproject.toml
└── .env
```
