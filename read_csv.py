import csv
import os
import student_class

file_path = os.path.dirname(__file__)
csv_path = f"{file_path}\Sample Student.csv"  

def read_rows_csv(file_path):
        '''
        Taking in a file path, it each row from the csv file and returns a list with all of the rows
        '''
        rows = []
        with open(csv_path) as file_obj:
                reader_obj = csv.reader(file_obj)
                for row in reader_obj:
                        rows.append(row)
        return rows

def make_list_into_numbers(string):
        '''
        Taking in a string, it transforms all items in that list into integers
        '''
        split = string.strip().split(',')
        return_list = []
        for item in split:
                if item != '':
                        return_list.append(int(item))
        return return_list


def make_strings_into_tuples(string):
        '''
        Taking in a string that contains tuples in a string format, make tuples for them
        '''
        split = string.split("),")
        clean_strings = []
        for item in split:
                if item != "":
                        clean = item.replace('(', '').replace(")", '')
                        clean = clean.strip()
                        if clean != '':
                                clean_strings.append(clean.strip())
        
        return_list = []
        for string in clean_strings:
                make_tuple = tuple(make_list_into_numbers(string))
                return_list.append(make_tuple)
        
        return return_list
        
        
def internal_rep(rows):
        '''
        Taking in the list of rows from the csv, it makes the header and the students class objects
        '''
        student_list = {}
        
        for i in range(1, len(rows)):
                current_row = rows[i]
                student_name = current_row[0]
                student_test_scores = make_list_into_numbers(current_row[1])
                student_quiz_scores  = make_list_into_numbers(current_row[2])
                student_exit_surveys = make_strings_into_tuples(current_row[3])
                student_before_test_scores = make_strings_into_tuples(current_row[4])
                student = student_class.student(student_name, student_test_scores, student_quiz_scores, student_exit_surveys, student_before_test_scores)
                student_list[student_name] = student
        
        return student_list

def make_internal_rep(file_path):
        '''
        Just a general function that just needs to be called with one line to make internal representation
        '''
        rows = read_rows_csv(file_path)
        internal = internal_rep(rows)
        return internal

student_dict = make_internal_rep(csv_path)
