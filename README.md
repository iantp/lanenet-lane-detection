# LaneNet-Lane-Detection

We modified the code in order to evaluate the performance on the tusimple dataset. In order to do so, we needed to
predict the x coordinates of the lanes at given y coordinates:

H_SAMPLES = [160, 170, 180, ..., 700, 710]

The tuSimple detection challenge requires us to return a list of x coordinates for each lane. For example if there are
two lanes, the output might be:


We modified the code in lanenet_model/lanenet_postprocess.py to compute the predicted x coordinates based on the fitted
polynomial. This was challenging since the polynomial is fitted after applying a perspective transform, so to get the
x coordinates in the source image we had to transform the fitted polynomial back using the inverse transform.

To run the algorithm to find the predicted labels, we modified the script tools/evaluate_lanenet_on_tusimple.py. We ran
the pretrained network in Google colab. The notebook can be accessed here:

https://colab.research.google.com/drive/1rGEwNYzrQWybjtZGBohw3_45QdUCXlIv

Here is the command to evaluate the model:

!python tools/evaluate_lanenet_on_tusimple.py \
  --image_dir <path to folder containing test images> \
  --weights_path <path to lanenet weights> \
  --save_dir <directory to save output>

The result of the above command is stored in 'data/predictions.json'.

We then wrote a script to evaluate the prediction accuracy. This is in the file tools/evaluate_performance_tusimple.py.

It does not have any arguments and can be run to see the performance of the algorithm on a set of test images as
compared with the ground truth provided by the tuSimple dataset.

python
tools/evaluate_performance_tusimple.py