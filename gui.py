import tkinter as tk    
from tkinter import ttk 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog as fd
import read_csv

class GUI():
        def __init__(self):
                self.student_dict = {}
                
                self.student_names = []
                
                self.main_window = tk.Tk()
                self.main_window.title("Student Information")
                
                self.left_frame = tk.Frame(self.main_window)
                self.left_frame.grid(row=0, column=0)
                
                self.choose_file_frame = tk.Frame(self.left_frame)
                self.choose_file_frame.pack()
                
                self.choose_file_button = ttk.Button(self.choose_file_frame, text='Choose File', command=self.choose_file_command)
                self.choose_file_button.pack()
                
                self.student_info_frame = tk.Frame(self.left_frame)
                self.student_info_frame.pack()
                
                
                #GRAPHSSS
                self.graph_frame = tk.LabelFrame(self.main_window, text="Graph")
                self.graph_frame.grid(row=0, column=1)
                
                self.test_score_frame = tk.Frame(self.graph_frame)
                self.test_score_frame.grid(row=0, column=0, padx=10, pady=10)
                
                self.quiz_score_frame = tk.Frame(self.graph_frame)
                self.quiz_score_frame.grid(row=0, column=1,padx=10, pady=10)
                
                self.exit_score_frame = tk.Frame(self.graph_frame)
                self.exit_score_frame.grid(row=1, column=0,padx=10, pady=10)
                
                self.before_test_score_frame = tk.Frame(self.graph_frame)
                self.before_test_score_frame.grid(row=1, column=1,padx=10, pady=10)
                
                
                
                self.test_fig = Figure(figsize = (4, 4),
                 dpi = 80)
                self.test_plot = self.test_fig.add_subplot(111) 
                self.test_canvas = FigureCanvasTkAgg(self.test_fig, master = self.test_score_frame)
                
                self.quiz_fig = Figure(figsize = (4, 4),
                 dpi = 80)
                self.quiz_plot = self.quiz_fig.add_subplot(111) 
                self.quiz_canvas = FigureCanvasTkAgg(self.quiz_fig, master = self.quiz_score_frame) 
                
                self.exit_fig = Figure(figsize = (4, 4),
                 dpi = 80)
                self.exit_plot = self.exit_fig.add_subplot(111) 
                self.exit_canvas = FigureCanvasTkAgg(self.exit_fig, master = self.exit_score_frame) 
                
                self.before_fig = Figure(figsize = (4, 4),
                 dpi = 80)
                self.before_plot = self.before_fig.add_subplot(111) 
                self.before_canvas = FigureCanvasTkAgg(self.before_fig, master = self.before_test_score_frame) 
                
                
                
                
                self.student_frame = ttk.LabelFrame(self.student_info_frame, text="Students")
                self.student_frame.grid(row=0, column=0)
                
                self.student_listbox_frame = tk.Frame(self.student_frame)
                self.student_listbox_frame.pack()
                
                self.get_info_frame = tk.Frame(self.student_frame)
                self.get_info_frame.pack()
                
                self.student_listbox = tk.Listbox(self.student_listbox_frame, width=50)
                self.student_listbox.pack(side=tk.LEFT, fill='both', expand=1)
                
                self.scrollbar = tk.Scrollbar(self.student_listbox_frame)
                self.scrollbar.pack(side="right", fill="both")
                
                for name in self.student_names:
                        self.student_listbox.insert(tk.END, name)
                
                self.student_listbox.config(yscrollcommand=self.scrollbar.set)
                
                self.scrollbar.config(command=self.student_listbox.yview)
                
                self.get_info_button = ttk.Button(self.get_info_frame, text="Get Info", command=lambda: self.button_command())
                
                self.get_info_button.pack()
                
                self.table_frame = tk.LabelFrame(self.student_info_frame, text='Student Info')
                self.table_frame.grid(row=1, column=0)
                
                self.header = ("#", "Test", "Quiz", "Exit Survey", "Before Test")
                
                self.table = ttk.Treeview(self.table_frame, columns=self.header, show='headings')

                self.setup_treeview()
                
                self.scrollbar = ttk.Scrollbar(self.table_frame, orient="vertical", command = self.table.yview)
                
                self.scrollbar.pack(side=tk.RIGHT, fill='y')
                self.table.pack(fill=tk.BOTH, expand=1, side=tk.RIGHT)
                
                self.main_window.mainloop()
        
        
        def choose_file_command(self):
                for item in self.table.get_children():
                        self.table.delete(item)
                
                self.student_listbox.delete(0, tk.END)
                
                self.test_plot.clear()
                self.test_canvas.draw()
                
                self.quiz_plot.clear()
                self.quiz_canvas.draw()
                
                self.exit_plot.clear()
                self.exit_canvas.draw()
                
                self.before_plot.clear()
                self.before_canvas.draw()
                
                file_path = fd.askopenfilename(filetypes=(("CSV Files","*.csv"),))
                self.student_dict = read_csv.make_internal_rep(file_path)
                self.student_names = list(self.student_dict.keys())
                
                for name in self.student_names:
                        self.student_listbox.insert(tk.END, name)
                        
                
        
        def plot_graph(self, plot_1,data_dict, canvas, title):
                plot_1.clear()
                plot_1.set_title(title)
                for key in data_dict:
                        plot_1.plot(data_dict[key], label=key)
                plot_1.legend()
                canvas.draw()
                canvas.get_tk_widget().pack()

        
        def add_to_treeview(self, student):
                '''
                Adds the student information to the table for better view
                '''
                self.table.delete(*self.table.get_children())
                
                student_test_scores = student.test_scores
                student_quiz_scores = student.quiz_scores
                student_exit_survey_scores = student.exit_survey_scores
                student_before_test_scores = student.before_test_scores
                
                for i in range(len(student_test_scores)):
                        row_value = (i, student_test_scores[i], student_quiz_scores[i], student_exit_survey_scores[i], student_before_test_scores[i])
                        self.table.insert('', tk.END, values=row_value)
                        
                data_dict = make_data_frames(student)
                test = data_dict['test_data']
                quiz = data_dict['quiz_data']
                exit_survey = data_dict['exit_survey']
                before_test = data_dict['before_test']
                
                self.plot_graph(self.test_plot, test, self.test_canvas, "Test")
                
                self.plot_graph(self.quiz_plot, quiz, self.quiz_canvas, "Quiz")
                
                self.plot_graph(self.exit_plot, exit_survey, self.exit_canvas, "Exit Survey")
                
                self.plot_graph(self.before_plot, before_test, self.before_canvas, "Before Test Survey")
                
        def button_command(self):
                selected_indices = self.student_listbox.curselection()
                student_name = self.student_listbox.get(selected_indices)
                student = self.student_dict[student_name]
                self.add_to_treeview(student)
                
        def setup_treeview(self):
                '''
                Just sets up the layout of the table
                '''
                for item in self.header:
                        self.table.heading(item , text = item)
                        self.table.column(item, anchor="center", stretch=tk.NO, width=100)
                        

def make_tuple_into_dict(list_of_tuple):
        '''
        Taking in a list of tuples, returns a dictionary that looks something like this: 
        {
                Question1: []
                Question2:[]
                
        }
        '''
        question_1 = []
        question_2 = []
        question_3 = []
        
        for item in list_of_tuple:
                question_1.append(item[0])
                question_2.append(item[1])
                question_3.append(item[2])
                
        return_dict = {
                "Q1": question_1,
                "Q2": question_2,
                "Q3": question_3
        }
        
        return return_dict
        

def make_data_frames(student):
        '''
        Given a student, make a data frame dictionary for that graph for plotting
        '''
        return_dict = {
                'test_data':{"Test":student.test_scores},
                'quiz_data': {"Quiz": student.quiz_scores}
        }    
        
        student_exit_survey_scores = student.exit_survey_scores
        exit_survey_dict = make_tuple_into_dict(student_exit_survey_scores)
        
        student_before_test_scores = student.before_test_scores
        before_test_dict = make_tuple_into_dict(student_before_test_scores)
        
        return_dict['exit_survey'] = exit_survey_dict
        return_dict['before_test'] = before_test_dict

        return return_dict

table_gui = GUI()