from pathlib import Path
from pipeline.networks.pix2pix import Pix2Pix
import os
# from tensorflow_large_model_support import LMS  # linux exclusive

import settings

from pipeline.processors.preprocessors import dataset_normalizer

__author__="cstur"


if __name__ == '__main__':
    # os.environ['CUDA_VISIBLE_DEVICES'] = '-1'   # to train on cpu
    data_dir = os.path.join(settings.dataset_dir, "pix2pix", "maps", "train")
    processed_data_dir = os.path.join(Path(data_dir).parent, "train_processed")

    pix2pix = Pix2Pix(image_shape=(128, 128, 3), gpu_memory_friendly=True)

    dataset_normalizer.process(input_dir=data_dir, output_dir=processed_data_dir)
    # batch size 1 is recommended in the paper; maybe abstraction is already too hard for this structure?
    pix2pix.train(epochs=100000, batch_size=1, sample_interval=100, data_dir=processed_data_dir, generate_right=False, load_last_chkpt=False)
