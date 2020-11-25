# Copyright 2020 Starcell Incorporation. All Rights Reserved.
# - N. Park
# ==============================================================================

import os
import argparse
import gc
import warnings
warnings.filterwarnings('ignore')

# for tensorflow v2.1
import tensorflow as tf
from tensorflow.keras import layers

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from tensorflow.keras.callbacks import ModelCheckpoint, Callback, ReduceLROnPlateau
from tensorflow.keras.utils import get_custom_objects

import numpy as np
import pandas as pd
import datetime
# from experiment_metrics.api import publish # nauta의 publish api 사용
from contextlib import redirect_stdout

gc.collect()
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

FLAGS = None

def gelu(x):
  return 0.5 * x * (1 + tf.tanh(tf.sqrt(2 / np.pi) * (x + 0.044715 * tf.pow(x, 3))))

get_custom_objects().update({'gelu': Activation(gelu)})

# 간단한 Sequential 모델을 정의합니다
def create_model(input_size, output_size):
  model = tf.keras.models.Sequential([
    layers.Dense(units=1024, activation='gelu', input_dim=input_size),
    layers.Dense(units=900, activation='gelu'),
    layers.Dropout(0.02),
    layers.Dense(units=1024, activation='gelu'),
    layers.Dense(units=512, activation='gelu'),
    layers.Dense(units=512, activation='gelu'),
    layers.Dense(units=output_size, activation='linear')
  ])
  # 모델을 컴파일합니다.
  model.compile(loss='mae', optimizer='adam', metrics=['mae'])
  return model


# callbacks
def callbacks(path):
  model_chk_path = os.path.join(path, 'checkpoints', 'model.ckpt')
  tb_path = os.path.join(path, 'tensorboard')
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

  reduce_lr = ReduceLROnPlateau(
    monitor='loss',
    factor=0.1,
    patience=10,
    verbose=1,
    mode='auto',
    # epsilon=1e-04,
    min_delta=1e-04,
    cooldown=0,
    min_lr=0
  )

  callback_list = [checkpoint, tensorboard, reduce_lr]
  return callback_list


def main(_):
  data_dir = '/mnt/input/home/data/thin-film'
  train_data = os.path.join(data_dir, 'train-0.99.csv')
  train = pd.read_csv(train_data)

  # 독립변수와 종속변수를 분리합니다.
  train_X = train.iloc[:, 5:]
  train_Y = train.iloc[:, 1:5]

  # export_dir FLAG
  if FLAGS.export_dir is not "":
    base_dir = os.path.join(EXPERIMENT_OUTPUT_PATH, FLAGS.export_dir)
    os.makedirs(base_dir, exist_ok=True)
  else:
    base_dir = EXPERIMENT_OUTPUT_PATH

  train_model_dir = os.path.join(base_dir, 'model')
  os.makedirs(train_model_dir, exist_ok=True)

  model = create_model(226, 4)
  model.save(train_model_dir)

  model_txt = os.path.join(EXPERIMENT_OUTPUT_PATH, 'modelsummary.txt')
  with open(model_txt, 'w') as f:
    with redirect_stdout(f):
      model.summary()

  callback_params = callbacks(EXPERIMENT_OUTPUT_PATH)

  batch_size = 2048
  epoch_num = 300
  model.fit(train_X, train_Y, epochs=epoch_num, batch_size=batch_size, validation_split=0.05, callbacks=callback_params)

  # loss, acc = model.evaluate(x_test, y1_test, batch_size=batch_size)
  # print("\nTest accuracy: %.1f%%" % (100.0 * acc))


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
