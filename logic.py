import csv


class GradeBook:
    def __init__(self):
        """Initialize an empty list of students."""
        self.students = []

    def add_student(self, name, student_id, attempts, scores):
        """add student to grade book"""
        final_score = sum(scores) / attempts
        student_data = {
            'Name': name,
            'Student ID': student_id,
            'Score 1': scores[0] if attempts > 0 else 0,
            'Score 2': scores[1] if attempts > 1 else 0,
            'Score 3': scores[2] if attempts > 2 else 0,
            'Score 4': scores[3] if attempts > 3 else 0,
            'Highest': max(scores) if scores else 0,
            'Lowest': min(scores) if scores else 0,
            'Final': final_score,
            'Grade': self.letter_grade(final_score)
        }
        self.students.append(student_data)

    def score_handling(self):
        """compute data (highest, lowest, average scores"""
        if not self.students:
            return None

        final_scores = [student['Final'] for student in self.students]
        highest = max(final_scores)
        lowest = min(final_scores)
        average = sum(final_scores) / len(final_scores)
        average_grade = self.letter_grade(average)

        return (f'Highest Score: {highest}, Lowest Score: {lowest}, '
                f'Class Average: {average:.2f}, Class Average Grade: {average_grade}')

    def export_csv(self, filename):
        """export students to csv file"""
        headers = ['Name', 'Student ID', 'Score 1', 'Score 2', 'Score 3', 'Score 4',
                   'Highest', 'Lowest', 'Final', 'Grade']
        data = self.score_handling()
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            writer.writerows(self.students)
            if data:
                writer.writerow({'Name': data, 'Student ID': '', 'Score 1': '', 'Score 2': '',
                                 'Score 3': '', 'Score 4': '', 'Highest': '', 'Lowest': '', 'Final': '', 'Grade': ''})

    def letter_grade(self, score):
        """calculate letter grade"""
        if score >= 97:
            return 'A+'
        elif score >= 93:
            return 'A'
        elif score >= 90:
            return 'A-'
        elif score >= 87:
            return 'B+'
        elif score >= 83:
            return 'B'
        elif score >= 80:
            return 'B-'
        elif score >= 77:
            return 'C+'
        elif score >= 73:
            return 'C'
        elif score >= 70:
            return 'C-'
        elif score >= 67:
            return 'D+'
        elif score >= 63:
            return 'D'
        elif score >= 60:
            return 'D-'
        else:
            return 'F'

    def __str__(self):
        """Return a string representation of the gradebook"""
        return f'{len(self.students)} students in the grade book'
