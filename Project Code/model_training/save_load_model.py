import lightgbm as lgb
import json
import joblib as jl
import os

def save_lgb_model(model, fname, dest):
    if os.path.exists(dest):
        pth = f'{dest}/{fname}'
        jl.dump(model, f'{pth}.pkl')
        dump = model.booster_.dump_model(importance_type='gain')
        with open(f'{pth}.json', 'w') as model_json:
            json.dump(dump, model_json, indent=2)
    else:
        print("Failed to save model.")


def load_lgb_model(fname, location):
    pth = f'{location}/{fname}.pkl'
    if os.path.exists(pth):
        model = jl.load(pth)
        return model
    else:
        print("Failed to load model.")