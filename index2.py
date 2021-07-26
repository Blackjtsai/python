#-*- coding: utf-8 -*-
# 設計輸入英文翻譯機By分類(color,size....)
from _typeshed import ReadableBuffer
import englishToChinese as s
x= input("請輸入英文顏色:")
y=s.color(x)
print(y)

x=input("請輸入size")
y=s.size(x)
print(y)
