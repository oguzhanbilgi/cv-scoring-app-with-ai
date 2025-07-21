import pandas as pd
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.preprocessing import StandardScaler

# Veri setini yükleyin
df = pd.read_csv('data/cv_data.csv')

# Özellikler ve hedefler
features = df[['Eğitim Seviyesi', 'Deneyim', 'Python', 'SQL', 'Yabancı Dil', 'İletişim Yeteneği']].values
labels = df['Puan'].values

# Veriyi normalize edin
scaler = StandardScaler()
features = scaler.fit_transform(features)

# PyTorch modelini tanımlayın
class CVScoringModel(nn.Module):
    def __init__(self):
        super(CVScoringModel, self).__init__()
        self.fc1 = nn.Linear(6, 128)  # 6 giriş (özellik), 128 çıkış
        self.fc2 = nn.Linear(128, 64)  # 128 giriş, 64 çıkış
        self.fc3 = nn.Linear(64, 1)   # 64 giriş, 1 çıkış (skor)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# Modeli oluştur
model = CVScoringModel()

# Kayıp fonksiyonu ve optimizer
criterion = nn.MSELoss()  # Kayıp fonksiyonu
optimizer = optim.Adam(model.parameters(), lr=0.001)  # Optimizer (Adam)

# Eğitim döngüsü
features_tensor = torch.tensor(features, dtype=torch.float32)
labels_tensor = torch.tensor(labels, dtype=torch.float32).view(-1, 1)

for epoch in range(100):  # 100 epoch
    model.train()  # Modeli eğitim modunda çalıştır

    optimizer.zero_grad()   # Gradient sıfırlama
    outputs = model(features_tensor) # Model çıktısını al
    loss = criterion(outputs, labels_tensor)  # Kayıp hesapla
    loss.backward()  # Backpropagation
    optimizer.step()  # Optimizer adımı

    if epoch % 10 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item()}")

# Modeli kaydedin

torch.save(model.state_dict(), 'models/cv_scoring_model.pth')  # Burada models klasörünü belirtiyoruz
print("Model başarıyla kaydedildi!")

