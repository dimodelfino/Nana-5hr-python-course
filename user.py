class User:
    def __init__(self, email, name, password, current_job_title):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, password):
        self.password = password

    def change_job_title(self, job_title):
        self.job_title = job_title

    def get_user_info(self):
        print(self.email, self.name, self.current_job_title)


new_user = User("nn@nn", "Jimi Hendrix", "pwd1", "Machine Learning Engineer")

new_user.get_user_info()
