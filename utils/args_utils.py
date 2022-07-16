import argparse


def build_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", type=str, default="voc/2007")
    parser.add_argument("--epochs", type=int, default=160)
    parser.add_argument("--base-model", type=str, default="vgg16")
    parser.add_argument("--batch-size", type=int, default=4)
    parser.add_argument("--data-dir", type=str, default="D:/won/data")
    parser.add_argument("--img-size", nargs="+", type=int, default=[500, 500])
    parser.add_argument("--feature-map-shape", nargs="+", type=int, default=[31, 31])
    parser.add_argument(
        "--anchor-ratios", nargs="+", type=float, default=[1.0, 2.0, 1.0 / 2.0]
    )
    parser.add_argument(
        "--anchor-scales", nargs="+", type=float, default=[64, 128, 256]
    )
    parser.add_argument("--pre-nms-topn", type=int, default=6000)
    parser.add_argument("--train-nms-topn", type=int, default=1500)
    parser.add_argument("--test-nms-topn", type=int, default=300)
    parser.add_argument("--total-pos-bboxes", type=int, default=128)
    parser.add_argument("--total-neg-bboxes", type=int, default=128)
    parser.add_argument("--pooling-size", nargs="+", type=int, default=[7, 7])
    parser.add_argument(
        "--variances", nargs="+", type=float, default=[0.1, 0.1, 0.2, 0.2]
    )
    parser.add_argument("--pos-threshold", type=float, default=0.65)
    parser.add_argument("--neg-threshold", type=float, default=0.25)
    args = parser.parse_args()

    return args
