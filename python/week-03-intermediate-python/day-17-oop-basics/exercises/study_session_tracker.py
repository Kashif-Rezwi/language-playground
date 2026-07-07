# Study Session Tracker
# Uses object attributes and methods to update and report learning progress.


class StudySession:
    def __init__(self, topic, planned_hours):
        self.topic = topic.strip().title()
        self.planned_hours = planned_hours
        self.completed_hours = 0

    def add_completed_hours(self, hours):
        if hours <= 0:
            print("Completed hours must be greater than zero.")
            return

        self.completed_hours = self.completed_hours + hours

    def calculate_remaining_hours(self):
        remaining_hours = self.planned_hours - self.completed_hours

        return 0 if remaining_hours < 0 else remaining_hours

    def print_summary(self):
        remaining_hours = self.calculate_remaining_hours()

        print("\n--- Study Progress ---")
        print(f"Topic:           {self.topic}")
        print(f"Planned hours:   {self.planned_hours:.2f}")
        print(f"Completed hours: {self.completed_hours:.2f}")
        print(f"Remaining hours: {remaining_hours:.2f}")


print("\n==========================================")
print("          STUDY SESSION TRACKER           ")
print("==========================================\n")

topic = input("Enter study topic: ")
planned_hours = float(input("Enter planned hours: "))

session = StudySession(topic, planned_hours)

while session.calculate_remaining_hours() > 0:
    completed_hours = float(input("Enter newly completed hours: "))
    session.add_completed_hours(completed_hours)
    session.print_summary()

print("\nStudy goal completed!")
