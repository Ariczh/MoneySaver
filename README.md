# MoneySaver
存钱辅助程序，半成品

>“拿出一张纸，写下1-365，每天从其中选出一个数字，存下等值的钱，然后把这个数字划掉。365天后，你将会存下60000多元钱”
基于这一原理，我写了这个能够每天不重复地随机选出1-365之间的任意一个整数，并记录已选出的数字总值的程序。
程序理论上可以跨平台运行，实际仅在windows下测试。
程序运行后会在main.py所在的目录建立一个ini文件用于存储数据，请勿删除，否则程序将会从头再来；
同理，想要从头再来时，可以删除此ini。
