# รับค่าจำนวนแถวจากผู้ใช้
n = int(input())

# วนลูปตามจำนวนแถว
for i in range(n):
    # คำนวณจำนวนช่องว่างด้านหน้า
    space = abs(n // 2 - i) #space = 2

    # คำนวณจำนวน * ที่ต้องพิมพ์ในแต่ละแถว
    star = n - 2 * space # 5-2*2=1

    # แสดงผลโดยพิมพ์ช่องว่างก่อน แล้วตามด้วย *
    print(' ' * space + '*' * star)