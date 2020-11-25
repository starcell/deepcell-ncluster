# Copyright 2020 Starcell Incorporation. All Rights Reserved.
# - N. Park
# ==============================================================================

from __future__ import absolute_import, division, print_function, unicode_literals
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)
import argparse
import os
# for tensorflow v2.1
import tensorflow as tf
from tensorflow.keras import layers
import numpy as np
# from experiment_metrics.api import publish # nauta의 publish api 사용
from contextlib import redirect_stdout

gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
  try:
    # Currently, memory growth needs to be the same across GPUs
    for gpu in gpus:
      tf.config.experimental.set_memory_growth(gpu, True)
    logical_gpus = tf.config.experimental.list_logical_devices('GPU')
    print(len(gpus), "Physical GPUs,", len(logical_gpus), "Logical GPUs")
  except RuntimeError as e:
    # Memory growth must be set before GPUs have been initialized
    print(e)

# Output produced by the experiment (summaries, checkpoints etc.) has to be placed in this folder.
EXPERIMENT_OUTPUT_PATH = "/mnt/output/experiment"
MODEL_VERSION = 1
# BASE_DIR = os.path.join(EXPERIMENT_OUTPUT_PATH, str(MODEL_VERSION))
# os.makedirs(BASE_DIR, exist_ok=True)

FLAGS = None

# Set of constant names related to served model.
# Look into example mnist conversion and checker scripts to see how these constants are used in TF Serving request
# creation.
# MODEL_NAME = "mnist" - Model name is not specified at this stage. It is given in "predict" commands as an argument.
MODEL_SIGNATURE_NAME = "predict_images"
MODEL_INPUT_NAME = "images"
MODEL_OUTPUT_NAME = "scores"


# 간단한 Sequential 모델을 정의합니다
def create_model(input_shape, num_labels):
  dropout = 0.5
  model = tf.keras.models.Sequential([
    layers.Conv2D(filters=32, kernel_size=5, activation='relu', padding='same', input_shape=input_shape),
    layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding='same'),
    layers.Conv2D(filters=64, kernel_size=5, activation='relu', padding='same', ),
    layers.MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding='same'),
    layers.Flatten(),
    layers.Dropout(dropout),
    layers.Dense(num_labels),
    layers.Activation('softmax')
  ])

  model.compile(
    loss='categorical_crossentropy',
    optimizer='adam',
    metrics=['accuracy']
  )

  return model


# callbacks
def callbacks(path):
  model_chk_path = os.path.join(path, 'checkpoints', 'model.ckpt')
  # os.makedirs(model_chk_base, exist_ok=True)
  # model_chk_path = os.path.join(model_chk_base, '{epoch:04d}-{val_loss:.4f}.hdf5')
  tb_path = os.path.join(path, 'tensorboard')
  # os.makedirs(tb_path, exist_ok=True)
  checkpoint = tf.keras.callbacks.ModelCheckpoint(
      model_chk_path,
      monitor='val_loss',
      verbose=1,
      save_best_only=True,
      mode='auto',
      save_weights_only=True
  )

  tensorboard = tf.keras.callbacks.TensorBoard(
      log_dir=tb_path,
      histogram_freq=0,
      write_graph=True,
      write_images=True,
  )

  callback_list = [checkpoint, tensorboard]
  return callback_list


def main(_):
  # base_dir = BASE_DIR
  (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
  num_labels = len(np.unique(y_train))

  y1_train = tf.keras.utils.to_categorical(y_train)
  y1_test = tf.keras.utils.to_categorical(y_test)

  image_size = x_train.shape[1]

  x_train = np.reshape(x_train, [-1, image_size, image_size, 1])
  x_test = np.reshape(x_test, [-1, image_size, image_size, 1])

  x_train = x_train.astype('float32') / 255
  x_test = x_test.astype('float32') / 255

  input_shape = (image_size, image_size, 1)
  batch_size = 64
  epoch_num = 10

  # export_dir FLAG
  if FLAGS.export_dir is not "":
    base_dir = os.path.join(EXPERIMENT_OUTPUT_PATH, FLAGS.export_dir)
    os.makedirs(base_dir, exist_ok=True)
  else:
    base_dir = EXPERIMENT_OUTPUT_PATH

  train_model_dir = os.path.join(base_dir, 'model')
  os.makedirs(train_model_dir, exist_ok=True)

  model = create_model(input_shape, num_labels)
  model.save(train_model_dir)

  model_txt = os.path.join(EXPERIMENT_OUTPUT_PATH, 'modelsummary.txt')
  with open(model_txt, 'w') as f:
    with redirect_stdout(f):
      model.summary()

  # chk_dir = os.path.join(base_dir, 'chk')
  callback_params = callbacks(EXPERIMENT_OUTPUT_PATH)

  model.fit(x_train, y1_train, epochs=epoch_num, batch_size=batch_size, validation_split=0.1, callbacks=callback_params)

  loss, acc = model.evaluate(x_test, y1_test, batch_size=batch_size)
  print("\nTest accuracy: %.1f%%" % (100.0 * acc))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", type=str,
                        default="/tmp/mnist-data",
                        help="Directory which contains dataset")
    parser.add_argument("--export_dir", type=str,
                        default="",
                        help="Export directory for model")
    parser.add_argument("--steps", type=int,
                        default=500,
                        help="Number of steps to run training")
    FLAGS, _ = parser.parse_known_args()
    main(_)
