import sys
class Chapter:
    "tcs project given "
    compny_name='TCS'
    def __init__(self,Name,SubjectName,Page,Marks):
        self.Name = Name
        self.SubjectName = SubjectName
        self.Page =Page
        self.Marks= Marks
    def Disply(self):
        print('Name is :',self.Name)
        print('Subject Name : ',self.SubjectName)
        print('Subject Page No :',self.Page)
        print('Subject Mark :',self.Marks)

    def FindMaxChapterByPage(self):
        n = List_of_chapter
        l =n[3::4]
        print(max(l))





    def SortChapterByMarks(self):
        pass
        # n = List_of_chapter
        # l = n[3::4]
        # f = l.sort(reverse=True)
        # lt = []
        # fi = lt.append(f)
        # print(l)
        # i = 0
        # while i < len(l):
        #     print(l[i])
        #     i = i + 1

List_of_chapter=[]
#chap =Chapter()
print('Welcome to',Chapter.compny_name)
while True:
    print('F-Fill Information\nD-Disply\nE-Exit')
    option = input('Choose Your Option :')
    if option =='F' or option =='f':
        Name = str(input('Enter Name :'))
        SubjectName = str(input('Enter Subject :'))
        Page = int(input('Enter Page :'))
        Marks = int(input('Enter Marks:'))
        c=Chapter(Name,SubjectName,Page,Marks)
        List_of_chapter.append(c)
        FL = []
        ML=FL.append(Marks)
        print('Add suceesfully')
        op = input('Do you want to add one more Data [Yes|No]: ')
        if op.lower() == 'no':
            continue
    if option =='D' or option == 'd':
        for data in List_of_chapter:
            data.Disply()
            # Chapter.SortChapterByMarks(a)
            Chapter.FindMaxChapterByPage(a=None)

    if option =='E' or option =='e':
        print('Thank you using TCS..')
        sys.exit()
    else:
        print('Invaild option..PLZ choose vaild option..')
        print('Thank you using TCS...')