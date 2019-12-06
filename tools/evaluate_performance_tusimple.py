import argparse
import json
import sys
sys.path.append("/content/")
import matplotlib.pyplot as plt


H_SAMPLES = [160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500,510,520,530,540,550,560,570,580,590,600,610,620,630,640,650,660,670,680,690,700,710]


def init_args():
    """

    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--predictions_path', type=str, help='The source tusimple lane test data dir')
    parser.add_argument('--labels_path', type=str, help='The model weights path')

    return parser.parse_args()


threshold = 20


def compute_accuracy(predicted_lanes, true_lanes):
    total = 0
    detected = 0
    for i in range(len(true_lanes[0])):
        for true_lane in true_lanes:
            total += 1
            for pred_lane in predicted_lanes:
                if abs(pred_lane[i] - true_lane[i]) < threshold:
                    detected += 1
                    break
    return total, detected


if __name__ == '__main__':
    """
    test code
    """
    # init args
    # args = init_args()

    test_labels = {}

    with open('../data/test_labels.json') as labels_file: # open('predictions.json') as predictions_file,
        # predictions = json.load(predictions_file)
        for line in labels_file:
            labels_obj = json.loads(line)
            test_labels[labels_obj['raw_file']] = labels_obj['lanes']

    predicted_labels = {}
    with open('../data/predictions.json') as predictions_file:
        predictions_obj = json.load(predictions_file)
        print(predictions_obj)
        for img_path, lane_labels in predictions_obj.items():
            if img_path.split('/')[-1] == '20.jpg':
                predicted_labels['/'.join(img_path.split('/')[4:])] = lane_labels

    for img, pred_lane_labels in predicted_labels.items():
        for lane in pred_lane_labels:
            plt.scatter(lane, H_SAMPLES)
        plt.show()
        for lane in test_labels[img]:
            plt.scatter(lane, H_SAMPLES)
        print(img, compute_accuracy(pred_lane_labels, test_labels[img]))
        plt.show()

