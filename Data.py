class Data:
    
    def __init__(self):
        self.Teachers = ['Hồ Minh chung', 'Lê Anh Cường', 'Bùi Thị Xuân', 'Tôn Đức Thắng', 'Nguyễn Văn Ngoan',
                'Trần trung Tín', 'Lê Kiều Oanh', 'Sương Nguyệt Anh', 'Võ Thị Sáu', 'Phạm Huyền Trang',
                'Lương Thế Vinh', 'Phan Thị Hằng', 'Phạm Thị Thùy Linh', 'Phạm Nhật Minh', 'Huỳnh Tấn Lợi',
                'Võ Tấn Lực', 'Nguyễn Nhật Linh', ' Thân Trọng Huỳnh Nhân', 'Nguyễn Văn Nam', ' Lưu Huy Thông']

        self.Period = [[4, 8], [4, 8], [3, 6], [3, 6], [1, 2],
                [4, 8], [3, 6], [2, 4], [3, 6], [2, 4],
                [2, 4], [2, 4], [1, 2], [3, 6], [3, 6],
                [3, 6], [3, 6], [2, 4], [2, 4], [3, 6]]

        self.Subjects = {
            'Hệ thống quản trị mạng': 3,
            'Công nghệ phần mềm': 4,
            'IoT cơ bản': 3,
            'Quản trị hệ thống thông tin': 3,
            'Phát triển ứng dụng di động nâng cao': 3,
            'Phát triển ứng dụng di động': 4,
            'Phân tích và thiết kế theo yêu cầu': 3,
            'Thiết kế giao diện người dùng': 3,
            'Kiểm thử phần mềm': 3,
            'Lập trình web': 4,
            'Lập trình web nâng cao': 4,
            'Trí tuệ nhân tạo': 4,
            'Xử lý ngôn ngữ tự nhiên': 3,
            'Học máy': 4,
            'Mác - Lênin': 2,
            'Đường lối': 2,
            'Tư tưởng': 2,
            'Giáo dục công dân': 2,
            'Pháp luật đại cương': 2,
            'Hệ điều hành': 2,
            'Tổ chức máy tính': 2,
            'Tiếng anh': 2,
            'Tiếng Trung Quốc': 2,
            'Tiếng Pháp': 2,
            'Lịch sử': 4,
            'Địa lý': 4,
            'Giáo dục quốc phòng học phần 1': 2,
            'Giáo dục quốc phòng học phần 2': 2,
            'Giáo dục quốc phòng học phần 3': 4,
            'Toán thống kê': 2,
            'Toán cao cấp': 2,
            'Hóa học vô cơ': 2,
            'Hóa học hữu cơ': 2,
            'Vật lý lượng tử': 2,
            'Học sâu': 4,
            'Bảo mật thông tin': 2,
            'Bảo mật máy tính': 2,
            'Giáo dục thể chất': 2,
            'Cấu trúc dữ liệu và giải thuật 1': 2,
            'Cấu trúc dữ liệu và giải thuật 2': 2,
            'Xác suất thông kê': 2,
            'Đại số tuyến tính': 2,
            'Giải tích ứng dụng cho CNTT': 2}

        self.Teachers_Subjects = [
            ['Phát triển ứng dụng di động', 'Lập trình web',
                'Phát triển ứng dụng di động nâng cao', 'Lập trình web nâng cao'],
            ['Trí tuệ nhân tạo', 'Xử lý ngôn ngữ tự nhiên', 'Học máy', 'Học sâu'],
            ['Mác - Lênin', 'Đường lối', 'Tư tưởng'],
            ['Giáo dục công dân', 'Lịch sử', 'Địa lý'],
            ['Pháp luật đại cương'],
            ['Hệ điều hành', 'Tổ chức máy tính', 'Kiểm thử phần mềm', 'Công nghệ phần mềm'],
            ['Tiếng anh', 'Tiếng Trung Quốc', 'Tiếng Pháp'],
            ['IoT cơ bản', 'Hệ thống quản trị mạng'],
            ['Giáo dục quốc phòng học phần 1', 'Giáo dục quốc phòng học phần 2',
                'Giáo dục quốc phòng học phần 3'],
            ['Lịch sử', 'Địa lý'],
            ['Toán thống kê', 'Toán cao cấp'],
            ['Hóa học vô cơ', 'Hóa học hữu cơ'],
            ['Vật lý lượng tử'],
            ['Học máy', 'Học sâu', 'Trí tuệ nhân tạo'],
            ['Lập trình web nâng cao', 'Lập trình web', 'Thiết kế giao diện người dùng'],
            ['Bảo mật thông tin', 'Bảo mật máy tính', 'Quản trị hệ thống thông tin'],
            ['Phát triển ứng dụng di động',
                'Phân tích và thiết kế theo yêu cầu', 'Công nghệ phần mềm'],
            ['Giáo dục thể chất', 'Giáo dục quốc phòng học phần 3'],
            ['Cấu trúc dữ liệu và giải thuật 1', 'Cấu trúc dữ liệu và giải thuật 2'],
            ['Xác suất thông kê', 'Đại số tuyến tính', 'Giải tích ứng dụng cho CNTT']]

        self.Rooms = ['Phòng 1', 'Phòng 2', 'Phòng 3', 'Phòng 4',
                'Phòng 5', 'Phòng 6', 'Phòng 7', 'Phòng 8', 'Phòng 9']
            
        self.Date = ['Thứ 2', 'Thứ 3', 'Thứ 4', 'Thứ 5', 'Thứ 6', 'Thứ 7']

    def addTeacher(self, teacher):
        self.Teachers.insert(0,teacher)

    def addPeriod(self, period):
        self.Period.insert(0,period)
    
    def addTeacher_Subject(self, teacher_sub):
        self.Teachers_Subjects.insert(0,teacher_sub)
    
    def addSubject(self, subject, noGroup):
        self.Subjects[subject] = noGroup

    def addRoom(self, room):
        self.Rooms.insert(0,room)

    def deleteTeacherData(self, teacher):
        index = self.Teachers.index(teacher)
        self.Period.pop(index)
        self.Teachers_Subjects.pop(index)
        self.Teachers.pop(index)
    
    def deleteSubject(self, subject):
        self.Subjects.pop(subject)
        for i in range(len(self.Teachers_Subjects)):
            if subject in self.Teachers_Subjects[i]:
                self.Period[i][0] -= 1
                self.Period[i][1] -= 2
                print(self.Teachers_Subjects[i])
                self.Teachers_Subjects[i].pop(self.Teachers_Subjects[i].index(subject))
                print(self.Teachers_Subjects[i])

    def deleteRoom(self, room):
        self.Rooms.pop(self.Rooms.index(room))


