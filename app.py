from flask import Flask, render_template, request, redirect
from GeneticAlgorithm import GeneticAlgorithmForSchedule
import webbrowser
from Data import Data

app = Flask(__name__)
Data = Data()
Schedule = GeneticAlgorithmForSchedule(
    Data.Teachers,
    Data.Subjects,
    Data.Period,
    Data.Teachers_Subjects,
    Data.Rooms,
    Data.Date)
genId = 0
teacherId = 0

def generateSche(sche):
    meetConstraints = []
    phong_thu_ca = sche[['Phòng','Ca','Thứ']].value_counts()
    gv_thu_ca = sche[['Môn học', 'Nhóm']].value_counts()
    monHoc_nhom = sche[['Môn học', 'Nhóm']].value_counts()
    for i in range(len(phong_thu_ca)):
        if (phong_thu_ca[i] > 1):
            meetConstraints.append(phong_thu_ca.index.tolist()[i])
    for i in range(len(gv_thu_ca)):
        if (gv_thu_ca[i] > 1):
            meetConstraints.append(gv_thu_ca.index.tolist()[i])
    for i in range(len(monHoc_nhom)):
        if (monHoc_nhom[i] > 1):
            meetConstraints.append(monHoc_nhom.index.tolist()[i])
	
    data = [[[] for col in range(6)] for row in range(4)]
    for i in range(len(sche)):
        isConstraint = False
        if (sche.iloc[i]['Phòng'], sche.iloc[i]['Ca'], sche.iloc[i]['Thứ']) in meetConstraints or (sche.iloc[i]['Môn học'], sche.iloc[i]['Nhóm']) in meetConstraints or (sche.iloc[i]['Giảng viên'], sche.iloc[i]['Thứ'], sche.iloc[i]['Ca']) in meetConstraints:
            isConstraint = True
        data[sche.iloc[i]['Ca']-1][Data.Date.index(sche.iloc[i]['Thứ'])] += [[sche.iloc[i]['Giảng viên'], sche.iloc[i]['Môn học'], sche.iloc[i]['Nhóm'], sche.iloc[i]['Phòng'], isConstraint]]
    return data

@app.route('/')
def index():
    global Schedule
    global genId
    global teacherId
    genId = 0
    teacherId = 0

    sche = Schedule.getSchedule()
    
    data = generateSche(sche)
    return render_template('index.html',attributes=getAttribute(), data=data, teachers=Data.Teachers, generation=len(Schedule.scheduleGen), teacherIsSelected=teacherId, genIsSelected=genId, id=1)

@app.route('/getGeneral')
def getGeneral():
    global Schedule
    global genId
    global teacherId
    teacherId = 0
    data = generateSche(Schedule.Schedule)
    return render_template('index.html',attributes=getAttribute(), data=data, teachers=Data.Teachers, generation=len(Schedule.scheduleGen), teacherIsSelected=teacherId, genIsSelected=genId, id=1) 

@app.route('/generateSchedule', methods=['POST'])
def generateSchedule():
    global Schedule
    global genId
    global teacherId
    population = int(request.form.get('population'))
    mutation_rate = float(request.form.get('mutation_rate'))
    fitness = float(request.form.get('fitness'))
    maxGen = int(request.form.get('maxGen'))
    Schedule = GeneticAlgorithmForSchedule(
            Data.Teachers,
            Data.Subjects,
            Data.Period,
            Data.Teachers_Subjects,
            Data.Rooms,
            Data.Date,
        population=population, 
        mutation_rate=mutation_rate, 
        fitness=fitness, 
        maxGen=maxGen)
    Schedule.Go()
    data = generateSche(Schedule.Schedule)
    return render_template('index.html',attributes=getAttribute(), data=data, teachers=Data.Teachers, generation=len(Schedule.scheduleGen), teacherIsSelected=teacherId, genIsSelected=genId,id=1)


@app.route('/getGen', methods=['GET'])
def getGen():
    global Schedule
    global genId
    global teacherId
    genId = int(request.args.get('generation'))
    data = generateSche(Schedule.scheduleGen[genId-1])
    Schedule.Schedule = Schedule.scheduleGen[genId-1]
    
    return render_template('index.html',attributes=getAttribute(), data=data, teachers=Data.Teachers, generation=len(Schedule.scheduleGen), teacherIsSelected=teacherId, genIsSelected=genId, id=1)

@app.route('/getTeacher', methods=['POST', 'GET'])
def getTeacher():
    global Schedule
    global genId
    global teacherId
    teacherId = int(request.form.get('teacher'))
    teacherName = Data.Teachers[teacherId]
    teacherSche = Schedule.Schedule[Schedule.Schedule['Giảng viên'] == teacherName]
    data = generateSche(teacherSche)
    return render_template('index.html',attributes=getAttribute(), data=data, teachers=Data.Teachers, generation=len(Schedule.scheduleGen), teacherIsSelected=teacherId, genIsSelected=genId, id=2) 

def getAttribute():
    global Schedule
    attr = {
        'population': Schedule.population,
        'mutation_rate': Schedule.mutation_rate,
        'fitness': Schedule.fitness,
        'maxGen': Schedule.maxGen,
    }
    return attr

def getTeacherData():
    teachers = list(zip(Data.Teachers, Data.Period, Data.Teachers_Subjects))
    return render_template('data.html', teachers=teachers, subjects=Data.Subjects, id=1)

def getSubjectData():
    subjectName = [i for i in Data.Subjects]
    return render_template('data.html',subjectName=list(zip(subjectName, list(range(len(subjectName))))), subjects=Data.Subjects, id=2)

def getRoomData():
    return render_template('data.html',rooms=Data.Rooms, id=3)

@app.route('/data', methods=['GET'])
def data():
    if (request.args.get('route') == 'teacher'):
        return getTeacherData()
    elif (request.args.get('route') == 'subject'):
        return getSubjectData()
    elif (request.args.get('route') == 'room'):
        return getRoomData()


@app.route('/addData',methods=['POST'])
def addData():
    global Schedule
    if (request.form.get('id') == '1'):
        name = request.form.get('teacherName')
        subjects = request.form.getlist('subs[]')
        minShift = request.form.get('minShift')
        maxShift = request.form.get('maxShift')
        Data.addTeacher(name)
        Data.addPeriod([int(minShift), int(maxShift)])
        Data.addTeacher_Subject(subjects)
        
        Schedule = GeneticAlgorithmForSchedule(
            Data.Teachers,
            Data.Subjects,
            Data.Period,
            Data.Teachers_Subjects,
            Data.Rooms,
            Data.Date)
        sche = Schedule.getSchedule()
        return getTeacherData()
    elif (request.form.get('id') == '2'):
        name = request.form.get('subName')
        noGroup = request.form.get('noGroup')
        Data.addSubject(name, noGroup)
        print(Data.Subjects)
        Schedule = GeneticAlgorithmForSchedule(
            Data.Teachers,
            Data.Subjects,
            Data.Period,
            Data.Teachers_Subjects,
            Data.Rooms,
            Data.Date)
        sche = Schedule.getSchedule()
        return getSubjectData()
    elif (request.form.get('id') == '3'):
        name = request.form.get('roomName')
        Data.addRoom(name)
        
        Schedule = GeneticAlgorithmForSchedule(
            Data.Teachers,
            Data.Subjects,
            Data.Period,
            Data.Teachers_Subjects,
            Data.Rooms,
            Data.Date)
        sche = Schedule.getSchedule()
        return getRoomData()
    
    


@app.route('/deleteData',methods=['POST'])
def deleteData():
    global Schedule
    if (request.get_json()['id']==1):
        name = request.get_json()['name']
        Data.deleteTeacherData(name)

        Schedule = GeneticAlgorithmForSchedule(
            Data.Teachers,
            Data.Subjects,
            Data.Period,
            Data.Teachers_Subjects,
            Data.Rooms,
            Data.Date)
        sche = Schedule.getSchedule()
        return getTeacherData()
    elif (request.get_json()['id']==2):
        name = request.get_json()['name']
        Data.deleteSubject(name)
        Data.Subjects = Data.Subjects
        Schedule = GeneticAlgorithmForSchedule(
            Data.Teachers,
            Data.Subjects,
            Data.Period,
            Data.Teachers_Subjects,
            Data.Rooms,
            Data.Date)
        sche = Schedule.getSchedule()
        return getSubjectData()
    elif (request.get_json()['id']==3):
        name = request.get_json()['name']
        print(name)
        Data.deleteRoom(name)

        Schedule = GeneticAlgorithmForSchedule(
            Data.Teachers,
            Data.Subjects,
            Data.Period,
            Data.Teachers_Subjects,
            Data.Rooms,
            Data.Date)
        sche = Schedule.getSchedule()
        return getRoomData()



if __name__ == "__main__":
    webbrowser.open('http://127.0.0.1:5000/')
    app.run(debug=True)
