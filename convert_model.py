import torch
from ultralytics.nn.tasks import DetectionModel

# Load the model checkpoint (set weights_only=False to load full model)
ckpt = torch.load("models/best.pt", map_location="cpu", weights_only=False)

# Optionally print or inspect loaded model
print("Model loaded successfully:", type(ckpt))
