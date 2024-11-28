# YOLO Data Collector

A Python application for collecting and processing data, likely for use with YOLO (You Only Look Once) machine learning models.

## Requirements

- Python 3.10+
- OpenCV Python (opencv-python) >= 4.5.0
- NumPy >= 1.19.0

## Installation

1. Clone the repository:
```bash
git clone https://github.com/[username]/yolo-data-collector.git
cd yolo-data-collector
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the data collection application:
```bash
python data_collection_app.py
```

Or use the compiled executable from the `dist` folder if available.

## Building the Executable

The project includes PyInstaller configuration for building a standalone executable:

```bash
pyinstaller --noconfirm --onefile -w data_collection_app.py
```

## Running the Executable
```bash
dist\data_collection_app.exe
```

The compiled executable will be created in the `dist` directory.

## Project Structure

```
├── data_collection_app.py    # Main application file
├── requirements.txt          # Python dependencies
├── build/                    # Build artifacts
├── dist/                     # Compiled executables
└── collected_data/          # Data collection output directory
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

[Add your license information here]

