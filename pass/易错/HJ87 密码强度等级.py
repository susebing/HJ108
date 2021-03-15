# coding=utf-8
"""
题目描述
密码按如下规则进行计分，并根据不同的得分为密码进行安全等级划分。
一、密码长度:
5 分: 小于等于4 个字符
10 分: 5 到7 字符
25 分: 大于等于8 个字符

二、字母:
0 分: 没有字母
10 分: 全都是小（大）写字母
20 分: 大小写混合字母

三、数字:
0 分: 没有数字
10 分: 1 个数字
20 分: 大于1 个数字

四、符号:
0 分: 没有符号
10 分: 1 个符号
25 分: 大于1 个符号

五、奖励:
2 分: 字母和数字
3 分: 字母、数字和符号
5 分: 大小写字母、数字和符号

最后的评分标准:
>= 90: 非常安全
>= 80: 安全（Secure）
>= 70: 非常强
>= 60: 强（Strong）
>= 50: 一般（Average）
>= 25: 弱（Weak）
>= 0:  非常弱

对应输出为：
VERY_SECURE
SECURE,
VERY_STRONG,
STRONG,
AVERAGE,
WEAK,
VERY_WEAK,

请根据输入的密码字符串，进行安全评定。
注：
字母：a-z, A-Z
数字：-9
符号包含如下： (ASCII码表可以在UltraEdit的菜单view->ASCII Table查看)

!"#$%&'()*+,-./     (ASCII码：x21~0x2F)
:;<=>?@             (ASCII<=><=><=><=><=>码：x3A~0x40)
[\]^_`              (ASCII码：x5B~0x60)
{|}~                (ASCII码：x7B~0x7E)

接口描述：
Input Param
String pPasswordStr:    密码，以字符串方式存放。

Return Value
根据规则评定的安全等级。

public static Safelevel GetPwdSecurityLevel(String pPasswordStr)
{
/*在这里实现功能*/
return null;
}

输入描述:
输入一个string的密码

输出描述:
输出密码等级

示例1
输入
复制
38$@NoNoNo
输出
复制
VERY_SECURE
"""

# //每个加分项都写成一个方法，这样更清晰明了一些
# 笨方法，还算清晰，示例是错的差点坑死我
# # 思路：将统计情况放主函数中一起写，避免分开写时多次遍历密码字符串。
# //题目是很简单的，就是要注意细节，真的很容易错，条件太多了，要仔细

while True:
    try:
        str_data = input().strip()
        num, up_char, low_char, other, score = 0, 0, 0, 0, 0

        for data in str_data:
            if data.isdigit():
                num += 1
            elif data.isalpha():
                if data.lower() == data:
                    low_char += 1
                else:
                    up_char += 1
            else:
                other += 1
        if len(str_data) < 5:
            score += 5
        elif len(str_data) < 8:
            score += 10
        else:
            score += 25
        if up_char == 0 and low_char == 0:
            pass
        elif (up_char == 0 and low_char != 0) or (up_char != 0 and low_char == 0):
            score += 10
        else:
            score += 20
        if num == 0:
            pass
        elif num == 1:
            score += 10
        else:
            score += 20
        if other == 0:
            pass
        elif other == 1:
            score += 10
        else:
            score += 25
        if num != 0 and (up_char + low_char) != 0 and other == 0:
            score += 2
        elif num != 0 and up_char != 0 and low_char != 0 and other != 0:
            score += 5
        elif num != 0 and (up_char + low_char) != 0 and other != 0:
            score += 3
        if score >= 90:
            print('VERY_SECURE')
        elif score >= 80:
            print('SECURE')
        elif score >= 70:
            print('VERY_STRONG')
        elif score >= 60:
            print('STRONG')
        elif score >= 50:
            print('AVERAGE')
        elif score >= 25:
            print('WEAK')
        else:
            print('VERY_WEAK')
    except:
        break
