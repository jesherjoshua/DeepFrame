# DeepFrame: A Scientific Framework for Advancing Ocean Cleanup through Underwater Debris Detection, Categorization, Tracking, and Geospatial Mapping

## Abstract

DeepFrame introduces an innovative scientific framework for comprehensive underwater debris detection, categorization, tracking, and geospatial mapping. Merging deep learning and low-level computer vision techniques, the system extracts real-time insights from underwater sensor data, facilitating precise identification and categorization of debris. Advanced tracking algorithms enhance monitoring capabilities, contributing to predictive analysis. Geospatial mapping techniques project debris onto world maps, enabling strategic cleanup efforts. Experimental results on an extended dataset showcase DeepFrame's efficacy for revolutionizing ocean conservation.

## Contributions

1. **Robust Extended Dataset:** Enriched with new images and augmented samples.
2. **Advanced Tracking Algorithms:** Enhanced monitoring and predictive capabilities.
3. **Innovative Geospatial Mapping:** Precise localization for strategic cleanup.

## Directory Structure

```
- dataset/
- logs/
- models/
- plots/
- supplementary_results/
- scripts/
- README.md
- requirements.txt
```

## Usage

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Explore `dehaze/` for image pre-processing.
3. Explore `scripts/` for reproducibility and testing.

   
## Dehazing & Pre-Processing
To increase the accuracy of debris detection under turbid conditions, The input image frames are pre-processed using image enhancement techniques.

To Reuse, cd `dehaze/` & Run the script:
   ```
   python main.py
   ```
This Python script is designed for image enhancement using various techniques such as RGB equalization, histogram stretching, and HSV stretching. The script takes the input images from `dehaze/Input_Images` folder, performs these enhancement processes, and saves the results to the `dehaze/Results` folder.

Sample results:
| Original Image | Pre-Processed Image |
|:--------------:|:----------:|
| ![Original Image](https://github.com/jesherjoshua/CVPR2024/blob/master/dehaze/Input_Images/set_f122.jpg?raw=true) | ![Pre-Processed Image](https://github.com/jesherjoshua/CVPR2024/blob/master/dehaze/Results/set_f122_UCM.jpg?raw=true) |


## Robust Augmentation

The dataset augmentation includes blur, bounding box-level exposure augmentation, and hue variation, tailored for underwater images.

![Augmentation Example](https://github.com/jesherjoshua/CVPR2024/assets/87414375/144d562f-94f1-4b2f-a250-b9059b20efbf)

## Geo-Spatial Mapping

| Intensity Plot | Count Plot |
|:--------------:|:----------:|
| ![Intensity Plot](https://github.com/jesherjoshua/CVPR2024/assets/87414375/468d5461-6d5f-46ce-82e0-19928c51629e) | ![Count Plot](https://github.com/jesherjoshua/CVPR2024/assets/87414375/d20b1356-30d3-475d-87fa-0ee03e01f495) |
|Plot obtained from TADD | Plot obtained from MOT |

## Benchmark Detections

![Benchmark Detections](https://github.com/jesherjoshua/CVPR2024/assets/87414375/c0d7b01d-d9ca-4204-9c3b-7fe4e3827f6b)

## How to Cite

[Author Name]. (2024). DeepFrame: A Scientific Framework for Advancing Ocean Cleanup through Underwater Debris Detection, Categorization, Tracking, and Geospatial Mapping. CVPR 2024.

## License

[License Name] - see [LICENSE.md](LICENSE.md) for details.

## Declaration

The code will be made publicly available on Github
