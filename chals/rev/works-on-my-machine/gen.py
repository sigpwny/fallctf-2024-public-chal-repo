nums = [
1804289383,846930886,1681692777,1714636915,1957747793,424238335,719885386,1649760492,596516649,1189641421,1025202362,1350490027,783368690,1102520059,2044897763,1967513926,1365180540,1540383426,304089172,1303455736,35005211,521595368,294702567,1726956429,336465782,861021530,278722862,233665123,2145174067,468703135,1101513929,1801979802,1315634022,635723058,1369133069,1125898167,1059961393,2089018456,628175011,1656478042,1131176229,1653377373,859484421,1914544919,608413784
]
flag = 'fallctf{lemme_borrow_ur_mainframe_real_quick}'

print([
  ord(x) ^ n for (x,n) in zip(flag, nums)
])