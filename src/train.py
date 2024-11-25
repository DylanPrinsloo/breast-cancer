# training
from tensorflow.keras.optimizers import Adam

def plot_training_metrics(history):
    plt.figure(figsize=(14, 5))
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.title('Accuracy during Training and Validation')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.title('Loss during Training and Validation')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()

def train_model(train_data_gen, valid_data_gen, train_steps_per_epoch, valid_steps_per_epoch, input_shape):
    model = breast_cancer_model(input_shape)
    model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])
    history = model.fit(
        train_data_gen,
        steps_per_epoch=train_steps_per_epoch,
        validation_data=valid_data_gen,
        validation_steps=valid_steps_per_epoch,
        epochs=7,
        verbose=1
    )
    plot_training_metrics(history)
    model.save('breast-cancer-segmentation.h5')
    return model
