/*#######################################
# University of Information Technology	#
# IT007 Operating System		#
# Nhom Ubuntu:				#
# 1. Le Xuan Quynh, 21520430		#
# 2. Truong Gia Man, 21521115		#
# 3. Nguyen Thanh Dat, 21521938		#
# File: srtf.cpp			#
#######################################*/

n = int(input('Enter total number of process: '))   # Nhập số lượng process cần được tính toán

# Tạo mảng với n Process, ID, BurstTime và ArrivalTime
Process = [0] * (n+1)
IDOfProcess = [0] * (n+1)
ArrivalTime = [0] * (n+1)
BurstTime = [0] * (n+1)

# Tạo mảng cho Finish Time, TurnAround Time và Waiting Time
finishTime = [0] * (n + 1)
turnTime = [0] * (n + 1)
waitTime = [0] * (n + 1)

# Nhập vào ID, BurstTime và ArrivalTime theo thứ tự n
for i in range(n):  # Chạy vòng lặp
    print("\n")
    IDOfProcess[i] = int(input("Enter the ID Of Process {}: ".format(i + 1)))
    BurstTime[i] = int(input('Enter the burst time for process {} : '.format(i + 1)))
    ArrivalTime[i] = int(input('Enter the arrival time for process {} : '.format(i + 1))) 
    Process[i] = [BurstTime[i], ArrivalTime[i], IDOfProcess[i], i]  # Cho BurstTime, ArrivalTime, ID Process và thứ tự Process vào một mảng Process

# Xóa phần tử 0 xuất hiện khi tạo mảng
Process.pop(-1) 
finishTime.pop(-1)
waitTime.pop(-1)
turnTime.pop(-1)
BurstTime.pop(-1)  
ArrivalTime.pop(-1) 
i = 0
list = []  # Tạo mảng chứa những Process đã được xử lí

for i in range(0, sum(BurstTime)):  #  Chạy vòng lặp trong khoảng từ 0 đến tổng thời gian BurstTime của các tiến trình
	l = [j for j in Process  if j[1] <= i]
	l.sort(reverse= False ,key=lambda x: x[0]) # Sắp xếp lại Burst Time của các process theo thứ tự tăng dần 
	Process[Process.index(l[0])][0] -= 1
	for k in Process:
		if k[0] == 0:   # Nếu Burst Time của 1 Process bằng 0 thì 
			t = Process.pop(Process.index(k))
			list.append([k, i + 1])	# Thêm process [thông tin process, thời gian hoàn thành] đã được xử lí vào mảng process đã được xử lí (list)

for i in list:
	finishTime[i[0][3]] = i[1] # Thêm thời gian hoàn thành (Finish time) vào mảng finishTime theo thứ tự i của Process

for i in range(len(finishTime)):    # Chạy vòng lặp theo số lượng phần tử có trong mảng finishTime
    # Tính toán TurnAround Time và Waiting Time
	turnTime[i] = finishTime[i] - ArrivalTime[i]    
	waitTime[i] = turnTime[i] - BurstTime[i]

print('ID\tBurstTime\tArrivalTime\tFinishTime\tTurnTime\tWaitTime')
for i in range(len(finishTime)):    # Chạy vòng lặp với độ dài của mảng Finish Time
	print("{}\t{}\t\t{}\t\t{}\t\t{}\t\t{}\n".format(IDOfProcess[i], BurstTime[i], ArrivalTime[i], finishTime[i], turnTime[i], waitTime[i]))   #In ra màn hình kết quả
print('Average Waiting Time = ', sum(waitTime)/len(waitTime))   # Tính toán và in ra màn hình kết quả của thời gian đợi trung bình
print('Average Turnaround Time = ', round(sum(turnTime)/len(turnTime),3))    # Tính toán và in ra màn hình kết quả của thời gian hoàn thành trung bình 
