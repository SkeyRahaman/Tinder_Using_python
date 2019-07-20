from tkinter import *
import tkinter.messagebox
import mysql.connector


class DatingApp:
    def __init__(self):


        try:
            self.conn = mysql.connector.connect(host='localhost', user='root', password='', database='tinder')
            self.mycursor = self.conn.cursor()
        except Exception as ProgrammingError:
            print('can\'t connect to the databace.try agane.')
            self.conn = 'undefined'
            self.mycursor = 'undefined'
        self.user_id = 0
        self.a1 = 0
        self.a2 = 0
        self.a3 = 0
        self.a4 = 0
        self.mycursor.execute("""SELECT * FROM `current_login_profile` WHERE `number` LIKE 0""")
        me_amni= self.mycursor.fetchall()
        login_check = 0
        for i in me_amni:
            login_check = login_check + 1
        if login_check > 1:
            self.user_id = me_amni[1][1]
            self.user_menu()
        else:
            self.program_menu()

    def program_menu(self):


        self.root_program_menu = Tk()
        self.root_program_menu.title('DATING APP')
        self.root_program_menu.minsize(500, 500)


        self.programmingMenuFrame = Frame(self.root_program_menu,bd=3).grid()
        self.heading = Label(self.programmingMenuFrame, text=('TINDER'), bg='red', width=15, height=0,
                             font=("Times", 50,"bold")).grid(row=0, column=1, columnspan=3)
        self.b = Label(self.programmingMenuFrame, text=(''), bg='pink', width=10, height=5).grid(row=0, column=0)
        self.b = Label(self.programmingMenuFrame, text=(''), bg='pink', width=10, height=5).grid(row=0, column=4)
        self.exit = Button(self.programmingMenuFrame, text="EXIT", fg='red', height=2,command=lambda: self.root_program_menu.destroy()).grid(row=0, column=4)

        Email_label = Label(self.programmingMenuFrame, text="Email address:-", font=("Helvetica", 16), width=20,
                            height=2).grid(row=1, column=0, columnspan=2)
        self.login_email_input = Entry(self.programmingMenuFrame,width=50)
        self.login_email_input.grid(row=1, column=2,columnspan=2)


        password_label = Label(self.programmingMenuFrame, text="Password:-", font=("Helvetica", 16), width=20,
                               height=2).grid(row=2, column=0, columnspan=2)
        self.login_Password_input = Entry(self.programmingMenuFrame,width = 50,exportselection=1001)
        self.login_Password_input.grid(row=2, column=2,columnspan=2)


        Login_button = Button(self.programmingMenuFrame, text="Login", font=("", 13),width=25,command = lambda : self.login_get_data()).grid(row=3, column=3)

        registration_intro_label = Label(self.programmingMenuFrame, text="""New user????..
        Quickly register yourself by clicking the register button.""",font=("helvetica", 16)).grid(row=4, column=0, columnspan=4, rowspan=2)
        registration_button = Button(self.programmingMenuFrame, text="Register", font=("", 13),width=25,command = lambda : self.programming_to_register()).grid(row=6, column=3)
        self.root_program_menu.mainloop()
    def programming_to_register(self):
        self.root_program_menu.destroy()
        self.register()

    def login_get_data(self):
        email = self.login_email_input.get()
        password = self.login_Password_input.get()
        self.login(email,password)

    def login(self,email,password):

        self.mycursor.execute(""" SELECT * FROM `users` WHERE `email` LIKE '{}' AND `password` LIKE '{}' """.format(email,password))
        user_list=self.mycursor.fetchall()

        counter=0
        for i in user_list:
            counter=counter+1
            current_user=i

        if counter == 1:
            tkinter.messagebox.showinfo('Login result','LOGIN SUCESSFULL.')
            user_id_l = user_list[0][0]
            name_l = user_list[0][1]
            email_l= user_list[0][2]
            password_l = user_list[0][3]
            gender_l = user_list[0][4]
            age_l =user_list[0][5]
            city_l = user_list[0][6]
            number = 0
            self.mycursor.execute("""INSERT INTO `current_login_profile`(`number`, `user_id`, `name`, `email`, `password`, `gender`, `age`, `city`) 
                                        VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')""".format(number,user_id_l,name_l,email_l,password_l,gender_l,age_l,city_l))
            self.conn.commit()

            self.root_program_menu.destroy()
            self.user_id = current_user[0]
            self.user_menu()


        else:
            tkinter.messagebox.showinfo('Login result','INCORRECT EMAIL ADDRESS OR PASSWORD')
            self.root_program_menu.destroy()
            self.program_menu()

    def register(self):
        self.root_register = Tk()
        self.root_register.title('DATING APP')
        self.root_register.minsize(500, 550)


        self.programmingMenuFrame = Frame(self.root_register,bd=3).grid()
        self.heading = Label(self.programmingMenuFrame, text=('TINDER'), bg='red', width=15, height=0,
                             font=("Times", 50,"bold")).grid(row=0, column=1, columnspan=3)
        self.b = Label(self.programmingMenuFrame, text=(''), bg='pink', width=10, height=5).grid(row=0, column=0)
        self.b = Label(self.programmingMenuFrame, text=(''), bg='pink', width=10, height=5).grid(row=0, column=4)
        self.exit = Button(self.programmingMenuFrame, text="EXIT", fg='red', height=2,
                           command=lambda: self.root_register.destroy()).grid(row=0, column=4)


        name_label = Label(self.programmingMenuFrame, text="Name:-", font=("Helvetica", 18)).grid(row=1, column=1,sticky=W)

        self.name_input = Entry(self.programmingMenuFrame,width=50)
        self.name_input.grid(row=1, column=2,columnspan=2)


        email_label = Label(self.programmingMenuFrame, text="Email Address:-", font=("Helvetica", 18)).grid(row=2, column=1,sticky=W)
        self.email_input = Entry(self.programmingMenuFrame,width = 50)
        self.email_input.grid(row=2, column=2,columnspan=2)


        password_label = Label(self.programmingMenuFrame, text="Password:-", font=("Helvetica", 18)).grid(row=3, column=1,sticky=W)
        self.password_input = Entry(self.programmingMenuFrame,width=50)
        self.password_input.grid(row=3, column=2,columnspan=2)


        gender_label = Label(self.programmingMenuFrame, text="Gender:-", font=("Helvetica", 18)).grid(row=4, column=1,sticky=W)
        self.gender_input = Entry(self.programmingMenuFrame,width = 50)
        self.gender_input.grid(row=4, column=2,columnspan=2)


        age_label = Label(self.programmingMenuFrame, text="Age:-", font=("Helvetica", 18)).grid(row=5, column=1,sticky=W)
        self.age_input = Entry(self.programmingMenuFrame,width=50)
        self.age_input.grid(row=5, column=2,columnspan=2)


        city_label = Label(self.programmingMenuFrame, text="City:-", font=('', 18)).grid(row=6, column=1,sticky=W)
        self.city_input = Entry(self.programmingMenuFrame,width = 50)
        self.city_input.grid(row=6, column=2,columnspan=2)


        registration_button = Button(self.programmingMenuFrame, text="Register", font=('', 13),width=25,command = lambda : self.fetch_register_data()).grid(row=7, column=3)


        self.login_introduction_label = Label(self.programmingMenuFrame, text="""Already a register user??
        To login using email address and password click the \"login\" button. """,font=("helvetica", 14)).grid(row=8, column=0, columnspan=4, rowspan=2)

        login_button = Button(self.programmingMenuFrame, text="Login", font=("", 13),width=25,command = lambda : self.program_menu_from_register()).grid(row=10, column=3)




    def program_menu_from_register(self):
        self.root_register.destroy()
        self.program_menu()
    def fetch_register_data(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()
        gender = self.gender_input.get()
        age = self.age_input.get()
        city = self.city_input.get()

        self.email_check(email)
        if self.email_c == 'yes':
            answer = tkinter.messagebox.askquestion('Repeted Email Address','This Email address is aldeady registered.click \'yes\' to try with another email address.')
            self.root_register.destroy()
            if answer == 'yes':
                self.register()
            else:
                self.program_menu()
        else:
            self.age_check(age)
            if self.age_c == 'yes':
                self.mycursor.execute("""INSERT INTO  `users` (`user_id`,`name`,`email`,`password`,`gender`,`age`,`city`)
                    VALUES(NULL, '{}','{}','{}','{}','{}','{}')""".format(name, email, password, gender, age, city))

                self.conn.commit()
                tkinter.messagebox.showinfo('Registration Report','Registration Sucessfull')
                self.root_register.destroy()
                self.program_menu()
            else:
                answer = tkinter.messagebox.askquestion('Not eligeble',
                                                        'Your AGE is too SMALL to use this application.to enter correct age and register press \'yes\' or to exit press \'no\'')
                self.root_register.destroy()
                if answer == 'yes':
                    self.register()
    def email_check(self,email):                                                #---check email is repeted or not--#
            self.mycursor.execute(""" SELECT * FROM `users` WHERE `email` LIKE '{}' """.format(email))
            email_detector=self.mycursor.fetchall()
            self.email_c='no'
            for i in email_detector:
                self.email_c='yes'
    def age_check(self,age):
        self.age_c = 'yes'
        if int(age) <= 16:
            self.age_c  = 'no'

    def user_menu(self):
        self.root_user_menu = Tk()
        self.root_user_menu.title('DATING APPum')
        self.root_user_menu.minsize(500, 500)
        self.heading = Label(self.root_user_menu, text=('TINDER'), bg='red', width=15, height=0,
                             font=("Times", 50,"bold")).grid(row=0, column=1, columnspan=3)
        self.b = Label(self.root_user_menu, text=(''), bg='pink', width=10, height=5).grid(row=0, column=0)
        self.b = Label(self.root_user_menu, text=(''), bg='pink', width=10, height=5).grid(row=0, column=4)
        self.exit = Button(self.root_user_menu, text="EXIT", fg='red', height=2,command=lambda: self.root_user_menu.destroy()).grid(row=0, column=4)
        view_user_button = Button(self.root_user_menu, text='View users', height = 1,width=30,
                                  font = ('',18,'bold'),command = lambda : self.user_menu_to_view_users()).grid(row=1, column=0,columnspan = 2)
        view_proposal_button = Button(self.root_user_menu, text='My proposals', height=1, width=30,
                                  font=('', 18, 'bold'),command = lambda : self.user_menu_to_view_proposals()).grid(row=2, column=0, columnspan=2)
        view_request_button = Button(self.root_user_menu, text='My requests', height=1, width=30,
                                  font=('', 18, 'bold'),command = lambda : self.user_menu_to_view_request()).grid(row=3, column=0, columnspan=2)
        view_matches_button = Button(self.root_user_menu, text='Matches', height=1, width=30,
                                  font=('', 18, 'bold'),command = lambda : self.user_menu_to_view_matches()).grid(row=4, column=0, columnspan=2)
        my_profile_button = Button(self.root_user_menu, text='My profile', height=1, width=20,
                                  font=('', 15, 'bold'),command = lambda : self.user_menu_to_my_profile()).grid(row=1, column=3, columnspan=2)
        log_out_button = Button(self.root_user_menu, text='Log Out', height=1, width=20,
                                  font=('', 15, 'bold'),command = lambda : self.logOut()).grid(row=2, column=3, columnspan=2)
        self.root_user_menu.mainloop()
    def user_menu_to_view_users(self):
        self.root_user_menu.destroy()
        self.view_users()
    def user_menu_to_view_proposals(self):
        self.root_user_menu.destroy()
        self.view_proposals()
    def user_menu_to_view_request(self):
        self.root_user_menu.destroy()
        self.view_request()
    def user_menu_to_view_matches(self):
        self.root_user_menu.destroy()
        self.view_matches()
    def user_menu_to_my_profile(self):
        self.root_user_menu.destroy()
        self.my_profile()
    def user_menu_to_program_menu(self):
        self.root_user_menu.destroy()
        self.program_menu()

    def view_users(self):
        self.root_view_users = Tk()
        self.root_view_users.title('DATING APP')
        self.root_view_users.minsize(500, 500)
        self.view_users_frame = Frame(self.root_view_users, bd=3).grid()
        self.heading = Label(self.view_users_frame, text=('TINDER'), bg='red', width=15, height=0,
                             font=("Times", 50, "bold")).grid(row=0, column=1, columnspan=3)
        self.b = Label(self.view_users_frame, text=(''), bg='pink', width=10, height=5).grid(row=0, column=0)
        self.b = Label(self.view_users_frame, text=(''), bg='pink', width=10, height=5).grid(row=0, column=4)
        self.exit = Button(self.view_users_frame, text="EXIT", fg='red', height=2,
                           command=lambda: self.root_view_users.destroy()).grid(row=0, column=4)
        self.mycursor.execute(""" SELECT `user_id`,`name`, `gender`, `age`, `city` FROM `users` WHERE `user_id` NOT LIKE '{}' """.format(self.user_id))
        self.all_users = self.mycursor.fetchall()
        self.number_of_users= 0
        for i in self.all_users:
            self.number_of_users = self.number_of_users + 1
        self.display_users()
    def display_users(self):
        Label(self.view_users_frame,text='Name:-',font=('',15)).grid(row=2,column=1,sticky=W)
        Label(self.view_users_frame,text='Gender:-',font=('',15)).grid(row=5,column=1,sticky=W)
        Label(self.view_users_frame,text='Age:-',font=('',15)).grid(row=6,column=1,sticky=W)
        Label(self.view_users_frame,text='City:-',font=('',15)).grid(row=7,column=1,sticky=W)
        Label(self.view_users_frame,text=self.all_users[self.a1][1],font=('',15,'bold')).grid(row=2,column=2,sticky=W)
        Label(self.view_users_frame,text=self.all_users[self.a1][2],font=('',15,'bold')).grid(row=5,column=2,sticky=W)
        Label(self.view_users_frame,text=self.all_users[self.a1][3],font=('',15,'bold')).grid(row=6,column=2,sticky=W)
        Label(self.view_users_frame,text=self.all_users[self.a1][4],font=('',15,'bold')).grid(row=7,column=2,sticky=W)
        Button(self.view_users_frame,text='Next',font=('',18),width=9,command=lambda:self.next()).grid(row=8,column=3,sticky=E)
        Button(self.view_users_frame,text='Previous',font=('',18),command =lambda :self.previous()).grid(row=8,column=0,columnspan=2)
        Button(self.view_users_frame,text='propose',bg='pink',font=('',18),command =lambda :self.propose(self.user_id,self.all_users[self.a1][0])).grid(row=8,column=2,sticky=W)
        Button(self.view_users_frame,text='Go back',font=('',18),command =lambda :self.view_users_to_user_menu()).grid(row=8,column=2,columnspan=2)
    def next(self):
        if self.a1 == (self.number_of_users -1):
            tkinter.messagebox.showinfo('error','this is the last user!')
            self.root_view_users.destroy()
            self.view_users()
        else:
            self.a1 = self.a1 + 1
            self.root_view_users.destroy()
            self.view_users()
    def previous(self):
        if self.a1 == 0:
            tkinter.messagebox.showinfo('error','This is the first user')
            self.root_view_users.destroy()
            self.view_users()
        else:
            self.a1 = self.a1 - 1
            self.root_view_users.destroy()
            self.view_users()
    def propose(self,romeo_id,juliet_id):
        self.check_proposal(romeo_id,juliet_id)
        if self.counterx != 0:
            tkinter.messagebox.showinfo('proposal report','You have already proposed that person')
        else:
            self.mycursor.execute(
                """INSERT INTO `proposal` (`proposal_id`, `romeo_id`,`juliet_id`) VALUES (NULL,'{}','{}') """.format(
                    romeo_id, juliet_id))

            self.conn.commit()
            tkinter.messagebox.showinfo('proposal report','Your proposal is send sucessfully')
    def check_proposal(self,romeo_id,juliet_id):
        self.mycursor.execute("""SELECT * FROM `proposal` WHERE `juliet_id` LIKE '{}' AND `romeo_id` LIKE '{}' """.format(juliet_id,romeo_id))
        self.counterx=0
        result=self.mycursor.fetchall()
        for i in result:
            self.counterx+=1
    def view_users_to_user_menu(self):
        self.root_view_users.destroy()
        self.user_menu()

    def view_proposals(self):
        self.root_view_proposals = Tk()
        self.root_view_proposals.title('DATING APPvp')
        self.root_view_proposals.minsize(500, 500)
        self.view_proposals_frame = Frame(self.root_view_proposals, bd=3).grid()
        self.heading = Label(self.view_proposals_frame, text=('TINDER'), bg='red', width=15, height=0,font=("Times", 50, "bold")).grid(row=0, column=1, columnspan=3)
        self.b = Label(self.view_proposals_frame, text=(''), bg='pink', width=10, height=5).grid(row=0, column=0)
        self.b = Label(self.view_proposals_frame, text=(''), bg='pink', width=10, height=5).grid(row=0, column=4)
        self.exit = Button(self.view_proposals_frame, text="EXIT", fg='red', height=2,command=lambda: self.root_view_proposals.destroy()).grid(row=0, column=4)

        self.mycursor.execute(
            """SELECT * FROM `proposal` p JOIN `users` u ON u.`user_id`=p. `juliet_id` WHERE p.`romeo_id` LIKE '{}'""".format(
                self.user_id))
        self.proposed_user_list = self.mycursor.fetchall()
        self.number_of_proposal = 0
        for i in self.proposed_user_list:
            self.number_of_proposal = self.number_of_proposal +  1
        if self.number_of_proposal == 0:
            Label(self.view_proposals_frame,text='You have not proposed anyone yet!',font=('',20,'bold')).grid(row=2,column=1,columnspan =3)
            Button(self.view_proposals_frame, text='Go back', font=('', 18),
                   command=lambda: self.view_proposal_to_user_menu()).grid(row=3, column=2, columnspan=2)
        elif self.number_of_proposal != 0:
            self.display_proposals()
    def display_proposals(self):
        self.proposal_entry_number = self.proposed_user_list[self.a2][0]
        Label(self.view_proposals_frame,text='Name:-',font=('',15)).grid(row=2,column=1,sticky=W)
        Label(self.view_proposals_frame,text='Gender:-',font=('',15)).grid(row=5,column=1,sticky=W)
        Label(self.view_proposals_frame,text='Age:-',font=('',15)).grid(row=6,column=1,sticky=W)
        Label(self.view_proposals_frame,text='City:-',font=('',15)).grid(row=7,column=1,sticky=W)
        Label(self.view_proposals_frame,text=self.proposed_user_list[self.a2][4],font=('',15,'bold')).grid(row=2,column=2,sticky=W)
        Label(self.view_proposals_frame,text=self.proposed_user_list[self.a2][7],font=('',15,'bold')).grid(row=5,column=2,sticky=W)
        Label(self.view_proposals_frame,text=self.proposed_user_list[self.a2][8],font=('',15,'bold')).grid(row=6,column=2,sticky=W)
        Label(self.view_proposals_frame,text=self.proposed_user_list[self.a2][9],font=('',15,'bold')).grid(row=7,column=2,sticky=W)
        Button(self.view_proposals_frame,text='Next',font=('',18),width=9,command=lambda: self.next_proposal()).grid(row=8,column=3,sticky=E)
        Button(self.view_proposals_frame,text='Previous',font=('',18),command =lambda :self.previous_proposal()).grid(row=8,column=0,columnspan=2)
        Button(self.view_proposals_frame,text='Go back',font=('',18),command =lambda :self.view_proposal_to_user_menu()).grid(row=8,column=2,columnspan=2)
        Button(self.view_proposals_frame,text='Undo propose',bg='red',font=('',18),command =lambda :self.undo_proposal(self.proposal_entry_number)).grid(row=8,column=2,sticky=W)
    def next_proposal(self):
        if self.a2 == (self.number_of_proposal -1):
            tkinter.messagebox.showinfo('error', 'This is the last user!')
            self.root_view_proposals.destroy()
            self.view_proposals()
        else:
            self.a2 = self.a2 + 1
            self.root_view_proposals.destroy()
            self.view_proposals()
    def previous_proposal(self):
        if self.a2 == 0:
            tkinter.messagebox.showinfo('error', 'This is the first user!')
            self.root_view_proposals.destroy()
            self.view_proposals()
        else:
            self.a2 = self.a2 - 1
            self.root_view_proposals.destroy()
            self.view_proposals()
    def view_proposal_to_user_menu(self):
        self.root_view_proposals.destroy()
        self.user_menu()
    def undo_proposal(self,proposal_entry):
        self.mycursor.execute("""DELETE FROM `proposal` WHERE `proposal_id` LIKE '{}'""".format(self.proposal_entry_number))
        self.conn.commit()
        tkinter.messagebox.showinfo('poposal result','Proposal to this user is remved sucessfully')
        self.root_view_proposals.destroy()
        self.view_proposals()


    def view_request(self):
        self.root_view_request = Tk()
        self.root_view_request.title('DATING APP')
        self.root_view_request.minsize(500, 500)
        self.view_request_frame = Frame(self.root_view_request, bd=3).grid()
        self.heading = Label(self.view_request_frame, text=('TINDER'), bg='red', width=15, height=0,
                             font=("Times", 50, "bold")).grid(row=0, column=1, columnspan=3)
        self.b = Label(self.view_request_frame, text=(''), bg='pink', width=10, height=5).grid(row=0, column=0)
        self.b = Label(self.view_request_frame, text=(''), bg='pink', width=10, height=5).grid(row=0, column=4)
        self.exit = Button(self.view_request_frame, text="EXIT", fg='red', height=2,
                           command=lambda: self.root_view_request.destroy()).grid(row=0, column=4)
        self.mycursor.execute(
            """SELECT * FROM `proposal` p JOIN `users` u ON u.`user_id`=p. `romeo_id` WHERE p.`juliet_id` LIKE '{}'""".format(
                self.user_id))

        self.requested_user_list = self.mycursor.fetchall()
        self.number_of_request = 0
        for  i in self.requested_user_list:
            self.number_of_request = self.number_of_request + 1
        if self.number_of_request == 0:
            Label(self.view_request_frame,text='You have not got any request from any users',font=('',20,'bold')).grid(row=2,column=1,columnspan =3)
            Button(self.view_request_frame, text='Go back', font=('', 18),
                   command=lambda: self.view_request_to_user_menu()).grid(row=3, column=2, columnspan=2)
        else:
            self.display_request()
    def display_request(self):
        print(self.requested_user_list)
        Label(self.view_request_frame,text='Name:-',font=('',15)).grid(row=2,column=1,sticky=W)
        Label(self.view_request_frame,text='Gender:-',font=('',15)).grid(row=5,column=1,sticky=W)
        Label(self.view_request_frame,text='Age:-',font=('',15)).grid(row=6,column=1,sticky=W)
        Label(self.view_request_frame,text='City:-',font=('',15)).grid(row=7,column=1,sticky=W)
        Label(self.view_request_frame,text=self.requested_user_list[self.a3][4],font=('',15,'bold')).grid(row=2,column=2,sticky=W)
        Label(self.view_request_frame,text=self.requested_user_list[self.a3][7],font=('',15,'bold')).grid(row=5,column=2,sticky=W)
        Label(self.view_request_frame,text=self.requested_user_list[self.a3][8],font=('',15,'bold')).grid(row=6,column=2,sticky=W)
        Label(self.view_request_frame,text=self.requested_user_list[self.a3][9],font=('',15,'bold')).grid(row=7,column=2,sticky=W)
        Button(self.view_request_frame,text='Next',font=('',18),width=9,command=lambda: self.next_request()).grid(row=8,column=3,sticky=E)
        Button(self.view_request_frame,text='Previous',font=('',18),command =lambda :self.previous_request()).grid(row=8,column=0,columnspan=2)
        Button(self.view_request_frame,text='Go back',font=('',18),command =lambda :self.view_request_to_user_menu()).grid(row=8,column=2,columnspan=2)
    def view_request_to_user_menu(self):
        self.root_view_request.destroy()
        self.user_menu()
    def next_request(self):
        if self.a3 == (self.number_of_request -1):
            tkinter.messagebox.showinfo('error', 'This is the last user!')
            self.root_view_request.destroy()
            self.view_request()
        else:
            self.a3 = self.a3 + 1
            self.root_view_request.destroy()
            self.view_request()
    def previous_request(self):
        if self.a3 == 0:
            tkinter.messagebox.showinfo('error', 'This is the first user!')
            self.root_view_request.destroy()
            self.view_request()
        else:
            self.a3 = self.a3 - 1
            self.root_view_request.destroy()
            self.view_request()


    def view_matches(self):
        self.root_view_matches = Tk()
        self.root_view_matches.title('DATING APP')
        self.root_view_matches.minsize(500, 500)
        self.view_matches_frame = Frame(self.root_view_matches, bd=3).grid()
        self.heading = Label(self.view_matches_frame, text=('TINDER'), bg='red', width=15, height=0,
                             font=("Times", 50, "bold")).grid(row=0, column=1, columnspan=3)
        self.b = Label(self.view_matches_frame, text=(''), bg='pink', width=10, height=5).grid(row=0, column=0)
        self.b = Label(self.view_matches_frame, text=(''), bg='pink', width=10, height=5).grid(row=0, column=4)
        self.exit = Button(self.view_matches_frame, text="EXIT", fg='red', height=2,
                           command=lambda: self.root_view_matches.destroy()).grid(row=0, column=4)
        self.mycursor.execute(
            """SELECT * FROM `proposal` p 
            JOIN`users` u ON u.`user_id`=p.`juliet_id`
             WHERE `juliet_id` IN
             (SELECT `romeo_id` FROM `proposal` WHERE `juliet_id` LIKE'{}')
             AND `romeo_id` LIKE '{}'""".format(self.user_id, self.user_id))

        self.matches_user_list = self.mycursor.fetchall()
        self.number_of_matches = 0
        for  i in self.matches_user_list:
            self.number_of_matches = self.number_of_matches + 1
        if self.number_of_matches == 0:
            Label(self.view_matches_frame,text='Be cum!.\n Right now you dont have any matches.\nBut don\'t worry,u will get soon',font=('',20,'bold')).grid(row=2,column=1,columnspan =3)
            Button(self.view_matches_frame, text='Go back', font=('', 18),
                   command=lambda: self.view_matches_to_user_menu()).grid(row=3, column=2, columnspan=2)
        else:
            self.display_matches()
    def display_matches(self):
        Label(self.view_matches_frame, text='Name:-', font=('', 15)).grid(row=2, column=1, sticky=W)
        Label(self.view_matches_frame, text='Email:-', font=('', 15)).grid(row=3, column=1, sticky=W)
        Label(self.view_matches_frame, text='Gender:-', font=('', 15)).grid(row=5, column=1, sticky=W)
        Label(self.view_matches_frame, text='Age:-', font=('', 15)).grid(row=6, column=1, sticky=W)
        Label(self.view_matches_frame, text='City:-', font=('', 15)).grid(row=7, column=1, sticky=W)
        Label(self.view_matches_frame, text=self.matches_user_list[self.a4][4], font=('', 15, 'bold')).grid(row=2,
                                                                                                              column=2,
                                                                                                              sticky=W)
        Label(self.view_matches_frame, text=self.matches_user_list[self.a4][5], font=('', 15, 'bold')).grid(row=3,
                                                                                                              column=2,
                                                                                                              sticky=W)
        Label(self.view_matches_frame, text=self.matches_user_list[self.a4][7], font=('', 15, 'bold')).grid(row=5,
                                                                                                              column=2,
                                                                                                              sticky=W)
        Label(self.view_matches_frame, text=self.matches_user_list[self.a4][8], font=('', 15, 'bold')).grid(row=6,
                                                                                                              column=2,
                                                                                                              sticky=W)
        Label(self.view_matches_frame, text=self.matches_user_list[self.a4][9], font=('', 15, 'bold')).grid(row=7,
                                                                                                              column=2,
                                                                                                              sticky=W)
        Button(self.view_matches_frame, text='Next', font=('', 18), width=9, command=lambda: self.next_matche()).grid(
            row=8, column=3, sticky=E)
        Button(self.view_matches_frame, text='Previous', font=('', 18), command=lambda: self.previous_match()).grid(
            row=8, column=0, columnspan=2)
        Button(self.view_matches_frame, text='Go back', font=('', 18),
               command=lambda: self.view_matches_to_user_menu()).grid(row=8, column=2, columnspan=2)
    def next_matche(self):
        if self.a4 == (self.number_of_matches - 1):
            tkinter.messagebox.showinfo('error', 'this is the last user!')
            self.root_view_matches.destroy()
            self.view_matches()
        else:
            self.a4 = self.a4 + 1
            self.root_view_matches.destroy()
            self.view_matches()
    def previous_match(self):
        if self.a4 == 0:
            tkinter.messagebox.showinfo('error', 'this is the first user!')
            self.root_view_matches.destroy()
            self.view_matches()
        else:
            self.a4 = self.a4 - 1
            self.root_view_matches.destroy()
            self.view_matches()
    def view_matches_to_user_menu(self):
        self.root_view_matches.destroy()
        self.user_menu()

    def my_profile(self):
        self.mycursor.execute("""SELECT * FROM `users` WHERE `user_id` LIKE '{}' """.format(self.user_id))
        me_one = self.mycursor.fetchall()
        for i in me_one:
            self.name = i[1]
            self.Email = i[2]
            self.Password = i[3]
            self.Gender = i[4]
            self.age = i[5]
            self.city = i[6]
        self.root_my_profile = Tk()
        self.root_my_profile.title('DATING APP')
        self.root_my_profile.minsize(500, 500)
        self.MyProfileFrame = Frame(self.root_my_profile,bd=3).grid()
        self.heading = Label(self.MyProfileFrame, text=('TINDER'), bg='red', width=15, height=0,
                             font=("Times", 50,"bold")).grid(row=0, column=1, columnspan=3)
        self.b = Label(self.MyProfileFrame, text=(''), bg='pink', width=10, height=5).grid(row=0, column=0)
        self.b = Label(self.MyProfileFrame, text=(''), bg='pink', width=10, height=5).grid(row=0, column=4)
        self.exit = Button(self.MyProfileFrame, text="EXIT", fg='red', height=2,command=lambda: self.root_my_profile.destroy()).grid(row=0, column=4)
        edit_name_button = Button(self.MyProfileFrame, text='Edit Name', height=1, width=20,
                                  font=('', 15),command = lambda : self.edit_name()).grid(row=2, column=3, columnspan=2)
        edit_password_button = Button(self.MyProfileFrame, text='Edit Password', height=1, width=20,
                                  font=('', 15),command = lambda : self.edit_password()).grid(row=4, column=3, columnspan=2)
        edit_gender_button = Button(self.MyProfileFrame, text='Edit Gender', height=1, width=20,
                                  font=('', 15),command = lambda : self.edit_gender()).grid(row=5, column=3, columnspan=2)
        edit_age_button = Button(self.MyProfileFrame, text='Edit age', height=1, width=20,
                                  font=('', 15),command = lambda : self.edit_age()).grid(row=6, column=3, columnspan=2)
        edit_city_button = Button(self.MyProfileFrame, text='Edit city', height=1, width=20,
                                  font=('', 15),command = lambda : self.edit_city()).grid(row=7, column=3, columnspan=2)
        save_button = Button(self.MyProfileFrame, text='SAVE', height=1, width=20,
                                  font=('', 18),command = lambda : self.my_profile_to_user_menu()).grid(row=8, column=3, columnspan=2)
        deactivate_button = Button(self.MyProfileFrame, text='DEACTIVATE', height=1, width=20,bg='red',
                                  font=('', 18),command = lambda : self.deactivate()).grid(row=9, column=3, columnspan=2)
        Label(self.MyProfileFrame,text='Name:-',font=('',15)).grid(row=2,column=1,sticky=W)
        Label(self.MyProfileFrame,text='Email Address:-',font=('',15)).grid(row=3,column=1,sticky=W)
        Label(self.MyProfileFrame,text='Password:-',font=('',15)).grid(row=4,column=1,sticky=W)
        Label(self.MyProfileFrame,text='Gender:-',font=('',15)).grid(row=5,column=1,sticky=W)
        Label(self.MyProfileFrame,text='Age:-',font=('',15)).grid(row=6,column=1,sticky=W)
        Label(self.MyProfileFrame,text='City:-',font=('',15)).grid(row=7,column=1,sticky=W)
        Label(self.MyProfileFrame,text=self.name,font=('',15,'bold')).grid(row=2,column=2,sticky=W)
        Label(self.MyProfileFrame,text=self.Email,font=('',15,'bold')).grid(row=3,column=2,sticky=W)
        Label(self.MyProfileFrame,text=self.Password,font=('',15,'bold')).grid(row=4,column=2,sticky=W)
        Label(self.MyProfileFrame,text=self.Gender,font=('',15,'bold')).grid(row=5,column=2,sticky=W)
        Label(self.MyProfileFrame,text=self.age,font=('',15,'bold')).grid(row=6,column=2,sticky=W)
        Label(self.MyProfileFrame,text=self.city,font=('',15,'bold')).grid(row=7,column=2,sticky=W)
    def edit_name(self):
        self.root_edit_name =Tk()
        self.root_edit_name.title('Edit Name')
        Label(self.root_edit_name,text='write your new Name',font=('',15)).grid(row=0,column=0)
        self.new_name = Entry(self.root_edit_name)
        self.new_name.grid(row=0,column=1)
        Button(self.root_edit_name,text='save',font=('18'),command=lambda :self.save_new_name()).grid(row=1,column=1)
    def save_new_name(self):
        self.new_name1 = self.new_name.get()
        print(self.new_name1)
        user_id = int(self.user_id)
        self.mycursor.execute("""UPDATE `users` SET `name`= '{}' WHERE `user_id` LIKE '{}'""".format(self.new_name1,user_id))
        self.conn.commit()
        self.root_edit_name.destroy()
        self.root_my_profile.destroy()
        self.my_profile()
    def edit_password(self):
        self.root_edit_password =Tk()
        self.root_edit_password.title('Edit Name')
        Label(self.root_edit_password,text='write your new Password',font=('',15)).grid(row=0,column=0)
        self.new_password = Entry(self.root_edit_password)
        self.new_password.grid(row=0,column=1)
        Button(self.root_edit_password,text='save',font=('18'),command=lambda :self.save_new_password()).grid(row=1,column=1)
    def save_new_password(self):
        self.new_password1 = self.new_password.get()
        self.mycursor.execute("""UPDATE `users` SET `password`= '{}' WHERE `user_id` LIKE '{}'""".format(self.new_password1,self.user_id))
        self.conn.commit()
        self.root_edit_password.destroy()
        self.root_my_profile.destroy()
        self.my_profile()
    def edit_gender(self):
        self.root_edit_gender = Tk()
        self.root_edit_gender.title('Edit Name')
        Label(self.root_edit_gender, text='write your Gender', font=('', 15)).grid(row=0, column=0)
        self.new_gender = Entry(self.root_edit_gender)
        self.new_gender.grid(row=0, column=1)
        Button(self.root_edit_gender, text='save', font=('',18), command=lambda: self.save_new_gender()).grid(row=1,
                                                                                                                 column=1)
    def save_new_gender(self):
        self.new_gender1 = self.new_gender.get()
        self.mycursor.execute(
            """UPDATE `users` SET `gender`= '{}' WHERE `user_id` LIKE '{}'""".format(self.new_gender1,
                                                                                       self.user_id))
        self.conn.commit()
        self.root_edit_gender.destroy()
        self.root_my_profile.destroy()
        self.my_profile()
    def edit_age(self):
        self.root_edit_age = Tk()
        self.root_edit_age.title('Edit Name')
        Label(self.root_edit_age, text='write your currect age', font=('', 15)).grid(row=0, column=0)
        self.new_age = Entry(self.root_edit_age)
        self.new_age.grid(row=0, column=1)
        Button(self.root_edit_age, text='save', font=('',18), command=lambda: self.save_new_age()).grid(row=1,
                                                                                                             column=1)
    def save_new_age(self):
        self.new_age1 = self.new_age.get()
        if int(self.new_age1) <= 18:
            tkinter.messagebox.showinfo('age error','Your age should be greater than 18')
            self.root_edit_age.destroy()
            self.root_my_profile.destroy()
            self.my_profile()
        else:
            self.mycursor.execute("""UPDATE `users` SET `age`= '{}' WHERE `user_id` LIKE '{}'""".format(self.new_age1,self.user_id))
            self.conn.commit()
            self.root_edit_age.destroy()
            self.root_my_profile.destroy()
            self.my_profile()
    def edit_city(self):
        self.root_edit_city = Tk()
        self.root_edit_city.title('Edit Name')
        Label(self.root_edit_city, text='write your currect city', font=('', 15)).grid(row=0, column=0)
        self.new_city = Entry(self.root_edit_city)
        self.new_city.grid(row=0, column=1)
        Button(self.root_edit_city, text='save', font=('', 18), command=lambda: self.save_new_city()).grid(row=1,
                                                                                                         column=1)
    def save_new_city(self):
        self.new_city1 = self.new_city.get()
        self.mycursor.execute(
            """UPDATE `users` SET `city`= '{}' WHERE `user_id` LIKE '{}'""".format(self.new_city1,
                                                                                  self.user_id))
        self.conn.commit()
        self.root_edit_city.destroy()
        self.root_my_profile.destroy()
        self.my_profile()
    def my_profile_to_user_menu(self):
        self.root_my_profile.destroy()
        self.user_menu()




    def logOut(self):
        self.mycursor.execute("""DELETE FROM `current_login_profile` WHERE `user_id` like '{}'""".format(self.user_id))
        self.conn.commit()
        self.user_id = 0
        tkinter.messagebox.showinfo('Logout report','you have been loged out sucessfully.')
        self.user_menu_to_program_menu()

    def deactivate(self):
        answer = tkinter.messagebox.askquestion('WARNING!','Are you sure that you want to deactivate your account.All data regarding your account will be lost')
        if answer == 'yes':
            self.mycursor.execute("""DELETE FROM `users` WHERE `user_id` LIKE '{}'""".format(self.user_id))
            self.conn.commit()
            self.mycursor.execute("""DELETE FROM `proposal` WHERE `romeo_id` LIKE '{}'""".format(self.user_id))
            self.conn.commit()
            self.mycursor.execute("""DELETE FROM `proposal` WHERE `juliet_id` LIKE '{}'""".format(self.user_id))
            self.conn.commit()
            self.mycursor.execute(
                """DELETE FROM `current_login_profile` WHERE `user_id` like '{}'""".format(self.user_id))
            self.conn.commit()
            self.user_id = 0
            tkinter.messagebox.showinfo('Logout report', 'Your account has been deactivated sucessfully! :-( :-( :-( :-( :-(')
            self.root_my_profile.destroy()
            self.program_menu()
        elif answer == 'no':
            print('no')



shakib = DatingApp()
