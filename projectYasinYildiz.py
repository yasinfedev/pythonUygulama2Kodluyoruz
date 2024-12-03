# Öklid mesafesi hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    # İki nokta arasındaki farkların karelerini topluyoruz
    distance_squared = (point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2
    
    # Toplamın karekökünü almak için üs kullanıyoruz (**0.5)
    distance = distance_squared ** 0.5
    
    return distance

# Noktaların tanımlanması
points = [(-7, -2), (-1, 0), (2, 6), (4, 8)]

# Mesafelerin saklanacağı liste
distances = []

# Her nokta çifti arasındaki mesafeyi hesaplama
for i in range(len(points)):
    for j in range(i + 1, len(points)):  # Aynı çifti mükerrer hesaplamamak için
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafenin bulunması
min_distance = distances[0]  # Başlangıç değeri olarak ilk mesafeyi alıyoruz
for dist in distances:
    if dist < min_distance:  # Daha küçük bir mesafe bulursak
        min_distance = dist

# Sonuçların yazdırılması
print("Tüm noktalar arası mesafeler:", distances)
print("Minimum Öklid mesafesi:", min_distance)
