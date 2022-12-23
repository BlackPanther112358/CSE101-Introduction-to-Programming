#Declaring global variables
ques_cnt = 0
answer_key = dict()
student_list = list()       #[[Student_name, Student_no.]]
score_list = list()     

#Declaring functions
def read_answer_key()->bool:
    global answer_key, ques_cnt
    with open(r'Q4\Admin\AnswerKey.txt', 'r') as f_key:
        for line in f_key:
            line.strip(r'\n')
            try:
                ques_num, correct_option = line.split()
            except Exception:
                print('Incorrect file format in answer key, Program terminated')
                return False
            if((ques_num.isdigit()) and (correct_option in 'ABCDabcd')and (int(ques_num) == (ques_cnt + 1))):
                ques_cnt += 1
                answer_key[ques_num] = correct_option
            else:
                print('Incorrect file format in answer key, Program terminated')
                return False
    return True

def read_students():
    global student_list
    with open(r'Q4\Admin\RegisteredStudents.txt', 'r') as f_students:
        for line in f_students:
            line.strip(r'\n')
            try:
                name, num = line.split()
            except Exception:
                print('Incorrect file format in file of registered students, Program terminated')
                return False
            if(num.isdigit()):
                student_list.append([name, num])
            else:
                print('Incorrect file format in file of registered students, Program terminated')
                return False
    return

def read_attempt(file_name:str)->int:
    score, cur_ques = 0, 1
    open_file = f"Q4\\Student\\{file_name}.txt"
    try:
        with open(open_file, 'r') as f_student:
            for line in f_student:
                line.strip(r'\n')
                try:
                    ques_num, choosen_option = line.split()
                except Exception:
                    return False
                if((ques_num.isdigit()) and (int(ques_num) == cur_ques) and (choosen_option in 'ABCDabcd-')):
                    cur_ques += 1
                    if(choosen_option == answer_key[ques_num]):
                        score += 4
                    elif(choosen_option == '-'):
                        score += 0
                    else:
                        score -= 1
                else:
                    return False
    except FileNotFoundError:
        return False
    return score

def write_results():
    f_result = open(r'Q4\Admin\FinalReport.txt', 'w')
    f_result.writelines(score_list)
    f_result.close()
    return

def compute_results()->tuple:
    global score_list
    tot_cnt, success = 0,0
    for student_details in student_list:
        tot_cnt += 1
        val = read_attempt('_'.join(student_details))
        if val is False:
            print(f'The file for {student_details[0]} (No.: {student_details[1]}) is not in proper format/ not present in directory')
        else:
            success += 1
            score_list.append(student_details[0] + ' ' + student_details[1] + ' ' + str(val) + '\n')
    write_results()
    return success, tot_cnt

def main():
    try:    #Check if file for registered student and answer key and is non-empty
        f_test = open(r'Q4\Admin\RegisteredStudents.txt', 'r')
        data = f_test.read()
        if data == '':
            print('The file for registered students is empty')
            f_test.close()
            return
        f_test.close()
    except FileNotFoundError:
        print("File for registered students doesn't exist in current directory.")
        return
    try:    
        f_test = open(r'Q4\Admin\AnswerKey.txt', 'r')
        data = f_test.read()
        if data == '':
            print('The file for answer key is empty')
            f_test.close()
            return
        f_test.close()
    except FileNotFoundError:
        print("File for answer key doesn't exist in current directory.")
        return
    try:        #check if result file also exists
        f_test = open(r'Q4\Admin\FinalReport.txt', 'r')
        data = f_test.read()
        if data != '':
            print('The result is already present in the directory, do you want to overwrite it?')
            try_cnt = 0
            while try_cnt < 3:
                try_cnt += 1
                ans = input('Please enter your choice (Yes/No): ').strip()
                if ans.lower() == 'no':
                    print('Program terminated')
                    f_test.close()
                    return
                elif ans.lower() == 'yes':
                    print('Contents of file will be overwritten.')
                    break
                print('Please enter a valid input')
            else:
                print('Program terminated due to multiple invalid inputs')
                f_test.close()
                return
        print()
        f_test.close()
    except FileNotFoundError:
        pass
    check = read_answer_key()
    if check is False:
        return
    check = read_students()
    if check is False:
        return
    result = compute_results()
    if result is False:
        return
    success, total = result
    print()
    print(f'The results for {success} students have been updated in the Admin folder, out of {total} studetnts.')
    print()
    return

#Driver code
if __name__ == '__main__':
    print('-'*100)
    main()
    print('-'*100)