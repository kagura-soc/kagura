from omegaconf import OmegaConf
import os

def load():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, '..', '..', '..', '.config', 'config.yml')
    config = OmegaConf.load(config_path)
    return config