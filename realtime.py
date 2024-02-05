import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# กำหนดตำแหน่งของไฟล์การกำหนดค่า
cred = credentials.Certificate('realtime-test-2acd8-firebase-adminsdk-3ndar-f6825cf50f.json')

# เริ่มต้นใช้งาน Firebase Admin ด้วย credential และ URL ของ database
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://realtime-test-2acd8-default-rtdb.asia-southeast1.firebasedatabase.app/'
})
ref = db.reference('user/user4')
ref.set({
    'old': '1234'
})

# อ่านข้อมูล
snapshot = ref.get()
print(snapshot)