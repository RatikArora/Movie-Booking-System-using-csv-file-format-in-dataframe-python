import pandas as pd
from tabulate import tabulate
import random
import os
from os import system
import csv
from datetime import datetime, timedelta


def create():
    print("------------------------------------------<< Add The Details >>------------------------------------------")
    if os.path.isfile('movie.csv'):
        file = open("movie.csv", 'a', newline='')
        df = csv.writer(file)
        # print("yes")
    else:
        file = open("movie.csv", 'a', newline='')
        df = csv.writer(file)
        field = ['code', 'name', 'details', 'status', 'show9-12',
                 'show12-15', 'show15-18', 'show18-21', 'show21-24', 'seats']
        df.writerow(field)
        # print(field)
    ch = 'y'
    while ch == 'y' or ch == 'Y':
        code = int(input("Enter the code of the movie : "))
        name = input("Enter the name of the film : ")
        details = input("Enter the details for the movie : ")
        status = input("Enter status (yes or no) : ")
        show912 = input("Enter status for 9 to 12 show (yes or no) : ")
        show1215 = input("Enter status for 12 to 3 show (yes or no) : ")
        show1518 = input("Enter status for 3 to 6 show (yes or no) : ")
        show1821 = input("Enter status for 6 to 9 show (yes or no) : ")
        show2124 = input("Enter status for midnight show (yes or no) : ")
        seats = 40
        record = [code, name, details, status, show912,
                  show1215, show1518, show1821, show2124, seats]
        df.writerow(record)
        ch = input("Enter more record??(Y/N)")
    file.close()
    try:
        input("Press enter to continue")
    except SyntaxError:
        pass


def update():
    print("------------------------------------------<< Update >>------------------------------------------")
    file = open("movie.csv", "r")
    file1 = open("temp.csv", "w", newline='')
    df = csv.reader(file)
    df1 = csv.writer(file1)
    next(file)
    code = int(input("enter the movie code that you wish to modify : "))
    field = ['code', 'name', 'details', 'status', 'show9-12',
             'show12-15', 'show15-18', 'show18-21', 'show21-24', 'seats']
    df1.writerow(field)
    for i in df:
        if int(i[0]) == code:
            print('found the record')
            code = i[0]
            name = i[1]
            details = i[2]
            status = input("Enter modified status :")
            if status == 'no':
                s912 = '-'
                s1215 = '-'
                s1518 = '-'
                s1821 = '-'
                s2124 = '-'
                seats = 0
            else:
                s912 = input("Will there be a movie for 9-12 show :")
                s1215 = input("Will there be a movie for 12-15 show :")
                s1518 = input("Will there be a movie for 15-18 show :")
                s1821 = input("Will there be a movie for 18-21 show :")
                s2124 = input("Will there be a movie for 21-24 show :")
                seats = i[9]
            record = [code, name, details, status,
                      s912, s1215, s1518, s1821, s2124, seats]
            df1.writerow(record)
        else:
            df1.writerow(i)
    file.close()
    file1.close()
    os.remove("movie.csv")
    os.rename("temp.csv", "movie.csv")
    file.close()
    file1.close()
    try:
        input("Press enter to continue")
    except SyntaxError:
        pass


def deletemovie():
    print("------------------------------------------<< Delete >>------------------------------------------")
    z = 0
    file = open('movie.csv', 'r')
    file1 = open('temp.csv', 'w', newline='')
    df = csv.reader(file)
    df1 = csv.writer(file1)
    next(file)
    code = int(input('\nEnter the rec you want to delete : '))
    field = ['code', 'name', 'details', 'status', 'show9-12',
             'show12-15', 'show15-18', 'show18-21', 'show21-24', 'seats']
    df1.writerow(field)
    for i in df:
        if int(i[0]) == code:
            print("<< The row was found and was deleted >> ")
            print("the code was ", i[0])
            z = 1
        else:
            df1.writerow(i)
    if z == 0:
        print("<< No Movie exists with this code >> ")
    file.close()
    file1.close()
    os.remove('movie.csv')
    os.rename('temp.csv', 'movie.csv')
    file.close()
    file1.close()
    try:
        input("Press enter to continue")
    except SyntaxError:
        pass


def show(x):

    if x == 1:
        print("------------------------------------------<< All Movies >>------------------------------------------")
        df = pd.read_csv('movie.csv')
        # pd.options.display.max_columns=None
        print(tabulate(df, headers='keys', tablefmt='pretty'))
    elif x == 2:
        print("------------------------------------------<< Available Movies >>------------------------------------------")
        df1 = pd.read_csv('movie2.csv')
        print(tabulate(df1, headers='keys', tablefmt='pretty'))

    try:
        input("Press enter to continue")
    except SyntaxError:
        pass


def find():
    file = open('movie.csv', 'r')
    file1 = open('movie2.csv', 'w', newline='')
    df = csv.reader(file)
    df1 = csv.writer(file1)
    next(file)
    field = ['code', 'name', 'details', 'status', '9 TO 12','12 TO 15', '15 TO 18', '18 TO 21', '21 TO 24', 'seats']

    df1.writerow(field)
    for i in df:
        # print(i[3])
        if i[3] != 'no' or i[3] == 'NO':
            df1.writerow(i)
    file.close()
    file1.close()
    show(2)
# find()


#  in delete movie delete the movie from both files movie and movie 2
#  to do : write its code yet

# create()
# show(1)
# update()
# deletemovie()
# show(1)
# find()
# find()


def movie():
    while 1:
        system('cls')
        print("------------------------------------------<< Cinemax >>------------------------------------------")
        choice = int(input(
            "1. Add Movie \n2. Show Shows \n3. Update Details \n4. Find \n5. Delete \n6. Bookmyshow \n7.Exit\nEnter your choice : "))
        if choice == 1:
            create()
        elif choice == 2:
            show(1)
        elif choice == 3:
            update()
        elif choice == 4:
            find()
        elif choice == 5:
            deletemovie()
        elif choice == 6:
            details()
        elif choice == 7:
            break
        else:
            print("--- << invalid syntax >> ---")


def timeslot():
    print("------------------------------------------<< Available Movies >>------------------------------------------")
    dataf = pd.read_csv('movie2.csv')
    print(tabulate(dataf, headers='keys', tablefmt='pretty'))
    # print(dataf)
    choice = int(input("Enter the movie index : "))
    # field = ['code','name','details','status','show9-12','show12-15','show15-18','show18-21','show21-24','seats']

    df = dataf.loc[[choice]]

    # print(df)
    # z = df.loc[[choice],['show9-12'][0]]
    # # print(type(z))
    # # print(z)
    # print(z[choice])

    print("\n << The availiable times slots are >>")
    i = 0
    times = []
    a = df.loc[[choice], ['9 TO 12'][0]]
    b = df.loc[[choice], ['12 TO 15'][0]]
    c = df.loc[[choice], ['15 TO 18'][0]]
    d = df.loc[[choice], ['18 TO 21'][0]]
    e = df.loc[[choice], ['21 TO 24'][0]]
    if a[choice] == 'yes':
        i = i+1
        print(i, '. 9 TO 12')
        times.append(1)

    if b[choice] == 'yes':
        i = i+1
        print(i, '. 12 TO 15')
        times.append(2)

    if c[choice] == 'yes':
        i = i+1
        print(i, '. 15 TO 18')
        times.append(3)

    if d[choice] == 'yes':
        i = i+1
        print(i, '. 18 TO 21')
        times.append(4)

    if e[choice] == 'yes':
        i = i+1
        print(i, '. 21 TO 24')
        times.append(5)

    timecons = int(input("Enter your preference : "))
    # print(times[timecons-1])
    timecons = int(times[timecons-1] + 3)
    # print(timecons)

    time = df.columns[timecons]
    # print(timeslot)

    return time, choice


def date():
    tomorrowsdate = datetime.now() + timedelta(1)
    tomorrowsdate = tomorrowsdate.strftime('%d-%m-%Y')
    return tomorrowsdate


def booking():
    # time = timeslot()
    # print(time)
    # toms_date = date()
    # print(toms_date)
    choice = 1
    dataf = pd.read_csv('movie2.csv')
    df = dataf.loc[[choice]]
    print(df)
    print(df.loc[:, 'name'][choice])  # movie name
    print(df.loc[:, 'code'][choice])  # movie code


# booking()
# movie()

# # df1 mein code , index from 100 , name , slot , seatnumber , and tomorrows date

def seatnumber():
    choice = 1
    dataf = pd.read_csv('movie2.csv')
    df = dataf.loc[[choice]]
    # print(df)
    noofseat = df.loc[:, 'seats'][choice]
    # print('number of seats',noofseat)

    seat = random.randrange(1, noofseat+1)
    # print(seat)
    return seat


def append(code, name, tomsdate, time, seat):
    df = pd.read_csv('trans.csv')
    df1 = df.tail(1)
    # print(df)
    df1 = df.loc[:, ['id'][0]]
    for i in df.index:
        a = i
    idd = df1[i]+1
    # print(idd)
    # print(code,name,tomsdate,time,seat)

    newrow = {
        'id': idd,
        'code': code,
        'name': name,
        'show_date': tomsdate,
        'show_time': time,
        "seat_number": seat
    }

    df = df.append(newrow, ignore_index=True)
    print(df)
    df.to_csv('trans.csv', index=False)


def details():
    time, choice = timeslot()
    dataf = pd.read_csv('movie2.csv')
    df = dataf.loc[[choice]]
    # print(df)
    name = df.loc[:, 'name'][choice]  # movie name
    code = int(df.loc[:, 'code'][choice])  # movie code
    tomsdate = date()
    # print(tomsdate)
    # # print(type(date))
    # print(type(choice))
    # print(type(time))
    # print(type(name))
    # print(type(code))

    i = 0
    seat = seatchecker(name, time, tomsdate, i)
    print('seat number is', seat)
    try:
        input("Press enter to continue")
    except SyntaxError:
        pass
    if seat:
        # print('yes seat')
        append(code, name, tomsdate, time, seat)
    system('clr')
    try:
        input("Press enter to continue")
    except SyntaxError:
        pass
    
    print(" ---------------------------------<< your ticket has been bocked >>-------------------------------------")


def seatchecker(name, time, tomsdate, i):
    seat = seatnumber()
    if (i == 500):
        return print("house full")
    df1 = pd.read_csv('trans.csv')
    for index, row in df1.iterrows():
        # print(row['code'],code,row['name'],name)
        if row['name'] == name and row['show_time'] == time and row['show_date'] == tomsdate and row['seat_number'] == seat:
            # print(index, row['name'],row['show_date'],row['show_time'],row['seat_number'])
            i = i+1
            seat = seatchecker(name, time, tomsdate, i)

    return seat


# details()


def main():
    while 1:    
        system('cls')
        print("------------------------------------------<< Cinemax >>------------------------------------------")
        choice = int(
            input("1. Movies \n2. Booking  \n3. EXIT \nEnter Your Choice : "))
        if choice == 1:
            movie()
        elif choice == 2:
            details()
        elif choice == 3:
            print("Open to feedback")
            break
        else:
            print("<< invalid syntax >>")


main()
# show(1)

