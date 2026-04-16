import matplotlib.pyplot as plt

train_losses = []
val_accuracies = []

# Inside your training loop, after each epoch
train_losses.append(epoch_loss)
val_accuracies.append(epoch_accuracy)

# After training
plt.plot(train_losses, label='Train Loss')
plt.plot(val_accuracies, label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Loss / Accuracy')
plt.legend()
plt.title('Training Curve - TB-XNet')
plt.savefig("training_curve.png")
