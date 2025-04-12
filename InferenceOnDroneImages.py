from PIL import Image
import torch
import torchvision.transforms as transforms
import torchvision.models as models

classes = ['grass', 'tree', 'dead']

# Load model
model = models.mobilenet_v2()
model.classifier[1] = nn.Linear(model.last_channel, 3)
model.load_state_dict(torch.load("vegetation_classifier.pth"))
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
])

img = Image.open("test_patch.jpg")
input_tensor = transform(img).unsqueeze(0)
output = model(input_tensor)
_, predicted = torch.max(output, 1)
print("Predicted class:", classes[predicted.item()])
