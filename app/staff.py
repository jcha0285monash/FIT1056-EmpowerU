from app.user import User
import os

class Staff(User):
    @staticmethod
    def authenticate(uid, password, filepath):
        staff_path = f"{filepath}/database/staff.txt"
        if os.path.exists(staff_path):
            with open(staff_path, "r", encoding="utf8") as rf:
                lines = rf.readlines()
            for line in lines:
                sta_id, email, stored_password, name, role, status = line.strip().split(",")
                if uid == sta_id and password == stored_password and status == "ACTIVE":
                    if "sta" in sta_id.lower():
                        return Staff(sta_id, email, password, name, role, status)
                    else:
                        return None

    def __init__(self, uid, email, password, name, role, status):
        super().__init__(uid, email, password, name, status)
        self.role = role
        
    def add_user(uid, name, email, password, user_path, unique="", status="ACTIVE"):
        if os.path.exists(user_path):
            with open(user_path, "a", encoding="utf8") as f:
                new_user = f"{uid},{email},{password},{name},{unique},{status}"
                f.write(new_user + "\n")
            return new_user
        else :
            return None
    
    def edit_user(uid, email, password, name, unique, user_path, selected_line, selected_user_status):
        user_details = uid + "," + email + "," + password + "," + name + "," + unique + "," + selected_user_status
        if os.path.exists(user_path):
            with open(user_path, "r", encoding="utf8") as rf:
                data = rf.readlines()
            data[selected_line] = user_details + "\n"
            with open(user_path, "w", encoding="utf8") as wf:
                wf.writelines(data)
        return user_details