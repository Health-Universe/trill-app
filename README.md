markdown
# TRILL Protein Engineering Streamlit App

## Summary

This repository contains a Streamlit app that provides a user-friendly interface for TRILL (TRaining and Inference using the Language of Life), a sandbox for creative protein engineering and discovery. This app allows researchers to perform various operations related to protein engineering using pretrained models and user-provided input files.

## Features

- Upload protein sequences in FASTA, PDB, or CIF formats
- Run various TRILL operations, such as embedding, fine-tuning, generating, folding, and visualizing
- Customize TRILL run configurations, such as the number of GPUs, RNG seed, and model type
- Extend the app to support more command-line arguments and features

## Usage

To use this app, first install the dependencies and then run the Streamlit app using the following command:

```bash
$ streamlit run trill_app.py
```

The app should open in your default web browser, allowing you to interact with the TRILL program.

## Requirements

- Python 3.8 or later
- Streamlit
- TRILL-Proteins
- PyG-Lib and related dependencies

## Installation

1. Clone this repository:

```bash
$ git clone https://github.com/your_username/trill-streamlit-app.git
```

2. Change into the `trill-streamlit-app` directory:

```bash
$ cd trill-streamlit-app
```

3. Install the dependencies:

```bash
$ conda create -n trill_env python=3.10
$ conda activate trill_env
$ pip install streamlit
$ pip install trill-proteins
$ pip install pyg-lib torch-scatter torch-sparse torch-cluster torch-spline-conv torch-geometric -f https://data.pyg.org/whl/torch-1.13.0+cu117.html
```

4. Run the app:

```bash
$ streamlit run trill_app.py
```

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or bugfix (`git checkout -b my-feature-branch`)
3. Make changes and commit them to your branch
4. Push your changes to your forked repository (`git push origin my-feature-branch`)
5. Create a new Pull Request for your changes

## Authors

- Zachary Martinez - martinez-zacharya - zmartine@caltech.edu

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details