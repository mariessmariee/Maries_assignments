from sys import argv
import csv
import random

students = []


def read_csv(filename):
    global students
    try:
        with open(filename, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        print("File not found.")
        exit()


def populate_scores():
    weeks = [f"week{i}" for i in range(1, 14) if i != 6]
    for student in students:
        for week in weeks:
            if week not in student or student[week].strip() in ["", "-"]:
                student[week] = str(random.randint(0, 3))


def calculate_all():
    for student in students:
        scores = [int(student[week]) for week in student if week.startswith("week") and student[week].strip().isdigit()]
        total = calculate_total(scores)
        average = calculate_average(scores)
        student["Total Points"] = total
        student["Average Points"] = average

def calculate_total(scores):
    total = sum(sorted(scores, reverse=True)[:10])
    return total

def calculate_average(scores):
    average = round(sum(scores) / len(scores), 2) if scores else 0
    return average

def write_csv(filename):
    if not students:
        return
    fieldnames = list(students[0].keys())
    with open(filename, mode="w", newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)


def print_analysis():
    stream_a = []
    stream_b = []
    for student in students:
        if "Stream" in student:
            avg = float(student["Average Points"])
            if student["Stream"].strip().upper() == "A":
                stream_a.append(avg)
            elif student["Stream"].strip().upper() == "B":
                stream_b.append(avg)
    if stream_a:
        print("Stream A average:", round(sum(stream_a) / len(stream_a), 2))
    if stream_b:
        print("Stream B average:", round(sum(stream_b) / len(stream_b), 2))
    weeks = [f"week{i}" for i in range(1, 14) if i != 6]
    for week in weeks:
        week_scores = []
        for student in students:
            if week in student and student[week].strip().isdigit():
                week_scores.append(int(student[week]))
        if week_scores:
            print(f"{week} average:", round(sum(week_scores) / len(week_scores), 2))

if __name__ == "__main__":
    filename = "class_grades.csv"

    print("Open file:", filename)

    read_csv(filename)
    populate_scores()
    calculate_all()

    user_name = "Marie"
    newname = filename.split(".")[0] + "_calculated_by_" + user_name + ".csv"

    write_csv(newname)
    print("New file written:", newname)

    print_analysis()