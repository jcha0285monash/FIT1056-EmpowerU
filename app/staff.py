from app.user import User
import os

class Staff(User):

    @staticmethod
    def authenticate(uid, password):
        staff_path = "./database/staff.txt"
        if os.path.exists(staff_path):
            with open(staff_path, "r", encoding="utf8") as rf:
                lines = rf.readlines()
            for line in lines:
                sta_id, email, stored_password, name, role, status = line.strip().split(",")
                if uid == sta_id and password == stored_password and (status != "DEACTIVATED" or status == None):
                    if "sta" in sta_id.lower():
                        return Staff(sta_id, email, password, name, role, status)
                    else:
                        return None

    def __init__(self, uid, email, password, name, role, status):
        super().__init__(uid, email, password, name, status)
        self.role = role
        