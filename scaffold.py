import os

# Define the project structure
structure = {
    "adversarial_ai_project": {
        "main.py": "",
        "config.py": "",
        "requirements.txt": "",
        "models": {
            "__init__.py": "",
            "model_utils.py": "",
            "defense.py": ""
        },
        "attacks": {
            "__init__.py": "",
            "adversarial_attacks.py": ""
        },
        "explainability": {
            "__init__.py": "",
            "xai.py": ""
        },
        "utils": {
            "__init__.py": "",
            "data_loader.py": "",
            "visualization.py": ""
        }
    }
}

def create_structure(base_path, structure_dict):
    for name, content in structure_dict.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)  # recurse into subfolder
        else:
            with open(path, "w") as f:
                f.write(content)

# Run the generator
create_structure(".", structure)
print("✅ Project structure created!")
