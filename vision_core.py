import cv2
import sys

def initialize_tactical_view(source_index=0):
    """
    ระบบเริ่มต้นการรับสัญญาณภาพจากกล้อง USB
    source_index: ปกติจะเป็น 0 สำหรับกล้องหลัก หรือ 1, 2 สำหรับ USB ภายนอก
    """
    # เริ่มต้นการจับภาพผ่าน OpenCV
    cap = cv2.VideoCapture(source_index)

    # ปรับแต่งค่าพารามิเตอร์เพื่อประสิทธิภาพสูงสุด (Military-grade latency tuning)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    cap.set(cv2.CAP_PROP_FPS, 30)

    if not cap.isOpened():
        print("[ERROR] ไม่สามารถเข้าถึงสัญญาณกล้องได้ ตรวจสอบการเชื่อมต่อ USB")
        return

    print(f"[SYSTEM] เริ่มการส่งสัญญาณภาพ... (Source: {source_index})")

    try:
        while True:
            # อ่านเฟรมภาพจากกล้อง
            ret, frame = cap.read()
            
            if not ret:
                print("[WARNING] สัญญาณภาพขาดหาย...")
                break

            # ส่วนนี้คุณสามารถเพิ่ม AI Filter หรือระบบตรวจจับเป้าหมายได้ในอนาคต
            # แสดงผลบนหน้าจอ
            cv2.imshow('TACTICAL EYE - HUD VERSION 1.0', frame)

            # กด 'q' เพื่อปิดระบบ
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        # คืนทรัพยากรให้ระบบ
        cap.release()
        cv2.destroyAllWindows()
        print("[SYSTEM] ปิดการทำงานโหมดสอดแนม")

if __name__ == "__main__":
    # ตรวจสอบ Argument หากต้องการระบุ Port กล้องผ่าน Command Line
    index = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    initialize_tactical_view(index)
