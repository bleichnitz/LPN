from pathlib import Path
import yaml as yaml
import shutil as shutil

def find_config_file(class_dir):
    valid_config = False
    class_folder = Path(class_dir)

    for item in class_folder.iterdir():
        if item.suffix == ".yaml" or item.suffix == ".yml":
            valid_config = True
            config_file = item
    print(config_file)

    if valid_config is True:
        with open(config_file, 'r') as file:
            config_data = yaml.safe_load(file)
        keys = config_data.keys()
        for key in keys:
            print(key)
            counter = 0
            sub_keys = list(config_data[key].keys())
            for sub_key in config_data[key]:
                sub_key = sub_keys[counter]
                print(f"\t{sub_key}:   {config_data[key][sub_key]}")
                counter += 1

    return config_data
