# from Database.database import get_connection
#
#
# def main():
#     connection = get_connection()
#     print('Bun venit!')
#
# if __name__ == '__main__':
#     main()
from GUI.login_window import LoginWindow

app = LoginWindow()
app.run()