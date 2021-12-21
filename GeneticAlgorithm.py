import random
import numpy as np
import pandas as pd
import copy


class GeneticAlgorithmForSchedule:
    def __init__(self, Teachers, Subjects, Period, Teachers_Subjects, Rooms, Date, population=20, mutation_rate=0.01, fitness=1, maxGen=100000):
        print("######### Initialized new Genetic Algorithm class #########")
        self.population = population
        self.mutation_rate = mutation_rate
        self.fitness = fitness
        self.maxGen = maxGen
        self.Teachers = Teachers
        self.Subjects = Subjects
        self.Period = Period
        self.Teachers_Subjects = Teachers_Subjects
        self.Rooms = Rooms
        self.Date = Date
        self.scheduleGen = []
        self.Schedule = None

    def getGroup(self, sub):
        return random.randint(1, self.Subjects[sub])

    def getSchedule(self):
        data = []
        for i in range(len(self.Teachers)):
            shiftThatTeacherCanTeach = random.randint(self.Period[i][0], self.Period[i][1])
            permutaionOfSub = []
            for sub in self.Teachers_Subjects[i]:
                for group in range(self.Subjects[sub]):
                    permutaionOfSub.append((sub, group+1))
            subPick = random.sample(permutaionOfSub, shiftThatTeacherCanTeach)
            for j in subPick:
                data.append([self.Teachers[i], j[0], j[1], random.choice(self.Rooms), random.choice(self.Date), random.randint(1, 4)])
        self.Schedule = pd.DataFrame(
            data=data, columns=['Giảng viên', 'Môn học', 'Nhóm', 'Phòng', 'Thứ', 'Ca'])
        self.scheduleGen = []
        return self.Schedule

    ## Hàm chọn ra các cá thể tốt nhất
    def selection(self, schedules):
        evaluatedSchedule = np.array([])
        for sche in schedules:
            evaluatedSchedule = np.append(evaluatedSchedule, self.evaluation(sche))
        print(np.average(evaluatedSchedule))
        topSchedule = []
        for i in evaluatedSchedule.argsort()[-(self.population//4):]:
            topSchedule.append(schedules[i])

        return topSchedule

    ## Hàm đánh giá cá thể
    def evaluation(self, schedule):
        sum = 0
        gvNotInPeriod = 0
        ## đánh giá các ràng buộc 
        phong_thu_ca = schedule[['Phòng','Thứ','Ca']].value_counts()
        gv_thu_ca = schedule[['Giảng viên','Thứ','Ca']].value_counts()
        monHoc_nhom = schedule[['Môn học', 'Nhóm']].value_counts()

        for i, j, k in zip(phong_thu_ca,gv_thu_ca, monHoc_nhom):
            if i > 1:
                sum += i
            if j > 1:
                sum += j
            if k > 1:
                sum += k
        ## Đánh giá xem số ca của giảng viên có nằm trong nhóm tối thiểu họặc tối đa
        for k in range(len(self.Teachers)):
            lenPeriod = len(schedule[schedule['Giảng viên'] == self.Teachers[k]])
            if lenPeriod < self.Period[k][0] or lenPeriod > self.Period[k][1]:
                gvNotInPeriod += 1

        result = ((len(schedule)*3-sum)/(len(schedule)*3) +
                  (len(self.Teachers) - gvNotInPeriod)/len(self.Teachers))/2
        return result

    def mate(self, schedules):
        pairs = []
        
        ## Chọn ngẫu nhiên cặp để lai
        for i in range(5):
            randomIndex = random.sample(list(range(0, len(schedules))), 2)
            pairs.append(randomIndex)

        tempTopSchedule = copy.deepcopy(schedules)

        crossOverSche = []

        for i in pairs:

            tempScheduleFemale = copy.deepcopy(tempTopSchedule[i[0]])
            tempScheduleMale = copy.deepcopy(tempTopSchedule[i[1]])

            ## Chọn dộ dài thời khoá biểu có độ dài nhỏ hơn
            length = len(tempScheduleFemale) if len(tempScheduleFemale) < len(
                tempScheduleMale) else len(tempScheduleMale)

            ## Chọn ngẫu nhiên cross point dựa trên độ dài đó
            randomCrossPoint = random.randint(0, length)

            ## Trao đổi gen
            tempFe = copy.deepcopy(
                tempScheduleFemale.iloc[randomCrossPoint:, ::])
            tempMa = copy.deepcopy(
                tempScheduleMale.iloc[randomCrossPoint:, ::])

            tempScheduleFemale.drop(
                [i for i in range(randomCrossPoint, len(tempScheduleFemale))])
            tempScheduleMale.drop(
                [i for i in range(randomCrossPoint, len(tempScheduleMale))])

            tempScheduleFemale.append(tempMa)
            tempScheduleMale.append(tempFe)

            crossOverSche.append(tempScheduleFemale)
            crossOverSche.append(tempScheduleMale)

        return crossOverSche

    def mutation(self, schedules):
        tempSches = copy.deepcopy(schedules)
        for sche in tempSches:
            ## Chọn ngẫu nhiên các gen với số lượng gen chọn dựa theo mutation_rate
            mutateIndx = random.sample(
                list(range(len(sche))),  round(self.mutation_rate*len(sche)))
            for indx in mutateIndx:
                ## Đột biến ngẫu nhiên Môn, Nhóm, Phòng, Thư, Ca
                sche.loc[indx, 'Môn học'] = random.choice(
                    self.Teachers_Subjects[self.Teachers.index(sche.iloc[indx]['Giảng viên'])])
                sche.loc[indx, 'Nhóm'] = self.getGroup(
                    sche.iloc[indx]['Môn học'])
                sche.loc[indx, 'Phòng'] = random.choice(self.Rooms)
                sche.loc[indx, 'Thứ'] = random.choice(self.Date)
                sche.loc[indx, 'Ca'] = random.randint(1, 4)
        return tempSches

    def Go(self):
        print("######### Start Genetic Algorithm #########")
        ## Khỏi tạo population
        population = []
        for i in range(self.population):
            sche = self.getSchedule()
            population.append(sche)
        ## Chạy thuật toán
        while(True):
            ## Chọn ra các cá thể tốt nhất trong quần thể
            population = self.selection(population)
            ## Copy lại các cá thể tốt
            goodIndi = copy.deepcopy(population)
            ## Biến để lưa lại cá tốt nhất để lưu cá thể đó vào mảng chứa cá thể tốt nhất trong từng thế hệ
            ## Mảng này sẽ đuọc lấy ra để hiện trên GUI
            bestEval = 0
            bestIndi = 0
            stopGA = False
            ## Duyệt xem có cá thể nào bằng với fitness không nếu có dừng thuật toán
            for sche in population:
                evalu = self.evaluation(sche)
                if evalu >= bestEval:
                    bestIndi = sche
                    bestEval = evalu
                if evalu >= self.fitness:
                    self.scheduleGen.append(bestIndi)
                    stopGA = True
            ## Bỏ cá thể tốt nhất vào mảng chứa cá thể tốt nhất trong từng thế hệ
            self.scheduleGen.append(bestIndi)
            ## Dừng thuật toán
            if stopGA:
                self.Schedule = self.scheduleGen[-1]
                return self.Schedule
            ## Nếu thuật toán đạt đến ngưỡng max thì dừng lại
            if len(self.scheduleGen) >= self.maxGen:
                self.Schedule = self.scheduleGen[-1]
                return self.Schedule
            ## Lai các cá thể tạo ra cá thể mới
            matedIndi = self.mate(goodIndi)
            ## đột biến các cá thể
            newIndi = self.mutation(matedIndi)
            ## Thêm các cá thể mới đó vào quần thể
            population += newIndi


