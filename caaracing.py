import itertools

def calculate_values(m1, m2, m3):
    def get_y(m):
        y_values = {
            0: 0.0,
            0.07208: 0.015,
            0.09676: 0.020,
            0.12145: 0.025,
            0.14641: 0.030,
            0.19551: 0.040,
            0.24488: 0.050,
            0.29426: 0.060,
            0.49175: 0.100
        }
        return y_values.get(m, 0.0)

    mtot = m1 + m2 + m3
    y1, y2, y3 = get_y(m1), get_y(m2), get_y(m3)
    
    Ycg = ((0.197 * 0.04187) + (m1 * (y1 + 0.07707)) + (m2 * (y2 + 0.07707)) + (m3 * (y3 + 0.07707))) / (mtot + 0.197)
    
    a = (((m1 + m2) * 0.09793) + (m3 * 0.06293) + (0.197 * 0.05467)) * 9.81 / ((mtot + 0.197) * Ycg)
    
    # คำนวณ M(weight)
    M_weight = (mtot + 0.197) * a / (9.81 - a)
    
    return a, Ycg, M_weight, m1, m2, m3

# รายการค่า m ที่เป็นไปได้
m_values = [0, 0.07208, 0.09676, 0.12145, 0.14641, 0.19551, 0.24488, 0.29426, 0.49175]

# สร้างทุกความเป็นไปได้ของ m1, m2, m3
combinations = list(itertools.product(m_values, repeat=3))

# คำนวณค่าต่าง ๆ สำหรับทุกความเป็นไปได้
results = [calculate_values(m1, m2, m3) for m1, m2, m3 in combinations]

# เรียงลำดับผลลัพธ์ตามค่า a จากมากไปน้อย
sorted_results = sorted(results, key=lambda x: x[0], reverse=True)

# เตรียมข้อความสำหรับแสดงผลและบันทึกไฟล์
output = []
for i, (a, Ycg, M_weight, m1, m2, m3) in enumerate(sorted_results, 1):
    line = f"{i}. a = {a:.4f}, Ycg = {Ycg:.4f}, M(weight) = {M_weight:.4f}, m1 = {m1:.5f}, m2 = {m2:.5f}, m3 = {m3:.5f}"
    print(line)
    output.append(line)

# บันทึกผลลัพธ์เป็นไฟล์ .txt
with open('aceleration_results.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(output))

print("\nผลลัพธ์ถูกบันทึกในไฟล์ 'aceleration_results.txt'")
