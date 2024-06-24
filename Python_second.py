

# str1 = 'QYTANG'
# str2 = 'day'
# date1 = '2014-9-19'
# result = ' '.join([str1,str2,date1])
# print(result)
#
# word = " scallywag"
# sub_word = word[3:7]
# print(sub_word)


# str1 ='Python'
# str2 = str1 + '-'
# str3 = str2[1:]+str2[0:1]
# str4 = str3 + 'y'
# print(str4)


# department1 = 'Security'
# department2 = 'Python'
# depart1_m = 'cq_bomb'
# depart2_m = 'qinke'
# COURSE_FEES_SEC = 456789.12456
# COURSE_FEES_Python = 1234.3456
#
# # #传统方法
# line1 = 'department1 name:%-15sManager:%-15sCOURSE FEES:%-15.2f'%(department1,depart1_m,COURSE_FEES_SEC)+'THE END!'
# line2 = 'department2 name:%-15sManager:%-15sCOURSE FEES:%-15.2f'%(department2,depart2_m,COURSE_FEES_Python)+'THE END!'
#
# #高级方法
# line1 = ('department1 name:{:<15}Manager:{:<15}Course Fees{:<15.2f}THE END!'
#          .format(department1, depart1_m, COURSE_FEES_SEC))
# line2 = ('department2 name:{:<15}Manager:{:<15}Course_Fees{:<15.2f}THE END!'
#          .format(department2, depart2_m,COURSE_FEES_Python))
#新方法
# line1 = (f'Department1 name: {department1:<10}'
#           f' Manager:{depart1_m:<10} '
#           f'COURSE FEES: {COURSE_FEES_SEC:<10.2f}'
#           f'The End!')
#
# line2 = (f'Department2 name: {department2:<10}'
#           f' Manager:{depart2_m:<10}'
#           f' COURSE FEES: {COURSE_FEES_Python:<10.2f}'
#           f'The End!')

# length = len(line1)
# print('=' * length )
# print(line1)
# print(line2)
# print('=' * length )

import re
str1 = 'Port-channel1.189    192.168.189.254  YES    CONFIG  up'
str2 = re.match(r'([A-Za-z-]+\d+\.\d+)\s+([\d.]+)\s+YES\s+CONFIG\s+(\w+)', str1).groups()
print(f'接口   ：{str2[0]}')
print(f'IP地址 ：{str2[1]}')
print(f'状态   ：{str2[2]}')




