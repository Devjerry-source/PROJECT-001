#Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# Declaration of variables
df1, df_per_std, relevant_columns, col_values, std, table  = [], [], [], [], [], []
dict1, dict2, std_attempt = {}, {}, {}
count1, count2, count3, count4, count5, count6, count7, perf, perf2, marks, mark2, mark3, std_grade, std_reg, std_total, reg_no, total_score, num, ID = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
std_name, std_sch, city_res, country_res, std_gender, std_date_of_birth, std_test_date, std_time, name, grade, sch_name, city_residence, country_residence, gender, date_of_birth, test_date, extra_time, comment_set1, remarks = "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""
  
#Reading the csv file
df_std = pd.read_csv('wizzy.csv')
#df_std = pd.read_csv('newWizzy.csv')

#this strips trailing spaces in each column name cells
clean_col = [i.strip() for i in df_std.columns]
df_std.columns = clean_col

#creating a list of unique student iDs
#student_list = [1,2,3]
student_list = list(set(val for val in df_std['Student No']))

def preprocessing():
    global df1, relevant_columns, std, df_per_std
    
    df1 = df_std[df_std['Student No'] == ID]
    
    #renaming long text column name
    df1.rename(columns = {'What you marked': 'Option marked', 'Outcome (Correct/Incorrect/Not Attempted)': 'Outcome', 'Time Spent on question (sec)': 'Time spent (Sec)'}, inplace = True)
        
    relevant_columns = ['Student No', 'Name of Candidate', 'Registration', 'Grade', 'Gender', 'Name of school', 'Date of Birth', 'City of Residence', 'Date and time of test', 'Country of Residence', 'Extra time assistance', 'Question No.', 'Time spent (Sec)', 'Score if correct', 'Score if incorrect', 'Attempt status', 'Option marked', 'Correct Answer', 'Outcome', 'Your score']
        
    #creating a data frame for each student based on the provided student number and selected relevant columns
    df_per_std = df1[relevant_columns]
    
    #create a data frame duplicate
    std = df_per_std.copy()
        
    #dropping irrelevant columns from students dataframe
    std = std.drop(['Student No', 'Name of Candidate', 'Registration', 'Grade', 'Gender', 'Name of school', 'Date of Birth', 'City of Residence', 'Date and time of test', 'Country of Residence', 'Extra time assistance'], axis = 1)


def processing():
    global count1, count2, count3, count4, count5, count6, count7, perf, perf2, mark2, mark3, std, std_attempt, remarks, marks
    
    # this maps the count of each items in the "outcome" column to some selected item names   
    for i in std['Outcome']:
        if i == 'Correct':
            dict1[i] = 1 + count1
            count1 += 1
        elif i == 'Incorrect':
            dict1[i] = 1 + count2
            count2 += 1
        elif i == 'Unattempted':
            dict1[i] = 1 + count3
            count3 += 1
        
    #this creates two list of the column values and how many times they appear against the other
    perf = list(dict1.keys())
    mark2 = list(dict1.values())
    
    # this maps the count of each items in the "Attempt status" column to their respective name    
    for z in std['Attempt status']:
      if z == 'Attempted':
          std_attempt[z] = 1 + count6
          count6 += 1
      elif z == 'Unattempted':
          std_attempt[z] = 1 + count7
          count7 += 1
                
    remarks = list(std_attempt.keys())
    marks = list(std_attempt.values())

    # this maps the count of each items in the "outcome" column to some selected item names
    for w in std['Outcome']:
        if w == 'Correct':
            dict2[w] = 1 + count4
            count4 += 1
        elif w == 'Incorrect':
            dict2[w] = 1 + count5
            count5 += 1
            
        
    #this creates two list of two column values out of the three expected and how many times they appear against the other
    perf2 = list(dict2.keys())
    mark3 = list(dict2.values())

# GENERATION OF GRAPH PLOTS    

def graph_plot():
    
    # BAR CHART
    
    #ploting a Bar chart of the time spent in sec 
    plt.bar(std['Question No.'], std['Time spent (Sec)'])
    plt.title('Time Spent in Seconds')
    plt.xlabel('Question Number')
    plt.ylabel('Time in Seconds')
    plt.legend('Seconds')
    plt.savefig('time_sec.png')
    plt.show()
       
    # PIE CHARTS
    
    #ploting the time in sec taken in hours
    plt.figure(0)
    plt.pie(std['Time spent (Sec)'], autopct = '%1.1f%%')
    plt.title('Time spent as a function of total time')
    plt.legend(labels = std['Question No.'], loc = 'best')
    plt.savefig('time_hrs.png')
    plt.show()
        
    #ploting the Attempts and Unattempts made
    plt.figure(1)
    plt.pie(marks, autopct = '%1.1f%%')
    plt.title('Attempts')
    plt.legend(remarks, loc = 'best')
    plt.savefig('Attempts.png')
    plt.show()
        
    #plotting the overall performance of the student
    plt.figure(2)
    plt.pie(mark2, autopct = '%1.1f%%')
    plt.title('Overall performance against the test')
    plt.legend(perf)
    plt.savefig('performance.png')
    plt.show()
        
    #plotting the students performance based on correct and incorrect answers
    plt.figure(3)
    plt.pie(mark3, autopct = '%1.1f%%')
    plt.title('Accuracy from attempted questions')
    plt.legend(perf2)
    plt.savefig('Accuracy.png')
    plt.show()
    

# GENERATION OF A TABLE 

def table_gen():
    global table 
    
    # a list of list containing each groups of row-times per column in "std" dataframe    
    for c in range(len(std.columns)):
        col_values.append([])
        for val in std[std.columns[c]]:
            col_values[c].append(val)
        
    #this converts each column name in "std" dataframe to a list of list for zipping
    columns = [[std.columns[i]] for i in range(len(std.columns))]
        
    #this zips the columns with their values into a list called table
    table_list = [list(x) + y for x, y in zip(columns, col_values)]
    table = list(zip(*table_list))
    
# STUDENT BIO-DATA EXTRACTION 

def bio_data():
    global df1, df_per_std,  df_std, num, std_name, std_sch, std_grade, city_res, country_res, std_reg, std_gender, std_date_of_birth, std_test_date, std_time, std_total, name, grade, sch_name, city_residence, country_residence, reg_no, gender, date_of_birth, test_date, extra_time, total_score, comment_set1 
    
    #extracting the first index position
    for ind in df_std.index[df_std['Student No'] == ID]:
        num = ind
        break
        
        
    #student Biodata
    std_name = df1.loc[num, 'Name of Candidate']
    std_sch = df1.loc[num, 'Name of school']
        
    std_grade = df1.loc[num, 'Grade']
    city_res = df1.loc[num, 'City of Residence']
        
    country_res = df1.loc[num, 'Country of Residence']
    std_reg = df1.loc[num, 'Registration']
        
    std_gender = df1.loc[num, 'Gender']
    std_date_of_birth = df1.loc[num, 'Date of Birth']
        
    std_test_date = df1.loc[num, 'Date and time of test']
    std_time = df1.loc[num, 'Extra time assistance']
    
    std_total = df_per_std['Your score'].sum()
        
    #Entering the values into the Pdf
    name = f'Name of Candidate:  {std_name}'
    grade = f'Grade:  {std_grade}'
        
    sch_name = f'School Name:  {std_sch}'
    city_residence = f'City of Residence:  {city_res}'
        
    country_residence = f'Country of Residence:  {country_res}'
    reg_no = f'Registration No:  {std_reg}'
        
    gender = f'Gender:  {std_gender}' 
    date_of_birth = f'Date of birth:  {std_date_of_birth}'
        
    test_date = f'Date of Test:  {std_test_date}' 
    extra_time = f'Extra Time assistance:  {std_time}'
        
    #the student's total score
    total_score = f'Total Score = {std_total}'
    comment_set1 = '1. Is showing interest and enthusiasm for things we do. 2. Is cooperative and happy. 3. Volunteers often in class 4. Works hard. 5. Is self confident 6. Is helpful to others 7. Needs to imporve work habits 8. Fails to complete assignments on time'

# GENERATION OF PDF

def pdf_gen():
    # Letter size paper, use inches as unit of measure
    pdf = FPDF(orientation = 'L', format = 'A4', unit = 'in')
        
    # Add new page. Without this you cannot create the document.\
    pdf.add_page()
        
    # Effective page width, or just epw
    epw = pdf.w - 2*pdf.l_margin
        
    pdf.set_font('Arial', 'B', 16.0)
    pdf.set_text_color(0, 0, 150)
    pdf.cell(11, 0.0, 'GREAT MINDS INSTITUTE REPORT CARD', align = 'R')
    
    pdf.ln(0.20)
    
    pdf.set_font('Arial', 'B', 14.0)
    pdf.cell(10, 0.0, 'PERFORMANCE REPORT', align = 'L')
    
    pdf.ln(0.50)
    
    pdf.set_font('Times', '', 12.5)
    pdf.set_text_color(0, 0, 0)
        
    #importing the students passport
    pdf.image(f'{ID}.jpg', x = 9.0, y = 1)
    
    pdf.ln(0.20)
    
    pdf.cell(6, 0.0, name)
    pdf.cell(10, 0.0, grade)
    
    pdf.ln(0.30)  
    
    pdf.cell(6, 0.0, sch_name)
    pdf.cell(10, 0.0, city_residence)
    
    pdf.ln(0.30)
        
    pdf.cell(6, 0.0, country_residence)
    pdf.cell(10, 0.0, reg_no)
    
    pdf.ln(0.30)
        
    pdf.cell(6, 0.0, gender)
    pdf.cell(10, 0.0, date_of_birth)
    
    pdf.ln(0.30)
        
    pdf.cell(6, 0.0, test_date)
    pdf.cell(10, 0.0, extra_time)
    
    pdf.ln(0.50)
        
    th = pdf.font_size
    
    # this inserts a table in the pdf    
    for data in table:
       for item in data:
           pdf.cell(1.25, th, str(item), border = 1)
            
       pdf.ln(0.20)
    
            
    pdf.ln(0.30)
    
    pdf.set_font('Arial', 'B', 14.0)
    pdf.cell(11, 0.0, total_score, align = 'R')
        
    pdf.ln(0.25)
    
    pdf.set_font('Times', '', 10)
    pdf.cell(8, th, 'PERFORMANCE ANALYSIS.', align = 'C')
        
    pdf.ln(0.20)
    
    # these inserts several plots in the pdf
    pdf.image('time_sec.png', x= 1, w = 2)
    pdf.image('time_hrs.png', x = 3, y = 5, w = 2)
    pdf.image('performance.png', x = 5, y = 5, w = 2)
    pdf.image('Attempts.png', x = 7, y = 5, w = 2)
    pdf.image('Accuracy.png', x = 9, y = 5, w = 2)
        
    #comments for the student.
    pdf.cell(8, th, 'Report Card Comments', align = 'C')
    pdf.ln(0.20)
    pdf.multi_cell(epw, 0.15, comment_set1)
        
    pdf.ln(0.20)
    
    pdf.cell(4, 0.13, 'Thanks for your patronage.')
    pdf.cell(7, 0.0, 'Motto: Knowledge for Excellence', align = 'R')
        
    #exporting the report card
    pdf.output(std_name + '_ReportCard.pdf', 'F')

def refresh():
    global dict1, dict2, col_values, std, std_attempt, count1, count2, count3, count4, count5, count6, count7, marks, mark2, mark3, mark, perf, perf2, remarks
    
    col_values, std = [], []
    dict1, dict2, std_attempt = {}, {}, {} 
    count1, count2, count3, count4, count5, count6, count7, marks, mark2, mark3, perf, perf2 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    remarks = ""      
    
def main():
    global ID 
    
    for i in student_list:
        ID =  i
            
        preprocessing()
        processing()
        bio_data()
        graph_plot()
        table_gen()
        pdf_gen()
        refresh()
        
main()

print(f'{len(student_list)} score card PDFs generated sucessfully!!!')        