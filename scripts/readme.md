# Guidelines for Reproduciblity and Testing

## Overview

This directory contains essential scripts for the DeepFrameframework, facilitating underwater debris detection, categorization, tracking, and geospatial mapping.

### Scripts

1. **inference_intensity.py**: Generates geospatial logs using temporal averaging of debris density.

2. **inference_tracking.py**: Performs multi-object tracking and generates corresponding geospatial logs.

3. **plotter.py**: Plots geospatial maps based on logs obtained from the inference scripts.

4. **robo_gen.py**: Simulates AUVs' geospatial data used in the inference scripts.

## How to Run

### Inference Scripts

To run the inference scripts, use the following commands:

```bash
python inference_intensity.py --video_path VIDEO_PATH
python inference_tracking.py --video_path VIDEO_PATH
```

Replace `VIDEO_PATH` with the path to the video file you want to process. This will generate log files in the `logs` directory.

### Plotter Script

To run the plotter script, use the following command:

```bash
python plotter.py --mode MODE
```

Replace `MODE` with either `intensity` (for temporal averaging of debris density) or `count` (for multi-object tracking). The plotter will use log files from the `logs` directory to generate world maps.

**Note**: The `robo_gen.py` script is automatically used in the inference scripts, and there's no need to run it separately.

## Directory Structure

```plaintext
- scripts/
  - inference_intensity.py
  - inference_tracking.py
  - plotter.py
  - robo_gen.py
```

## Example Usage

1. Run the intensity inference script:
    ```bash
    python inference_intensity.py --video_path ./data/sample_video.mp4
    ```

2. Run the tracking inference script:
    ```bash
    python inference_tracking.py --video_path ./data/sample_video.mp4
    ```

3. Run the plotter script for intensity:
    ```bash
    python plotter.py --mode intensity
    ```

4. Run the plotter script for count:
    ```bash
    python plotter.py --mode count
    ```

## License

[License Name] - see [LICENSE.md](LICENSE.md) for details.

---
