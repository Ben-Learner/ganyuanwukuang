"""
1，定义产量,价格,销售额
2，计算成本
3，计算净利润
4，计算项目投资回收期
"""
# 定义年产量(t)，价格(万元/t)
Basic_Production = 300000
Dynamic_Production = 330000
Production_Factor = Dynamic_Production / Basic_Production #大于1
Price_Factor = 1 #大于1
wu = [2525 * Production_Factor, 12 * Price_Factor]
mu = [32 * Production_Factor, 8 * Price_Factor]
tong = [338 * Production_Factor, 0.7 * Price_Factor]
bi = [43 * Production_Factor, 2 * Price_Factor]
xi = [81 * Production_Factor, 5 * Price_Factor]
All_Metal = [wu, mu, tong, bi, xi]
Sales_revenues = 0
# 年销售额（万元）
for i in range(len(All_Metal)):
    Sales_revenues += All_Metal[i][0] * All_Metal[i][1]
print('年销售额：',Sales_revenues)
# 成本（元/吨）
Total_Cost_Unit = 286.14
Total_Cost_Year = 8584.2 * Production_Factor
# 增值税
VAT_rate = 0.1185
#销售税金及附加
Sales_Tax_rate = 0.06463
#所得税
Income_Tax_Rate = 0.25
#税后净利润
Profit_After_Tax = (Sales_revenues *(1 - VAT_rate - Sales_Tax_rate) - Total_Cost_Year) * (1 - Income_Tax_Rate)
print('税后净利润：',Profit_After_Tax)
#平均未分配利润
Average_Undistributed_Profit = Profit_After_Tax * (1 - 0.1)
#项目投资回收期（税后）
Project_Investment = 42619.11 #项目投资总额
Payback_Time = Project_Investment/Profit_After_Tax
print('项目投资回收期：',Payback_Time)

