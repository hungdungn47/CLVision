# 5th CLVision Workshop @ CVPR 2024 Challenge

This is the official starting repository for the Continual Learning Challenge held in the 5th CLVision Workshop @ CVPR 2024.

Please refer to the [**challenge website**](https://sites.google.com/view/clvision2024/challenge) for more details and [**FAQ**](https://sites.google.com/view/clvision2024/challenge#h.iz67c0d6y6ry)!

To participate in the challenge: [**CodaLab website**](https://codalab.lisn.upsaclay.fr/competitions/17780)

## IMPORTANT UPDATE
**[2024-April-09]** ❗Due to discrepancies in the data configuration files provided in the repository,
the pickle configurations have been updated to reflect the scenarios depicted on the challenge website.
We kindly ask you to pull the latest commit with the configurations, retrain your models and submit your best strategies.
The Codalab leaderboard has been reset, and all participants have regained the original 50 attempts.

We apologize for any inconvenience this may have caused.


## Getting started

The devkit is based on the [Avalanche library](https://github.com/ContinualAI/avalanche). We warmly recommend looking at the [documentation](https://avalanche.continualai.org/) (especially the ["Zero To Hero tutorials"](https://avalanche.continualai.org/from-zero-to-hero-tutorial/01_introduction)) if this is your first time using it!

The recommended setup steps are as follows:

1. **Install [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html)** (and [mamba](https://github.com/mamba-org/mamba); recommended)

2. **Clone the repo** and **create the conda environment**:
```bash
git clone https://github.com/ContinualAI/clvision-challenge-2024.git
cd clvision-challenge-2024
conda env create -f environment.yml
```
Although we recommend using mamba for a faster environment creation: `mamba env create -f environment.yml`.

3. **Download the competition data**: download the data for the scenarios [here](https://files.icg.tugraz.at/f/deb8e57ba0534350a160/?dl=1) or [here](https://drive.google.com/file/d/1amesMabV-GQYVhCCeWeFA_PhYkpD2-ii/view?usp=sharing) and unzip it into the **data** folder.
```bash
cd data
wget --content-disposition 'https://files.icg.tugraz.at/f/deb8e57ba0534350a160/?dl=1'
unzip clvision2024-data.zip
cd ..
```

4. **Start training**: you can directly start training a baseline strategy by running:
```bash
conda activate clvision24
python train.py --config_file scenario_1.pkl
```

The aforementioned steps should be OS-agnostic. However, we recommend setting up your dev environment using a
mainstream Linux distribution.

## Code Structure


    ├── benchmarks
        ├── ... 
        ├── generate_scenario.py       # benchmark generator for the challenge
     
    ├── data 
        ├── ...                        # dataset train/test splits 

    ├── scenario_config
        ├── ...                        # stream config files used for benchmark generation
    
    ├── strategies
        ├── competition_template.py    # base strategy for the challenge
        ├── my_plugin.py               # template for implementing new plugins
        ├── my_strategy.py             # template for implementing new strategies

    ├── utils
        ├── ...                        # utility scripts

    ├── train.py                       # trainer script 
    ├── environment.yml                # conda environment file
    
## Implementing a strategy 
Use your creativity to implement strategies that tackle the three scenarios in this challenge. You have two options for implementing a new strategy:

#### Strategy as a plugin
The straightforward method to design a strategy is to implement it as a plugin. Plugins extend an existing strategy by implementing a particular set of callbacks. You can implement your plugin in `strategies/my_plugin.py`, and add it a base strategy (e.g. Naive strategy) in `train.py`.

#### Strategy as a subclass
Another way to implement your strategy is to define a class that inherits from `CompetitionTemplate` class. This method is suggested when the training epoch loops or other behaviors in a strategy are different from the default ones defined in the `CompetitionTemplate`, and cannot be implemented by extending existing strategies via plugins.  


*For a deeper dive into the implementation of strategies, please refer to [**this link**](https://avalanche.continualai.org/from-zero-to-hero-tutorial/04_training). 

#### Baseline strategy
As a baseline strategy, we also provide LwFUnlabelled in `strategies/lwf_unlabelled.py`, which applies the well-known Learning without Forgetting (LwF) strategy described in https://arxiv.org/abs/1606.09282 to both the labelled and the unlabelled data streams. For reference, the results from this strategy are listed in the [CodaLab leaderboard](https://codalab.lisn.upsaclay.fr/competitions/17780#results) under the user `test_clvision24`.

## Submitting a solution
Solutions must be submitted through the CodaLab portal:
tba

A solution must be a zip file that contains **three** prediction files generated by `train.py`. The file names must follow the pattern below:
- `pred_scenario_1.pkl`
- `pred_scenario_2.pkl`
- `pred_scenario_3.pkl`

where the numbers indicate the scenario ID on which the model is trained.

Teams can make up to 3 submissions daily, with an overall cap of 50 submissions throughout the competition. 
We will ensure that submissions from each team stay within this limit.

## Suggestions

- The devkit may be updated when new features are requested by participants. We recommend frequently checking if there are new updates.
- Consider using dashboard loggers, such as *Tensorboard* or *Weights & Biases*. See the tutorial on loggers [here](https://avalanche.continualai.org/from-zero-to-hero-tutorial/06_loggers). You can use more than one logger at the same time!
- Please check the ❗❗❗ [**FAQ**](https://sites.google.com/view/clvision2024/challenge#h.iz67c0d6y6ry) ❗❗❗ for common problems or clarification and updates of the competition rules!

## Acknowledgements
We would like to thank the _ImageNet Large Scale Visual Recognition Challenge_ for providing the base of the dataset used in the challenge.
```
Olga Russakovsky*, Jia Deng*, Hao Su, Jonathan Krause, Sanjeev Satheesh, Sean Ma, Zhiheng Huang, Andrej Karpathy, Aditya Khosla, Michael Bernstein, Alexander C. Berg and Li Fei-Fei. ImageNet Large Scale Visual Recognition Challenge. IJCV, 2015.
```
