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
2. Explore `scripts/` for reproducibility and testing.

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
