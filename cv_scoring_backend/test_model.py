import torch
import torch.nn as nn

# Modeli tekrar oluşturuyoruz
class CVScoringModel(nn.Module):
    def __init__(self):
        super(CVScoringModel, self).__init__()
        self.fc1 = nn.Linear(10, 64)  # 10 giriş, 64 çıkış
        self.fc2 = nn.Linear(64, 32)  # 64 giriş, 32 çıkış
        self.fc3 = nn.Linear(32, 1)   # 32 giriş, 1 çıkış (skor)

    def forward(self, x):
        x = torch.relu(self.fc1(x))  # ReLU aktivasyonu
        x = torch.relu(self.fc2(x))  # ReLU aktivasyonu
        x = self.fc3(x)              # Son katman (skor)
        return x

# Modeli yüklemek için
model = CVScoringModel()  # Modeli tekrar oluşturuyoruz
model.load_state_dict(torch.load('./models/cv_scoring_model.pth'))  # Kaydedilen modeli yüklüyoruz
model.eval()  # Modeli değerlendirme moduna alıyoruz

# Test verisi (rastgele bir test verisi)
test_input = torch.tensor([[7, 5, 3, 2, 1, 5, 4, 2, 3, 1]], dtype=torch.float32)  # Test verisi
test_output = model(test_input)  # Tahmin

print(f"Test verisi için tahmin edilen skor: {test_output.item()}")
