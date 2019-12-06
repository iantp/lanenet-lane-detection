import argparse


def init_args():
    """

    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--predictions_dir', type=str, help='The source tusimple lane test data dir')
    parser.add_argument('--labels_dir', type=str, help='The model weights path')

    return parser.parse_args()


if __name__ == '__main__':
    """
    test code
    """
    # init args
    args = init_args()

    test_lanenet_batch(
        src_dir=args.image_dir,
        weights_path=args.weights_path,
        save_dir=args.save_dir
    )
