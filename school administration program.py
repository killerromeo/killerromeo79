if __name__=='__main__':
     condition=True
     student_num=1
     print("------------------------------------------------------")
     print("\SCHOOL ADMINISTRTION PROGRAM")
     print("------------------------------------------------------")
     while(condition):
          student_info=input("\nEnter student information for student #{} in the following format (Name Age Contact_number E-mail_ID):". format(student_num))
          student_info_list=student_info.split(' ')
          print("\nThe entered information is- \n1)NAME: {} \n2)AGE: {} \n3)CONTACT_NUMBER: {} \n4)E-MAIL_ID: {}". format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
          choice_check=input("Is the entered information correct?(yes/no):")
          if choice_check=='yes':
               condition_check=input("Enter (yes/no) if you want to enter information for another student:")
               if condition_check=='yes':
                        condition=True
                        student_num=student_num+1
               elif condition_check=='no':
                        condition=False
          elif choice_check=='no':
               print("\n please re-enter the value!")
print("\n------------------------------------------------------")
print("----------------------THE END-------------------------")
print("------------------------------------------------------")
