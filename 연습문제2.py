#평균값
#my list [[100,200],[400,800],[1000,1400]]
#출력결과= 150 600 1200

m = [[100,200],[400,800], [1000,1400]]

for i in  m:
    data = 0
    for a in i:
        data = data + a
    print(data/2)

