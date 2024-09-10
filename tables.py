import random


class TimeTableGenerator:
    def __init__(self):
        self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        self.time_slots = ['8:00 AM', '9:00 AM', '10:00 AM', '11:00 AM',
                           '12:00 PM', '2:00 PM', '3:00 PM', '4:00 PM', '5:00 PM']
        self.subjects = ['Math', 'Science', 'English',
                         'History', 'Geography', 'Physics', 'Chemistry']

    def generate_timetable(self):
        timetable = {}
        for day in self.days:
            timetable[day] = {}
            available_subjects = self.subjects.copy()
            for time in self.time_slots:
                if available_subjects:
                    subject = random.choice(available_subjects)
                    timetable[day][time] = subject
                    available_subjects.remove(subject)
                else:
                    timetable[day][time] = 'Free Period'
        return timetable

    def print_timetable(self, timetable):
        print("Weekly Time Table")
        print("----------------")
        for day, schedule in timetable.items():
            print(f"\n{day}")
            print("--------------------")
            for time, subject in schedule.items():
                print(f"{time}: {subject}")

    def generate_and_print(self):
        timetable = self.generate_timetable()
        self.print_timetable(timetable)


# Usage
if __name__ == "__main__":
    generator = TimeTableGenerator()
    generator.generate_and_print()
