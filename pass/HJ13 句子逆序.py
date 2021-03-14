"""
题目描述
将一个英文语句以单词为单位逆序排放。例如“I am a boy”，逆序排放后为“boy a am I”
所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符

接口说明

/**
 * 反转句子
 *
 * @param sentence 原句子
 * @return 反转后的句子
 */
public String reverse(String sentence);

输入描述:
将一个英文语句以单词为单位逆序排放。

输出描述:
得到逆序的句子

示例1
输入
复制
I am a boy
输出
复制
boy a am I
"""

# 把输入的句子分割成单词数组
# 使用 [::-1] 倒序单词数组

while 1:
    try:
        print(' '.join(input().split()[::-1]))
    except:
        break