# This project is going to use some SQL tables.
# So we need to create the SQL database for this program explicitly.
# All the required name of the tables and rows and columns are listed below.
# The database is created using XAMPP application and local server.
# The name of the database will be 'tinder'.
# There will be 2 tables in the database named as 
# 1. "users"  ( for all the users' details.)
# 2. "proposal"  (proposal details.i.e.:-this table will contain all the details of all the proposals.)

import mysql.connector


class Tinder:
    def __init__(self):
        self.conn = mysql.connector.connect(host='localhost', user='root', password='', database='tinder')
        self.mycursor = self.conn.cursor()
        self.program_menu()
        self.login=0

    def program_menu(self):                                                     #-------Programme menu------#
        program_input = input("""Hi what you want to do....
           1. Enter 1 for Registration-->
           2. Enter 2 for Login-->
           3. enter 3 for Exit--->
           :""")

        if program_input == '1':
            self.register()

        elif program_input == '2':
            self.login()
        elif program_input=='3':
            print("Byeee!")
        else:
            print('Enter a valid input')
            self.program_menu()

    def register(self):                                                         #-----regiter menu-------#
        name = input('Enter your name--:(If you want to go back enter \'go back\'.)')
        if name.lower()=='go back': 
            self.program_menu()
        else:    
            email = input('Enter your email--:')
            self.email_check(email)
            password = input('Enter your password--:')
            gender = input('Enter your gender--:')
            age = input('Enter your age--:')
            city = input('Enter your city--:')
    
            print("--------------Registration successful!!!--------------------")
            self.program_menu()
            self.mycursor.execute("""INSERT INTO  `users` (`user_id`,`name`,`email`,`password`,`gender`,`age`,`city`)
            VALUES(NULL, '{}','{}','{}','{}','{}','{}')""".format(name, email, password, gender, age, city))

            self.conn.commit()

    def email_check(self,email):                                                #---check email is repeted or not--#
            self.mycursor.execute(""" SELECT * FROM `users` WHERE `email` LIKE '{}' """.format(email))
            email_detector=self.mycursor.fetchall()
            email_c='no'
            for i in email_detector:
                email_c='yes'
            if email_c=='yes':
                print('This email address has been used once,please try again with another email address.')
                self.register()


    def login(self):                                                            #------login menu---------#
        email=input(' Enter your Email to login--> ')
        password=input('Enter your password to login-->')

        self.mycursor.execute(""" SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}' """.format(email,password))

        user_list=self.mycursor.fetchall()
        counter=0

        for i in user_list:
            counter=counter+1
            current_user=i

        if counter>0:
            print("WELCOME!!")
            self.current_user_id=current_user[0]
            self.login=1

            self.user_menu()
        else:
            print("Incorrect credentials!")
            self.login()

        
            

    def user_menu(self):                                                        #------user menu---------#
        if self.login==1:
            user_input=input("""How would you like to proceed=
            1.Enter 1 to view all users---
            2.Enter 2 to view your all proposal---
            3.Enter 3 to view your all proposal request---
            4.Enter 4 to view all your matches if any---
            5.Enter 5 to Logout---""")


            if user_input=='1':
                self.view_users()
            elif user_input=='2':
                self.view_proposal()
            elif user_input=='3':
                self.view_request()
            elif user_input=='4':
                self.view_matches()
            elif user_input=='5':
                self.logout()
            else:
                print('Enter a valid input')
                self.user_menu()

        else :
            print('Please login.\n')
            self.login()
            




    def view_users(self):                                                   #show all users

        if self.login==1:
            self.mycursor.execute(""" SELECT * FROM `users` WHERE `user_id` NOT LIKE '{}' """.format(self.current_user_id))
            all_users=self.mycursor.fetchall()

            for i in (all_users):
                print(i[0],'|', i[1],'|',i[4],'|',i[5],'|',i[6])
                print('_______________________________________')

            user_data=input("Enter the ID of the user whom you want to Propose.or enter \'go back\' to go back to the previous menu.")
            if user_data.lower()=='go back':
                self.user_menu()
            else:
                juliet_id=user_data
                self.propose(juliet_id=juliet_id, romeo_id=self.current_user_id)
        else:
            print('Please login to conteneu')
            self.login()

                                                                                               #sending proposal########################################
    def propose(self,juliet_id,romeo_id):
        if self.login==1:
            self.check_proposal(juliet_id,romeo_id)
            if self.counterx!=0:
                self.view_users()
            else:
                self.mycursor.execute("""INSERT INTO `proposal` (`proposal_id`, `romeo_id`,`juliet_id`) VALUES (NULL,'{}','{}') """.format(romeo_id,juliet_id))

                self.conn.commit()

                print("Proposal send successfully!. Fingers crossed")
                self.user_menu()

        else:
            print('Please login to conteneu')
            self.login()

    def check_proposal(self,juliet_id,romeo_id):                                #checking if already proposed or not.
        self.mycursor.execute("""SELECT * FROM `proposal` WHERE `juliet_id` LIKE '{}' AND `romeo_id` LIKE '{}' """.format(juliet_id,romeo_id))
        self.counterx=0
        result=self.mycursor.fetchall()
        for i in result:
            self.counterx+=1

        if self.counterx!=0:
            print('You have already proposed that person.please choose another one.\n')
        


    def view_proposal(self):                                                        #--view proposal list
        if self.login==1:
            self.mycursor.execute("""SELECT * FROM `proposal` p JOIN `users` u ON u.`user_id`=p. `juliet_id` WHERE p.`romeo_id` LIKE '{}'""".format(self.current_user_id))


            proposed_user_list=self.mycursor.fetchall()

            for i in proposed_user_list:
                print(i[4], '|' , i[7], '|',i[8], '| ',i[9])
                print('------------------------------------')

            self.user_menu()

        else:
            print('Please login to conteneu')
            self.login()

    def view_request(self):                                                         #view request list
        if self.login==1:
            self.mycursor.execute("""SELECT * FROM `proposal` p JOIN `users` u ON u.`user_id`=p. `romeo_id` WHERE p.`juliet_id` LIKE '{}'""".format(self.current_user_id))


            requested_user_list=self.mycursor.fetchall()

            for i in requested_user_list:
                print(i[4], '|' , i[7], '|',i[8], '| ',i[9])
                print('------------------------------------')

            self.user_menu()

        else:
            print('Please login to conteneu')
            self.login()





    def view_matches(self):                                                         #view matches
        if self.login==1:
            self.mycursor.execute(
            """SELECT * FROM `proposal` p 
            JOIN`users` u ON u.`user_id`=p.`juliet_id`
             WHERE `juliet_id` IN
             (SELECT `romeo_id` FROM `proposal` WHERE `juliet_id` LIKE'{}')
             AND `romeo_id` LIKE '{}'""".format(self.current_user_id,self.current_user_id))


            requested_user_list=self.mycursor.fetchall()

            for i in requested_user_list:
                print(i[4], '|' , i[5], '|', i[7], '|',i[8], '| ',i[9])
                print('------------------------------------')

            self.user_menu()

        else:
            print('Please login to conteneu')
            self.login()


    def logout(self):
        self.login=0
        self.program_menu()

                


        
        

            



user=Tinder()
print("765")

